# Commit 09 — Toàn bộ test backend, công cụ và tài liệu chức năng

Thông điệp: `test(backend): add API database and AI regression suites`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/09/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "test(backend): add API database and AI regression suites"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `COMMUNITY.md`
- `FEATURES.md`
- `MAP_AI_TOOLS.md`
- `MapAI_BE-main/AI_CHAT_SETUP.md`
- `MapAI_BE-main/AUTH_INTEGRATION.md`
- `MapAI_BE-main/ListTables.cs`
- `MapAI_BE-main/PROJECT_DOCUMENTATION.md`
- `MapAI_BE-main/README.md`
- `MapAI_BE-main/src/README.md`
- `MapAI_BE-main/tests/MapAI.AiChatTests/MapAI.AiChatTests.csproj`
- `MapAI_BE-main/tests/MapAI.AiChatTests/Program.cs`
- `MapAI_BE-main/tests/MapAI.AuthTests/MapAI.AuthTests.csproj`
- `MapAI_BE-main/tests/MapAI.AuthTests/Program.cs`
- `MapAI_BE-main/tests/MapAI.CommunityTests/MapAI.CommunityTests.csproj`
- `MapAI_BE-main/tests/MapAI.CommunityTests/Program.cs`
- `MapAI_BE-main/tests/MapAI.MapToolsTests/MapAI.MapToolsTests.csproj`
- `MapAI_BE-main/tests/MapAI.MapToolsTests/Program.cs`
- `MapAI_BE-main/tests/MapAI.Tests/FeatureTests.cs`
- `MapAI_BE-main/tests/MapAI.Tests/MapAI.Tests.csproj`
- `MapAI_BE-main/tests/MapAI.Tests/MapAiFactory.cs`
- `MapAI_BE-main/tests/MapAI.Tests/MapSearchTests.cs`
