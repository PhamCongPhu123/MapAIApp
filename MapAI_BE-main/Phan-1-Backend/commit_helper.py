#!/usr/bin/env python3
"""Import one reviewed handoff batch using the current user's Git identity."""
import argparse
import hashlib
import json
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys


def git(repo, *args, check=True):
    return subprocess.run(['git', '-C', str(repo), *args], check=check,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)


def fail(message):
    raise SystemExit(message)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--list', action='store_true')
    actions.add_argument('--init', action='store_true')
    actions.add_argument('--next', action='store_true')
    actions.add_argument('--all', action='store_true')
    actions.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    package = Path(__file__).resolve().parent
    plan = json.loads((package / 'commit-plan.json').read_text(encoding='utf-8'))
    if args.list:
        for step in plan['commits']:
            print(f"{step['id']}: {step['message']} ({len(step['files'])} files)")
        return
    if not args.repo:
        fail('Thieu --repo DUONG_DAN_CHECKOUT')
    repo = args.repo.resolve()
    if Path(git(repo, 'rev-parse', '--show-toplevel').stdout.strip()).resolve() != repo:
        fail('--repo phai la thu muc goc cua Git checkout.')
    if git(repo, 'status', '--porcelain', '--untracked-files=all').stdout.strip():
        fail('Checkout chua sach. Luu/commit thay doi hien tai truoc; cong cu khong tu xoa hay stash.')
    for key in ['user.name', 'user.email']:
        if not git(repo, 'config', '--get', key, check=False).stdout.strip():
            fail(f'Hay cau hinh git config {key} bang thong tin cua CHINH BAN.')
    if args.init:
        bootstrap = package / 'bootstrap'
        if not bootstrap.is_dir():
            fail('--init chi co trong goi Phan 1.')
        if git(repo, 'rev-parse', '--verify', 'HEAD', check=False).returncode == 0:
            fail('--init chi dung cho repository rong, chua co commit. Xem huong dan neu da co README.')
        for path in sorted(bootstrap.rglob('*')):
            if path.is_file():
                target = repo / path.relative_to(bootstrap)
                if target.exists():
                    fail(f'Khong ghi de file da co: {target}')
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(path, target)
        git(repo, 'branch', '-m', 'main')
        git(repo, 'add', '--', *[p.relative_to(bootstrap).as_posix() for p in bootstrap.rglob('*') if p.is_file()])
        result = git(repo, 'commit', '-m', 'chore: initialize MapAI team handoff')
        print(result.stdout)
        return
    if git(repo, 'rev-parse', '--verify', 'main', check=False).returncode != 0:
        fail('Chua co main. Nguoi 1 tao commit nen va push main, sau do moi clone goi 2/3.')
    # Validate every payload before creating branches or changing the checkout.
    for step in plan['commits']:
        for name, expected in step['files'].items():
            relative = PurePosixPath(name)
            if relative.is_absolute() or '..' in relative.parts or '.git' in relative.parts:
                fail(f'Duong dan khong hop le: {name}')
            payload = package / 'commits' / step['id'] / 'files' / name
            if hashlib.sha256(payload.read_bytes()).hexdigest() != expected:
                fail(f'File trong goi da bi thay doi: {name}')
            target = repo / name
            for parent in [target, *target.parents]:
                if parent == repo:
                    break
                if parent.is_symlink():
                    fail(f'Khong ghi qua symlink: {parent}')
    branch = git(repo, 'branch', '--show-current').stdout.strip()
    desired = plan['branch']
    if branch != desired:
        if branch != 'main':
            fail(f'Hay quay ve main sach hoac nhanh {desired}; cong cu khong tu doi nhanh dang lam.')
        if git(repo, 'show-ref', '--verify', 'refs/heads/' + desired, check=False).returncode == 0:
            fail(f'Nhanh da ton tai. Chay git switch {desired} de tiep tuc.')
    pending = []
    for step in plan['commits']:
        committed = []
        for name, expected in step['files'].items():
            target = repo / name
            tracked = git(repo, 'ls-files', '--error-unmatch', '--', name, check=False).returncode == 0
            if target.exists():
                if not target.is_file() or hashlib.sha256(target.read_bytes()).hexdigest() != expected:
                    fail(f'File da co noi dung khac: {name}. Xu ly thu cong de khong ghi de cong viec.')
                if not tracked:
                    fail(f'File da ton tai nhung chua tracked: {name}. Kiem tra file ignored truoc.')
            committed.append(target.exists() and tracked)
        if all(committed):
            continue
        if any(committed):
            fail(f'Nhom {step["id"]} da duoc nhap mot phan; hoan tat thu cong truoc khi chay lai.')
        pending.append(step)
    if not pending:
        print('Da nhap du tat ca nhom; khong tao commit rong.')
        return
    chosen = pending if args.all or args.dry_run else pending[:1]
    for step in chosen:
        print(f"{step['id']}: {step['message']} ({len(step['files'])} files)", flush=True)
    if args.dry_run:
        print('Chi xem ke hoach; chua tao nhanh, copy file hay commit.')
        return
    if branch != desired:
        git(repo, 'switch', '-c', desired, 'main')
    for step in chosen:
        for name in step['files']:
            source = package / 'commits' / step['id'] / 'files' / name
            target = repo / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)
            target.chmod(0o755 if name in step.get('executable_files', []) else 0o644)
        git(repo, 'add', '--', *step['files'].keys())
        if step.get('executable_files'):
            git(repo, 'update-index', '--chmod=+x', '--', *step['executable_files'])
        try:
            result = git(repo, 'commit', '-m', step['message'])
        except subprocess.CalledProcessError as exc:
            print(exc.stderr, file=sys.stderr)
            fail('Commit chua thanh cong; file van duoc giu nguyen. Kiem tra git status va hoan tat commit thu cong.')
        print(result.stdout, flush=True)
    print(f'Kiem tra git log va git status. Push khi san sang: git push -u origin {desired}')


if __name__ == '__main__':
    try:
        main()
    except subprocess.CalledProcessError as exc:
        print(exc.stderr, file=sys.stderr)
        sys.exit(exc.returncode)
