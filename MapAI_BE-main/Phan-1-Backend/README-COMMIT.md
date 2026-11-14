# Phần 1: Backend / API / database

- **Người nhận:** người 1.
- **Nhánh làm việc:** `contrib/backend`.
- **Số commit source:** 9 (không tính commit nền do người 1 tạo).
- **Số file source:** 126.
- **Nguồn:** nhánh `work`, commit `b75372d` của `PhamCongPhu123/MapAi_test`.

## A. Một người tạo repository GitHub mới — chỉ làm một lần

Tên mặc định đề xuất: `MapAI-team`, chế độ **Private**, tài khoản/organization sở hữu tùy nhóm.

1. Đăng nhập GitHub → nút **+** → **New repository**.
2. Nhập `MapAI-team`, chọn Private. **Không chọn** tạo README, .gitignore hoặc license để repo hoàn toàn rỗng.
3. Nhấn **Create repository**. Copy URL HTTPS được GitHub hiển thị; ví dụ `https://github.com/OWNER/MapAI-team.git` (thay `OWNER` bằng tài khoản thật).
4. Vào **Settings → Collaborators** (hoặc Collaborators and teams), mời 2 thành viên còn lại bằng username GitHub; họ cần chấp nhận lời mời.
5. Người 1 dùng gói Backend để tạo commit nền và push `main` theo phần B. Người 2/3 chờ đến khi `main` đã có commit nền rồi mới clone.

Chưa có repository mới nào được tạo thay bạn trong môi trường bàn giao: API GitHub đang bị chặn và chưa xác nhận được quyền tạo repo. Không gửi token/mật khẩu trong chat. Thao tác trên web này chỉ tạo vỏ repo; đủ mã nguồn sẽ nằm trong repo sau khi 3 PR được merge.

## B. Chuẩn bị trên máy từng người

Cài Git và Python 3. Mở Terminal/PowerShell tại một thư mục làm việc. Lệnh dưới đây dùng `python`; trên Windows nếu chỉ có launcher thì thay bằng `py -3`, trên macOS/Linux có thể cần `python3`.

```sh
git clone https://github.com/OWNER/MapAI-team.git
cd MapAI-team
git config user.name "TEN CUA CHINH BAN"
git config user.email "EMAIL GITHUB CUA CHINH BAN"
```

Có thể dùng email `noreply` từ GitHub Settings → Emails. Nếu cần đăng nhập khi push, dùng trình duyệt/Git Credential Manager hoặc `gh auth login`; không đặt token vào URL, script hoặc file mã nguồn.

Giải nén gói mình phụ trách thành thư mục **bên cạnh** checkout, ví dụ:

```text
team/
  MapAI-team/                 # checkout clone từ GitHub
  Phan-1-Backend/             # người 1, hoặc thư mục phần 2/3
    README-COMMIT.md
    commit_helper.py
    commit-plan.json
    commits/
      01/ ...
```

Đừng copy nguyên ZIP, `commit_helper.py` hoặc toàn bộ thư mục `commits/` vào repo. Công cụ chỉ copy source file đúng đường dẫn. Không xóa checkout gốc, không `git push --force`, không đổi tác giả hoặc ngày commit.

### Người 1 khởi tạo `main` trước

Sau khi clone **repo rỗng**, đang ở trong `MapAI-team`, người 1 chạy:

```sh
python ../Phan-1-Backend/commit_helper.py --repo . --init
git push -u origin main
```

Lệnh `--init` chỉ tạo 1 commit tài liệu nền (.gitignore, README, SOURCE). Sau đó người 1 tiếp tục phần C. Thông báo cho người 2/3 clone repository đã có `main`.

Nếu GitHub repo đã có README/commit trước đó: **không chạy `--init`**, không xóa lịch sử. Đảm bảo nhánh nền tên `main`, rồi copy 3 file trong `bootstrap/` của gói 1 vào checkout sau khi kiểm tra nội dung hiện có; commit với `git add .gitignore README.md SOURCE.md` và `git commit -m "docs: add MapAI handoff instructions"`, rồi push main. Nếu không có nhánh main, kiểm tra tên nhánh và thống nhất tạo main từ nhánh hiện có trước khi tiếp tục.

## C. Tự commit từng nhóm của phần 1

Sau khi checkout đã có `main` và đã cấu hình danh tính Git, chạy từ **bên trong checkout `MapAI-team`**:

```sh
python ../Phan-1-Backend/commit_helper.py --list
python ../Phan-1-Backend/commit_helper.py --repo . --dry-run
```

Xem file `COMMIT.md` và nội dung trong `commits/01/files/` trước khi nhập. Khi sẵn sàng, mỗi lần chạy lệnh này sẽ copy, stage và tạo **đúng một commit tiếp theo**, tự tạo nhánh `contrib/backend` từ `main` ở lần đầu:

```sh
python ../Phan-1-Backend/commit_helper.py --repo . --next
git show --stat --oneline HEAD
```

Lặp lại lệnh `--next` **9 lần tổng cộng** cho đủ các nhóm. Công cụ kiểm tra SHA-256, không tự push và không ghi đè file khác nội dung. Danh tính commit lấy từ `git config` của bạn. Không cần cài dependency ứng dụng chỉ để nhập file/commit. Có thể dùng `--all` nếu muốn tạo tất cả 9 commit một lượt, nhưng nên xem từng nhóm trước.

