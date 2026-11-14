# Commit 06 — Service tài khoản, session và interface ứng dụng

Thông điệp: `feat(auth): add authentication services and application contracts`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/06/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(auth): add authentication services and application contracts"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.Application/Exceptions/AuthException.cs`
- `MapAI_BE-main/src/MapAI.Application/Exceptions/CommunityConflictException.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/IAiService.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/IAuthService.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/ICommunityLocationService.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/IFoursquareService.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/ILocationService.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/IMapService.cs`
- `MapAI_BE-main/src/MapAI.Application/Interfaces/ITokenStoreService.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/AuthService.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/TokenStoreService.cs`
