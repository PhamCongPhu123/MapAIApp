# Commit 05 — OSM, Foursquare, Gemini và prompt backend

Thông điệp: `feat(integrations): add map and AI provider repositories`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/05/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(integrations): add map and AI provider repositories"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IAiRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IFoursquareRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/ILocationRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Interfaces/IOsmRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/FoursquareRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/GeminiRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/LocationRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/Repositories/OsmRepository.cs`
- `MapAI_BE-main/src/MapAI.Infrastructure/TemplatePrompts/AiPrompt.cs`
