# Commit 08 — Controller, Program.cs và HTTP sample

Thông điệp: `feat(api): wire controllers and HTTP application pipeline`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/08/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(api): wire controllers and HTTP application pipeline"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.API/Controllers/AdminController.cs`
- `MapAI_BE-main/src/MapAI.API/Controllers/AiController.cs`
- `MapAI_BE-main/src/MapAI.API/Controllers/AuthController.cs`
- `MapAI_BE-main/src/MapAI.API/Controllers/CommunityLocationController.cs`
- `MapAI_BE-main/src/MapAI.API/Controllers/LocationController.cs`
- `MapAI_BE-main/src/MapAI.API/Controllers/MapController.cs`
- `MapAI_BE-main/src/MapAI.API/Controllers/UserController.cs`
- `MapAI_BE-main/src/MapAI.API/MapAI.API.http`
- `MapAI_BE-main/src/MapAI.API/Program.cs`
