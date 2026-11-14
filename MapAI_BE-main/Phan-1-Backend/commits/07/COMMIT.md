# Commit 07 — Service địa điểm, cộng đồng, bản đồ và AI

Thông điệp: `feat(places): add map AI and community application services`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/07/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(places): add map AI and community application services"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.Application/Services/AiService.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/CommunityLocationService.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/FoursquareService.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/LocationService.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/MapCommandRouter.cs`
- `MapAI_BE-main/src/MapAI.Application/Services/MapService.cs`
