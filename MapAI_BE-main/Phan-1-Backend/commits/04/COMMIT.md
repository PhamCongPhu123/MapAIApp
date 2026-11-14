# Commit 04 — User, token, JWT, email và storage repositories

Thông điệp: `feat(auth): add account and authentication repositories`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/04/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(auth): add account and authentication repositories"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IAccountTokenRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IEmailRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IJwtRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IStorageRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IUserRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/AccountTokenRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/EmailRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/JwtRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/StorageRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/UserRepository.cs`
