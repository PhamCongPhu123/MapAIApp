# MapAI — team repository

Project đầy đủ gồm backend ASP.NET Core 9 và frontend React 19/Vite 8, kèm Android/iOS Capacitor.

## Các nhánh và phân công

| Nhánh | Người phụ trách | Nội dung |
| --- | --- | --- |
| `contrib/backend` | Người 1 | Backend, database, API, test backend |
| `contrib/frontend` | Người 2 | Giao diện web, tài khoản, admin, cộng đồng |
| `contrib/map-ai-mobile` | Người 3 | Bản đồ, AI frontend, Android/iOS |

`main` bắt đầu bằng tài liệu nền. Mỗi người nhập gói của mình thành các commit nhỏ rồi mở Pull Request vào `main`. Chỉ build toàn bộ sau khi cả 3 PR đã merge. Nếu được đẩy kèm, nhánh `work` là ảnh chụp đầy đủ đã thay cấu hình bí mật, dùng để tham khảo; không merge trực tiếp `work` vào `main` nếu muốn giữ các commit nhập của 3 người.

## Chạy sau khi đã ghép đủ 3 phần

1. Cài Node.js >=22.12, .NET SDK 9, Docker và Git. Python 3 chỉ cần cho công cụ nhập gói.
2. Chạy PostgreSQL chỉ lắng nghe loopback (terminal Bash hoặc PowerShell, một dòng):

```sh
docker run -d --name mapai-team-postgres -p 127.0.0.1:54329:5432 -e POSTGRES_USER=mapai -e POSTGRES_DB=mapai_dev -e POSTGRES_HOST_AUTH_METHOD=trust -v mapai-team-pgdata:/var/lib/postgresql/data postgres:17-bookworm
```

Đây là database phát triển cục bộ, không dùng cho production. Khi container đã tồn tại: `docker start mapai-team-postgres`.

3. Trong `MapAI_BE-main`: `dotnet restore src/MapAI.sln`, `dotnet build src/MapAI.sln`, `dotnet tool restore`.
4. Chạy migration: `dotnet ef database update --project src/MapAI.Domain --startup-project src/MapAI.API`.
5. Chạy backend: `dotnet run --project src/MapAI.API --launch-profile http --urls http://127.0.0.1:5028`.
6. Terminal khác, trong `MapAI_FE-feature-map-api`: `npm ci`, copy `.env.example` thành `.env.local`, rồi `npm run dev -- --port 5173 --strictPort`.
7. Kiểm tra API: `curl http://127.0.0.1:5028/api/v1/location` (database mới trả `[]`).

Cấu hình đã đổi sang database local và loại thông tin bí mật có sẵn trong bản nguồn. Gemini, SMTP, Google OAuth, Foursquare và Supabase upload cần cấu hình riêng nếu muốn dùng dịch vụ thật. Không commit `.env.local`, khóa API hay mật khẩu. Dùng .NET User Secrets/biến môi trường và đọc tài liệu tương ứng trong backend. Các phụ thuộc hiện có cảnh báo bảo mật cần xử lý trong công việc riêng.

## Kiểm tra sau khi ghép đủ

```sh
cd MapAI_FE-feature-map-api
npm run build
node --test tests/*.test.mjs
npm run lint
npx playwright install chromium
npm run test:mobile:e2e
```

Trong backend:

```sh
dotnet test tests/MapAI.Tests
dotnet run --project tests/MapAI.MapToolsTests
dotnet run --project tests/MapAI.AiChatTests
```

Hai suite `MapAI.CommunityTests` và `MapAI.AuthTests` cần biến `MAPAI_TEST_CONNECTION=Host=127.0.0.1;Port=54329;Database=mapai_dev;Username=mapai`; chúng tạo/xóa database test riêng trên máy local. Bash: `export MAPAI_TEST_CONNECTION='...'`; PowerShell: `$env:MAPAI_TEST_CONNECTION='...'`.

Android/iOS cần toolchain native riêng; iOS cần macOS/Xcode. Không commit thư mục dependency hoặc kết quả build.
