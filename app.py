import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SkinTrip", layout="centered")

st.markdown(
    """
    <style>
      /* 아이폰 16 Pro 기준 고정 뷰포트(393x852, CSS 논리 픽셀). 이후 작업에서
         화면 크기 자체는 이 값을 그대로 유지하고, 내부 요소만 수정할 것.
         바깥 영역(브라우저 창이 더 넓거나 좁을 때)은 배경색으로 채워서
         기기 프레임처럼 보이게 함 */
      html, body { margin: 0 !important; padding: 0 !important; background: #e5e7eb; }
      [data-testid="stHeader"] { display: none; }
      [data-testid="stApp"],
      [data-testid="stAppViewContainer"],
      [data-testid="stMain"] {
        padding: 0 !important;
        margin: 0 !important;
        background: #e5e7eb;
        display: flex;
        justify-content: center;
      }
      [data-testid="stMainBlockContainer"] {
        padding: 0 !important;
        margin: 0 !important;
        max-width: 393px !important;
      }
      [data-testid="stVerticalBlock"] { gap: 0 !important; }
      [data-testid="stElementContainer"]:has(iframe) {
        width: 393px !important;
        height: 852px !important;
      }
      [data-testid="stElementContainer"] iframe {
        display: block !important;
        width: 393px !important;
        height: 852px !important;
        border: none !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

HTML_PAGE = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>SkinTrip — 여행지 스킨케어 플래너</title>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://unpkg.com/maplibre-gl@5.24.0/dist/maplibre-gl.css" rel="stylesheet" />
<script src="https://unpkg.com/maplibre-gl@5.24.0/dist/maplibre-gl.js"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          sans: ['"Pretendard"', '"Apple SD Gothic Neo"', '"Malgun Gothic"', 'sans-serif'],
        },
        colors: {
          // SkinTrip 디자인 시스템의 유일한 포인트 컬러 (토스 스타일 블루)
          brand: {
            50: '#EFF6FF',
            100: '#DCE9FE',
            400: '#5B9DF9',
            500: '#3182F6',
            600: '#1B64DA',
          },
        },
      },
    },
  };
</script>
<style>
  /* 아이폰 16 Pro 기준 고정 뷰포트(393x852, CSS 논리 픽셀). 화면 크기 자체는
     앞으로도 이 값을 그대로 유지하고, 내부 요소(레이아웃/스타일)만 수정할 것 */
  :root {
    --app-width: 393px;
    --app-height: 852px;
  }
  body {
    background: #f3f4f6;
  }
  .bottom-nav-btn {
    color: #9ca3af;
  }
  .bottom-nav-btn.active {
    color: #3182f6;
  }
  .skin-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .skin-btn.active {
    border-color: #3182f6;
    background: #eff6ff;
    color: #1b64da;
  }
  .gender-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .gender-btn.active {
    border-color: #3182f6;
    background: #eff6ff;
    color: #1b64da;
  }
  .tone-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .tone-btn.active {
    border-color: #3182f6;
    background: #eff6ff;
    color: #1b64da;
  }
  .feedback-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .feedback-btn.active {
    border-color: #3182f6;
    background: #eff6ff;
    color: #1b64da;
  }
  .concern-chip {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .concern-chip.active {
    border-color: #3182f6;
    background: #eff6ff;
    color: #1b64da;
  }
  /* 버튼을 누를 때 살짝 눌리는 느낌 (절제된 인터랙션 포인트) */
  button {
    transition: transform 0.1s ease;
  }
  button:active {
    transform: scale(0.96);
  }
  /* 화면/단계 전환 시 부드러운 페이드 */
  @keyframes screenFadeIn {
    from {
      opacity: 0;
      transform: translateY(6px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  .screen-transition {
    animation: screenFadeIn 0.22s ease;
  }
  /* 온보딩 완료 후: 앱 셸을 고정 뷰포트 높이(--app-height)로 만들고 본문만
     스크롤되게 해서 화면 길이가 어떻든 하단 메뉴바가 항상 화면 하단에
     붙어있도록 함 */
  .app-shell-fixed {
    height: var(--app-height);
    display: flex;
    flex-direction: column;
    overflow: hidden;
  }
  .app-shell-fixed > main {
    flex: 1 1 auto;
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }
  /* 랜딩 페이지: 지구 위에 떠 있는 사용자 프로필 사진 말풍선 */
  .landing-bubble {
    position: absolute;
    width: 52px;
    height: 52px;
    border-radius: 9999px;
    overflow: hidden;
    border: 2.5px solid rgba(255, 255, 255, 0.9);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.25);
    animation: landingFloat 3.2s ease-in-out infinite;
  }
  .landing-bubble img {
    width: 100%;
    height: 100%;
    object-fit: cover;
  }
  @keyframes landingFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-7px); }
  }
  /* 매장 찾기 지도: 기본 파란 핀 대신 주황색 원형 커스텀 마커 */
  .store-marker {
    width: 22px;
    height: 22px;
    border-radius: 9999px;
    background: #f97316;
    border: 3px solid #ffffff;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.25);
    cursor: pointer;
    transition: transform 0.15s ease;
  }
  .store-marker:hover,
  .store-marker:active {
    transform: scale(1.2);
  }
  /* 마커 팝업을 앱의 화이트·라운드 톤과 통일 */
  .store-popup .maplibregl-popup-content {
    border-radius: 14px;
    padding: 10px 12px;
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.18);
  }
  .store-popup.maplibregl-popup-anchor-bottom .maplibregl-popup-tip {
    border-top-color: #ffffff;
  }
  /* 리스트 아이템이 지도로 flyTo되는 동안 살짝 강조 */
  .map-store-list-item.active-store-item {
    background-color: #fff7ed;
    border-color: #fdba74;
  }
</style>
</head>
<body class="font-sans text-gray-900">

  <!-- ============ 랜딩 페이지 ============ -->
  <div id="screen-landing" class="relative mx-auto overflow-hidden bg-black text-white" style="width: var(--app-width); height: var(--app-height);">
    <div class="absolute inset-0">
      <img src="https://eoimages.gsfc.nasa.gov/images/imagerecords/57000/57723/globe_west_2048.jpg" alt="지구" class="w-full h-full object-cover object-[62%_38%]" />
      <div class="absolute inset-0 bg-gradient-to-b from-black/25 via-black/0 to-black/75"></div>
    </div>

        <div class="landing-bubble" style="top:24%; left:16%; animation-delay:0s;">
          <img src="https://randomuser.me/api/portraits/women/44.jpg" alt="사용자" />
        </div>
        <div class="landing-bubble" style="top:33%; left:66%; animation-delay:0.5s;">
          <img src="https://randomuser.me/api/portraits/men/32.jpg" alt="사용자" />
        </div>
        <div class="landing-bubble" style="top:50%; left:38%; animation-delay:1s;">
          <img src="https://randomuser.me/api/portraits/men/12.jpg" alt="사용자" />
        </div>
        <div class="landing-bubble" style="top:53%; left:75%; animation-delay:1.4s;">
          <img src="https://randomuser.me/api/portraits/women/68.jpg" alt="사용자" />
        </div>
        <div class="landing-bubble" style="top:68%; left:24%; animation-delay:0.8s;">
          <img src="https://randomuser.me/api/portraits/men/76.jpg" alt="사용자" />
        </div>

    <div class="relative z-10 px-6 pt-10">
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQsAAABPCAYAAAD86+CcAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAOdEVYdFNvZnR3YXJlAEZpZ21hnrGWYwAAChhJREFUeAHtnf912zYQx899+b/eoMgEcScovYEzQeUJ6kxgeoI4E0SdwM4EpieIO4GYCeJMgOKCY0zRInkAf4g/vp/38GRLIAWRhwNwdzgSAQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgLlyQgCA3rDWnrqXC1eMvPXE5eTkJKeZA2XRM05YEvdy5sqpvPXsyv0ShAU04+79R/dyVfNx6mTghmZMJ2XhLo6hl45hKh/nUp7dRXqihSMjyp0rSU2V2QtLFbn/U4Hl7JmORIuiKPjg2nhLa4FHTlc+u/Ld6uG6d65sqCMsoIpySiPjvnOruA5XtCDstEjpSFgvcxq4H4wum6PjfuS1DVMQdexspNIIuCkZjYhdqbDYaZHSkXDffRHQzguaKb+1VXA/7syVnfszpZd1eBeMK5+tVxoJLQOtAPD1OyOwNELu6WwHi0Zl4Trz3+7lK722R/SBceXBfcc1zZ8QATAElkaIreRodpWu1CoL69fXWxqedAEKI0QAcgJLI8SAP1tj/0FlYb2V+yONRzrntRyFCUBOYFE4D0fmXjJF1e2cXeh1M4sHGh+2Y8xyPbcWYQGNXFLzQMCfzdp1/qb6hvWeCkPjw4qClz4pzRMWFlaypubzR1c+EFgkPAi4vnNOPs6GZ8nFwJeTn3lujxkH0gevgrLcD2aBT0jPF/K2jV8hrfYlWIsv2t8B5+KL+bbuosp5d9TOoztHQkdAlG1VWLYy+1gUNtxF/TvpPAd8//+jMPgabwmMg9XHC1it69P6IK5dwHk3PbQvIzA5+N7i/s2X6jIkxF98rll/84hq/fSMXbAam8RfNI4XBoBWrJ/NGvl30lsX7Mu+pHe0vz8pJz9b46XwU+wsN1ZZBBnqZD33yf2pcZEiaCkC643DG/KCkpAXlLKwcOGp/f0Sl0RVpJM3Geozdx0ua47dkF8+lzscw50tkTq81IzyGLrvfUv9t/cfqu87Rl4vpH7uXm5Cl21VZaH1RjxSOLekUxaGRkY08mdFVdbOPKN67ltYSm25J9/h69ib0YmSYEFh43Dd/TNSEq4bKywzxDR8dqjDJuTloOm4glPqX1ZNw2eH2svK4Y7C22HIex+5P6rlIFZZ5BSIdLBv7s8/WqqO6j4Vja4VkMuS8XUIYWF+1563NBqp6pcw5IXlj6XthI3F+iDEMWOLOmF9dPWWumHIy8E7JwetnrqqstC6dgzFsaHpodXMkxqJOyiKMhwMd6oRlCUj0/i1KYoyVyIHl02VYpVFVGOntlaWaZjGRsJGoZSmRVdFUcCC8m1VeRZKiNKdzXYDae8Q94o9Vc9NA0c1glNr6U1Eu80WGU1SRdXclfc0IUTJGeqPa7uGPAuHSWlem/t4kBjqXl3ZhpwrVWWRkZ6t9TkuZidkNmzvy+UEQ7Q31C9F9OyqEDmYzaBnx4muru3Te8sQMUJmpI/gTMlrI56RsFsuJ7+U+fU60RBXrXa+maCbcUPDCAx7VFJaFwnFk5EP8S/DA9CQg2eTYvsZQ0EvqwNuR0I+bimkTbXbLt4cqHxDYRexaNTBY3gdRP4HsDLJyPuLj50r0Siq3rfYKTIaX1iYvxo+4+v6g9o9Toc4ZdfhGmIwStR1Pr6O/5KX27zy/k9ktrktH2R9tq6h7j/fU3PgfVYSVzXBYrcye9pQmF2G3eu3qn7qKj7YYXmwEan1bMdwb/f+lfL4nY1IRuuOyTUnbznHQ8vh3w/8/9OrUTkP25U0eUHLDGrktCOGe9t2Wcns62u5sx1SJdgO99+GbbUoUC8drU/9F5IWU3duaXgf+Tbb2NkApWE7KAsb9psMRWDHURZldm1ttV6RaLmnAbHTUhbfQ6+l4jvHVBYpBWL11595FU16MJ+FTLHG8AAYesnHaWggrB91tXaKDxM0aNZx3tZWWUpplcA7Wg9VWTif0X3fxrjyJU4oU1Y/q77xW8OJM/fyJ42T2cm48tUOly3rlnR2ik8zijcI2Z/zSVnP0DqZW1KifykebcQu27D2FEZjwl4xmvCO0S6N08Kanp8tklCPWB+ToHGPsedmTu7DL9qKovi/aeoOOcObMGPId1/kXYzQcqzWwaBXFnJybtyGvOU/ZgNZKHd9CaycJ1VUzckrxTmRUxiapEGrZGYeoNCkQIfQDjR7S7VWZVHA6x3JPsW733gqM5Ti4AZqdoA2Ytu3/Jb5NLNpKDPF+JU58kTz4jt1J1fW21MWbygQ6VRp8b+sa4odmKb0N7++ozi/M7v9uvr8tfEUDPuVZ58jEUTxg9ZHlJwHK4sqJy2Zg2SET8gHhjQFFFVhO0NGcYR8D2PIz2YmtQcEgCmhXobEIjaPYgnDdg+tVhvKM1L7fXZhDy4GoIaoKNPBlUUZ8fNqR+/TDoZOtqe8LZVMedz1Sr0BYF2cKevtDeyjKgsm4IE8jKFIZEaTi41FO6PpxbgKwIBoO3oT2uC7vPzPT2UhoaY7RemrI6l8/n0hCkMbjJJgOQImzJntkBZCHBJGWf31zEI6k1GUvuwIQ+3Mq0UiMzNl9etq9BoAE6LLYBZy7J7zorwMUU3Te4qw1E6D+nZlBi1H7HqzR4FpEzWY2ZdHHGh4rIYSlJWFNjilU75CG5btJ6ceKdkvNPDNmE1uRrA67kIUhg3PNXpffaOsLLQhoLymjxp1ZVaiTWf3NESQlDsnX4R7ZfUr2/NeFQB6wpDffNmqAMQG95XCHAaNymJLejbkG7rRVGYNaH2GqpBko0Nu7gmJ98ByBEyZtHA+WJ/gJhGHBf99LXkpQjO4HdyF+yuCMyL/piHfkbghfBxvcHmml07In3MqsDOKc/doR/9g5LeywrhTVDfkp2+rfrYGmDSG/AC+oX446Dmshntzh/hKYbDGuqB+Iy5vht7YxcsR65+/+o+iOi9HHmUJA8CSqd1UuReUJfs8jj2C5jTMQ1QOkZLeiPoZ0Z1g4eTUkNLhVQSnxCMcKxlITvLgYRoB+R6tdwTRnWAK5DRM/8yppe/V5eDc0PgKI3fl/dh5JST8XJt2DtGdYAqwDGpDHTTkpMhB2pSDc0P6EOmu8Mav87bt7gOSkn45gs1m4Kjw6O8K58fVDnJNsB3uT80g3ZaDMyW/a3OorFg85eFs2skxM1VFLEc0XhQABkVyxvIu7phUe8UA/b73Zb99eWhNH88Tyax/4E9Q/ILt+JAhxflvrZ6PB46Pfm5E6RwPVoehsN82yHlBP1i9bO9qjudYJpbfQw9PsvJeJnUSiuCEIpAvK0qRPq8O3mFaPMIwI/9YwFEMmADMBVHSmqTKnHbhreJ83C+Lwfi5jz4XpSwOUWmcP/n8kuACcBT6VhZD0DkHZ4FoLswYAFgoo2fKAgDMEygLAIAKKAsAgAooCwCACigLAIAKKAsAgAooCwCACigLAICK3oKyAACd0G5mROAjAAAAAAAAAAAAAAAAAADAIPwPhIHT1DYG6ucAAAAASUVORK5CYII=" alt="SkinTrip" class="h-9 mb-3" />
      <p class="text-base font-bold leading-snug drop-shadow-md">
        <span class="font-extrabold">스킨트립</span>과 함께,<br />피부 걱정 없이 어디든
      </p>
    </div>

    <div class="absolute inset-x-0 bottom-0 z-10 px-6 pb-9 pt-6 bg-gradient-to-t from-black/60 via-black/10 to-transparent">
      <button id="startBtn" type="button" class="w-full py-3.5 rounded-full bg-gray-900 border border-white/15 text-white text-sm font-bold shadow-lg">시작하기</button>
    </div>
  </div>

  <!-- 여행지 등록 완료 시, 해당 국가에서 반입 금지된 성분이 있으면 경고하는 팝업 (전략미션A) -->
  <div id="importBanModal" class="hidden fixed inset-0 bg-black/40 px-6 z-50">
    <div class="flex items-center justify-center h-full">
      <div class="bg-white rounded-2xl p-5 w-full max-w-xs">
        <p class="text-[10px] font-bold text-red-500 mb-1">⚠️ 반입 금지 성분 주의</p>
        <p id="importBanTitle" class="text-base font-bold mb-3">이 제품은 반입 금지 물품이에요</p>
        <div class="bg-red-50 border border-red-100 rounded-xl p-3 mb-3">
          <p id="importBanMessage" class="text-xs text-red-600 leading-relaxed"></p>
        </div>
        <div class="space-y-1.5 mb-4 text-xs text-gray-500">
          <p><span class="font-semibold text-gray-700">규제 기관</span> · <span id="importBanAuthority"></span></p>
          <p><span class="font-semibold text-gray-700">규제 성분</span> · <span id="importBanIngredient"></span></p>
          <p><span class="font-semibold text-gray-700">대체 제품 제안</span> · <span id="importBanAlternative"></span></p>
          <p id="importBanSource" class="text-gray-400"></p>
        </div>
        <button id="importBanCloseBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">확인했어요</button>
      </div>
    </div>
  </div>

  <!-- 여행지 등록 완료 후, 파우치가 비어있으면 화장품 등록을 권하는 팝업 -->
  <div id="pouchPromptModal" class="hidden fixed inset-0 bg-black/40 px-6 z-50">
    <div class="flex items-center justify-center h-full">
      <div class="bg-white rounded-2xl p-5 w-full max-w-xs">
        <p class="text-base font-bold mb-1">화장품도 등록해볼까요?</p>
        <p class="text-sm text-gray-500 mb-5">파우치에 화장품을 등록하면 여행지 날씨에 맞는 루틴을 추천해드려요.</p>
        <div class="space-y-2">
          <button id="pouchPromptYesBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">지금 등록할게요</button>
          <button id="pouchPromptLaterBtn" type="button" class="w-full py-2 text-xs text-gray-400 underline">나중에 할게요</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ 앱 화면 ============ -->
  <div id="appContainer" class="hidden mx-auto bg-gray-50 border-x border-gray-100" style="width: var(--app-width);">

    <!-- 상단 로고 -->
    <header class="px-5 pt-6 pb-4">
      <p class="text-lg font-bold tracking-tight">Skin<span class="text-brand-500">Trip</span></p>
    </header>

    <main class="px-5 pb-6">

      <!-- ============ 1. 등록 페이지 ============ -->
      <section id="screen-register" class="py-6">

        <!-- 등록 (1): 내 정보 등록 (온보딩에서 유일하게 필수인 단계) -->
        <div id="register-step1">

          <!-- 상단 바: 제목 · 완료 -->
          <div class="flex items-center justify-between mb-4">
            <p class="text-base font-bold">내 정보 등록</p>
            <button id="step1ToStep2Btn" type="button" class="text-sm font-bold text-brand-500">완료</button>
          </div>

          <p id="step1Warning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2 mb-4"></p>

          <div class="space-y-6">

            <!-- 기본 정보 -->
            <div>
              <div class="bg-white rounded-xl px-4 py-2.5 mb-3">
                <p class="text-sm font-bold text-gray-700">기본 정보</p>
              </div>
              <div class="px-1 space-y-4">
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">나이</p>
                  <input id="ageInput" type="number" min="1" max="120" placeholder="예: 27" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
                </div>
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">성별</p>
                  <div class="flex flex-wrap gap-2">
                    <button type="button" data-gender="여성" class="gender-btn rounded-full px-5 py-2 text-sm font-semibold">여성</button>
                    <button type="button" data-gender="남성" class="gender-btn rounded-full px-5 py-2 text-sm font-semibold">남성</button>
                  </div>
                </div>
              </div>
            </div>

            <!-- 피부 정보 -->
            <div>
              <div class="bg-white rounded-xl px-4 py-2.5 mb-3">
                <p class="text-sm font-bold text-gray-700">피부 정보</p>
                <p class="text-xs text-gray-400 mt-0.5">맞춤 루틴을 위해 꼭 선택해주세요</p>
              </div>
              <div class="px-1 space-y-4">
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">피부 타입 <span class="text-gray-300 font-normal">(1개)</span></p>
                  <div class="flex flex-wrap gap-2">
                    <button type="button" data-skin="dry" class="skin-btn active rounded-full px-4 py-2 text-sm font-semibold">건성</button>
                    <button type="button" data-skin="normal" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">중성</button>
                    <button type="button" data-skin="oily" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">지성</button>
                    <button type="button" data-skin="combination" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">복합성</button>
                    <button type="button" data-skin="dehydrated" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">수부지</button>
                  </div>
                </div>
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">퍼스널컬러 <span class="text-gray-300 font-normal">(1개, 메이크업 추천에 활용돼요)</span></p>
                  <div class="flex flex-wrap gap-2">
                    <button type="button" data-tone="spring" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">봄웜톤</button>
                    <button type="button" data-tone="summer" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">여름쿨톤</button>
                    <button type="button" data-tone="autumn" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">가을웜톤</button>
                    <button type="button" data-tone="winter" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">겨울쿨톤</button>
                    <button type="button" data-tone="unknown" class="tone-btn active rounded-full px-4 py-2 text-sm font-semibold">잘 모르겠어요</button>
                  </div>
                </div>
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">피부 고민 <span class="text-gray-300 font-normal">(중복 선택 가능)</span></p>
                  <div class="flex flex-wrap gap-2">
                    <button type="button" data-concern="atopy" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">아토피</button>
                    <button type="button" data-concern="acne" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">여드름</button>
                    <button type="button" data-concern="sensitivity" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">민감성</button>
                    <button type="button" data-concern="pigmentation" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">미백/잡티</button>
                    <button type="button" data-concern="blackhead" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">피지/블랙헤드</button>
                    <button type="button" data-concern="darkcircle" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">다크서클</button>
                    <button type="button" data-concern="dryness" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">속건조</button>
                    <button type="button" data-concern="elasticity" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">주름/탄력</button>
                    <button type="button" data-concern="pore" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">모공</button>
                    <button type="button" data-concern="redness" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">홍조</button>
                    <button type="button" data-concern="flaking" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">각질</button>
                    <button type="button" data-concern="none" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">해당없음</button>
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- 등록 (2): 여행지·여행 계획 입력 -->
        <div id="register-step2" class="hidden space-y-8">

          <div>
            <button id="step2ToMainBtn" type="button" class="text-xs text-gray-400 mb-3">← 이전</button>
            <h2 class="text-base font-bold mb-1">여행지와 여행 계획을 알려주세요</h2>
            <p class="text-sm text-gray-400 mb-4">입력한 여행지 기후에 맞춰 루틴을 조정해드려요</p>

            <p class="text-xs font-semibold text-gray-400 mb-2">여행지</p>
            <select id="destinationSelect" class="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm mb-4 focus:outline-none focus:border-brand-500">
              <option value="">여행지를 선택해주세요</option>
              <option value="가나">가나</option>
              <option value="가봉">가봉</option>
              <option value="가이아나">가이아나</option>
              <option value="감비아">감비아</option>
              <option value="과테말라">과테말라</option>
              <option value="그레나다">그레나다</option>
              <option value="그리스">그리스</option>
              <option value="기니">기니</option>
              <option value="기니비사우">기니비사우</option>
              <option value="나미비아">나미비아</option>
              <option value="나우루">나우루</option>
              <option value="나이지리아">나이지리아</option>
              <option value="남수단">남수단</option>
              <option value="남아프리카공화국">남아프리카공화국</option>
              <option value="네덜란드">네덜란드</option>
              <option value="네팔">네팔</option>
              <option value="노르웨이">노르웨이</option>
              <option value="뉴질랜드">뉴질랜드</option>
              <option value="니제르">니제르</option>
              <option value="니카라과">니카라과</option>
              <option value="대만">대만</option>
              <option value="대한민국">대한민국</option>
              <option value="덴마크">덴마크</option>
              <option value="도미니카">도미니카</option>
              <option value="도미니카공화국">도미니카공화국</option>
              <option value="독일">독일</option>
              <option value="동티모르">동티모르</option>
              <option value="라오스">라오스</option>
              <option value="라이베리아">라이베리아</option>
              <option value="라트비아">라트비아</option>
              <option value="러시아">러시아</option>
              <option value="레바논">레바논</option>
              <option value="레소토">레소토</option>
              <option value="루마니아">루마니아</option>
              <option value="룩셈부르크">룩셈부르크</option>
              <option value="르완다">르완다</option>
              <option value="리비아">리비아</option>
              <option value="리투아니아">리투아니아</option>
              <option value="리히텐슈타인">리히텐슈타인</option>
              <option value="마다가스카르">마다가스카르</option>
              <option value="마셜제도">마셜제도</option>
              <option value="말라위">말라위</option>
              <option value="말레이시아">말레이시아</option>
              <option value="말리">말리</option>
              <option value="멕시코">멕시코</option>
              <option value="모나코">모나코</option>
              <option value="모로코">모로코</option>
              <option value="모리셔스">모리셔스</option>
              <option value="모리타니">모리타니</option>
              <option value="모잠비크">모잠비크</option>
              <option value="몬테네그로">몬테네그로</option>
              <option value="몰도바">몰도바</option>
              <option value="몰디브">몰디브</option>
              <option value="몰타">몰타</option>
              <option value="몽골">몽골</option>
              <option value="미국">미국</option>
              <option value="미얀마">미얀마</option>
              <option value="미크로네시아">미크로네시아</option>
              <option value="바누아투">바누아투</option>
              <option value="바레인">바레인</option>
              <option value="바베이도스">바베이도스</option>
              <option value="바티칸">바티칸</option>
              <option value="바하마">바하마</option>
              <option value="방글라데시">방글라데시</option>
              <option value="베냉">베냉</option>
              <option value="베네수엘라">베네수엘라</option>
              <option value="베트남">베트남</option>
              <option value="벨기에">벨기에</option>
              <option value="벨라루스">벨라루스</option>
              <option value="벨리즈">벨리즈</option>
              <option value="보스니아헤르체고비나">보스니아헤르체고비나</option>
              <option value="보츠와나">보츠와나</option>
              <option value="볼리비아">볼리비아</option>
              <option value="부룬디">부룬디</option>
              <option value="부르키나파소">부르키나파소</option>
              <option value="부탄">부탄</option>
              <option value="북마케도니아">북마케도니아</option>
              <option value="북한">북한</option>
              <option value="불가리아">불가리아</option>
              <option value="브라질">브라질</option>
              <option value="브루나이">브루나이</option>
              <option value="사모아">사모아</option>
              <option value="사우디아라비아">사우디아라비아</option>
              <option value="산마리노">산마리노</option>
              <option value="상투메프린시페">상투메프린시페</option>
              <option value="세네갈">세네갈</option>
              <option value="세르비아">세르비아</option>
              <option value="세이셸">세이셸</option>
              <option value="세인트루시아">세인트루시아</option>
              <option value="세인트빈센트그레나딘">세인트빈센트그레나딘</option>
              <option value="세인트키츠네비스">세인트키츠네비스</option>
              <option value="소말리아">소말리아</option>
              <option value="솔로몬제도">솔로몬제도</option>
              <option value="수단">수단</option>
              <option value="수리남">수리남</option>
              <option value="스리랑카">스리랑카</option>
              <option value="스웨덴">스웨덴</option>
              <option value="스위스">스위스</option>
              <option value="스페인">스페인</option>
              <option value="슬로바키아">슬로바키아</option>
              <option value="슬로베니아">슬로베니아</option>
              <option value="시리아">시리아</option>
              <option value="시에라리온">시에라리온</option>
              <option value="싱가포르">싱가포르</option>
              <option value="아랍에미리트">아랍에미리트</option>
              <option value="아르메니아">아르메니아</option>
              <option value="아르헨티나">아르헨티나</option>
              <option value="아이슬란드">아이슬란드</option>
              <option value="아이티">아이티</option>
              <option value="아일랜드">아일랜드</option>
              <option value="아제르바이잔">아제르바이잔</option>
              <option value="아프가니스탄">아프가니스탄</option>
              <option value="안도라">안도라</option>
              <option value="알바니아">알바니아</option>
              <option value="알제리">알제리</option>
              <option value="앙골라">앙골라</option>
              <option value="앤티가바부다">앤티가바부다</option>
              <option value="에리트레아">에리트레아</option>
              <option value="에스와티니">에스와티니</option>
              <option value="에스토니아">에스토니아</option>
              <option value="에콰도르">에콰도르</option>
              <option value="에티오피아">에티오피아</option>
              <option value="엘살바도르">엘살바도르</option>
              <option value="영국">영국</option>
              <option value="예멘">예멘</option>
              <option value="오만">오만</option>
              <option value="오스트리아">오스트리아</option>
              <option value="온두라스">온두라스</option>
              <option value="요르단">요르단</option>
              <option value="우간다">우간다</option>
              <option value="우루과이">우루과이</option>
              <option value="우즈베키스탄">우즈베키스탄</option>
              <option value="우크라이나">우크라이나</option>
              <option value="이라크">이라크</option>
              <option value="이란">이란</option>
              <option value="이스라엘">이스라엘</option>
              <option value="이집트">이집트</option>
              <option value="이탈리아">이탈리아</option>
              <option value="인도">인도</option>
              <option value="인도네시아">인도네시아</option>
              <option value="일본">일본</option>
              <option value="자메이카">자메이카</option>
              <option value="잠비아">잠비아</option>
              <option value="적도기니">적도기니</option>
              <option value="조지아">조지아</option>
              <option value="중국">중국</option>
              <option value="중앙아프리카공화국">중앙아프리카공화국</option>
              <option value="지부티">지부티</option>
              <option value="짐바브웨">짐바브웨</option>
              <option value="차드">차드</option>
              <option value="체코">체코</option>
              <option value="칠레">칠레</option>
              <option value="카메룬">카메룬</option>
              <option value="카보베르데">카보베르데</option>
              <option value="카자흐스탄">카자흐스탄</option>
              <option value="카타르">카타르</option>
              <option value="캄보디아">캄보디아</option>
              <option value="캐나다">캐나다</option>
              <option value="케냐">케냐</option>
              <option value="코모로">코모로</option>
              <option value="코스타리카">코스타리카</option>
              <option value="코트디부아르">코트디부아르</option>
              <option value="콜롬비아">콜롬비아</option>
              <option value="콩고공화국">콩고공화국</option>
              <option value="콩고민주공화국">콩고민주공화국</option>
              <option value="쿠바">쿠바</option>
              <option value="쿠웨이트">쿠웨이트</option>
              <option value="크로아티아">크로아티아</option>
              <option value="키르기스스탄">키르기스스탄</option>
              <option value="키리바시">키리바시</option>
              <option value="키프로스">키프로스</option>
              <option value="타지키스탄">타지키스탄</option>
              <option value="탄자니아">탄자니아</option>
              <option value="태국">태국</option>
              <option value="토고">토고</option>
              <option value="통가">통가</option>
              <option value="투르크메니스탄">투르크메니스탄</option>
              <option value="투발루">투발루</option>
              <option value="튀니지">튀니지</option>
              <option value="튀르키예">튀르키예</option>
              <option value="트리니다드토바고">트리니다드토바고</option>
              <option value="파나마">파나마</option>
              <option value="파라과이">파라과이</option>
              <option value="파키스탄">파키스탄</option>
              <option value="파푸아뉴기니">파푸아뉴기니</option>
              <option value="팔라우">팔라우</option>
              <option value="팔레스타인">팔레스타인</option>
              <option value="페루">페루</option>
              <option value="포르투갈">포르투갈</option>
              <option value="폴란드">폴란드</option>
              <option value="프랑스">프랑스</option>
              <option value="피지">피지</option>
              <option value="핀란드">핀란드</option>
              <option value="필리핀">필리핀</option>
              <option value="헝가리">헝가리</option>
              <option value="호주">호주</option>
            </select>

            <p class="text-xs font-semibold text-gray-400 mb-2">여행 계획</p>
            <div class="grid grid-cols-2 gap-2">
              <input id="tripStartDate" type="date" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
              <input id="tripEndDate" type="date" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
            </div>
          </div>

          <div>
            <p id="step2Warning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2 mb-3"></p>
            <button id="completeOnboardingBtn" type="button" class="w-full py-3.5 rounded-xl bg-brand-500 text-white text-sm font-bold">
              여행지 등록 완료
            </button>
          </div>

        </div>

      </section>

      <!-- ============ 2. 메인 페이지 (대시보드) ============ -->
      <section id="screen-inuse" class="hidden py-6 space-y-6">

        <!-- 상단 바: 프로필 설정 바로가기 -->
        <div class="flex justify-end">
          <button id="mainProfileBtn" type="button" class="text-xs font-semibold text-gray-500 bg-white border border-gray-200 rounded-full px-3 py-1.5">프로필 설정</button>
        </div>

        <p id="mainGreeting" class="text-sm text-gray-400 mb-1">안녕하세요!</p>

        <!-- 여행지 미등록 상태 -->
        <div id="mainEmptyState">
          <h2 class="text-2xl font-bold leading-snug mb-2">어디로<br />여행가시나요?</h2>
          <button id="mainRegisterTripBtn" type="button" class="text-sm font-semibold text-brand-500">여행지 등록하기 →</button>

          <button id="mainPouchCardEmpty" type="button" class="w-full flex items-center gap-3 bg-white border border-gray-100 rounded-2xl p-4 mt-10 text-left">
            <div class="w-11 h-11 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-xl shrink-0">👝</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">내 파우치</p>
              <p id="mainPouchEmptyText" class="text-xs text-gray-400">아직 등록된 화장품이 없어요</p>
            </div>
            <span class="text-gray-300">→</span>
          </button>
        </div>

        <!-- 여행지 등록 상태: 대시보드 -->
        <div id="mainDashboard" class="hidden space-y-6">

          <!-- 오늘의 날씨 히어로 카드: 메인 문구를 크게 강조 (메인 상단에 항시 표시) -->
          <div id="weatherHeroCard" class="rounded-2xl p-5 text-white" style="background: linear-gradient(135deg, #60a5fa 0%, #2563eb 100%);">
            <div class="flex items-start justify-between mb-6">
              <p id="weatherHeroHeadline" class="text-2xl font-bold leading-snug whitespace-pre-line"></p>
              <span id="weatherHeroLocation" class="text-xs font-semibold bg-white/20 rounded-full px-3 py-1.5 shrink-0">📍 여행지</span>
            </div>
            <div class="flex items-center gap-3">
              <span id="weatherHeroIcon" class="text-4xl"></span>
              <p>
                <span id="weatherHeroTemp" class="text-3xl font-bold"></span>
                <span id="weatherHeroCondition" class="text-base font-medium opacity-90 ml-1"></span>
              </p>
            </div>
          </div>

          <!-- 여행 일정 -->
          <div id="tripSummaryBanner" class="bg-white border border-gray-100 rounded-2xl p-4"></div>

          <!-- 파우치가 비어있을 때는 이 자리로 파우치 카드가 올라옴 -->
          <div id="pouchCardTopSlot"></div>

          <!-- 내 화장품 루틴 (카드 형식) -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">내 화장품 루틴</h3>
            <div id="myRoutineGrid" class="grid grid-cols-2 gap-2"></div>
          </div>

          <!-- 일정 기반 기후 안내 -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">일정 기반 기후 안내</h3>
            <div id="climateTable" class="bg-white border border-gray-100 rounded-xl divide-y divide-gray-100"></div>
          </div>

          <!-- 알림 목업 -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">오늘의 알림</h3>
            <p class="text-xs text-gray-400 mb-3">실제 앱에서는 푸시 알림으로 도착해요. 아래는 미리보기예요</p>
            <div class="space-y-3">
              <div class="bg-white border border-gray-100 rounded-2xl p-3">
                <div class="flex gap-3">
                  <div class="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center text-sm shrink-0">🧴</div>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between">
                      <p class="text-xs font-bold text-gray-500">SkinTrip</p>
                      <p class="text-[10px] text-gray-400">지금</p>
                    </div>
                    <p class="text-sm font-semibold text-gray-900 mt-0.5">습도가 오늘 밤부터 오를 예정이에요</p>
                    <p class="text-xs text-gray-500 mt-0.5">보유 중인 <span class="text-brand-500 font-semibold">에멀전</span>은 오늘 저녁 루틴에서 빼는 걸 추천해요</p>
                  </div>
                </div>
              </div>
              <div class="bg-white border border-gray-100 rounded-2xl p-3">
                <div class="flex gap-3">
                  <div class="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center text-sm shrink-0">☀️</div>
                  <div class="flex-1 min-w-0">
                    <div class="flex items-center justify-between">
                      <p class="text-xs font-bold text-gray-500">SkinTrip</p>
                      <p class="text-[10px] text-gray-400">3시간 전</p>
                    </div>
                    <p class="text-sm font-semibold text-gray-900 mt-0.5">오늘 자외선 지수 매우 높음</p>
                    <p class="text-xs text-gray-500 mt-0.5">2~3시간마다 <span class="text-brand-500 font-semibold">선크림</span> 재도포를 잊지 마세요</p>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- 오늘의 루틴 조정 제안 (갖고 있는 화장품 기반) -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">오늘의 루틴 조정 제안</h3>
            <div id="adjustmentWarnings" class="space-y-2 mb-2"></div>
            <div id="adjustmentTips" class="space-y-2 mb-2"></div>
            <div id="adjustmentList" class="space-y-2"></div>
          </div>

          <!-- 다른 여행자의 추천 루틴 (리뷰 기반) -->
          <div id="recommendedRoutineSection" class="hidden">
            <h3 class="text-sm font-semibold text-gray-700 mb-1">다른 여행자의 추천 루틴</h3>
            <p id="recommendedRoutineNote" class="text-xs text-gray-400 mb-3"></p>
            <div class="bg-white border border-gray-100 rounded-2xl p-4 space-y-3">
              <div>
                <p class="text-xs font-semibold text-brand-600 mb-1">추천 화장품</p>
                <p id="recommendedCosmetics" class="text-sm text-gray-600 leading-relaxed"></p>
              </div>
              <div class="border-t border-gray-100 pt-3">
                <p class="text-xs font-semibold text-brand-600 mb-1">스킨 루틴</p>
                <p id="recommendedSkincare" class="text-sm text-gray-600 leading-relaxed"></p>
              </div>
              <div class="border-t border-gray-100 pt-3">
                <p class="text-xs font-semibold text-brand-600 mb-1">메이크업 루틴</p>
                <p id="recommendedMakeup" class="text-sm text-gray-600 leading-relaxed"></p>
              </div>
            </div>
          </div>

          <!-- 내 파우치 요약 -->
          <button id="mainPouchCardFilled" type="button" class="w-full flex items-center gap-3 bg-white border border-gray-100 rounded-2xl p-4 text-left">
            <div id="mainPouchIcon" class="w-11 h-11 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-xl shrink-0">👝</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">내 파우치</p>
              <p id="mainPouchFilledText" class="text-xs text-gray-400">화장품 0개 등록됨</p>
            </div>
            <span class="text-gray-300">→</span>
          </button>

          <!-- 주변 매장 미리보기 -->
          <button id="mainMapCard" type="button" class="w-full flex items-center gap-3 bg-white border border-gray-100 rounded-2xl p-4 text-left">
            <div class="w-11 h-11 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">내 주위 화장품 매장</p>
              <p class="text-xs text-gray-400">올리브영 강남역점 · 250m</p>
            </div>
            <span class="text-gray-300">→</span>
          </button>

        </div>

      </section>

      <!-- ============ 3. 사용후 페이지 (입국신고서 컨셉) ============ -->
      <section id="screen-afteruse" class="hidden py-6 space-y-6">

        <button id="afterUseToSettingsBtn" type="button" class="text-xs text-gray-400">← 이전</button>

        <div class="border border-gray-200 rounded-2xl p-5">
          <div class="flex items-center justify-between mb-1">
            <p class="text-[10px] font-semibold tracking-widest text-gray-400 uppercase">Arrival Skin Declaration</p>
            <span class="text-[10px] font-bold text-brand-500 border border-brand-100 rounded-full px-2 py-0.5">DAY 5</span>
          </div>
          <h2 class="text-base font-bold mb-4">여행 후 피부 신고서</h2>

          <!-- 피부 사진 업로드 -->
          <div class="border-t border-dashed border-gray-200 pt-4 mb-4">
            <p class="text-xs font-semibold text-gray-500 mb-2">마지막 날 피부 사진</p>
            <div class="border-2 border-dashed border-gray-200 rounded-xl h-28 flex flex-col items-center justify-center text-gray-400 gap-1">
              <span class="text-xl">📷</span>
              <span class="text-xs">사진 업로드 (mock)</span>
            </div>
          </div>

          <!-- 피드백 입력 -->
          <div class="border-t border-dashed border-gray-200 pt-4 mb-4">
            <p class="text-xs font-semibold text-gray-500 mb-2">여행 중 피부는 어땠나요?</p>
            <div class="grid grid-cols-3 gap-2 mb-3">
              <button type="button" data-feedback="good" class="feedback-btn rounded-xl py-2 text-xs font-semibold">좋음</button>
              <button type="button" data-feedback="normal" class="feedback-btn rounded-xl py-2 text-xs font-semibold">보통</button>
              <button type="button" data-feedback="trouble" class="feedback-btn rounded-xl py-2 text-xs font-semibold">트러블 있었음</button>
            </div>
            <textarea rows="3" placeholder="자유롭게 남겨주세요 (선택)" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500"></textarea>
          </div>

          <!-- 추가 케어 제안 -->
          <div class="border-t border-dashed border-gray-200 pt-4">
            <p class="text-xs font-semibold text-gray-500 mb-2">귀국 후 추가 케어 제안</p>
            <ul class="space-y-2 text-sm text-gray-700">
              <li class="flex gap-2"><span class="text-brand-500">•</span>장시간 비행 후 진정 마스크팩으로 수분 보충</li>
              <li class="flex gap-2"><span class="text-brand-500">•</span>건조해진 각질 정리를 위한 약산성 필링</li>
              <li class="flex gap-2"><span class="text-brand-500">•</span>2~3일간 저자극 로션으로 피부 장벽 회복</li>
            </ul>
          </div>
        </div>

        <button type="button" class="w-full py-3.5 rounded-xl bg-brand-500 text-white text-sm font-bold">제출하기</button>

      </section>

      <!-- ============ 4. 지도 페이지 ============ -->
      <section id="screen-map" class="hidden py-6 space-y-4">
        <div>
          <h2 id="mapStoreListTitle" class="text-base font-bold mb-1">내 주위 화장품 매장</h2>
          <p id="mapStoreListSubtitle" class="text-sm text-gray-400 mb-4">현재 위치 기준으로 가까운 매장을 보여드려요 (mock)</p>
        </div>

        <div class="relative w-full">
          <div id="mapViz" class="relative w-full rounded-2xl overflow-hidden" style="height: 320px; background: linear-gradient(180deg, #eaf6ff 0%, #cfeeff 100%);"></div>
          <div class="absolute top-3 left-3 right-3 z-10">
            <input id="globeSearchInput" type="text" placeholder="나라 또는 도시를 검색해보세요" class="w-full py-2.5 px-4 rounded-full bg-white shadow-sm border-2 border-transparent text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:border-orange-400 transition-colors" />
            <p id="globeSearchNotFound" class="hidden mt-1.5 ml-2 inline-block text-[11px] font-medium text-orange-500 bg-orange-50 px-2 py-1 rounded-full">찾을 수 없어요</p>
          </div>
        </div>

        <div id="mapStoreList" class="space-y-2">
          <div class="flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-xl bg-pink-50 text-pink-400 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">올리브영 강남역점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 3분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">250m</p>
          </div>
          <div class="flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-xl bg-pink-50 text-pink-400 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">시코르 강남점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 5분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">410m</p>
          </div>
          <div class="flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-xl bg-pink-50 text-pink-400 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">랄라블라 신논현점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 8분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">600m</p>
          </div>
        </div>
      </section>

      <!-- ============ 5. 커뮤니티 페이지 ============ -->
      <section id="screen-community" class="hidden py-6 space-y-3">
        <div>
          <h2 class="text-base font-bold mb-1">커뮤니티</h2>
          <p class="text-sm text-gray-400 mb-4">다른 여행자들의 스킨케어 이야기를 둘러보세요</p>
        </div>

        <!-- 필터 -->
        <div class="space-y-2 mb-2">
          <select id="communityCountryFilter" class="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm bg-white focus:outline-none focus:border-brand-500">
            <option value="">전체 여행지</option>
            <option value="이탈리아">이탈리아</option>
            <option value="일본">일본</option>
            <option value="태국">태국</option>
            <option value="아랍에미리트">아랍에미리트</option>
            <option value="프랑스">프랑스</option>
            <option value="싱가포르">싱가포르</option>
          </select>
          <div class="grid grid-cols-3 gap-2">
            <select id="communityGenderFilter" class="w-full border border-gray-200 rounded-xl px-2 py-2 text-xs bg-white focus:outline-none focus:border-brand-500">
              <option value="">성별 전체</option>
              <option value="여성">여성</option>
              <option value="남성">남성</option>
            </select>
            <select id="communityAgeFilter" class="w-full border border-gray-200 rounded-xl px-2 py-2 text-xs bg-white focus:outline-none focus:border-brand-500">
              <option value="">나이대 전체</option>
              <option value="20대">20대</option>
              <option value="30대">30대</option>
              <option value="40대">40대</option>
              <option value="50대 이상">50대 이상</option>
            </select>
            <select id="communitySkinFilter" class="w-full border border-gray-200 rounded-xl px-2 py-2 text-xs bg-white focus:outline-none focus:border-brand-500">
              <option value="">피부타입 전체</option>
              <option value="지성">지성</option>
              <option value="건성">건성</option>
              <option value="복합성">복합성</option>
              <option value="민감성">민감성</option>
            </select>
          </div>
        </div>

        <p id="communityEmptyNote" class="hidden text-sm text-gray-400 text-center py-8">조건에 맞는 리뷰가 없어요</p>
        <div id="communityFeed" class="space-y-3"></div>
      </section>

      <!-- ============ 6. 개인설정 페이지 ============ -->
      <section id="screen-settings" class="hidden py-6 space-y-6">
        <div>
          <h2 id="settingsGreeting" class="text-base font-bold mb-1">개인설정</h2>
          <p class="text-sm text-gray-400 mb-4">내 프로필과 여행 정보를 확인하고 수정할 수 있어요</p>
        </div>

        <div class="bg-white border border-gray-100 rounded-2xl p-4 space-y-3">
          <div>
            <p class="text-xs font-semibold text-gray-400 mb-2">이름</p>
            <input id="nameInput" type="text" placeholder="이름을 입력해주세요" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
          </div>
          <div>
            <p class="text-xs font-semibold text-gray-400 mb-2">닉네임 <span class="text-gray-300 font-normal">(선택, 설정하면 닉네임으로 불러드려요)</span></p>
            <input id="nicknameInput" type="text" placeholder="닉네임을 입력해주세요" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
          </div>
        </div>

        <div id="profileSummaryCard" class="bg-white border border-gray-100 rounded-2xl p-4 space-y-2"></div>

        <div class="space-y-2">
          <button id="settingsEditBtn" type="button" class="w-full py-3 rounded-xl border border-gray-200 text-gray-700 text-sm font-semibold">
            정보 수정하기
          </button>
          <button id="goToAfterUseBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">
            여행 후 피부 신고서 작성하기
          </button>
        </div>
      </section>

      <!-- ============ 7. 파우치 페이지 (보유 화장품 촬영·관리) ============ -->
      <section id="screen-pouch" class="hidden py-6 space-y-8">

        <div>
          <h2 class="text-base font-bold mb-1">내 파우치</h2>
          <p class="text-sm text-gray-400 mb-4">사진 한 장이면 화장품 이름과 종류를 자동으로 인식해드려요</p>

          <label for="cosmeticPhotoInput" class="flex flex-col items-center justify-center gap-1.5 border-2 border-dashed border-gray-300 rounded-2xl py-10 text-gray-400 cursor-pointer hover:border-brand-500 hover:text-brand-500 transition">
            <span class="text-3xl">📷</span>
            <span class="text-sm font-semibold">탭해서 촬영하기</span>
            <span class="text-xs text-gray-300">또는 앨범에서 사진 선택</span>
          </label>
          <input id="cosmeticPhotoInput" type="file" accept="image/*" capture="environment" class="hidden" />

          <!-- 인식 중 -->
          <div id="scanningState" class="hidden bg-white border border-gray-100 rounded-2xl p-3 mt-3">
            <div class="flex items-center gap-3">
              <img id="scanningThumb" src="" alt="촬영한 화장품" class="w-14 h-14 rounded-xl object-cover shrink-0" />
              <div class="flex-1 min-w-0">
                <p class="text-sm font-semibold text-gray-700">화장품 정보를 인식하고 있어요...</p>
                <div class="h-1.5 bg-gray-100 rounded-full mt-2 overflow-hidden">
                  <div id="scanningBar" class="h-full bg-brand-400 rounded-full" style="width: 0%;"></div>
                </div>
              </div>
            </div>
          </div>

          <!-- 인식 결과 확인 -->
          <div id="scanResult" class="hidden border border-gray-200 bg-white rounded-2xl p-3 mt-3">
            <div class="flex items-center gap-3 mb-3">
              <img id="scanResultThumb" src="" alt="촬영한 화장품" class="w-14 h-14 rounded-xl object-cover shrink-0" />
              <div class="flex-1 min-w-0">
                <p class="text-[10px] font-semibold text-brand-500 mb-1">인식 완료 · 맞는지 확인해주세요</p>
                <input id="scanResultName" type="text" class="w-full bg-white border border-gray-200 rounded-xl px-2 py-1.5 text-sm font-semibold focus:outline-none focus:border-brand-500" />
              </div>
            </div>
            <div class="flex gap-2">
              <select id="scanResultCategory" class="flex-1 border border-gray-200 rounded-xl px-2 py-2 text-sm text-gray-600 bg-white focus:outline-none focus:border-brand-500"></select>
              <button id="confirmScanBtn" type="button" class="px-4 rounded-xl bg-brand-500 text-white text-sm font-bold">추가</button>
            </div>
          </div>
        </div>

        <!-- 갖고 있는 화장품 리스트 -->
        <div>
          <h3 class="text-sm font-semibold text-gray-700 mb-3">갖고 있는 화장품 <span id="cosmeticCountBadge" class="text-gray-400 font-normal"></span></h3>
          <div id="cosmeticRows" class="space-y-2 mb-3"></div>
          <button id="addCosmeticRowBtn" type="button" class="w-full text-center text-xs text-gray-400 underline">
            직접 입력하기
          </button>
        </div>

        <div>
          <p id="pouchWarning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2 mb-3"></p>
          <button id="pouchDoneBtn" type="button" class="w-full py-3.5 rounded-xl bg-brand-500 text-white text-sm font-bold">
            등록하기
          </button>
        </div>

      </section>

    </main>

    <!-- 하단 메뉴바 (등록 완료 후에만 표시, 화면 길이와 무관하게 항상 하단에 고정) -->
    <nav id="bottomNav" class="hidden shrink-0 bg-white border-t border-gray-100">
      <button type="button" data-tab="map" class="bottom-nav-btn flex-1 flex flex-col items-center gap-0.5 py-2.5 text-[11px] font-medium">
        <span class="text-xl">🗺️</span>
        <span>지도</span>
      </button>
      <button type="button" data-tab="inuse" class="bottom-nav-btn flex-1 flex flex-col items-center gap-0.5 py-2.5 text-[11px] font-medium">
        <span class="text-xl">🏠</span>
        <span>메인</span>
      </button>
      <button type="button" data-tab="community" class="bottom-nav-btn flex-1 flex flex-col items-center gap-0.5 py-2.5 text-[11px] font-medium">
        <span class="text-xl">💬</span>
        <span>커뮤니티</span>
      </button>
      <button type="button" data-tab="pouch" class="bottom-nav-btn flex-1 flex flex-col items-center gap-0.5 py-2.5 text-[11px] font-medium">
        <span class="text-xl">👝</span>
        <span>파우치</span>
      </button>
    </nav>

  </div>

  <script>
    // 현재 보이는 화면의 실제 높이에 맞춰 Streamlit iframe 높이를 동적으로 조정
    // (고정 높이를 쓰면 화면마다 내용 길이가 달라 불필요한 스크롤이 생김)
    function resizeFrame() {
      const height = document.documentElement.scrollHeight;
      try {
        if (window.frameElement) {
          window.frameElement.style.height = `${height}px`;
        }
      } catch (e) {
        // 프레임에 접근할 수 없는 환경이면 무시
      }
      try {
        // Streamlit Cloud 등 iframe이 sandbox 처리되어 frameElement에 직접 접근할 수 없는
        // 환경에서도 높이가 반영되도록, Streamlit이 공식적으로 지원하는
        // postMessage 기반 iframe 높이 조정 프로토콜을 함께 사용
        window.parent.postMessage({ type: 'streamlit:setFrameHeight', height }, '*');
      } catch (e) {
        // 무시
      }
    }
    let resizeScheduled = false;
    function scheduleResize() {
      if (resizeScheduled) return;
      resizeScheduled = true;
      requestAnimationFrame(() => {
        resizeScheduled = false;
        resizeFrame();
      });
    }
    new MutationObserver(scheduleResize).observe(document.documentElement, {
      childList: true,
      subtree: true,
      attributes: true,
      attributeFilter: ['class', 'style'],
    });
    window.addEventListener('resize', scheduleResize);
    window.addEventListener('load', scheduleResize);
    setTimeout(scheduleResize, 300); // Tailwind CDN(JIT) 스타일 주입 이후 재계산
    scheduleResize();

    // 화면이 바뀔 때마다 살짝 페이드인되도록 애니메이션 클래스를 다시 걸어줌
    function playScreenTransition(el) {
      el.classList.remove('screen-transition');
      void el.offsetWidth; // 리플로우를 강제로 일으켜 애니메이션을 재시작
      el.classList.add('screen-transition');
    }

    // 랜딩 페이지 -> 앱 진입 (회원가입 / 구글 로그인 모두 동일하게 mock 처리)
    function enterApp() {
      document.getElementById('screen-landing').classList.add('hidden');
      const app = document.getElementById('appContainer');
      app.classList.remove('hidden');
      try {
        playScreenTransition(app);
      } catch (e) {
        console.error('enterApp 전환 중 오류:', e);
      }
    }
    document.getElementById('startBtn').addEventListener('click', enterApp);

    // 하단 메뉴바 전환 (지도/메인/커뮤니티/파우치)
    const bottomNavButtons = document.querySelectorAll('.bottom-nav-btn');
    const screens = {
      register: document.getElementById('screen-register'),
      inuse: document.getElementById('screen-inuse'),
      afteruse: document.getElementById('screen-afteruse'),
      map: document.getElementById('screen-map'),
      community: document.getElementById('screen-community'),
      settings: document.getElementById('screen-settings'),
      pouch: document.getElementById('screen-pouch'),
    };
    let onboardingComplete = false;

    // 탭 전환(hidden 토글) 자체는 항상 먼저 실행하고, 화면별 렌더링 로직은
    // try/catch로 감싸서 그 안에서 오류가 나더라도 탭 전환 자체는 항상 되게 함
    // 지도 탭: MapLibre GL JS (globe projection) — 처음 지도 탭을 열 때 한 번만 초기화
    let mapInstance = null;
    let cityMarkers = [];
    let currentCityStores = [];

    function initMapIfNeeded() {
      if (mapInstance) return;
      const el = document.getElementById('mapViz');
      if (!el || typeof maplibregl === 'undefined') return;

      mapInstance = new maplibregl.Map({
        container: el,
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [20, 15],
        zoom: 1.3,
        attributionControl: false,
      });

      mapInstance.on('load', () => {
        try {
          // MapOptions 생성자에는 projection이 없어서 setProjection()으로 globe 투영을 켜야 함
          mapInstance.setProjection({ type: 'globe' });
        } catch (e) {
          console.error('setProjection 오류:', e);
        }
        try {
          // 초기 지구본 화면의 우주/대기 배경을 어둡지 않고 밝고 깔끔한 톤으로
          mapInstance.setSky({
            'sky-color': '#eaf6ff',
            'sky-horizon-blend': 0.8,
            'horizon-color': '#ffffff',
            'horizon-fog-blend': 0.6,
            'fog-color': '#eaf6ff',
            'fog-ground-blend': 0.5,
          });
        } catch (e) {
          console.error('setSky 오류:', e);
        }
      });

      window.addEventListener('resize', () => {
        if (mapInstance) mapInstance.resize();
      });

      // 검색창: 나라/도시 이름(한글 또는 영어 일부)으로 weatherData를 찾아 지도를 그 위치로 flyTo
      document.getElementById('globeSearchInput').addEventListener('keydown', (e) => {
        if (e.key !== 'Enter') return;
        searchCityOnMap();
      });
    }

    function searchCityOnMap() {
      const input = document.getElementById('globeSearchInput');
      const notFound = document.getElementById('globeSearchNotFound');
      const query = input.value.trim().toLowerCase();
      if (!query) {
        notFound.classList.add('hidden');
        return;
      }
      const matchKey = Object.keys(weatherData).find((key) => {
        const entry = weatherData[key];
        return key.toLowerCase().includes(query) || (entry.en && entry.en.toLowerCase().includes(query));
      });
      const match = matchKey ? weatherData[matchKey] : null;
      if (match && match.lat != null && match.lng != null) {
        notFound.classList.add('hidden');
        flyToCity(matchKey, match);
      } else {
        notFound.classList.remove('hidden');
      }
    }

    // 도시 좌표로 부드럽게 확대(zoom 11 이상 → globe 투영이 자연스럽게 평면 지도처럼 전환됨)
    // 1.5~2초 사이의 자연스러운 속도가 되도록 거리와 무관하게 duration을 고정
    function flyToCity(cityKey, weather) {
      if (!mapInstance) return;
      mapInstance.flyTo({ center: [weather.lng, weather.lat], zoom: 11, duration: 1800, essential: true });
      mapInstance.once('moveend', () => {
        renderCityStoreMarkers(cityKey, weather);
      });
    }

    function clearCityMarkers() {
      cityMarkers.forEach((m) => m.remove());
      cityMarkers = [];
    }

    // 매장 카테고리별로 채도가 낮은 파스텔 배경/텍스트 색 (아이콘 배경 구분용)
    function getCategoryStyle(category) {
      const styles = {
        드럭스토어: 'bg-blue-50 text-blue-400',
        '뷰티 편집샵': 'bg-purple-50 text-purple-400',
        라이프스타일샵: 'bg-green-50 text-green-400',
        '헬스&뷰티': 'bg-pink-50 text-pink-400',
      };
      return styles[category] || 'bg-gray-100 text-gray-400';
    }

    // 도시 확대가 끝나면 storeData의 매장들을 도시 중심 근처 mock 좌표에 주황색 원형 마커로 표시
    function renderCityStoreMarkers(cityKey, weather) {
      clearCityMarkers();
      const storeKey = weather.en ? weather.en.toLowerCase() : '';
      const baseStores = storeData[storeKey] || [];
      const offsets = [
        [0.008, 0.006], [-0.009, 0.004], [0.004, -0.009], [-0.006, -0.007], [0.011, -0.002],
      ];
      currentCityStores = baseStores.map((store, i) => {
        const off = offsets[i % offsets.length];
        return { ...store, lng: weather.lng + off[0], lat: weather.lat + off[1] };
      });
      currentCityStores.forEach((store) => {
        const popup = new maplibregl.Popup({ offset: 18, closeButton: false, className: 'store-popup' }).setHTML(`
          <div style="min-width:140px;">
            <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:5px;">
              <p style="font-weight:700;font-size:12px;color:#111827;">${store.name}</p>
              <span style="font-size:10px;color:#9ca3af;white-space:nowrap;">${store.distance}</span>
            </div>
            <span style="display:inline-block;font-size:10px;padding:2px 8px;border-radius:9999px;background:#ffedd5;color:#c2410c;font-weight:600;">${store.category}</span>
          </div>
        `);
        const el = document.createElement('div');
        el.className = 'store-marker';
        const marker = new maplibregl.Marker({ element: el })
          .setLngLat([store.lng, store.lat])
          .setPopup(popup)
          .addTo(mapInstance);
        store.marker = marker;
        cityMarkers.push(marker);
      });
      renderMapStoreList(cityKey, currentCityStores);
    }

    // 지도 아래 매장 리스트 카드: 클릭 시 지도가 해당 매장 마커로 다시 flyTo
    function renderMapStoreList(cityKey, stores) {
      document.getElementById('mapStoreListTitle').textContent = `${cityKey} 근처 화장품 매장`;
      document.getElementById('mapStoreListSubtitle').textContent = '지도에 표시된 마커를 눌러도 위치를 확인할 수 있어요 (mock)';
      const list = document.getElementById('mapStoreList');
      if (stores.length === 0) {
        list.innerHTML = '<p class="text-xs text-gray-400 py-2">아직 등록된 매장 정보가 없어요</p>';
        return;
      }
      list.innerHTML = stores.map((store, i) => `
        <button type="button" class="map-store-list-item w-full flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3 text-left" data-index="${i}">
          <div class="w-10 h-10 rounded-xl ${getCategoryStyle(store.category)} flex items-center justify-center text-lg shrink-0">🏬</div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-semibold truncate">${store.name}</p>
            <p class="text-xs text-gray-400 truncate">${store.category} · ${store.products.join(', ')}</p>
          </div>
          <p class="text-xs text-gray-500 shrink-0">${store.distance}</p>
        </button>
      `).join('');
      list.querySelectorAll('.map-store-list-item').forEach((btn) => {
        btn.addEventListener('click', () => {
          const store = currentCityStores[Number(btn.dataset.index)];
          if (!mapInstance || !store) return;
          list.querySelectorAll('.map-store-list-item').forEach((b) => b.classList.remove('active-store-item'));
          btn.classList.add('active-store-item');
          mapInstance.flyTo({ center: [store.lng, store.lat], zoom: 15, duration: 1200, essential: true });
          mapInstance.once('moveend', () => {
            btn.classList.remove('active-store-item');
          });
          if (store.marker) store.marker.togglePopup();
        });
      });
    }

    function switchTab(tabName) {
      bottomNavButtons.forEach((b) => b.classList.toggle('active', b.dataset.tab === tabName));
      Object.entries(screens).forEach(([key, el]) => el.classList.toggle('hidden', key !== tabName));
      try {
        playScreenTransition(screens[tabName]);
        if (tabName === 'inuse') {
          refreshAdjustedRoutine();
        } else if (tabName === 'settings') {
          renderProfileSummary();
        } else if (tabName === 'community') {
          if (!communityDefaultApplied) {
            applyDefaultCommunityFilter();
            communityDefaultApplied = true;
          }
          renderCommunityFeed();
        } else if (tabName === 'map') {
          initMapIfNeeded();
        }
      } catch (e) {
        console.error(`switchTab('${tabName}') 렌더링 중 오류:`, e);
      }
    }

    // 등록 완료 전에는 하단 메뉴바 자체를 숨김 (등록 흐름 중에는 이전/다음 버튼으로만 이동)
    function updateTabLockUI() {
      const bottomNav = document.getElementById('bottomNav');
      bottomNav.classList.toggle('hidden', !onboardingComplete);
      bottomNav.classList.toggle('flex', onboardingComplete);
      // 하단 메뉴바가 보이는 동안에는 앱 셸을 고정 높이로 만들어 본문만 스크롤되게 함
      document.getElementById('appContainer').classList.toggle('app-shell-fixed', onboardingComplete);
    }

    document.getElementById('settingsEditBtn').addEventListener('click', () => {
      switchTab('register');
    });

    document.getElementById('goToAfterUseBtn').addEventListener('click', () => {
      switchTab('afteruse');
    });

    document.getElementById('afterUseToSettingsBtn').addEventListener('click', () => {
      switchTab('settings');
    });

    // 메인 대시보드의 바로가기 카드/버튼
    document.getElementById('mainProfileBtn').addEventListener('click', () => {
      switchTab('settings');
    });
    document.getElementById('mainRegisterTripBtn').addEventListener('click', () => {
      switchTab('register');
      showRegisterStep('step2');
    });
    document.getElementById('mainPouchCardEmpty').addEventListener('click', () => {
      switchTab('pouch');
    });
    document.getElementById('mainPouchCardFilled').addEventListener('click', () => {
      switchTab('pouch');
    });
    document.getElementById('mainMapCard').addEventListener('click', () => {
      switchTab('map');
    });

    bottomNavButtons.forEach((btn) => {
      btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });

    function showWarning(id, message) {
      const warning = document.getElementById(id);
      warning.textContent = message;
      warning.classList.remove('hidden');
    }

    function hideWarning(id) {
      document.getElementById(id).classList.add('hidden');
    }

    function showRegisterStep(stepName) {
      ['step1', 'step2'].forEach((key) => {
        document.getElementById(`register-${key}`).classList.toggle('hidden', key !== stepName);
      });
      playScreenTransition(document.getElementById(`register-${stepName}`));
    }

    // 등록 2단계에서 선택한 여행지를 사용중 탭의 기후 mock 데이터 키에 반영
    document.getElementById('destinationSelect').addEventListener('change', () => {
      const key = document.getElementById('destinationSelect').value;
      if (key) {
        currentTripDestination = key;
      }
    });

    // 피부 타입 버튼 토글 (등록 1단계)
    document.querySelectorAll('.skin-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.skin-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // 성별 버튼 토글 (등록 1단계)
    document.querySelectorAll('.gender-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.gender-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // 퍼스널컬러 버튼 토글 (등록 1단계)
    document.querySelectorAll('.tone-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.tone-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // 온보딩 완료 조건 (피부 정보만 필수): 나이 입력 + 성별 선택 + 피부 고민 1개 이상
    function validateStep1() {
      const missing = [];
      if (!document.getElementById('ageInput').value.trim()) {
        missing.push('나이');
      }
      if (!document.querySelector('.gender-btn.active')) {
        missing.push('성별');
      }
      if (document.querySelectorAll('.concern-chip.active').length === 0) {
        missing.push('피부 고민');
      }
      return { valid: missing.length === 0, missing };
    }

    // 피부 정보 입력을 마치면 화장품·여행지 등록 없이 바로 메인 페이지로 이동
    // (화장품·여행지 등록은 이후 개인설정 메뉴에서 별도로 진행)
    document.getElementById('step1ToStep2Btn').addEventListener('click', () => {
      const result = validateStep1();
      if (!result.valid) {
        showWarning('step1Warning', `${result.missing.join(', ')}을(를) 먼저 입력해주세요`);
        return;
      }
      hideWarning('step1Warning');
      onboardingComplete = true;
      updateTabLockUI();
      switchTab('inuse');
    });

    document.getElementById('step2ToMainBtn').addEventListener('click', () => {
      switchTab('inuse');
    });

    // 피부 고민 칩 토글 (중복 선택 가능)
    document.querySelectorAll('.concern-chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        chip.classList.toggle('active');
      });
    });

    // 보유 화장품 - 제품명 + 카테고리 행 추가
    const cosmeticCategories = [
      { value: 'cleanser', label: '클렌저', icon: '🧼' },
      { value: 'toner', label: '토너', icon: '💧' },
      { value: 'essence', label: '에센스', icon: '✨' },
      { value: 'lotion', label: '로션', icon: '🧴' },
      { value: 'cream', label: '크림', icon: '🫙' },
      { value: 'emulsion', label: '에멀전', icon: '🧴' },
      { value: 'sunscreen', label: '선크림', icon: '☀️' },
    ];
    function buildCosmeticRow(productName, category) {
      const row = document.createElement('div');
      row.className = 'cosmetic-row flex gap-2 items-center';
      const options = cosmeticCategories
        .map((c) => `<option value="${c.value}" ${c.value === category ? 'selected' : ''}>${c.label}</option>`)
        .join('');
      row.innerHTML = `
        <input type="text" value="${productName}" placeholder="제품명" class="flex-1 min-w-0 border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
        <select class="border border-gray-200 rounded-xl px-2 py-2 text-sm text-gray-600 focus:outline-none focus:border-brand-500">${options}</select>
        <button type="button" class="remove-cosmetic-btn text-gray-300 hover:text-gray-500 text-sm px-1">✕</button>
      `;
      row.querySelector('.remove-cosmetic-btn').addEventListener('click', () => row.remove());
      return row;
    }

    const cosmeticRows = document.getElementById('cosmeticRows');

    document.getElementById('addCosmeticRowBtn').addEventListener('click', () => {
      cosmeticRows.appendChild(buildCosmeticRow('', cosmeticCategories[0].value));
    });

    // 화장품이 추가/삭제될 때마다 카운트 배지 갱신
    const cosmeticCountBadge = document.getElementById('cosmeticCountBadge');
    function updateCosmeticCountBadge() {
      const count = cosmeticRows.querySelectorAll('.cosmetic-row').length;
      cosmeticCountBadge.textContent = count > 0 ? `(${count})` : '';
    }
    new MutationObserver(updateCosmeticCountBadge).observe(cosmeticRows, { childList: true });
    updateCosmeticCountBadge();

    // 화장품 사진 촬영 → 인식 중 애니메이션 → 인식 결과 확인 인터랙션
    const scanResultCategorySelect = document.getElementById('scanResultCategory');
    scanResultCategorySelect.innerHTML = cosmeticCategories
      .map((c) => `<option value="${c.value}">${c.label}</option>`)
      .join('');

    const mockRecognizedProducts = [
      { name: '이니스프리 그린티 클렌징폼', category: 'cleanser' },
      { name: '라운드랩 자작나무 수분 토너', category: 'toner' },
      { name: '라네즈 워터뱅크 에센스', category: 'essence' },
      { name: '설화수 자음 로션', category: 'lotion' },
      { name: '닥터자르트 세라마이딘 크림', category: 'cream' },
      { name: '라네즈 워터뱅크 에멀전', category: 'emulsion' },
      { name: '아이소이 브루쿤달 선크림', category: 'sunscreen' },
      { name: '헤라 선메이트 선크림', category: 'sunscreen' },
      { name: '토니모리 시카 클렌징폼', category: 'cleanser' },
      { name: '마몽드 로즈워터 토너', category: 'toner' },
    ];

    const cosmeticPhotoInput = document.getElementById('cosmeticPhotoInput');
    const scanningState = document.getElementById('scanningState');
    const scanningThumb = document.getElementById('scanningThumb');
    const scanningBar = document.getElementById('scanningBar');
    const scanResult = document.getElementById('scanResult');
    const scanResultThumb = document.getElementById('scanResultThumb');
    const scanResultName = document.getElementById('scanResultName');

    cosmeticPhotoInput.addEventListener('change', () => {
      const file = cosmeticPhotoInput.files[0];
      if (!file) return;

      const reader = new FileReader();
      reader.onload = () => {
        const photoDataUrl = reader.result;

        scanResult.classList.add('hidden');
        scanningThumb.src = photoDataUrl;
        scanningBar.style.width = '0%';
        scanningState.classList.remove('hidden');
        requestAnimationFrame(() => {
          scanningBar.style.transition = 'width 1.3s ease-out';
          scanningBar.style.width = '100%';
        });

        setTimeout(() => {
          scanningState.classList.add('hidden');

          const picked = mockRecognizedProducts[Math.floor(Math.random() * mockRecognizedProducts.length)];
          scanResultThumb.src = photoDataUrl;
          scanResultName.value = picked.name;
          scanResultCategorySelect.value = picked.category;
          scanResult.classList.remove('hidden');
        }, 1400);
      };
      reader.readAsDataURL(file);
    });

    document.getElementById('confirmScanBtn').addEventListener('click', () => {
      const name = scanResultName.value.trim();
      if (!name) return;
      cosmeticRows.appendChild(buildCosmeticRow(name, scanResultCategorySelect.value));
      scanResult.classList.add('hidden');
      cosmeticPhotoInput.value = '';
    });

    document.getElementById('pouchDoneBtn').addEventListener('click', () => {
      if (getMyProducts().length === 0) {
        showWarning('pouchWarning', '화장품을 1개 이상 등록해주세요');
        return;
      }
      hideWarning('pouchWarning');
      switchTab('inuse');
    });

    // 등록 페이지에 입력된 보유 화장품을 { name, category } 배열로 읽어옴
    function getMyProducts() {
      return Array.from(cosmeticRows.querySelectorAll('.cosmetic-row'))
        .map((row) => ({
          name: row.querySelector('input').value.trim(),
          category: row.querySelector('select').value,
        }))
        .filter((product) => product.name);
    }

    // 여행지 등록 완료 조건: 여행지 선택
    function validateOnboarding() {
      const missing = [];
      if (!document.getElementById('destinationSelect').value) {
        missing.push('여행지');
      }
      const start = document.getElementById('tripStartDate').value;
      const end = document.getElementById('tripEndDate').value;
      if (!start) {
        missing.push('여행 시작일');
      }
      if (!end) {
        missing.push('여행 종료일');
      }
      if (start && end && end < start) {
        return { valid: false, missing: [], customMessage: '종료일은 시작일보다 늦어야 해요' };
      }
      return { valid: missing.length === 0, missing };
    }

    // 전략미션A: 여행지별 반입 금지 성분 정보 (우선 이탈리아/EU만 반영, 이후 일본·미국 등으로 확장 가능)
    const importBanData = {
      이탈리아: {
        displayCountry: '이탈리아(EU)',
        authority: 'EU 화장품 규정 (EC No 1223/2009)',
        ingredient: '하이드로퀴논 (Hydroquinone)',
        productHint: '미백·잡티 개선 크림, 톤업크림',
        alternative: '나이아신아마이드, 알부틴 등 EU에서 허용된 미백 성분 제품으로 교체를 추천해요',
        source: 'EU Cosmetics Regulation (EC) No 1223/2009, Annex II',
        lastUpdated: '2024.03 개정',
      },
    };

    // 반입 금지 성분에 해당하면 경고 팝업을 띄우고 true를 반환
    function checkImportBan() {
      const destinationKey = document.getElementById('destinationSelect').value;
      const info = importBanData[destinationKey];
      if (!info) return false;

      document.getElementById('importBanTitle').textContent = `이 제품은 ${info.displayCountry}에서 반입 금지 물품이에요`;
      document.getElementById('importBanMessage').textContent =
        `보유 중인 ${info.productHint} 제품에 포함된 ${info.ingredient} 성분이 ${info.displayCountry} 반입 금지 물질로 분류되어 있어요.`;
      document.getElementById('importBanAuthority').textContent = info.authority;
      document.getElementById('importBanIngredient').textContent = info.ingredient;
      document.getElementById('importBanAlternative').textContent = info.alternative;
      document.getElementById('importBanSource').textContent = `출처 · ${info.source} · ${info.lastUpdated}`;
      document.getElementById('importBanModal').classList.remove('hidden');
      return true;
    }

    // 반입 금지 경고(있다면) 이후 이어지는 흐름: 파우치가 비어있으면 등록을 권하고, 아니면 메인으로
    function continueAfterDestinationRegistration() {
      if (getMyProducts().length === 0) {
        document.getElementById('pouchPromptModal').classList.remove('hidden');
      } else {
        switchTab('inuse');
      }
    }

    document.getElementById('importBanCloseBtn').addEventListener('click', () => {
      document.getElementById('importBanModal').classList.add('hidden');
      continueAfterDestinationRegistration();
    });

    document.getElementById('completeOnboardingBtn').addEventListener('click', () => {
      const result = validateOnboarding();
      if (!result.valid) {
        showWarning('step2Warning', result.customMessage || `${result.missing.join(', ')}을(를) 먼저 입력해주세요`);
        return;
      }
      onboardingComplete = true;
      updateTabLockUI();
      hideWarning('step2Warning');
      if (checkImportBan()) {
        return; // 확인했어요 버튼을 누르면 continueAfterDestinationRegistration()으로 이어짐
      }
      continueAfterDestinationRegistration();
    });

    document.getElementById('pouchPromptYesBtn').addEventListener('click', () => {
      document.getElementById('pouchPromptModal').classList.add('hidden');
      switchTab('pouch');
    });

    document.getElementById('pouchPromptLaterBtn').addEventListener('click', () => {
      document.getElementById('pouchPromptModal').classList.add('hidden');
      switchTab('inuse');
    });

    updateTabLockUI();

    // 국가별 기후 데이터 (전세계 196개국, '리뷰, 국가_수질 추가 DB' 원본의 체감온도·습도·기후·수질 평균값을 반영)
    // 여행지 선택값(destinationSelect)이 국가명 그대로이므로 키도 국가명을 그대로 사용
    const weatherData = {
      가나: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      가봉: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      가이아나: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      감비아: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      과테말라: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      그레나다: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      그리스: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      기니: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      기니비사우: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      나미비아: { temp: 36, humidity: 22, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      나우루: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      나이지리아: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      남수단: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      남아프리카공화국: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      네덜란드: { temp: 22, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      네팔: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      노르웨이: { temp: 5, humidity: 42, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      뉴질랜드: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      니제르: { temp: 35, humidity: 22, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      니카라과: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      대만: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      대한민국: { temp: 23, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      덴마크: { temp: 23, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      도미니카: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      도미니카공화국: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      독일: { temp: 23, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      동티모르: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      라오스: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      라이베리아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      라트비아: { temp: 6, humidity: 42, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      러시아: { temp: 5, humidity: 43, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      레바논: { temp: 22, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      레소토: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      루마니아: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      룩셈부르크: { temp: 22, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      르완다: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      리비아: { temp: 35, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      리투아니아: { temp: 6, humidity: 42, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      리히텐슈타인: { temp: 23, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      마다가스카르: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      마셜제도: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      말라위: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      말레이시아: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      말리: { temp: 36, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      멕시코: { temp: 35, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      모나코: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      모로코: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      모리셔스: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      모리타니: { temp: 33, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      모잠비크: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      몬테네그로: { temp: 23, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      몰도바: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      몰디브: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      몰타: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      몽골: { temp: 23, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      미국: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      미얀마: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      미크로네시아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      바누아투: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      바레인: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      바베이도스: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      바티칸: { temp: 23, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      바하마: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      방글라데시: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      베냉: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      베네수엘라: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      베트남: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      벨기에: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      벨라루스: { temp: 5, humidity: 42, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      벨리즈: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      보스니아헤르체고비나: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      보츠와나: { temp: 35, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      볼리비아: { temp: 33, humidity: 84, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      부룬디: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      부르키나파소: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      부탄: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      북마케도니아: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      북한: { temp: 23, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      불가리아: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      브라질: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      브루나이: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      사모아: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      사우디아라비아: { temp: 33, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      산마리노: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      상투메프린시페: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      세네갈: { temp: 35, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      세르비아: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      세이셸: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      세인트루시아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      세인트빈센트그레나딘: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      세인트키츠네비스: { temp: 33, humidity: 84, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      소말리아: { temp: 33, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      솔로몬제도: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      수단: { temp: 36, humidity: 22, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      수리남: { temp: 33, humidity: 84, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      스리랑카: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      스웨덴: { temp: 5, humidity: 42, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      스위스: { temp: 20, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      스페인: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      슬로바키아: { temp: 21, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      슬로베니아: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      시리아: { temp: 35, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      시에라리온: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      싱가포르: { temp: 34, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수`, en: `Singapore`, lat: 1.3521, lng: 103.8198 },
      아랍에미리트: { temp: 36, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },

      // 지구본 검색용 도시 좌표 (국가 키와 별도로 도시명으로도 검색 가능하게 추가)
      도쿄: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수`, en: `Tokyo`, lat: 35.6762, lng: 139.6503 },
      방콕: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수`, en: `Bangkok`, lat: 13.7563, lng: 100.5018 },
      두바이: { temp: 36, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수`, en: `Dubai`, lat: 25.2048, lng: 55.2708 },
      파리: { temp: 22, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수`, en: `Paris`, lat: 48.8566, lng: 2.3522 },
      밀라노: { temp: 26, humidity: 55, uvi: 7, climate: `건조기후`, waterQuality: `경수`, en: `Milan`, lat: 45.4642, lng: 9.19 },
      판교: { temp: 30, humidity: 70, uvi: 8, climate: `열대기후`, waterQuality: `연수`, en: `Pangyo`, lat: 37.3947, lng: 127.1112 },
      아르메니아: { temp: 36, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      아르헨티나: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      아이슬란드: { temp: 7, humidity: 56, uvi: 2, climate: `한대기후`, waterQuality: `연수` },
      아이티: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      아일랜드: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      아제르바이잔: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      아프가니스탄: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      안도라: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      알바니아: { temp: 23, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      알제리: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      앙골라: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      앤티가바부다: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      에리트레아: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      에스와티니: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      에스토니아: { temp: 5, humidity: 44, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      에콰도르: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      에티오피아: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      엘살바도르: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      영국: { temp: 22, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      예멘: { temp: 35, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      오만: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      오스트리아: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      온두라스: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      요르단: { temp: 34, humidity: 22, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      우간다: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      우루과이: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      우즈베키스탄: { temp: 35, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      우크라이나: { temp: 22, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      이라크: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      이란: { temp: 35, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      이스라엘: { temp: 35, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      이집트: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      이탈리아: { temp: 26, humidity: 47, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      인도: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      인도네시아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      일본: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      자메이카: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      잠비아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      적도기니: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      조지아: { temp: 21, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      중국: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      중앙아프리카공화국: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      지부티: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      짐바브웨: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      차드: { temp: 36, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      체코: { temp: 22, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      칠레: { temp: 23, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      카메룬: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      카보베르데: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      카자흐스탄: { temp: 36, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      카타르: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      캄보디아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      캐나다: { temp: 5, humidity: 42, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      케냐: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      코모로: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      코스타리카: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      코트디부아르: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      콜롬비아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      콩고공화국: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      콩고민주공화국: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      쿠바: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      쿠웨이트: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      크로아티아: { temp: 22, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      키르기스스탄: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      키리바시: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      키프로스: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      타지키스탄: { temp: 34, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      탄자니아: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      태국: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      토고: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      통가: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      투르크메니스탄: { temp: 36, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      투발루: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      튀니지: { temp: 33, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      튀르키예: { temp: 20, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      트리니다드토바고: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `경수` },
      파나마: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      파라과이: { temp: 22, humidity: 52, uvi: 6, climate: `온대기후`, waterQuality: `연수` },
      파키스탄: { temp: 34, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      파푸아뉴기니: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      팔라우: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      팔레스타인: { temp: 36, humidity: 24, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
      페루: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      포르투갈: { temp: 21, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      폴란드: { temp: 21, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      프랑스: { temp: 22, humidity: 56, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      피지: { temp: 33, humidity: 82, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      핀란드: { temp: 6, humidity: 40, uvi: 4, climate: `냉대기후`, waterQuality: `연수` },
      필리핀: { temp: 33, humidity: 83, uvi: 10, climate: `열대기후`, waterQuality: `연수` },
      헝가리: { temp: 20, humidity: 54, uvi: 6, climate: `온대기후`, waterQuality: `경수` },
      호주: { temp: 33, humidity: 26, uvi: 11, climate: `건조기후`, waterQuality: `경수` },
    };

    // 지구본 마커를 클릭했을 때 보여줄 도시별 mock 매장 데이터 (weatherData의 en 필드를 소문자로 변환한 값이 키)
    const storeData = {
      singapore: [
        { name: 'Watsons Orchard', category: '드럭스토어', distance: '0.3km', products: ['진정 크림', '쿨링 미스트'] },
        { name: 'Guardian Bugis', category: '드럭스토어', distance: '0.8km', products: ['수분 세럼', '선크림'] },
        { name: 'Sephora ION', category: '뷰티 편집샵', distance: '1.2km', products: ['진정 마스크팩'] },
      ],
      tokyo: [
        { name: '@cosme store 시부야', category: '뷰티 편집샵', distance: '0.4km', products: ['수분 크림', '아이크림'] },
        { name: '마츠모토키요시 신주쿠', category: '드럭스토어', distance: '0.6km', products: ['선크림', '립밤'] },
        { name: '로프트 긴자', category: '라이프스타일샵', distance: '1.5km', products: ['핸드크림'] },
      ],
      bangkok: [
        { name: 'Eveandboy 시암', category: '뷰티 편집샵', distance: '0.5km', products: ['쿨링 토너', '피지 흡수 패드'] },
        { name: 'Boots 수쿰빗', category: '드럭스토어', distance: '0.9km', products: ['워터프루프 선크림', '미스트'] },
        { name: 'Watsons MBK', category: '드럭스토어', distance: '1.1km', products: ['블로팅 페이퍼'] },
      ],
      dubai: [
        { name: 'Sephora 두바이몰', category: '뷰티 편집샵', distance: '0.7km', products: ['수분 세럼', '저자극 선크림'] },
        { name: 'Boots 알와슬', category: '드럭스토어', distance: '1.0km', products: ['진정 젤', '핸드크림'] },
        { name: 'Bath & Body Works 몰오브에미리츠', category: '라이프스타일샵', distance: '1.8km', products: ['립밤'] },
      ],
      paris: [
        { name: 'Sephora 샹젤리제', category: '뷰티 편집샵', distance: '0.3km', products: ['수분 크림', '립틴트'] },
        { name: 'Monoprix 오페라', category: '드럭스토어', distance: '0.9km', products: ['올인원 로션'] },
        { name: 'Marionnaud 생라자르', category: '뷰티 편집샵', distance: '1.4km', products: ['선쿠션'] },
      ],
      milan: [
        { name: 'Sephora Duomo', category: '뷰티 편집샵', distance: '0.2km', products: ['수분 크림', '립틴트'] },
        { name: 'Douglas 코르소 비토리오 에마누엘레', category: '드럭스토어', distance: '0.5km', products: ['선크림', '핸드크림'] },
        { name: 'Kiko Milano 본점', category: '뷰티 편집샵', distance: '0.8km', products: ['톤업크림', '아이라이너'] },
        { name: 'Rinascente 뷰티 코너', category: '라이프스타일샵', distance: '1.1km', products: ['향수', '립밤'] },
      ],
      pangyo: [
        { name: '올리브영 판교역점', category: '헬스&뷰티', distance: '0.3km', products: ['수분 크림', '선크림'] },
        { name: '시코르 현대백화점 판교점', category: '뷰티 편집샵', distance: '0.6km', products: ['진정 마스크팩', '쿨링 미스트'] },
        { name: '아리따움 판교점', category: '헬스&뷰티', distance: '0.9km', products: ['수분 세럼'] },
      ],
    };

    // 커뮤니티 피드 ('리뷰, 국가_수질 추가 DB' 원본에서 5개 지원 국가 리뷰 전체(국가별 10건, 총 50건) 반영
    const communityReviews = [
      { id: `glowup_diary`, gender: `여성`, age: 26, rating: 3, skinType: `건성`, country: `일본`, cosmetics: `고보습 크림, 립밤, 수분 앰플`, makeup: `촉촉한 쿠션과 크림 블러셔로 생기 있는 룩 연출.`, skincare: `건조한 날씨라 고보습 크림과 앰플로 수분 층 강화.`, review: `가을 날씨라 입술이 자주 텄어요. 립밤 없이는 하루도 못 버텼습니다.` },
      { id: `coolbreeze07`, gender: `남성`, age: 29, rating: 3, skinType: `복합성`, country: `일본`, cosmetics: `올인원 로션, 선크림, 미스트`, makeup: `가벼운 톤업로션 정도로 자연스럽게.`, skincare: `환절기 피부라 올인원 로션으로 간편하게 보습 유지.`, review: `일교차가 커서 아침저녁으로 피부 컨디션이 달랐어요.` },
      { id: `hyejin_92`, gender: `여성`, age: 33, rating: 4, skinType: `민감성`, country: `일본`, cosmetics: `저자극 크림, 진정 토너, 수분 마스크팩`, makeup: `저자극 톤업크림 위주, 색조는 최소화.`, skincare: `일교차로 예민해진 피부에 저자극 진정 라인 사용 권장.`, review: `건조하고 쌀쌀해서 얼굴이 당기고 붉어지는 느낌이 있었어요.` },
      { id: `areum23`, gender: `남성`, age: 45, rating: 4, skinType: `지성`, country: `일본`, cosmetics: `산뜻한 로션, 선크림, 블로팅 페이퍼`, makeup: `가벼운 산뜻한 로션 타입 선호, 유분 적은 제품 위주.`, skincare: `낮 동안 블로팅 페이퍼로 피지 관리.`, review: `날씨는 선선했는데 실내 난방 때문에 오히려 번들거렸어요.` },
      { id: `sora_k`, gender: `여성`, age: 24, rating: 5, skinType: `복합성`, country: `일본`, cosmetics: `수분 크림, 립틴트, 선쿠션`, makeup: `촉촉한 선쿠션 + 립틴트로 화사한 인상 연출.`, skincare: `건조함 방지를 위해 수분 크림 두껍게 레이어링.`, review: `실내외 온도차가 커서 수분크림을 자주 덧발라야 했어요.` },
      { id: `jetsetter_k`, gender: `남성`, age: 25, rating: 5, skinType: `민감성`, country: `일본`, cosmetics: `수분 크림, 립틴트, 선쿠션`, makeup: `촉촉한 쿠션과 크림 블러셔로 생기 있는 룩을 연출하는 것을 추천합니다.`, skincare: `환절기 피부 컨디션 변화에 대비해 올인원 로션으로 간편하게 보습을 유지하세요.`, review: `사계절이 뚜렷한 곳이라 그런지 여행 기간 내내 온도 변화에 신경 써야 했어요.` },
      { id: `clearskin_92`, gender: `여성`, age: 32, rating: 2, skinType: `민감성`, country: `일본`, cosmetics: `수분 크림, 선크림, 립밤`, makeup: `가벼운 톤업로션 정도로 자연스럽게 표현하는 메이크업이 잘 어울립니다.`, skincare: `일교차로 예민해지기 쉬운 피부에는 저자극 진정 라인 사용을 권장합니다.`, review: `생각보다 자외선이 강해서 선크림을 안 쓰면 금방 붉어졌어요.` },
      { id: `quinn_vibe`, gender: `남성`, age: 39, rating: 4, skinType: `민감성`, country: `일본`, cosmetics: `올인원 로션, 선크림, 미스트`, makeup: `저자극 톤업크림 위주로 하고 색조는 최소화하는 것을 권장합니다.`, skincare: `실내 난방·냉방으로 건조해지기 쉬우니 블로팅 페이퍼와 미스트를 함께 챙기세요.`, review: `쾌적한 날씨였지만 건조해서 립밤과 수분크림을 자주 발라야 했어요.` },
      { id: `beautyaddict07`, gender: `여성`, age: 46, rating: 4, skinType: `민감성`, country: `일본`, cosmetics: `저자극 크림, 진정 토너, 수분 마스크팩`, makeup: `가벼운 산뜻한 로션 타입으로 유분이 적은 제품 위주로 사용하세요.`, skincare: `실내외 온도차가 큰 날에는 수분크림을 자주 덧발라 주는 것이 좋습니다.`, review: `일교차가 커서 아침저녁으로 피부 컨디션이 완전히 달랐어요. 저자극 크림이 도움이 됐어요.` },
      { id: `jiyeon_life`, gender: `남성`, age: 53, rating: 5, skinType: `민감성`, country: `일본`, cosmetics: `산뜻한 로션, 선크림, 블로팅 페이퍼`, makeup: `촉촉한 선쿠션과 립틴트로 화사한 인상을 연출할 수 있습니다.`, skincare: `일교차가 크므로 수분 크림으로 아침저녁 보습을 꼼꼼히 챙겨주세요.`, review: `날씨는 선선했는데 실내 난방 때문에 오히려 피부가 건조하고 번들거렸어요.` },
      { id: `sunnytraveler23`, gender: `여성`, age: 54, rating: 3, skinType: `복합성`, country: `태국`, cosmetics: `가벼운 수분 선크림, 쿠션, 미스트`, makeup: `워터프루프 아이라이너와 마스카라로 땀과 습기에 대비하는 것이 좋습니다.`, skincare: `저녁에 이중세안을 꼭 하고 산뜻한 젤 타입 제품으로 유수분 밸런스를 유지하세요.`, review: `생각보다 더 더워서 땀 때문에 끈적임이 심했는데 가벼운 수분 선크림이 정말 큰 도움이 됐습니다.` },
      { id: `dahye_life`, gender: `남성`, age: 21, rating: 5, skinType: `복합성`, country: `태국`, cosmetics: `워터프루프 아이라이너, 피지 흡수 패드, 쿨링 젤`, makeup: `얇은 베이스에 워터프루프 제품 위주로 메이크업하고 픽싱 스프레이로 마무리하는 것을 추천합니다.`, skincare: `외출 중 블로팅 페이퍼로 피지를 자주 관리하고 쿨링 토너로 진정시켜 주세요.`, review: `야외 일정이 많았는데 자외선이 강해서 워터프루프 아이라이너을 자주 덧발라야 했어요.` },
      { id: `sunnytraveler_log`, gender: `여성`, age: 28, rating: 2, skinType: `복합성`, country: `태국`, cosmetics: `워터프루프 선크림, 피지 컨트롤 파우더, 픽싱 미스트`, makeup: `매트한 베이스로 유분과 땀을 컨트롤하며 색조는 최소화하는 것이 좋습니다.`, skincare: `자외선 노출 후에는 진정 스프레이와 수분 시트마스크로 피부를 달래주는 것이 좋습니다.`, review: `고온다습한 날씨 탓에 피부 트러블이 갑자기 올라와서 당황했어요.` },
      { id: `desertrose_life`, gender: `남성`, age: 35, rating: 2, skinType: `복합성`, country: `태국`, cosmetics: `매트 선크림, 블로팅 페이퍼, 쿨링 토너`, makeup: `촉촉한 쿠션으로 습기에도 밀리지 않게 가볍게 표현하는 것을 추천합니다.`, skincare: `실내외 온습도 차이가 크므로 미스트로 수시로 수분을 보충해 주세요.`, review: `에어컨 실내와 습한 실외를 오가다 보니 피부 컨디션이 계속 오락가락했어요.` },
      { id: `glowygirl_life`, gender: `여성`, age: 42, rating: 4, skinType: `복합성`, country: `태국`, cosmetics: `저자극 선크림, 진정 스프레이, 수분 시트마스크`, makeup: `색조보다는 톤업 선크림 위주로 산뜻하게 마무리하는 것을 권장합니다.`, skincare: `피지 분비가 많아지는 시기이므로 클레이 마스크로 주 1~2회 관리해 주는 것을 추천합니다.`, review: `습도가 정말 높아서 화장이 금방 무너졌어요. 저자극 선크림 없이는 하루도 버티기 힘들었어요.` },
      { id: `nomakeupdays_story`, gender: `남성`, age: 49, rating: 4, skinType: `복합성`, country: `태국`, cosmetics: `가벼운 수분 선크림, 쿠션, 미스트`, makeup: `워터프루프 아이라이너와 마스카라로 땀과 습기에 대비하는 것이 좋습니다.`, skincare: `저녁에 이중세안을 꼭 하고 산뜻한 젤 타입 제품으로 유수분 밸런스를 유지하세요.`, review: `생각보다 더 더워서 땀 때문에 끈적임이 심했는데 가벼운 수분 선크림이 정말 큰 도움이 됐습니다.` },
      { id: `jiwoo_mode`, gender: `여성`, age: 56, rating: 4, skinType: `복합성`, country: `태국`, cosmetics: `워터프루프 아이라이너, 피지 흡수 패드, 쿨링 젤`, makeup: `얇은 베이스에 워터프루프 제품 위주로 메이크업하고 픽싱 스프레이로 마무리하는 것을 추천합니다.`, skincare: `외출 중 블로팅 페이퍼로 피지를 자주 관리하고 쿨링 토너로 진정시켜 주세요.`, review: `야외 일정이 많았는데 자외선이 강해서 워터프루프 아이라이너을 자주 덧발라야 했어요.` },
      { id: `hydrated_log`, gender: `남성`, age: 23, rating: 4, skinType: `복합성`, country: `태국`, cosmetics: `워터프루프 선크림, 피지 컨트롤 파우더, 픽싱 미스트`, makeup: `매트한 베이스로 유분과 땀을 컨트롤하며 색조는 최소화하는 것이 좋습니다.`, skincare: `자외선 노출 후에는 진정 스프레이와 수분 시트마스크로 피부를 달래주는 것이 좋습니다.`, review: `고온다습한 날씨 탓에 피부 트러블이 갑자기 올라와서 당황했어요.` },
      { id: `serumfan_k`, gender: `여성`, age: 30, rating: 1, skinType: `복합성`, country: `태국`, cosmetics: `매트 선크림, 블로팅 페이퍼, 쿨링 토너`, makeup: `촉촉한 쿠션으로 습기에도 밀리지 않게 가볍게 표현하는 것을 추천합니다.`, skincare: `실내외 온습도 차이가 크므로 미스트로 수시로 수분을 보충해 주세요.`, review: `에어컨 실내와 습한 실외를 오가다 보니 피부 컨디션이 계속 오락가락했어요.` },
      { id: `sunkissed07`, gender: `남성`, age: 37, rating: 4, skinType: `복합성`, country: `태국`, cosmetics: `저자극 선크림, 진정 스프레이, 수분 시트마스크`, makeup: `색조보다는 톤업 선크림 위주로 산뜻하게 마무리하는 것을 권장합니다.`, skincare: `피지 분비가 많아지는 시기이므로 클레이 마스크로 주 1~2회 관리해 주는 것을 추천합니다.`, review: `습도가 정말 높아서 화장이 금방 무너졌어요. 저자극 선크림 없이는 하루도 버티기 힘들었어요.` },
      { id: `desertrose99`, gender: `여성`, age: 22, rating: 1, skinType: `건성`, country: `아랍에미리트`, cosmetics: `저자극 선크림, 진정 젤, 수분 세럼`, makeup: `가벼운 수분 쿠션으로 건조함을 커버하며 자연스러운 룩을 연출하세요.`, skincare: `낮은 습도로 인한 수분 손실을 막기 위해 고보습 크림을 겹겹이 발라주세요.`, review: `사막성 기후라 그런지 평소보다 피부가 훨씬 건조해지는 걸 느꼈어요.` },
      { id: `hana99`, gender: `남성`, age: 29, rating: 4, skinType: `건성`, country: `아랍에미리트`, cosmetics: `수분 로션, 선크림, 핸드크림`, makeup: `고보습 베이스 제품으로 들뜸 없이 매끈한 피부 표현이 가능합니다.`, skincare: `입술과 손이 트기 쉬우므로 립밤과 핸드크림을 항상 휴대하는 것이 좋습니다.`, review: `낮은 습도 때문에 피부가 계속 당기고 화장이 들떴어요. 수분 로션이 필수였습니다.` },
      { id: `clearskin_vibe`, gender: `여성`, age: 36, rating: 2, skinType: `건성`, country: `아랍에미리트`, cosmetics: `고SPF 선크림, 쿨링 미스트, 립밤`, makeup: `립 제품은 보습 밤 타입을 선택해 건조함으로 인한 각질을 예방하세요.`, skincare: `건조한 기후이므로 미스트를 수시로 뿌려 수분을 보충하는 것이 중요합니다.`, review: `일교차가 커서 낮에는 덥고 밤에는 쌀쌀해 피부가 예민해졌어요.` },
      { id: `jiwoo_log`, gender: `남성`, age: 43, rating: 4, skinType: `건성`, country: `아랍에미리트`, cosmetics: `수분 크림, 선쿠션, 진정 스프레이`, makeup: `촉촉한 베이스에 크림 타입 블러셔로 생기를 더하는 메이크업을 추천합니다.`, skincare: `강한 햇빛 대비 SPF 높은 제품을 사용하고 쿨링 미스트로 열감을 진정시켜 주세요.`, review: `건조한 바람 때문에 입술과 볼이 자주 텄어요. 수분 크림 없이는 힘들었을 것 같아요.` },
      { id: `islandhopper_log`, gender: `여성`, age: 50, rating: 4, skinType: `건성`, country: `아랍에미리트`, cosmetics: `고보습 선크림, 미스트, 영양 크림`, makeup: `메이크업은 최소화하고 톤업 선크림으로 자연스럽게 마무리하는 것을 권장합니다.`, skincare: `자외선 노출 후 진정 젤로 쿨다운하고 세럼으로 수분을 채워주는 것을 추천합니다.`, review: `햇빛이 강렬해서 선크림을 2~3시간마다 덧발라야 했어요.` },
      { id: `hydrationqueen_official`, gender: `남성`, age: 57, rating: 5, skinType: `건성`, country: `아랍에미리트`, cosmetics: `저자극 선크림, 진정 젤, 수분 세럼`, makeup: `가벼운 수분 쿠션으로 건조함을 커버하며 자연스러운 룩을 연출하세요.`, skincare: `낮은 습도로 인한 수분 손실을 막기 위해 고보습 크림을 겹겹이 발라주세요.`, review: `사막성 기후라 그런지 평소보다 피부가 훨씬 건조해지는 걸 느꼈어요.` },
      { id: `seojun_story`, gender: `여성`, age: 24, rating: 2, skinType: `건성`, country: `아랍에미리트`, cosmetics: `수분 로션, 선크림, 핸드크림`, makeup: `고보습 베이스 제품으로 들뜸 없이 매끈한 피부 표현이 가능합니다.`, skincare: `입술과 손이 트기 쉬우므로 립밤과 핸드크림을 항상 휴대하는 것이 좋습니다.`, review: `낮은 습도 때문에 피부가 계속 당기고 화장이 들떴어요. 수분 로션이 필수였습니다.` },
      { id: `mattefinish_official`, gender: `남성`, age: 31, rating: 5, skinType: `건성`, country: `아랍에미리트`, cosmetics: `고SPF 선크림, 쿨링 미스트, 립밤`, makeup: `립 제품은 보습 밤 타입을 선택해 건조함으로 인한 각질을 예방하세요.`, skincare: `건조한 기후이므로 미스트를 수시로 뿌려 수분을 보충하는 것이 중요합니다.`, review: `일교차가 커서 낮에는 덥고 밤에는 쌀쌀해 피부가 예민해졌어요.` },
      { id: `makeupfan_zone`, gender: `여성`, age: 38, rating: 5, skinType: `건성`, country: `아랍에미리트`, cosmetics: `수분 크림, 선쿠션, 진정 스프레이`, makeup: `촉촉한 베이스에 크림 타입 블러셔로 생기를 더하는 메이크업을 추천합니다.`, skincare: `강한 햇빛 대비 SPF 높은 제품을 사용하고 쿨링 미스트로 열감을 진정시켜 주세요.`, review: `건조한 바람 때문에 입술과 볼이 자주 텄어요. 수분 크림 없이는 힘들었을 것 같아요.` },
      { id: `frostyvibe23`, gender: `남성`, age: 45, rating: 3, skinType: `건성`, country: `아랍에미리트`, cosmetics: `고보습 선크림, 미스트, 영양 크림`, makeup: `메이크업은 최소화하고 톤업 선크림으로 자연스럽게 마무리하는 것을 권장합니다.`, skincare: `자외선 노출 후 진정 젤로 쿨다운하고 세럼으로 수분을 채워주는 것을 추천합니다.`, review: `햇빛이 강렬해서 선크림을 2~3시간마다 덧발라야 했어요.` },
      { id: `wanderlust_log`, gender: `여성`, age: 34, rating: 3, skinType: `복합성`, country: `프랑스`, cosmetics: `산뜻한 로션, 선크림, 블로팅 페이퍼`, makeup: `촉촉한 선쿠션과 립틴트로 화사한 인상을 연출할 수 있습니다.`, skincare: `일교차가 크므로 수분 크림으로 아침저녁 보습을 꼼꼼히 챙겨주세요.`, review: `날씨는 선선했는데 실내 난방 때문에 오히려 피부가 건조하고 번들거렸어요.` },
      { id: `tropicalgirl_official`, gender: `남성`, age: 41, rating: 5, skinType: `복합성`, country: `프랑스`, cosmetics: `수분 크림, 립틴트, 선쿠션`, makeup: `촉촉한 쿠션과 크림 블러셔로 생기 있는 룩을 연출하는 것을 추천합니다.`, skincare: `환절기 피부 컨디션 변화에 대비해 올인원 로션으로 간편하게 보습을 유지하세요.`, review: `사계절이 뚜렷한 곳이라 그런지 여행 기간 내내 온도 변화에 신경 써야 했어요.` },
      { id: `yuna_diary`, gender: `여성`, age: 48, rating: 3, skinType: `복합성`, country: `프랑스`, cosmetics: `수분 크림, 선크림, 립밤`, makeup: `가벼운 톤업로션 정도로 자연스럽게 표현하는 메이크업이 잘 어울립니다.`, skincare: `일교차로 예민해지기 쉬운 피부에는 저자극 진정 라인 사용을 권장합니다.`, review: `생각보다 자외선이 강해서 선크림을 안 쓰면 금방 붉어졌어요.` },
      { id: `haru_note`, gender: `남성`, age: 55, rating: 1, skinType: `복합성`, country: `프랑스`, cosmetics: `올인원 로션, 선크림, 미스트`, makeup: `저자극 톤업크림 위주로 하고 색조는 최소화하는 것을 권장합니다.`, skincare: `실내 난방·냉방으로 건조해지기 쉬우니 블로팅 페이퍼와 미스트를 함께 챙기세요.`, review: `쾌적한 날씨였지만 건조해서 립밤과 수분크림을 자주 발라야 했어요.` },
      { id: `dewyskin_k`, gender: `여성`, age: 22, rating: 5, skinType: `복합성`, country: `프랑스`, cosmetics: `저자극 크림, 진정 토너, 수분 마스크팩`, makeup: `가벼운 산뜻한 로션 타입으로 유분이 적은 제품 위주로 사용하세요.`, skincare: `실내외 온도차가 큰 날에는 수분크림을 자주 덧발라 주는 것이 좋습니다.`, review: `일교차가 커서 아침저녁으로 피부 컨디션이 완전히 달랐어요. 저자극 크림이 도움이 됐어요.` },
      { id: `toneuplife_world`, gender: `남성`, age: 29, rating: 4, skinType: `복합성`, country: `프랑스`, cosmetics: `산뜻한 로션, 선크림, 블로팅 페이퍼`, makeup: `촉촉한 선쿠션과 립틴트로 화사한 인상을 연출할 수 있습니다.`, skincare: `일교차가 크므로 수분 크림으로 아침저녁 보습을 꼼꼼히 챙겨주세요.`, review: `날씨는 선선했는데 실내 난방 때문에 오히려 피부가 건조하고 번들거렸어요.` },
      { id: `somin99`, gender: `여성`, age: 36, rating: 4, skinType: `복합성`, country: `프랑스`, cosmetics: `수분 크림, 립틴트, 선쿠션`, makeup: `촉촉한 쿠션과 크림 블러셔로 생기 있는 룩을 연출하는 것을 추천합니다.`, skincare: `환절기 피부 컨디션 변화에 대비해 올인원 로션으로 간편하게 보습을 유지하세요.`, review: `사계절이 뚜렷한 곳이라 그런지 여행 기간 내내 온도 변화에 신경 써야 했어요.` },
      { id: `roadtripper88`, gender: `남성`, age: 43, rating: 2, skinType: `복합성`, country: `프랑스`, cosmetics: `수분 크림, 선크림, 립밤`, makeup: `가벼운 톤업로션 정도로 자연스럽게 표현하는 메이크업이 잘 어울립니다.`, skincare: `일교차로 예민해지기 쉬운 피부에는 저자극 진정 라인 사용을 권장합니다.`, review: `생각보다 자외선이 강해서 선크림을 안 쓰면 금방 붉어졌어요.` },
      { id: `iseul_k`, gender: `여성`, age: 50, rating: 4, skinType: `복합성`, country: `프랑스`, cosmetics: `올인원 로션, 선크림, 미스트`, makeup: `저자극 톤업크림 위주로 하고 색조는 최소화하는 것을 권장합니다.`, skincare: `실내 난방·냉방으로 건조해지기 쉬우니 블로팅 페이퍼와 미스트를 함께 챙기세요.`, review: `쾌적한 날씨였지만 건조해서 립밤과 수분크림을 자주 발라야 했어요.` },
      { id: `desertrose_diary`, gender: `남성`, age: 57, rating: 5, skinType: `복합성`, country: `프랑스`, cosmetics: `저자극 크림, 진정 토너, 수분 마스크팩`, makeup: `가벼운 산뜻한 로션 타입으로 유분이 적은 제품 위주로 사용하세요.`, skincare: `실내외 온도차가 큰 날에는 수분크림을 자주 덧발라 주는 것이 좋습니다.`, review: `일교차가 커서 아침저녁으로 피부 컨디션이 완전히 달랐어요. 저자극 크림이 도움이 됐어요.` },
      { id: `yeji_life`, gender: `여성`, age: 27, rating: 5, skinType: `지성`, country: `싱가포르`, cosmetics: `피지 컨트롤 파우더, 워터프루프 선크림, 미스트`, makeup: `베이스는 얇게, 픽싱 스프레이로 마무리해 번들거림 방지. 아이라이너는 워터프루프 필수.`, skincare: `저녁에 이중세안 필수, 가벼운 젤 타입 로션 위주로 유수분 밸런스 유지.`, review: `습도가 높아서 파운데이션이 계속 뜨더라고요. 워터프루프 제품 없이는 3시간도 못 버텼어요.` },
      { id: `funtraveler_world`, gender: `남성`, age: 34, rating: 3, skinType: `복합성`, country: `싱가포르`, cosmetics: `선크림 SPF50+, 블로팅 페이퍼, 쿨링 토너`, makeup: `남성용 톤업크림 정도만 가볍게, 유분 많은 제품은 피하기.`, skincare: `외출 전후 블로팅 페이퍼로 피지 제거, 쿨링 토너로 진정.`, review: `야외 일정이 많았는데 선크림 안 바르면 바로 붉어졌어요. 자주 덧발라야 합니다.` },
      { id: `backpacklife_daily`, gender: `여성`, age: 22, rating: 4, skinType: `건성`, country: `싱가포르`, cosmetics: `수분 세럼, 저자극 선크림, 쿠션 팩트`, makeup: `쿠션은 촉촉 타입으로, 하이라이터는 최소화.`, skincare: `에어컨 실내가 많아 건조해지기 쉬우니 수분 세럼 필수 휴대.`, review: `실내는 에어컨 때문에 건조하고 밖은 습해서 피부가 오락가락했어요.` },
      { id: `backpacklife_ing`, gender: `남성`, age: 41, rating: 4, skinType: `민감성`, country: `싱가포르`, cosmetics: `저자극 선크림, 진정 스프레이, 쿨링 시트마스크`, makeup: `메이크업은 생략 권장, 톤업 선크림으로 대체.`, skincare: `자외선 노출 후 진정 스프레이로 즉시 쿨링, 저녁엔 시트마스크로 진정 케어.`, review: `더위에 피부가 예민해져서 평소 안 쓰던 진정 제품을 계속 챙겨 발랐어요.` },
      { id: `sensitiveskin_love`, gender: `여성`, age: 30, rating: 5, skinType: `지성`, country: `싱가포르`, cosmetics: `매트 선크림, 픽싱 스프레이, 유분 흡수 패드`, makeup: `매트 베이스 + 픽싱 스프레이 조합으로 지속력 강화.`, skincare: `낮 동안 유분 흡수 패드로 T존 관리, 밤엔 클레이 마스크 추천.`, review: `사진 찍을 일이 많았는데 매트 선크림 덕분에 오래 유지됐어요.` },
      { id: `calmnface_life`, gender: `남성`, age: 23, rating: 5, skinType: `지성`, country: `싱가포르`, cosmetics: `저자극 선크림, 진정 스프레이, 수분 시트마스크`, makeup: `색조보다는 톤업 선크림 위주로 산뜻하게 마무리하는 것을 권장합니다.`, skincare: `피지 분비가 많아지는 시기이므로 클레이 마스크로 주 1~2회 관리해 주는 것을 추천합니다.`, review: `습도가 정말 높아서 화장이 금방 무너졌어요. 저자극 선크림 없이는 하루도 버티기 힘들었어요.` },
      { id: `chillmode07`, gender: `여성`, age: 30, rating: 1, skinType: `지성`, country: `싱가포르`, cosmetics: `가벼운 수분 선크림, 쿠션, 미스트`, makeup: `워터프루프 아이라이너와 마스카라로 땀과 습기에 대비하는 것이 좋습니다.`, skincare: `저녁에 이중세안을 꼭 하고 산뜻한 젤 타입 제품으로 유수분 밸런스를 유지하세요.`, review: `생각보다 더 더워서 땀 때문에 끈적임이 심했는데 가벼운 수분 선크림이 정말 큰 도움이 됐습니다.` },
      { id: `frostyvibe_daily`, gender: `남성`, age: 37, rating: 4, skinType: `지성`, country: `싱가포르`, cosmetics: `워터프루프 아이라이너, 피지 흡수 패드, 쿨링 젤`, makeup: `얇은 베이스에 워터프루프 제품 위주로 메이크업하고 픽싱 스프레이로 마무리하는 것을 추천합니다.`, skincare: `외출 중 블로팅 페이퍼로 피지를 자주 관리하고 쿨링 토너로 진정시켜 주세요.`, review: `야외 일정이 많았는데 자외선이 강해서 워터프루프 아이라이너을 자주 덧발라야 했어요.` },
      { id: `jaewon_diary`, gender: `여성`, age: 44, rating: 5, skinType: `지성`, country: `싱가포르`, cosmetics: `워터프루프 선크림, 피지 컨트롤 파우더, 픽싱 미스트`, makeup: `매트한 베이스로 유분과 땀을 컨트롤하며 색조는 최소화하는 것이 좋습니다.`, skincare: `자외선 노출 후에는 진정 스프레이와 수분 시트마스크로 피부를 달래주는 것이 좋습니다.`, review: `고온다습한 날씨 탓에 피부 트러블이 갑자기 올라와서 당황했어요.` },
      { id: `serumfan01`, gender: `남성`, age: 51, rating: 3, skinType: `지성`, country: `싱가포르`, cosmetics: `매트 선크림, 블로팅 페이퍼, 쿨링 토너`, makeup: `촉촉한 쿠션으로 습기에도 밀리지 않게 가볍게 표현하는 것을 추천합니다.`, skincare: `실내외 온습도 차이가 크므로 미스트로 수시로 수분을 보충해 주세요.`, review: `에어컨 실내와 습한 실외를 오가다 보니 피부 컨디션이 계속 오락가락했어요.` },
      { id: `sunnykiss_roma`, gender: `여성`, age: 26, rating: 5, skinType: `건성`, country: `이탈리아`, cosmetics: `저자극 선크림, 수분 크림, 립밤`, makeup: `촉촉한 쿠션으로 건조함을 가려주고 립밤을 자주 덧발라주세요.`, skincare: `자외선이 강해 저자극 선크림을 2~3시간마다 덧바르고, 밤에는 고보습 크림으로 마무리하세요.`, review: `로마는 해가 정말 강해서 선크림 없이는 하루도 못 버텼어요. 걷다 보면 입술도 금방 트더라고요.` },
      { id: `pastachef_mimo`, gender: `남성`, age: 33, rating: 4, skinType: `복합성`, country: `이탈리아`, cosmetics: `올인원 로션, 톤업 선크림`, makeup: `간단하게 톤업 선크림만 발라도 자연스러운 피부 표현이 가능합니다.`, skincare: `낮에는 가벼운 로션, 저녁엔 이중세안으로 하루종일 쌓인 유분을 깨끗이 씻어내세요.`, review: `낮엔 건조한데 저녁엔 유분이 올라와서 복합성 피부 관리가 애매했어요. 로션 하나로 버티기엔 부족했습니다.` },
      { id: `gelato_girl92`, gender: `여성`, age: 24, rating: 3, skinType: `지성`, country: `이탈리아`, cosmetics: `피지 컨트롤 파우더, 블로팅 페이퍼`, makeup: `베이스는 얇게 펴 바르고 픽싱 스프레이로 유지력을 높이세요.`, skincare: `외출 중 블로팅 페이퍼로 피지를 자주 정리하고 저녁엔 약산성 클렌저로 세안하세요.`, review: `생각보다 햇볕이 강해서 피지가 많이 올라왔어요. 블로팅 페이퍼가 정말 필수였습니다.` },
      { id: `duomo_wanderer`, gender: `남성`, age: 45, rating: 5, skinType: `민감성`, country: `이탈리아`, cosmetics: `저자극 진정 크림, 무향 선크림`, makeup: `자극이 적은 무향 제품 위주로 가볍게 사용하는 것이 좋습니다.`, skincare: `강한 자외선에 피부가 쉽게 붉어져서 저자극 진정 크림으로 꾸준히 관리했습니다.`, review: `두오모 광장에서 오래 걸었더니 얼굴이 금방 붉어지더라고요. 진정 크림 없이는 힘들었을 것 같아요.` },
      { id: `veneto_breeze`, gender: `여성`, age: 31, rating: 4, skinType: `건성`, country: `이탈리아`, cosmetics: `고보습 세럼, 미스트, 립밤`, makeup: `수분감 있는 쿠션으로 건조함을 커버하는 것을 추천합니다.`, skincare: `건조한 바람 때문에 수시로 미스트를 뿌려주고 자기 전엔 고보습 세럼을 겹겹이 발라주세요.`, review: `베네치아는 바람이 많이 불어서 피부가 계속 당기는 느낌이었어요. 미스트를 손에서 놓을 수가 없었습니다.` },
      { id: `espresso_daily`, gender: `남성`, age: 28, rating: 3, skinType: `지성`, country: `이탈리아`, cosmetics: `선크림 SPF50+, 쿨링 토너`, makeup: `유분이 적은 제품 위주로 가볍게 사용하세요.`, skincare: `낮 동안 쌓인 유분과 열기를 쿨링 토너로 진정시켜주는 게 도움이 됩니다.`, review: `카페 투어 다니면서 뜨거운 햇볕 아래 오래 있었더니 얼굴이 번들거리더라고요. 쿨링 토너가 큰 도움이 됐습니다.` },
      { id: `tuscan_sunny`, gender: `여성`, age: 37, rating: 5, skinType: `복합성`, country: `이탈리아`, cosmetics: `수분 크림, 피지 조절 로션`, makeup: `T존은 가볍게, 볼은 촉촉하게 이중 관리하는 것을 추천합니다.`, skincare: `부위별로 다르게 관리해야 해서 T존엔 산뜻한 로션, 볼엔 수분 크림을 따로 발랐어요.`, review: `토스카나 시골길을 걸을 때마다 볼은 건조하고 T존은 번들거려서 부위별 관리가 필요했어요.` },
      { id: `milano_walker`, gender: `남성`, age: 40, rating: 4, skinType: `민감성`, country: `이탈리아`, cosmetics: `저자극 로션, 진정 젤`, makeup: `자극적인 성분이 없는 제품으로 최소한만 사용하세요.`, skincare: `도심 매장을 오래 돌아다니느라 자외선과 스트레스에 피부가 예민해져서 진정 젤로 자주 케어했습니다.`, review: `밀라노에서 종일 쇼핑하며 걸었더니 피부가 화끈거리더라고요. 진정 젤이 없었으면 고생했을 것 같아요.` },
      { id: `cinquestrada`, gender: `여성`, age: 29, rating: 4, skinType: `건성`, country: `이탈리아`, cosmetics: `수분 앰플, 저자극 선크림`, makeup: `촉촉한 베이스 위에 가볍게 파우더만 얹는 정도로 마무리하세요.`, skincare: `해안가 마을을 걷다 보니 소금기와 바람에 피부가 쉽게 건조해져서 수분 앰플로 집중 케어했어요.`, review: `친퀘테레 절벽길을 걷는 내내 바닷바람에 피부가 뻣뻣해지는 느낌이었어요. 앰플 없인 힘들었을 거예요.` },
      { id: `romanholiday7`, gender: `여성`, age: 34, rating: 5, skinType: `복합성`, country: `이탈리아`, cosmetics: `수분 크림, 피지 흡수 패드, 선크림`, makeup: `이른 아침엔 촉촉하게, 낮엔 피지 흡수 패드로 유지력을 챙기세요.`, skincare: `아침저녁 온도차가 커서 아침엔 수분 크림, 낮엔 피지 관리로 이원화했습니다.`, review: `아침엔 쌀쌀하고 낮엔 뜨거워서 하루에도 피부 상태가 계속 바뀌더라고요. 시간대별로 다르게 관리해야 했어요.` },
    ];

    // 리뷰 ID를 시드로 항상 같은 조합이 나오는 귀여운 닉네임 생성 (수분/피부 관련 단어 + 동물 이름)
    const nicknameWords = ['고보습', '산뜻한', '촉촉한', '진정력만렙', '수분폭탄', '유수분밸런스', '트러블제로', '광채나는', '뽀송뽀송', '탱글탱글'];
    const nicknameAnimals = ['두더지', '라마', '수달', '코알라', '판다', '여우', '펭귄', '토끼', '고슴도치', '알파카'];
    function hashStringToInt(str) {
      let hash = 0;
      for (let i = 0; i < str.length; i++) {
        hash = (hash * 31 + str.charCodeAt(i)) >>> 0;
      }
      return hash;
    }
    function getNicknameForId(id) {
      const hash = hashStringToInt(id);
      const wordIndex = hash % nicknameWords.length;
      const animalIndex = Math.floor(hash / nicknameWords.length) % nicknameAnimals.length;
      return `${nicknameWords[wordIndex]} ${nicknameAnimals[animalIndex]}`;
    }

    // 피부타입별 아바타 배경 파스텔 컬러 (지성=블루, 건성=오렌지, 복합성=퍼플, 민감성=그린)
    function getSkinTypeAvatarBg(skinType) {
      const bgMap = { 지성: 'bg-blue-100', 건성: 'bg-orange-100', 복합성: 'bg-purple-100', 민감성: 'bg-green-100' };
      return bgMap[skinType] || 'bg-gray-100';
    }

    function renderStars(rating) {
      const filled = '★'.repeat(rating);
      const empty = '★'.repeat(5 - rating);
      return `<span class="text-brand-500">${filled}</span><span class="text-gray-300">${empty}</span>`;
    }

    function getAgeGroup(age) {
      if (age < 30) return '20대';
      if (age < 40) return '30대';
      if (age < 50) return '40대';
      return '50대 이상';
    }

    function renderCommunityFeed() {
      const countryFilter = document.getElementById('communityCountryFilter').value;
      const genderFilter = document.getElementById('communityGenderFilter').value;
      const ageFilter = document.getElementById('communityAgeFilter').value;
      const skinFilter = document.getElementById('communitySkinFilter').value;

      const filtered = communityReviews.filter((post) => {
        if (countryFilter && post.country !== countryFilter) return false;
        if (genderFilter && post.gender !== genderFilter) return false;
        if (ageFilter && getAgeGroup(post.age) !== ageFilter) return false;
        if (skinFilter && post.skinType !== skinFilter) return false;
        return true;
      });

      const communityFeed = document.getElementById('communityFeed');
      const emptyNote = document.getElementById('communityEmptyNote');
      communityFeed.innerHTML = '';
      emptyNote.classList.toggle('hidden', filtered.length > 0);

      filtered.forEach((post) => {
        const card = document.createElement('div');
        card.className = 'bg-white border border-gray-100 rounded-xl p-4';
        card.innerHTML = `
          <div class="flex items-center gap-3 mb-2">
            <div class="w-11 h-11 rounded-full ${getSkinTypeAvatarBg(post.skinType)} shrink-0 relative overflow-hidden">
              <img src="https://api.dicebear.com/9.x/personas/svg?seed=${encodeURIComponent(post.id)}" alt="${post.id}" class="absolute inset-0 z-10 w-full h-full object-cover bg-white" onerror="this.style.display='none';" />
              <div class="absolute inset-0 flex items-center justify-center text-gray-600 text-sm font-bold">${post.id.charAt(0).toUpperCase()}</div>
            </div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-bold truncate">${getNicknameForId(post.id)}</p>
              <span class="block text-[11px] text-gray-400 truncate">@${post.id} · ${post.country} 여행 · ${post.gender} · ${post.age}세 · ${post.skinType} 피부</span>
            </div>
            <p class="text-xs shrink-0">${renderStars(post.rating)}</p>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed mb-2">${post.review}</p>
          <button type="button" class="more-btn text-xs font-semibold text-brand-500">더보기</button>
          <div class="more-detail hidden mt-2 pt-2 border-t border-gray-100 space-y-1.5">
            <p class="text-xs text-gray-500"><span class="font-semibold text-gray-700">추천 화장품</span> · ${post.cosmetics}</p>
            <p class="text-xs text-gray-500"><span class="font-semibold text-gray-700">추천 메이크업</span> · ${post.makeup}</p>
            <p class="text-xs text-gray-500"><span class="font-semibold text-gray-700">추천 스킨케어</span> · ${post.skincare}</p>
          </div>
        `;
        const moreBtn = card.querySelector('.more-btn');
        const detail = card.querySelector('.more-detail');
        moreBtn.addEventListener('click', () => {
          const isHidden = detail.classList.toggle('hidden');
          moreBtn.textContent = isHidden ? '더보기' : '접기';
        });
        communityFeed.appendChild(card);
      });
    }

    // 커뮤니티 탭에 처음 들어올 때만 기본 필터를 이탈리아로 고정 (이후엔 사용자가 고른 필터를 유지)
    let communityDefaultApplied = false;
    function applyDefaultCommunityFilter() {
      document.getElementById('communityCountryFilter').value = '이탈리아';
    }

    ['communityCountryFilter', 'communityGenderFilter', 'communityAgeFilter', 'communitySkinFilter'].forEach((id) => {
      document.getElementById(id).addEventListener('change', renderCommunityFeed);
    });
    renderCommunityFeed();

    // 개인설정 탭에 등록된 내 정보를 요약해서 보여줌
    // 닉네임이 있으면 닉네임으로, 없으면 이름으로 사용자를 부름
    function getDisplayName() {
      const nickname = document.getElementById('nicknameInput').value.trim();
      if (nickname) return nickname;
      const name = document.getElementById('nameInput').value.trim();
      if (name) return name;
      return '여행자';
    }

    function refreshGreetings() {
      const displayName = getDisplayName();
      document.getElementById('mainGreeting').textContent = `${displayName}님, 안녕하세요!`;
      document.getElementById('settingsGreeting').textContent = `${displayName}님의 정보`;
    }

    document.getElementById('nameInput').addEventListener('input', refreshGreetings);
    document.getElementById('nicknameInput').addEventListener('input', refreshGreetings);
    refreshGreetings();

    function renderProfileSummary() {
      refreshGreetings();
      const age = document.getElementById('ageInput').value.trim() || '-';
      const genderBtn = document.querySelector('.gender-btn.active');
      const gender = genderBtn ? genderBtn.dataset.gender : '-';
      const skinBtn = document.querySelector('.skin-btn.active');
      const skinLabel = skinBtn ? skinBtn.textContent : '-';
      const toneBtn = document.querySelector('.tone-btn.active');
      const toneLabel = toneBtn ? toneBtn.textContent : '-';
      const concernCount = document.querySelectorAll('.concern-chip.active').length;
      const productCount = getMyProducts().length;
      const destinationKey = document.getElementById('destinationSelect').value;
      const destinationLabel = destinationKey || '미선택';
      const start = document.getElementById('tripStartDate').value || '-';
      const end = document.getElementById('tripEndDate').value || '-';

      const rows = [
        ['나이', `${age}세`],
        ['성별', gender],
        ['피부 타입', skinLabel],
        ['퍼스널컬러', toneLabel],
        ['피부 고민', `${concernCount}개 선택`],
        ['보유 화장품', `${productCount}개`],
        ['여행지', destinationLabel],
        ['여행 기간', `${start} ~ ${end}`],
      ];

      document.getElementById('profileSummaryCard').innerHTML = rows
        .map(
          ([label, value]) => `
            <div class="flex items-center justify-between text-sm">
              <span class="text-gray-400">${label}</span>
              <span class="font-semibold">${value}</span>
            </div>
          `
        )
        .join('');
    }

    // 기후 + 보유 화장품을 기준으로 기존 루틴에서 뺄 것/조정할 것을 계산
    function getAdjustedRoutine(destination, skinType, myProducts) {
      const weather = weatherData[destination];
      const adjustments = [];
      const warnings = [];

      if (weather.humidity >= 70) {
        const emulsion = myProducts.find((p) => p.category === 'emulsion');
        if (emulsion) {
          adjustments.push({
            action: 'remove',
            productName: emulsion.name,
            reason: '습도가 높아 유분감이 과할 수 있어요',
          });
        } else {
          const toner = myProducts.find((p) => p.category === 'toner');
          adjustments.push({
            action: 'modify',
            productName: toner ? toner.name : '토너',
            reason: '오늘은 토너만 가볍게 발라 산뜻하게 마무리하세요',
          });
        }
      }

      if (weather.humidity <= 30) {
        const cream = myProducts.find((p) => p.category === 'cream');
        if (cream) {
          adjustments.push({
            action: 'modify',
            productName: cream.name,
            reason: '평소보다 두껍게 발라주세요',
          });
        } else {
          warnings.push('보습 크림이 없어서 건조 위험이 있어요, 현지 조달을 고려하세요');
        }
      }

      if (weather.uvi >= 8) {
        const sunscreen = myProducts.find((p) => p.category === 'sunscreen');
        if (!sunscreen) {
          warnings.push('선크림이 리스트에 없어요! 꼭 챙기세요');
        }
      }

      // 현지 수질에 따른 팁 ('리뷰, 국가 DB'의 수질(경수/연수) 데이터 반영)
      const tips = [];
      if (weather.waterQuality === '경수') {
        tips.push('이 지역은 석회수(경수)라 머리가 뻑뻑해질 수 있어요. 헤어팩이나 클래리파잉 샴푸로 마무리해보세요');
      } else {
        tips.push('이 지역은 연수 지역이에요. 그래도 마지막 세안 단계는 생수로 헹궈내면 트러블을 예방할 수 있어요');
      }

      return { adjustments, warnings, tips };
    }

    // 조정 제안 카드 렌더링 (remove: 빨강 취소선 / modify·add: 포인트 컬러)
    function renderAdjustedRoutine(result) {
      const actionStyle = {
        remove: { label: '빼기', badge: 'bg-red-50 text-red-500', bar: 'border-red-300', text: 'text-red-500 line-through' },
        modify: { label: '조정', badge: 'bg-brand-50 text-brand-600', bar: 'border-brand-500', text: 'text-brand-600' },
        add: { label: '추가', badge: 'bg-brand-50 text-brand-600', bar: 'border-brand-500', text: 'text-brand-600' },
      };

      const adjustmentList = document.getElementById('adjustmentList');
      adjustmentList.innerHTML = '';
      result.adjustments.forEach((item) => {
        const style = actionStyle[item.action];
        const card = document.createElement('div');
        card.className = `border-l-4 ${style.bar} bg-white rounded-r-xl p-3 flex items-start gap-3`;
        card.innerHTML = `
          <span class="text-[10px] font-bold px-2 py-1 rounded-full shrink-0 ${style.badge}">${style.label}</span>
          <div class="min-w-0">
            <p class="text-sm font-semibold ${style.text}">${item.productName}</p>
            <p class="text-xs text-gray-500 mt-0.5">${item.reason}</p>
          </div>
        `;
        adjustmentList.appendChild(card);
      });

      const adjustmentWarnings = document.getElementById('adjustmentWarnings');
      adjustmentWarnings.innerHTML = '';
      result.warnings.forEach((message) => {
        const card = document.createElement('div');
        card.className = 'border border-red-100 bg-red-50 rounded-xl p-3 flex items-start gap-2';
        card.innerHTML = `
          <span class="text-sm">⚠️</span>
          <p class="text-xs font-medium text-red-600">${message}</p>
        `;
        adjustmentWarnings.appendChild(card);
      });

      const adjustmentTips = document.getElementById('adjustmentTips');
      adjustmentTips.innerHTML = '';
      (result.tips || []).forEach((message) => {
        const card = document.createElement('div');
        card.className = 'border border-brand-100 bg-brand-50 rounded-xl p-3 flex items-start gap-2';
        card.innerHTML = `
          <span class="text-sm">💧</span>
          <p class="text-xs font-medium text-brand-600">${message}</p>
        `;
        adjustmentTips.appendChild(card);
      });
    }

    // 내가 파우치에 등록한 화장품을 카드 형식으로 보여줌
    function renderMyRoutineGrid() {
      const grid = document.getElementById('myRoutineGrid');
      const products = getMyProducts();
      grid.innerHTML = '';

      if (products.length === 0) {
        grid.innerHTML = `
          <button id="myRoutineEmptyCard" type="button" class="col-span-2 flex items-center gap-3 bg-white border border-gray-100 rounded-2xl p-4 text-left">
            <span class="text-2xl">👝</span>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">아직 등록된 화장품이 없어요</p>
              <p class="text-xs text-gray-400">파우치에서 화장품을 등록해보세요</p>
            </div>
            <span class="text-gray-300">→</span>
          </button>
        `;
        document.getElementById('myRoutineEmptyCard').addEventListener('click', () => switchTab('pouch'));
        return;
      }

      products.forEach((product) => {
        const category = cosmeticCategories.find((c) => c.value === product.category);
        const card = document.createElement('div');
        card.className = 'bg-white border border-gray-100 rounded-2xl p-3';
        card.innerHTML = `
          <div class="w-10 h-10 rounded-xl bg-brand-50 flex items-center justify-center text-lg mb-2">${category ? category.icon : '🧴'}</div>
          <p class="text-sm font-semibold truncate">${product.name}</p>
          <p class="text-xs text-gray-400">${category ? category.label : ''}</p>
        `;
        grid.appendChild(card);
      });
    }

    // 다른 여행자 리뷰(communityReviews)에서 내 여행지·피부타입에 맞는 추천 루틴을 찾아 보여줌
    function renderRecommendedRoutine() {
      const section = document.getElementById('recommendedRoutineSection');
      const activeSkinBtn = document.querySelector('.skin-btn.active');
      const skinTypeMap = { dry: '건성', normal: '중성', oily: '지성', combination: '복합성', dehydrated: '수부지' };
      const skinType = skinTypeMap[activeSkinBtn ? activeSkinBtn.dataset.skin : 'dry'];

      const byCountry = communityReviews.filter((r) => r.country === currentTripDestination);
      if (byCountry.length === 0) {
        section.classList.add('hidden');
        return;
      }

      let matched = byCountry.filter((r) => r.skinType === skinType);
      let usedFallback = false;
      if (matched.length === 0) {
        matched = byCountry;
        usedFallback = true;
      }
      const pick = matched[Math.floor(Math.random() * matched.length)];

      document.getElementById('recommendedRoutineNote').textContent = usedFallback
        ? `${currentTripDestination}을 다녀온 여행자 ${pick.id}님의 추천이에요`
        : `나와 같은 ${skinType} 피부의 ${pick.id}님이 ${currentTripDestination}에서 추천한 루틴이에요`;
      document.getElementById('recommendedCosmetics').textContent = pick.cosmetics;
      document.getElementById('recommendedSkincare').textContent = pick.skincare;
      document.getElementById('recommendedMakeup').textContent = pick.makeup;
      section.classList.remove('hidden');
    }

    // 등록 2단계에서 선택한 여행지를 사용중 탭의 알림/기후 안내에도 동일하게 반영
    // 등록한 여행 시작일·종료일을 기준으로 D-day 또는 며칠차 여행인지 계산
    function getTripScheduleLabel(start, end) {
      const oneDay = 24 * 60 * 60 * 1000;
      const startDate = new Date(`${start}T00:00:00`);
      const endDate = new Date(`${end}T00:00:00`);
      const today = new Date();
      const todayDate = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const totalDays = Math.round((endDate - startDate) / oneDay) + 1;

      if (todayDate < startDate) {
        const dDay = Math.round((startDate - todayDate) / oneDay);
        return `D-${dDay} · 총 ${totalDays}일 일정`;
      }
      if (todayDate > endDate) {
        return `여행이 종료됐어요 · 총 ${totalDays}일 일정이었어요`;
      }
      const dayNumber = Math.round((todayDate - startDate) / oneDay) + 1;
      return `여행 ${dayNumber}일차 · 총 ${totalDays}일 일정`;
    }

    function renderTripOverview() {
      const destinationKey = document.getElementById('destinationSelect').value;
      const productCount = getMyProducts().length;

      if (!destinationKey) {
        document.getElementById('mainEmptyState').classList.remove('hidden');
        document.getElementById('mainDashboard').classList.add('hidden');
        document.getElementById('mainPouchEmptyText').textContent =
          productCount > 0 ? `화장품 ${productCount}개 등록됨` : '아직 등록된 화장품이 없어요';
        return;
      }

      document.getElementById('mainEmptyState').classList.add('hidden');
      document.getElementById('mainDashboard').classList.remove('hidden');
      renderMyRoutineGrid();

      // 여행지는 등록했지만 파우치가 비어있으면 살짝 눈에 띄는 알림 스타일로 표시
      const pouchCard = document.getElementById('mainPouchCardFilled');
      const pouchIcon = document.getElementById('mainPouchIcon');
      const pouchText = document.getElementById('mainPouchFilledText');
      const pouchEmpty = productCount === 0;
      pouchCard.className = `w-full flex items-center gap-3 border rounded-2xl p-4 text-left ${pouchEmpty ? 'bg-red-50 border-red-100' : 'bg-white border-gray-100'}`;
      pouchIcon.className = `w-11 h-11 rounded-xl flex items-center justify-center text-xl shrink-0 ${pouchEmpty ? 'bg-red-100 text-red-500' : 'bg-brand-50 text-brand-500'}`;
      pouchText.className = pouchEmpty ? 'text-xs font-medium text-red-500' : 'text-xs text-gray-400';
      pouchText.textContent = pouchEmpty ? '파우치가 비어있어요! 화장품을 등록해주세요' : `화장품 ${productCount}개 등록됨`;

      // 파우치가 비어있으면 눈에 잘 띄도록 카드를 상단(여행 요약 배너 바로 아래)으로 옮김
      if (pouchEmpty) {
        document.getElementById('pouchCardTopSlot').appendChild(pouchCard);
      } else {
        document.getElementById('mainMapCard').insertAdjacentElement('beforebegin', pouchCard);
      }

      const label = currentTripDestination || '여행지';
      const start = document.getElementById('tripStartDate').value;
      const end = document.getElementById('tripEndDate').value;
      document.getElementById('tripSummaryBanner').innerHTML = `
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-gray-400 mb-0.5">이번 여행</p>
            <p class="text-base font-bold">📍 ${label}</p>
            ${start && end ? `<p class="text-xs text-gray-400 mt-0.5">${start} ~ ${end}</p><p class="text-xs font-semibold text-brand-500 mt-1">${getTripScheduleLabel(start, end)}</p>` : ''}
          </div>
          <button id="tripSummaryEditBtn" type="button" class="text-xs font-semibold text-brand-500">여행지 수정 →</button>
        </div>
      `;
      document.getElementById('tripSummaryEditBtn').addEventListener('click', () => {
        switchTab('register');
        showRegisterStep('step2');
      });

      const weather = weatherData[currentTripDestination];
      let todayCondition = '쾌적한 날씨';
      if (weather.humidity >= 70) {
        todayCondition = '습도 상승 주의';
      } else if (weather.humidity <= 30) {
        todayCondition = '건조 주의';
      } else if (weather.uvi >= 8) {
        todayCondition = '자외선 주의';
      }

      // 오늘의 날씨 히어로 카드: 상황별 아이콘·문구를 매핑
      const weatherMoodByCondition = {
        '쾌적한 날씨': { icon: '☀️', label: '맑음', headline: '선크림 바르기\\n좋은 날' },
        '습도 상승 주의': { icon: '💧', label: '습함', headline: '가벼운 스킨케어 하기\\n좋은 날' },
        '건조 주의': { icon: '🌬️', label: '건조함', headline: '수분크림 챙기기\\n좋은 날' },
        '자외선 주의': { icon: '🔆', label: '맑음', headline: '선크림 덧바르기\\n좋은 날' },
      };
      const mood = weatherMoodByCondition[todayCondition];
      document.getElementById('weatherHeroHeadline').textContent = mood.headline;
      document.getElementById('weatherHeroLocation').textContent = `📍 ${label}`;
      document.getElementById('weatherHeroIcon').textContent = mood.icon;
      document.getElementById('weatherHeroTemp').textContent = `${weather.temp}°C`;
      document.getElementById('weatherHeroCondition').textContent = mood.label;

      const days = [
        { dayLabel: '어제', temp: weather.temp - 1, humidity: weather.humidity - 13, uvi: Math.max(weather.uvi - 2, 1), condition: '맑음', highlight: false },
        { dayLabel: '오늘', temp: weather.temp, humidity: weather.humidity, uvi: weather.uvi, condition: todayCondition, highlight: true },
        { dayLabel: '내일', temp: weather.temp - 2, humidity: weather.humidity - 8, uvi: Math.max(weather.uvi - 1, 1), condition: '흐림', highlight: false },
      ];

      const climateTable = document.getElementById('climateTable');
      climateTable.innerHTML = '';
      days.forEach((day) => {
        const row = document.createElement('div');
        row.className = `flex items-center justify-between px-4 py-3${day.highlight ? ' bg-brand-50' : ''}`;
        row.innerHTML = `
          <div>
            <p class="text-sm font-semibold">${day.dayLabel} · ${label}</p>
            <p class="text-xs ${day.highlight ? 'text-brand-500 font-semibold' : 'text-gray-400'}">${day.condition}</p>
          </div>
          <div class="text-right">
            <p class="text-base font-bold text-gray-800">${day.temp}°C <span class="text-xs font-normal text-gray-400">· 습도 ${day.humidity}%</span></p>
            <p class="text-[10px] text-gray-400 mt-0.5">자외선 ${getUviLabel(day.uvi)} · 미세먼지 ${getDustLabel(weather.climate)}</p>
          </div>
        `;
        climateTable.appendChild(row);
      });

      renderRecommendedRoutine();
    }

    // 자외선 지수를 사람이 읽기 쉬운 단계로 변환
    function getUviLabel(uvi) {
      if (uvi >= 11) return '위험';
      if (uvi >= 8) return '매우 높음';
      if (uvi >= 6) return '높음';
      if (uvi >= 3) return '보통';
      return '낮음';
    }

    // 미세먼지는 실측 데이터가 없어 기후유형 기반으로 추정 (건조기후일수록 먼지가 많은 경향을 반영한 mock)
    function getDustLabel(climate) {
      const dustByClimate = {
        건조기후: '높음',
        열대기후: '보통',
        온대기후: '보통',
        냉대기후: '낮음',
        한대기후: '낮음',
      };
      return dustByClimate[climate] || '보통';
    }

    // 사용중 탭의 여행지 기준으로 조정 제안 계산 (등록 2단계에서 선택한 여행지로 갱신됨)
    let currentTripDestination = '일본';
    function refreshAdjustedRoutine() {
      renderTripOverview();
      const activeSkinBtn = document.querySelector('.skin-btn.active');
      const skinType = activeSkinBtn ? activeSkinBtn.dataset.skin : 'oily';
      const result = getAdjustedRoutine(currentTripDestination, skinType, getMyProducts());
      renderAdjustedRoutine(result);
    }
    refreshAdjustedRoutine();

    // 피드백 버튼 토글 (사용후 페이지)
    document.querySelectorAll('.feedback-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.feedback-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });
  </script>

</body>
</html>
"""


components.html(HTML_PAGE, height=852, scrolling=True)