# Commit 03 — Entity, DbContext và migration PostgreSQL

Thông điệp: `feat(database): add entities and EF Core migrations`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/03/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(database): add entities and EF Core migrations"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.Domain/Entities/AccountTokenEntity.cs`
- `MapAI_BE-main/src/MapAI.Domain/Entities/LocationEntity.cs`
- `MapAI_BE-main/src/MapAI.Domain/Entities/LocationReviewEntity.cs`
- `MapAI_BE-main/src/MapAI.Domain/Entities/MapAIContext.cs`
- `MapAI_BE-main/src/MapAI.Domain/Entities/UserEntity.cs`
- `MapAI_BE-main/src/MapAI.Domain/Migrations/20260325135420_TestCheck.Designer.cs`
- `MapAI_BE-main/src/MapAI.Domain/Migrations/20260325135420_TestCheck.cs`
- `MapAI_BE-main/src/MapAI.Domain/Migrations/20261108092824_AddCommunityPlacesAndReviews.Designer.cs`
- `MapAI_BE-main/src/MapAI.Domain/Migrations/20261108092824_AddCommunityPlacesAndReviews.cs`
- `MapAI_BE-main/src/MapAI.Domain/Migrations/MapAIContextModelSnapshot.cs`
