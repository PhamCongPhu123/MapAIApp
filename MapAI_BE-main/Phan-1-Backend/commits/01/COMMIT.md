# Commit 01 — Solution .NET, project references, Docker, cấu hình mẫu

Thông điệp: `chore(backend): add solution and development configuration`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/01/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "chore(backend): add solution and development configuration"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/.config/dotnet-tools.json`
- `MapAI_BE-main/.dockerignore`
- `MapAI_BE-main/.gitignore`
- `MapAI_BE-main/Dockerfile`
- `MapAI_BE-main/src/.gitignore`
- `MapAI_BE-main/src/MapAI.API/MapAI.API.csproj`
- `MapAI_BE-main/src/MapAI.API/Properties/launchSettings.json`
- `MapAI_BE-main/src/MapAI.API/appsettings.Development.json`
- `MapAI_BE-main/src/MapAI.API/appsettings.json`
- `MapAI_BE-main/src/MapAI.Application/MapAI.Application.csproj`
- `MapAI_BE-main/src/MapAI.Common/MapAI.Common.csproj`
- `MapAI_BE-main/src/MapAI.Domain/MapAI.Domain.csproj`
- `MapAI_BE-main/src/MapAI.Infrastructure/MapAI.Infrastructure.csproj`
- `MapAI_BE-main/src/MapAI.sln`
