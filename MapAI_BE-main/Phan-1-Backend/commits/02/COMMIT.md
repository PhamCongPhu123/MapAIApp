# Commit 02 — DTO, enum, cấu hình và helper dùng chung

Thông điệp: `feat(domain): add shared models and contracts`

Từ checkout Git, copy **nội dung bên trong** thư mục `files/` của nhóm này vào gốc checkout, giữ nguyên cấu trúc đường dẫn. Không copy chính thư mục `files` vào repo. Chỉ thực hiện nhóm này khi nhóm trước đã commit xong.

```sh
git add --pathspec-from-file="../Phan-1-Backend/commits/02/paths.txt"
git diff --cached --stat
git diff --cached
git commit -m "feat(domain): add shared models and contracts"
```

Các đường dẫn `../Phan-1-Backend` giả định bạn giải nén gói bên cạnh checkout. Chỉnh đường dẫn nếu đặt ở nơi khác. Lần đầu cần `git switch main` rồi `git switch -c contrib/backend`; những lần sau tiếp tục chính nhánh đó. Dùng danh tính Git của chính bạn.

## File trong commit này

- `MapAI_BE-main/src/MapAI.Common/Configs/MailSetting.cs`
- `MapAI_BE-main/src/MapAI.Common/Helpers/GlobalExceptionHandler.cs`
- `MapAI_BE-main/src/MapAI.Common/Helpers/HashHelper.cs`
- `MapAI_BE-main/src/MapAI.Domain/Common/BaseEntity.cs`
- `MapAI_BE-main/src/MapAI.Domain/Enums/EAuthEnums.cs`
- `MapAI_BE-main/src/MapAI.Domain/Enums/EUser.cs`
- `MapAI_BE-main/src/MapAI.Domain/Enums/LocationStatus.cs`
- `MapAI_BE-main/src/MapAI.Domain/Exceptions/AiProviderException.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Ai/AiModels.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Ai/AiResult.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Ai/ChatMessage.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/ForgotPasswordRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/GoogleLoginRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/LoginRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/LoginResponse.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/RefreshRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/RefreshResponse.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/RegisterRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/ResendVerificationRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Auth/ResetPasswordRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquareCategory.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquareGeocodes.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquareLocation.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquareNearbyResult.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquarePlace.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquarePoint.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquareSearchRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Foursquare/FoursquareSearchResponse.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Location/CommunityLocationModels.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Location/CreateLocationRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Location/LocationResponse.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Location/UpdateLocationRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Osm/MapPlaceTools.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/Osm/OsmModels.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/User/UpdateUserRequest.cs`
- `MapAI_BE-main/src/MapAI.Domain/Models/User/UserProfileResponse.cs`