### Chọn cách hoàn toàn thủ công

Không chạy `--next` nếu dùng cách thủ công. Từ checkout sạch:

```sh
git switch main
git switch -c contrib/backend
```

Với từng nhóm, mở `commits/NN/COMMIT.md`. Copy nội dung `files/` vào gốc checkout, rồi thực hiện lệnh `git add`, xem diff và `git commit` trong tài liệu đó. Các file chỉ xuất hiện trong một nhóm nên không bị lặp source giữa 3 người. Phải giữ nguyên cấu trúc thư mục `MapAI_BE-main`/`MapAI_FE-feature-map-api`.

### Lịch commit chi tiết

| Nhóm | Commit message | Nội dung | Số file |
| --- | --- | --- | ---: |
| 01 | `chore(backend): add solution and development configuration` | Solution .NET, project references, Docker, cấu hình mẫu | 14 |
| 02 | `feat(domain): add shared models and contracts` | DTO, enum, cấu hình và helper dùng chung | 36 |
| 03 | `feat(database): add entities and EF Core migrations` | Entity, DbContext và migration PostgreSQL | 10 |
| 04 | `feat(auth): add account and authentication repositories` | User, token, JWT, email và storage repositories | 10 |
| 05 | `feat(integrations): add map and AI provider repositories` | OSM, Foursquare, Gemini và prompt backend | 9 |
| 06 | `feat(auth): add authentication services and application contracts` | Service tài khoản, session và interface ứng dụng | 11 |
| 07 | `feat(places): add map AI and community application services` | Service địa điểm, cộng đồng, bản đồ và AI | 6 |
| 08 | `feat(api): wire controllers and HTTP application pipeline` | Controller, Program.cs và HTTP sample | 9 |
| 09 | `test(backend): add API database and AI regression suites` | Toàn bộ test backend, công cụ và tài liệu chức năng | 21 |

## D. Push và mở Pull Request

Sau khi commit xong các nhóm của mình:

```sh
git status
git log --oneline -12
git push -u origin contrib/backend
```

Thay `BRANCH_CUA_BAN` bằng tên nhánh ghi ở đầu tài liệu này. Trên GitHub → **Pull requests → New pull request** → base `main`, compare nhánh của bạn → **Create pull request**. Ghi rõ số nhóm file, việc cấu hình dịch vụ thật chưa có, và các kiểm tra đã chạy.

Người quản lý kiểm tra rồi merge lần lượt: **Backend → Frontend → Map/AI/Mobile**. Chọn **Create a merge commit** (hoặc Rebase and merge); **không chọn Squash and merge** nếu muốn giữ từng commit nhỏ của mỗi người. Quyền chọn kiểu merge có thể cần bật ở Settings → General → Pull Requests.

Sau khi cả 3 PR đã merge:

```sh
git switch main
git pull --ff-only origin main
```

Lúc này toàn bộ project nằm trong **một repository**, gồm cả Android/iOS. Các phần chia theo file nên không chồng lấn source; module có tham chiếu lẫn nhau. Các commit nhập trung gian chưa đảm bảo build độc lập; chỉ kết luận build/chạy sau khi ghép đủ 3 phần. Đọc README ở gốc repo để cài dependency, chạy migration, chạy app và test. Không commit `node_modules`, `bin`, `obj`, `.env.local` hoặc database.

## E. Lỗi thường gặp

- **Commit không được tính vào tài khoản**: kiểm tra `git config user.email`; email phải đã xác minh hoặc đúng noreply của GitHub. Cấu hình trước khi commit; không giả danh người khác.
- **Permission denied / Repository not found**: kiểm tra URL, tài khoản đã đăng nhập và lời mời collaborator đã được chấp nhận.
- **Công cụ báo checkout chưa sạch**: xem `git status`; lưu/commit công việc đang có. Công cụ không tự stash hoặc xóa file.
- **Chạy trên nhánh sai**: gói cần `main` sạch để tạo nhánh mới, hoặc chính nhánh `contrib/...` tương ứng để tiếp tục. Không chạy trên nhánh `work` chứa sẵn toàn bộ code.
- **Các file đã giống hệt bản bàn giao**: công cụ bỏ qua nhóm đã nhập và không tạo commit rỗng. Nếu repo đã có toàn bộ project thì không thể thêm lại cùng file để tạo commit thay đổi mới.
- **Có file đã sửa khác bản bàn giao**: công cụ dừng trước khi ghi đè; xử lý thủ công hoặc dùng checkout sạch riêng.
- **Commit thất bại vì hook/ký GPG**: nội dung đã stage vẫn còn. Sửa cấu hình/hook đúng cách và hoàn tất `git commit -m "THONG_DIEP_CUA_NHOM"` thủ công, rồi mới chạy tiếp.
- **Push main bị chặn do branch protection**: người quản lý khởi tạo main bằng cách được GitHub cho phép; không tắt bảo vệ để ép push. Các phần sau vẫn dùng Pull Request.

Khóa Supabase, mật khẩu SMTP/database, Foursquare và JWT cũ không được đưa vào gói. Vì chúng đã có trong lịch sử repository cũ, chủ dự án nên thu hồi/đổi chúng tại dịch vụ tương ứng; bản bàn giao không thể thu hồi thay bạn.
