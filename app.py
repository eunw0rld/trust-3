import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SkinTrip", layout="centered")

# 웰컴 화면에 쓰이는 로컬 이미지들을 base64 data URI로 인코딩
# (components.html은 srcdoc 기반 sandbox iframe이라 상대경로로 로컬 파일을 못 읽어옴)
_ASSET_DIR = Path(__file__).parent / "01 landing page"
_AVATAR_DIR = _ASSET_DIR / "사람 이미지"


def _data_uri(path: Path, mime: str) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


EARTH_BG_URI = _data_uri(_ASSET_DIR / "지구.jpg", "image/jpeg")
LOGO_URI = _data_uri(_ASSET_DIR / "logo.png", "image/png")
AVATAR_URIS = [
    _data_uri(_AVATAR_DIR / "p1.jpg", "image/jpeg"),
    _data_uri(_AVATAR_DIR / "p3.jpg", "image/jpeg"),
    _data_uri(_AVATAR_DIR / "p5.jpg", "image/jpeg"),
    _data_uri(_AVATAR_DIR / "다운로드 (1).jpg", "image/jpeg"),
]

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
          // SkinTrip 디자인 시스템의 유일한 포인트 컬러 (주황)
          brand: {
            50: '#FFF7ED',
            100: '#FFEDD5',
            400: '#FB923C',
            500: '#F97316',
            600: '#EA580C',
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
  .bottom-nav-v2 {
    position: fixed;
    left: 16px;
    right: 16px;
    bottom: 16px;
    height: 58px;
    background: #f1f1f1;
    border-radius: 9999px;
    display: flex;
    align-items: stretch;
    padding: 6px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
    z-index: 50;
  }
  .bottom-nav-v2.hidden {
    display: none;
  }
  .bottom-nav-active-pill {
    position: absolute;
    top: 6px;
    bottom: 6px;
    left: 6px;
    width: calc((100% - 12px) / 3);
    background: #f97316;
    border-radius: 9999px;
    transform: translateX(0);
    transition: transform 0.28s cubic-bezier(0.4, 0, 0.2, 1);
    z-index: 0;
  }
  .bottom-nav-btn {
    position: relative;
    z-index: 1;
    flex: 1 1 0;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    background: none;
    border: none;
    color: #9ca3af;
    transition: color 0.2s ease;
  }
  .bottom-nav-btn.active {
    color: #ffffff;
  }
  .nav-icon-v2 {
    width: 20px;
    height: 20px;
    fill: none;
    stroke: currentColor;
    stroke-width: 1.9;
    stroke-linecap: round;
    stroke-linejoin: round;
    flex-shrink: 0;
  }
  .nav-label-v2 {
    font-size: 13px;
    font-weight: 600;
    white-space: nowrap;
  }
  .more-menu-item {
    display: flex;
    align-items: center;
    gap: 12px;
    width: 100%;
    padding: 12px 8px;
    border-radius: 12px;
    color: #374151;
    transition: background 0.15s ease;
  }
  .more-menu-item:active {
    background: #f9fafb;
  }
  .back-to-nav-btn {
    display: inline-block;
  }
  .wizard-choice-btn {
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 16px 10px;
    font-size: 14px;
    font-weight: 700;
    color: #6b7280;
    background: #ffffff;
  }
  .wizard-choice-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #c2410c;
  }
  .wizard-progress-track {
    height: 4px;
    background: #e5e7eb;
    border-radius: 9999px;
    overflow: hidden;
  }
  .wizard-progress-fill {
    height: 100%;
    background: #f97316;
    border-radius: 9999px;
    transition: width 0.25s ease;
  }
  .wizard-cta-btn {
    height: 54px;
    border-radius: 16px;
    background: #f97316;
    color: #ffffff;
    font-weight: 600;
    font-size: 15px;
    transition: background 0.15s ease;
  }
  .wizard-cta-btn:disabled {
    background: #d1d5db;
  }
  .history-view-toggle-btn {
    color: #6b7280;
    transition: background 0.15s ease, color 0.15s ease;
  }
  .history-view-toggle-btn.active {
    background: #ffffff;
    color: #f97316;
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
  }
  .skin-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .skin-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #c2410c;
  }
  .gender-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .gender-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #c2410c;
  }
  .tone-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .tone-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #c2410c;
  }
  .concern-chip {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .concern-chip.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #c2410c;
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
    /* 하단 네비게이션이 position:fixed로 떠 있으므로, 콘텐츠 마지막 줄이
       가려지지 않도록 네비 높이(58px) + 여백만큼 아래쪽을 비워둠 */
    padding-bottom: 96px;
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
  /* 웰컴 화면: 지구 배경 위/아래 가장자리를 살짝 어둡게 페이드 */
  .welcome-vignette {
    position: absolute;
    inset: 0;
    z-index: 1;
    pointer-events: none;
    background:
      radial-gradient(ellipse 100% 38% at 50% 0%, rgba(0, 0, 0, 0.65) 0%, rgba(0, 0, 0, 0) 70%),
      radial-gradient(ellipse 100% 45% at 50% 100%, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0) 70%);
  }
  .welcome-logo {
    height: 36px;
    width: auto;
    object-fit: contain;
    margin: 0 auto;
    display: block;
    filter: drop-shadow(0 1px 6px rgba(255, 255, 255, 0.35));
  }
  .welcome-logo-hero {
    height: 64px;
    margin: 0;
    filter: drop-shadow(0 2px 10px rgba(255, 255, 255, 0.3));
  }
  .app-header-logo {
    height: 22px;
    width: auto;
    object-fit: contain;
    display: block;
    /* 로고 파일이 흰색이라, 밝은 배경인 앱 상단 헤더에서는 검게 반전해서 사용 */
    filter: brightness(0);
  }
  /* 웰컴 화면 "시작하기": 리퀴드 글래스 스타일 */
  .welcome-cta-btn {
    position: relative;
    overflow: hidden;
    background: rgba(20, 25, 40, 0.55);
    -webkit-backdrop-filter: blur(20px);
    backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.25);
    border-radius: 9999px;
    padding: 14px 0;
    color: #ffffff;
    font-weight: 600;
    font-size: 14px;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    transition: transform 0.12s ease, background 0.12s ease;
  }
  .welcome-cta-btn::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(255, 255, 255, 0.25) 0%, rgba(255, 255, 255, 0) 50%);
    pointer-events: none;
  }
  .welcome-cta-btn:active {
    transform: scale(0.97);
    background: rgba(20, 25, 40, 0.7);
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
  /* 매장/도시 마커(주황)와 구분되는 "내 위치" 전용 파란 마커 + pulse + 라벨 */
  .my-location-marker {
    position: relative;
    width: 20px;
    height: 20px;
  }
  .my-location-dot {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 16px;
    height: 16px;
    border-radius: 9999px;
    background: #2563eb;
    border: 3px solid #ffffff;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.3);
    z-index: 2;
  }
  .my-location-pulse {
    position: absolute;
    top: 50%;
    left: 50%;
    width: 20px;
    height: 20px;
    margin-top: -10px;
    margin-left: -10px;
    border-radius: 9999px;
    background: rgba(37, 99, 235, 0.35);
    animation: myLocationPulse 2s ease-out infinite;
    z-index: 1;
  }
  @keyframes myLocationPulse {
    0% { transform: scale(1); opacity: 0.7; }
    100% { transform: scale(3.2); opacity: 0; }
  }
  .my-location-label {
    position: absolute;
    top: 22px;
    left: 50%;
    transform: translateX(-50%);
    white-space: nowrap;
    background: rgba(37, 99, 235, 0.95);
    color: #ffffff;
    font-size: 11px;
    font-weight: 600;
    padding: 3px 9px;
    border-radius: 9999px;
    box-shadow: 0 2px 6px rgba(0, 0, 0, 0.2);
    z-index: 2;
  }
  /* 위치 확인 중 로딩 스피너 */
  .my-location-spinner {
    display: inline-block;
    width: 14px;
    height: 14px;
    border: 2px solid #e5e7eb;
    border-top-color: #f97316;
    border-radius: 9999px;
    animation: myLocationSpin 0.7s linear infinite;
  }
  @keyframes myLocationSpin {
    to { transform: rotate(360deg); }
  }
  .trip-destination-sheet {
    animation: tripSheetSlideUp 0.3s ease-out;
  }
  @keyframes tripSheetSlideUp {
    from { transform: translateY(100%); }
    to { transform: translateY(0); }
  }
  .trip-destination-chip {
    padding: 6px 12px;
    border-radius: 9999px;
    background: #fff7ed;
    color: #c2410c;
    font-size: 12px;
    font-weight: 600;
    border: 1px solid #fed7aa;
  }
  /* 리스트 아이템이 지도로 flyTo되는 동안 살짝 강조 */
  .map-store-list-item.active-store-item {
    background-color: #fff7ed;
    border-color: #fdba74;
  }

  /* 피부 변화 리포트: 두 사진이 모두 등록된 직후 재생되는 "스캔 중" 연출 */
  .skin-scan-overlay {
    background: rgba(17, 24, 39, 0.15);
  }
  .skin-scan-line {
    position: absolute;
    left: 0;
    right: 0;
    top: -30%;
    height: 30%;
    background: linear-gradient(180deg, rgba(249, 115, 22, 0) 0%, rgba(249, 115, 22, 0.65) 50%, rgba(249, 115, 22, 0) 100%);
    filter: blur(2px);
    box-shadow: 0 0 14px 3px rgba(249, 115, 22, 0.55);
    animation: skinScanMove 1.5s ease-in-out infinite;
  }
  @keyframes skinScanMove {
    0% { top: -30%; }
    100% { top: 100%; }
  }
  /* "피부를 분석하고 있어요" 문구 옆 점 3개 깜빡임 */
  .skin-scan-dots span {
    display: inline-block;
    width: 4px;
    height: 4px;
    margin-left: 3px;
    border-radius: 9999px;
    background: currentColor;
    opacity: 0.25;
    animation: skinScanDotPulse 1.2s infinite;
  }
  .skin-scan-dots span:nth-child(2) { animation-delay: 0.2s; }
  .skin-scan-dots span:nth-child(3) { animation-delay: 0.4s; }
  @keyframes skinScanDotPulse {
    0%, 80%, 100% { opacity: 0.25; }
    40% { opacity: 1; }
  }
  /* 스캔 진행 프로그레스 바: 스캔 연출 시간(3초)과 맞춰 왼쪽에서 오른쪽으로 채워짐 */
  .skin-scan-progress {
    width: 55%;
    height: 4px;
    margin: 0 auto;
    border-radius: 9999px;
    background: #f3f4f6;
    overflow: hidden;
  }
  .skin-scan-progress-bar {
    height: 100%;
    width: 100%;
    background: linear-gradient(90deg, #fb923c, #f97316);
    border-radius: 9999px;
    transform-origin: left;
    animation: skinScanProgress 3s linear forwards;
  }
  @keyframes skinScanProgress {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
  }
  /* 스캔 연출이 끝나고 결과 카드가 나타날 때 부드럽게 페이드인 */
  @keyframes skinFadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .skin-fade-in {
    animation: skinFadeIn 0.4s ease-out;
  }
</style>
</head>
<body class="font-sans text-gray-900">

  <!-- ============ 랜딩 페이지 (웰컴 화면) ============ -->
  <div id="screen-welcome" class="relative mx-auto overflow-hidden" style="width: var(--app-width); height: var(--app-height); background-image: url('__EARTH_BG_URI__'); background-size: cover; background-position: center;">
    <div class="welcome-vignette"></div>

    <div class="relative z-10 pt-8 px-6 text-left">
      <img src="__LOGO_URI__" alt="SkinTrip" class="welcome-logo welcome-logo-hero" />
      <p class="mt-2 text-sm text-white/90 leading-relaxed font-normal">
        <span class="font-bold">스킨트립</span>과 함께,<br />피부 걱정 없이 어디든
      </p>
    </div>

    <div class="landing-bubble" style="top: 28%; left: 22%; z-index: 2;"><img src="__AVATAR_URI_1__" alt="" /></div>
    <div class="landing-bubble" style="top: 38%; left: 10%; z-index: 2;"><img src="__AVATAR_URI_2__" alt="" /></div>
    <div class="landing-bubble" style="top: 50%; left: 62%; z-index: 2;"><img src="__AVATAR_URI_3__" alt="" /></div>
    <div class="landing-bubble" style="top: 56%; left: 76%; z-index: 2;"><img src="__AVATAR_URI_4__" alt="" /></div>

    <div class="absolute inset-x-0 bottom-0 z-10 px-6 pb-9">
      <button id="welcomeStartBtn" type="button" class="welcome-cta-btn w-full">시작하기</button>
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
  <div id="appContainer" class="hidden mx-auto bg-gray-50 border-x border-gray-100" style="width: var(--app-width); position: relative;">

    <!-- 상단 로고 (온보딩 위저드 중에는 화면 정중앙 배치를 위해 숨김) -->
    <header id="appHeader" class="hidden px-5 pt-6 pb-4">
      <img src="__LOGO_URI__" alt="SkinTrip" class="app-header-logo" />
    </header>

    <main class="px-5 pb-6">

      <!-- ============ 1. 등록 페이지 ============ -->
      <section id="screen-register" class="py-2">

        <!-- 온보딩 진행 바 (완료 화면에서는 숨김) -->
        <div id="wizardProgressTrack" class="wizard-progress-track mx-1 mb-1">
          <div id="wizardProgressFill" class="wizard-progress-fill" style="width: 14.2857%;"></div>
        </div>

        <!-- 온보딩 1단계: 이름 (텍스트 입력, "다음" 버튼으로 진행) -->
        <div id="reg-name" class="wizard-step relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="welcome">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2">
            <h2 class="text-xl font-bold mb-8">이름이<br />어떻게 되나요?</h2>
            <input id="regNameInput" type="text" placeholder="이름을 입력해주세요" class="w-full max-w-xs border border-gray-200 rounded-xl px-4 py-3 text-sm text-center focus:outline-none focus:border-brand-500" />
          </div>
          <div class="absolute inset-x-0 bottom-6 px-4">
            <button type="button" class="wizard-next-btn wizard-cta-btn w-full" data-next="reg-nickname" disabled>다음</button>
          </div>
        </div>

        <!-- 온보딩 2단계: 닉네임 (텍스트 입력, "다음" 버튼으로 진행) -->
        <div id="reg-nickname" class="wizard-step hidden relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="reg-name">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2">
            <h2 class="text-xl font-bold mb-8">어떻게<br />불러드릴까요?</h2>
            <input id="regNicknameInput" type="text" placeholder="다른 사용자에게 보여질 닉네임이에요" class="w-full max-w-xs border border-gray-200 rounded-xl px-4 py-3 text-sm text-center focus:outline-none focus:border-brand-500" />
            <p class="text-xs text-gray-400 mt-2">커뮤니티에서 이 닉네임으로 보여요</p>
          </div>
          <div class="absolute inset-x-0 bottom-6 px-4">
            <button type="button" class="wizard-next-btn wizard-cta-btn w-full" data-next="reg-gender" disabled>다음</button>
          </div>
        </div>

        <!-- 온보딩 3단계: 성별 (단일 선택, 선택 즉시 자동 진행) -->
        <div id="reg-gender" class="wizard-step hidden relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="reg-nickname">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2">
            <h2 class="text-xl font-bold mb-8">성별이<br />어떻게 되나요?</h2>
            <div class="grid grid-cols-2 gap-3 w-full max-w-xs">
              <button type="button" data-gender="여성" class="onboard-gender-btn wizard-choice-btn">여성</button>
              <button type="button" data-gender="남성" class="onboard-gender-btn wizard-choice-btn">남성</button>
              <button type="button" data-gender="선택 안 함" class="onboard-gender-btn wizard-choice-btn col-span-2">선택 안 함</button>
            </div>
          </div>
        </div>

        <!-- 온보딩 4단계: 생년월일 (날짜 입력, "다음" 버튼으로 진행) -->
        <div id="reg-age" class="wizard-step hidden relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="reg-gender">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2">
            <h2 class="text-xl font-bold mb-8">생년월일이<br />어떻게 되나요?</h2>
            <input id="regBirthdateInput" type="date" class="w-full max-w-xs border border-gray-200 rounded-xl px-4 py-3 text-sm text-center focus:outline-none focus:border-brand-500" />
          </div>
          <div class="absolute inset-x-0 bottom-6 px-4">
            <button type="button" class="wizard-next-btn wizard-cta-btn w-full" data-next="reg-tone" disabled>다음</button>
          </div>
        </div>

        <!-- 온보딩 5단계: 퍼스널컬러 (단일 선택, 선택 즉시 자동 진행) -->
        <div id="reg-tone" class="wizard-step hidden relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="reg-age">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2">
            <h2 class="text-xl font-bold mb-8">퍼스널컬러가<br />어떻게 되나요?</h2>
            <div class="grid grid-cols-2 gap-3 w-full max-w-xs">
              <button type="button" data-tone="spring" class="onboard-tone-btn wizard-choice-btn">봄웜톤</button>
              <button type="button" data-tone="summer" class="onboard-tone-btn wizard-choice-btn">여름쿨톤</button>
              <button type="button" data-tone="autumn" class="onboard-tone-btn wizard-choice-btn">가을웜톤</button>
              <button type="button" data-tone="winter" class="onboard-tone-btn wizard-choice-btn">겨울쿨톤</button>
              <button type="button" data-tone="unknown" class="onboard-tone-btn wizard-choice-btn col-span-2">잘 모르겠어요</button>
            </div>
          </div>
        </div>

        <!-- 온보딩 6단계: 피부타입 (단일 선택, 선택 즉시 자동 진행) -->
        <div id="reg-skintype" class="wizard-step hidden relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="reg-tone">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2">
            <h2 class="text-xl font-bold mb-8">피부타입이<br />어떻게 되나요?</h2>
            <div class="grid grid-cols-2 gap-3 w-full max-w-xs">
              <button type="button" data-skin="dry" class="skin-btn wizard-choice-btn">건성</button>
              <button type="button" data-skin="normal" class="skin-btn wizard-choice-btn">중성</button>
              <button type="button" data-skin="oily" class="skin-btn wizard-choice-btn">지성</button>
              <button type="button" data-skin="combination" class="skin-btn wizard-choice-btn">복합성</button>
              <button type="button" data-skin="dehydrated" class="skin-btn wizard-choice-btn col-span-2">수부지</button>
            </div>
          </div>
        </div>

        <!-- 온보딩 7단계: 피부 고민 (다중 선택, 선택 완료 버튼으로 진행) -->
        <div id="reg-concerns" class="wizard-step hidden relative flex flex-col" style="min-height: calc(var(--app-height) - 40px);">
          <div class="flex items-center mb-2">
            <button type="button" class="wizard-back-btn text-xs text-gray-400" data-prev="reg-skintype">← 이전</button>
          </div>
          <div class="flex-1 flex flex-col items-center justify-center text-center px-2 pb-20">
            <h2 class="text-xl font-bold mb-8">요즘 피부 고민이<br />있나요?</h2>
            <div class="flex flex-wrap gap-2 justify-center max-w-xs">
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
          <div class="absolute inset-x-0 bottom-6 px-4">
            <button type="button" class="wizard-next-btn wizard-cta-btn w-full" data-next="reg-complete" disabled>선택 완료</button>
          </div>
        </div>

        <!-- 온보딩 완료 화면 -->
        <div id="reg-complete" class="wizard-step hidden flex flex-col items-center justify-center text-center px-8" style="min-height: calc(var(--app-height) - 40px);">
          <span class="text-5xl mb-4">✅</span>
          <h2 class="text-xl font-bold mb-2">Thanks!</h2>
          <p class="text-sm text-gray-400 mb-10">이제 다 준비됐어요</p>
          <button id="wizardFinishBtn" type="button" class="wizard-cta-btn w-full max-w-xs">시작하기</button>
        </div>

      </section>

      <!-- ============ 2. 메인 페이지 (대시보드) ============ -->
      <section id="screen-inuse" class="hidden py-6 space-y-6">

        <!-- 상단 바: 프로필 설정 바로가기 -->
        <div class="flex justify-end">
          <button id="mainProfileBtn" type="button" class="text-xs font-semibold text-gray-500 bg-white border border-gray-200 rounded-full px-3 py-1.5">프로필 설정</button>
        </div>

        <!-- 인사말 + 여행지 등록/수정 진입점 (화면 최상단, 여행 계획 폼은 이 링크로만 펼쳐짐) -->
        <div>
          <p id="mainGreeting" class="text-sm text-gray-400 mb-1">안녕하세요!</p>
          <h2 class="text-2xl font-bold leading-snug mb-2">어디로<br />여행가시나요?</h2>
          <button id="mainRegisterTripBtn" type="button" class="text-sm font-semibold text-brand-500">여행지 등록하기 →</button>
        </div>

        <!-- 여행 계획 입력 폼 (평소엔 숨김, 위 링크를 눌렀을 때만 펼쳐짐) -->
        <div id="tripSegmentsSection" class="hidden bg-white border border-gray-100 rounded-2xl p-4 space-y-3">
          <div id="tripSegmentRows" class="space-y-3"></div>
          <button id="addTripSegmentBtn" type="button" class="w-full py-2.5 rounded-xl border border-dashed border-gray-300 text-gray-500 text-sm font-semibold">+ 구간 추가</button>
          <p id="tripSegmentWarning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2"></p>
          <button id="tripSegmentsSaveBtn" type="button" class="w-full py-2.5 rounded-xl bg-brand-500 text-white text-sm font-bold">저장</button>
        </div>

        <!-- 내 파우치 (촬영/직접입력 UI가 클릭 없이 항상 바로 노출) -->
        <div id="pouchSection" class="bg-white border border-gray-100 rounded-2xl p-4">
          <div class="flex items-center justify-between mb-1">
            <h2 class="text-base font-bold">내 파우치</h2>
            <button id="pouchAddMoreBtn" type="button" class="hidden text-xs font-semibold text-brand-500">+ 추가</button>
          </div>
          <p id="pouchSectionSubtitle" class="text-sm text-gray-400 mb-4">사진 한 장이면 화장품 이름과 종류를 자동으로 인식해드려요</p>

          <!-- 등록된 화장품 카드 그리드 (1개 이상 등록되면 노출) -->
          <div id="pouchProductGrid" class="hidden grid grid-cols-2 gap-2"></div>

          <!-- 촬영/직접입력 UI (비어있을 때 기본 노출, "+ 추가" 클릭 시 다시 노출) -->
          <div id="pouchCaptureUI">
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

            <!-- 갖고 있는 화장품 리스트 (직접 입력) -->
            <div class="mt-3">
              <h3 class="text-sm font-semibold text-gray-700 mb-3">갖고 있는 화장품 <span id="cosmeticCountBadge" class="text-gray-400 font-normal"></span></h3>
              <div id="cosmeticRows" class="space-y-2 mb-3"></div>
              <button id="addCosmeticRowBtn" type="button" class="w-full text-center text-xs text-gray-400 underline">
                직접 입력하기
              </button>
            </div>
          </div>
        </div>

        <!-- 오늘의 날씨 + 뷰티 인사이트 통합 카드 (여행지 등록 후에만 표시) -->
        <div id="todayInsightCard" class="hidden rounded-2xl p-5 text-white" style="background: linear-gradient(135deg, #fb923c 0%, #ea580c 100%);">
          <div class="flex items-center justify-between mb-3">
            <p id="todayInsightLocation" class="text-sm font-bold">📍 여행지</p>
            <p id="todayInsightDate" class="text-xs font-medium text-white/80"></p>
          </div>
          <div id="todayInsightMetrics" class="flex items-center gap-3 text-sm font-semibold mb-4"></div>
          <div class="flex items-start gap-2 bg-black/15 rounded-xl p-3">
            <span class="text-base shrink-0">🔔</span>
            <p id="todayInsightText" class="text-sm font-medium leading-relaxed"></p>
          </div>
        </div>

        <!-- 내 주위 화장품 매장 (기존 지도 탭 내용을 메인 화면 안으로 흡수) -->
        <div id="mapStoreSection" class="space-y-4">
          <div>
            <h2 id="mapStoreListTitle" class="text-base font-bold mb-1">내 주위 화장품 매장</h2>
            <p id="mapStoreListSubtitle" class="text-sm text-gray-400 mb-4">현재 위치 기준으로 가까운 매장을 보여드려요 (mock)</p>
          </div>

          <!-- 지도 위 작은 검색 아이콘 버튼: 필요할 때만 펼쳐지는 검색바 (기본 접힘) -->
          <div class="relative w-full">
            <div id="mapViz" class="relative w-full rounded-2xl overflow-hidden" style="height: 320px; background: linear-gradient(180deg, #eaf6ff 0%, #cfeeff 100%);"></div>
            <div id="myLocationLoading" class="hidden absolute inset-0 z-20 rounded-2xl flex items-center justify-center bg-white/85">
              <div class="flex items-center gap-2 bg-white rounded-full px-4 py-2 shadow-md">
                <span class="my-location-spinner"></span>
                <span class="text-xs font-semibold text-gray-600">현재 위치를 확인하고 있어요...</span>
              </div>
            </div>
            <div class="absolute top-3 left-3 z-30 flex items-start gap-2" style="max-width: calc(100% - 24px);">
              <button id="mapSearchToggleBtn" type="button" aria-label="여행지 검색" class="w-9 h-9 rounded-full bg-white shadow-md flex items-center justify-center shrink-0">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#374151" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="7"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              </button>
              <div id="mapSearchBar" class="hidden flex-1 min-w-0 bg-white rounded-2xl shadow-md p-3">
                <input id="globeSearchInput" type="text" placeholder="나라 또는 도시를 검색해보세요" class="w-full py-2 px-3 rounded-full bg-gray-50 border-2 border-transparent text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:border-orange-400 transition-colors" />
                <p id="globeSearchNotFound" class="hidden mt-1.5 ml-1 inline-block text-[11px] font-medium text-orange-500 bg-orange-50 px-2 py-1 rounded-full">찾을 수 없어요</p>
                <p class="text-[11px] font-semibold text-gray-400 mt-2.5 mb-1.5">인기 여행지</p>
                <div class="flex flex-wrap gap-1.5">
                  <button type="button" class="trip-destination-chip" data-city="이탈리아">이탈리아</button>
                  <button type="button" class="trip-destination-chip" data-city="밀라노">밀라노</button>
                  <button type="button" class="trip-destination-chip" data-city="도쿄">도쿄</button>
                  <button type="button" class="trip-destination-chip" data-city="파리">파리</button>
                  <button type="button" class="trip-destination-chip" data-city="두바이">두바이</button>
                  <button type="button" class="trip-destination-chip" data-city="방콕">방콕</button>
                </div>
              </div>
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
        </div>

        <!-- 여행지 등록 상태에서만 노출되는 세부 정보 -->
        <div id="mainDashboard" class="hidden space-y-6">

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

        </div>

      </section>

      <!-- ============ 3. 기록 페이지 (달력별 기록 / 지구본 기록) ============ -->
      <section id="screen-history" class="hidden py-6 space-y-4">
        <div>
          <h2 class="text-base font-bold mb-1">여행 기록</h2>
          <p class="text-sm text-gray-400 mb-4">등록한 여행 일정을 달력 또는 지구본으로 확인해보세요</p>
        </div>

        <div class="flex bg-gray-100 rounded-full p-1">
          <button type="button" class="history-view-toggle-btn active flex-1 py-2 rounded-full text-sm font-semibold" data-view="calendar">📅 달력별 기록</button>
          <button type="button" class="history-view-toggle-btn flex-1 py-2 rounded-full text-sm font-semibold" data-view="globe">🌐 지구본 기록</button>
        </div>

        <div id="historyCalendarView" class="space-y-2">
          <p id="historyCalendarEmpty" class="hidden text-sm text-gray-400 text-center py-10">아직 등록된 여행 일정이 없어요</p>
          <div id="historyCalendarList" class="space-y-2"></div>
        </div>

        <div id="historyGlobeView" class="hidden space-y-3">
          <div id="historyGlobeViz" class="relative w-full rounded-2xl overflow-hidden" style="height: 320px; background: linear-gradient(180deg, #eaf6ff 0%, #cfeeff 100%);"></div>
          <p id="historyGlobeEmpty" class="hidden text-sm text-gray-400 text-center py-6">아직 등록된 여행 일정이 없어요</p>
          <div id="historyGlobeList" class="space-y-2"></div>
        </div>
      </section>

      <!-- ============ 4. 피부 변화 리포트 ============ -->
      <section id="screen-afteruse" class="hidden py-6 space-y-6">

        <button id="afterUseToSettingsBtn" type="button" class="back-to-nav-btn text-xs text-gray-400">← 이전</button>

        <div class="border border-gray-200 rounded-2xl p-5">
          <div class="flex items-center justify-between mb-1">
            <p id="skinReportDayLabel" class="text-xs text-gray-400"></p>
            <span id="skinReportDestinationChip" class="text-[10px] font-bold text-brand-500 border border-brand-100 rounded-full px-2 py-0.5"></span>
          </div>
          <h2 class="text-base font-bold mb-4">피부 변화 리포트</h2>

          <!-- 1일차 vs 마지막날 사진 비교: 탭하면 실제 카메라 촬영 화면(getUserMedia)이 열림.
               카메라 권한이 없거나 지원하지 않는 환경에서는 숨겨진 file input(capture="user")으로 자동 대체됨 -->
          <div class="grid grid-cols-2 gap-3 mb-2">
            <div>
              <button type="button" id="skinPhotoStartBox" class="relative overflow-hidden block w-full border-2 border-dashed border-gray-200 rounded-xl h-28 flex flex-col items-center justify-center text-gray-400 gap-1 cursor-pointer">
                <img id="skinPhotoStartPreview" class="hidden absolute inset-0 w-full h-full object-cover" alt="1일차 피부 사진" />
                <div id="skinPhotoStartPlaceholder" class="flex flex-col items-center gap-1">
                  <span class="text-xl">📷</span>
                  <span class="text-xs">1일차 사진</span>
                </div>
                <!-- 분석 스캔 연출: 두 사진이 모두 등록된 직후 3초간만 표시 -->
                <div id="skinPhotoStartScanOverlay" class="hidden absolute inset-0 skin-scan-overlay">
                  <div class="skin-scan-line"></div>
                </div>
              </button>
              <input id="skinPhotoStartInput" type="file" accept="image/*" capture="user" class="hidden" />
              <p id="skinReportStartDate" class="text-xs text-gray-400 text-center mt-2"></p>
            </div>
            <div>
              <button type="button" id="skinPhotoEndBox" class="relative overflow-hidden block w-full border-2 border-brand-500 rounded-xl h-28 flex flex-col items-center justify-center text-brand-500 gap-1 cursor-pointer">
                <img id="skinPhotoEndPreview" class="hidden absolute inset-0 w-full h-full object-cover" alt="마지막날 피부 사진" />
                <div id="skinPhotoEndPlaceholder" class="flex flex-col items-center gap-1">
                  <span class="text-xl">📷</span>
                  <span class="text-xs">마지막날 사진</span>
                </div>
                <!-- 분석 스캔 연출: 두 사진이 모두 등록된 직후 3초간만 표시 -->
                <div id="skinPhotoEndScanOverlay" class="hidden absolute inset-0 skin-scan-overlay">
                  <div class="skin-scan-line"></div>
                </div>
              </button>
              <input id="skinPhotoEndInput" type="file" accept="image/*" capture="user" class="hidden" />
              <p id="skinReportEndDate" class="text-xs text-gray-400 text-center mt-2"></p>
            </div>
          </div>
          <p id="skinPhotoHint" class="text-xs text-gray-400 mt-1">→ 카메라 아이콘을 누르면 촬영 후 AI가 두 사진을 비교해 분석해드려요</p>
        </div>

        <!-- 항목별 변화 -->
        <div>
          <h3 class="text-sm font-semibold text-gray-700 mb-3">항목별 변화</h3>

          <!-- 초기 빈 상태 / 사진 등록 안내: 분석 전에는 mock 점수 대신 이 안내만 노출 -->
          <div id="skinChangeEmptyState" class="text-center text-sm text-gray-400 py-10 leading-relaxed">
            1일차 사진과 마지막날 사진을 등록하면<br />항목별 분석 결과가 여기에 표시됩니다.
          </div>

          <!-- 스캔 연출: 두 사진이 모두 등록된 직후 약 3초간 표시 (실제 분석은 이미 끝난 상태, 연출용 지연) -->
          <div id="skinChangeScanningState" class="hidden text-center py-10">
            <p class="text-sm text-gray-500 mb-3">피부를 분석하고 있어요<span class="skin-scan-dots"><span></span><span></span><span></span></span></p>
            <div class="skin-scan-progress"><div class="skin-scan-progress-bar"></div></div>
          </div>

          <!-- 분석 결과 카드: 스캔 연출이 끝난 뒤에만 노출. 카드별로 "상세보기"를 누르면 세부 피드백이 펼쳐짐 -->
          <div id="skinChangeCards" class="hidden space-y-3">
            <div class="bg-white border border-gray-100 rounded-2xl p-4">
              <div class="flex items-center justify-between mb-2">
                <p class="text-sm font-semibold">💧 수분</p>
                <span id="hydrationBadge" class="text-xs font-bold text-green-600 bg-green-50 rounded-full px-2 py-0.5">개선됨</span>
              </div>
              <p id="hydrationScoreLine" class="text-sm text-gray-500 mb-2">1일차 <span class="font-bold text-gray-900">54</span> → 마지막날 <span class="font-bold text-gray-900">72</span>/100 <span class="text-green-600 font-semibold ml-1">+18%</span></p>
              <button type="button" id="hydrationToggleBtn" aria-expanded="false" aria-controls="hydrationDetail" class="text-xs font-semibold text-brand-600 flex items-center gap-0.5">
                상세보기 <span id="hydrationToggleArrow">▾</span>
              </button>
              <div id="hydrationDetail" class="hidden mt-2 pt-2 border-t border-dashed border-gray-100 space-y-1.5">
                <p id="hydrationDesc" class="text-xs text-gray-400 leading-relaxed">여행지 습도가 높고 물을 자주 마신 덕에 여행 중 수분감이 뚜렷하게 올라갔어요.</p>
                <p class="text-[11px] text-gray-400"><span class="font-semibold text-gray-500">분석 기준</span> · 피부 표면 미세 텍스처 분석</p>
                <p class="text-xs text-gray-600 leading-relaxed">💡 세안 후 3분 이내에 스킨·로션으로 수분을 먼저 채우고, 자기 전 수분크림을 충분히 발라보세요.</p>
              </div>
            </div>
            <div class="bg-white border border-gray-100 rounded-2xl p-4">
              <div class="flex items-center justify-between mb-2">
                <p class="text-sm font-semibold">☀️ 톤·홍조</p>
                <span id="rednessBadge" class="text-xs font-bold text-amber-600 bg-amber-50 rounded-full px-2 py-0.5">주의 필요</span>
              </div>
              <p id="rednessScoreLine" class="text-sm text-gray-500 mb-2">1일차 <span class="font-bold text-gray-900">21</span> → 마지막날 <span class="font-bold text-gray-900">30</span>/100 <span class="text-amber-600 font-semibold ml-1">+9%</span></p>
              <button type="button" id="rednessToggleBtn" aria-expanded="false" aria-controls="rednessDetail" class="text-xs font-semibold text-brand-600 flex items-center gap-0.5">
                상세보기 <span id="rednessToggleArrow">▾</span>
              </button>
              <div id="rednessDetail" class="hidden mt-2 pt-2 border-t border-dashed border-gray-100 space-y-1.5">
                <p id="rednessDesc" class="text-xs text-gray-400 leading-relaxed">양볼 쪽에 붉은 기가 늘어난 편이에요. 강한 햇빛에 노출된 오후 시간대와 겹쳐요.</p>
                <p class="text-[11px] text-gray-400"><span class="font-semibold text-gray-500">분석 기준</span> · R 채널 대비 붉은기 초과분 측정</p>
                <p class="text-xs text-gray-600 leading-relaxed">💡 자외선 차단제를 2~3시간마다 덧바르고, 진정 성분(마데카소사이드·판테놀) 제품을 밤 루틴에 더해보세요.</p>
              </div>
            </div>
            <div class="bg-white border border-gray-100 rounded-2xl p-4">
              <div class="flex items-center justify-between mb-2">
                <p class="text-sm font-semibold">💧 유분</p>
                <span id="oilinessBadge" class="text-xs font-bold text-gray-500 bg-gray-100 rounded-full px-2 py-0.5">변화 없음</span>
              </div>
              <p id="oilinessScoreLine" class="text-sm text-gray-500 mb-2">1일차 <span class="font-bold text-gray-900">46</span> → 마지막날 <span class="font-bold text-gray-900">48</span>/100 T존 <span class="text-gray-500 font-semibold ml-1">±2%</span></p>
              <button type="button" id="oilinessToggleBtn" aria-expanded="false" aria-controls="oilinessDetail" class="text-xs font-semibold text-brand-600 flex items-center gap-0.5">
                상세보기 <span id="oilinessToggleArrow">▾</span>
              </button>
              <div id="oilinessDetail" class="hidden mt-2 pt-2 border-t border-dashed border-gray-100 space-y-1.5">
                <p id="oilinessDesc" class="text-xs text-gray-400 leading-relaxed">T존 유분은 여행 전과 큰 차이가 없어요. 기존 루틴이 잘 유지된 편이에요.</p>
                <p class="text-[11px] text-gray-400"><span class="font-semibold text-gray-500">분석 기준</span> · 빛 반사·번들거림 측정</p>
                <p class="text-xs text-gray-600 leading-relaxed">💡 T존 위주로 피지 흡수 시트나 매트 선크림을 사용해 유분을 관리해보세요.</p>
              </div>
            </div>
            <div class="bg-white border border-gray-100 rounded-2xl p-4">
              <div class="flex items-center justify-between mb-2">
                <p class="text-sm font-semibold">🦠 트러블</p>
                <span id="blemishBadge" class="text-xs font-bold text-red-600 bg-red-50 rounded-full px-2 py-0.5">2건 증가</span>
              </div>
              <p id="blemishScoreLine" class="text-sm text-gray-500 mb-2">1일차 <span class="font-bold text-gray-900">0건</span> → 마지막날 <span class="font-bold text-gray-900">2건</span> <span class="text-red-600 font-semibold ml-1">+2건</span></p>
              <button type="button" id="blemishToggleBtn" aria-expanded="false" aria-controls="blemishDetail" class="text-xs font-semibold text-brand-600 flex items-center gap-0.5">
                상세보기 <span id="blemishToggleArrow">▾</span>
              </button>
              <div id="blemishDetail" class="hidden mt-2 pt-2 border-t border-dashed border-gray-100 space-y-1.5">
                <p id="blemishDesc" class="text-xs text-gray-400 leading-relaxed">턱선에 좁쌀 트러블 2개가 새로 보여요. 자기 전 세안이 부실했던 날과 맞물려요.</p>
                <p class="text-[11px] text-gray-400"><span class="font-semibold text-gray-500">분석 기준</span> · 붉은 반점 군집(blob) 탐지</p>
                <p class="text-xs text-gray-600 leading-relaxed">💡 자기 전 세안을 꼼꼼히 하고, 트러블 부위는 손으로 만지지 않는 게 좋아요.</p>
              </div>
            </div>
          </div>
        </div>

        <!-- 종합 요약 -->
        <div class="bg-brand-50 border border-brand-100 rounded-2xl p-4">
          <p id="skinReportSummary" class="text-sm text-brand-700 leading-relaxed">여행 중 자외선 노출이 늘면서 홍조와 트러블이 조금 생겼어요. 자외선 차단제를 2~3시간마다 다시 발라주면 다음 여행에서 더 편안한 피부를 유지할 수 있을 거예요.</p>
        </div>

        <button type="button" class="w-full py-3.5 rounded-xl bg-brand-500 text-white text-sm font-bold">내 피부 사후관리하기</button>

      </section>

      <!-- ============ 5. 커뮤니티 페이지 ============ -->
      <section id="screen-community" class="hidden py-6 space-y-3">
        <button type="button" class="back-to-nav-btn text-xs text-gray-400" data-back-target="inuse">← 이전</button>
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
        <button type="button" class="back-to-nav-btn text-xs text-gray-400" data-back-target="inuse">← 이전</button>
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

        <div class="bg-white border border-gray-100 rounded-2xl p-4 space-y-4">
          <div>
            <p class="text-xs font-semibold text-gray-400 mb-2">나이 <span class="text-gray-300 font-normal">(선택)</span></p>
            <input id="ageInput" type="number" min="1" max="120" placeholder="예: 27" class="w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
          </div>
          <div>
            <p class="text-xs font-semibold text-gray-400 mb-2">성별 <span class="text-gray-300 font-normal">(선택)</span></p>
            <div class="flex flex-wrap gap-2">
              <button type="button" data-gender="여성" class="gender-btn rounded-full px-5 py-2 text-sm font-semibold">여성</button>
              <button type="button" data-gender="남성" class="gender-btn rounded-full px-5 py-2 text-sm font-semibold">남성</button>
            </div>
          </div>
          <div>
            <p class="text-xs font-semibold text-gray-400 mb-2">퍼스널컬러 <span class="text-gray-300 font-normal">(선택, 메이크업 추천에 활용돼요)</span></p>
            <div class="flex flex-wrap gap-2">
              <button type="button" data-tone="spring" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">봄웜톤</button>
              <button type="button" data-tone="summer" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">여름쿨톤</button>
              <button type="button" data-tone="autumn" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">가을웜톤</button>
              <button type="button" data-tone="winter" class="tone-btn rounded-full px-4 py-2 text-sm font-semibold">겨울쿨톤</button>
              <button type="button" data-tone="unknown" class="tone-btn active rounded-full px-4 py-2 text-sm font-semibold">잘 모르겠어요</button>
            </div>
          </div>
        </div>

        <div id="profileSummaryCard" class="bg-white border border-gray-100 rounded-2xl p-4 space-y-2"></div>

        <div class="space-y-2">
          <button id="settingsEditBtn" type="button" class="w-full py-3 rounded-xl border border-gray-200 text-gray-700 text-sm font-semibold">
            정보 수정하기
          </button>
          <button id="goToAfterUseBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">
            피부 변화 리포트 보기
          </button>
        </div>
      </section>

      <!-- ============ 8. 나라별 인기템 (placeholder) ============ -->
      <section id="screen-country-popular" class="hidden py-6 space-y-6">
        <button type="button" class="back-to-nav-btn text-xs text-gray-400" data-back-target="inuse">← 이전</button>
        <div class="flex flex-col items-center justify-center text-center py-20 gap-3">
          <span class="text-4xl">🌍</span>
          <h2 class="text-base font-bold">나라별 인기템</h2>
          <p class="text-sm text-gray-400">여행지별 인기 화장품 정보를 준비하고 있어요</p>
        </div>
      </section>

    </main>

    <!-- 부가서비스 메뉴 패널 (하단 네비 위로 올라오는 오버레이) -->
    <div id="moreMenuBackdrop" class="hidden absolute inset-0 z-30 bg-black/40"></div>
    <div id="moreMenuModal" class="trip-destination-sheet hidden absolute left-0 right-0 bottom-0 z-40 bg-white rounded-t-3xl px-5 pt-4 pb-6">
      <div class="flex items-center justify-between mb-3">
        <p class="text-sm font-bold">부가서비스</p>
        <button id="moreMenuCloseBtn" type="button" class="text-gray-400 text-lg leading-none">✕</button>
      </div>
      <div class="space-y-1">
        <button type="button" class="more-menu-item" data-target="community">
          <span class="text-lg">💬</span>
          <span class="flex-1 text-left text-sm font-semibold">커뮤니티</span>
          <span class="text-gray-300">›</span>
        </button>
        <button type="button" class="more-menu-item" data-target="countryPopular">
          <span class="text-lg">🌍</span>
          <span class="flex-1 text-left text-sm font-semibold">나라별 인기템</span>
          <span class="text-gray-300">›</span>
        </button>
        <button type="button" class="more-menu-item" data-target="skinReport">
          <span class="text-lg">📝</span>
          <span class="flex-1 text-left text-sm font-semibold">피부 변화 리포트</span>
          <span class="text-gray-300">›</span>
        </button>
        <button type="button" class="more-menu-item" data-target="settings">
          <span class="text-lg">⚙️</span>
          <span class="flex-1 text-left text-sm font-semibold">프로필 설정</span>
          <span class="text-gray-300">›</span>
        </button>
      </div>
    </div>

    <!-- 피부 변화 리포트: 실제 카메라 촬영 화면 (getUserMedia 라이브 프리뷰 + 셔터) -->
    <div id="skinCameraModal" class="hidden absolute inset-0 z-[60] bg-black flex flex-col">
      <video id="skinCameraVideo" autoplay playsinline muted class="flex-1 w-full object-cover"></video>
      <div class="p-5 flex items-center justify-between bg-black">
        <button id="skinCameraCancelBtn" type="button" class="text-white text-sm font-semibold px-2">취소</button>
        <button id="skinCameraShutterBtn" type="button" class="w-14 h-14 rounded-full bg-white border-4 border-gray-400" aria-label="촬영"></button>
        <span class="w-10"></span>
      </div>
    </div>

    <!-- 하단 메뉴바 (등록 완료 후에만 표시, 화면 길이와 무관하게 항상 하단에 고정) -->
    <nav id="bottomNav" class="hidden bottom-nav-v2">
      <div id="bottomNavActivePill" class="bottom-nav-active-pill"></div>
      <button type="button" data-tab="inuse" class="bottom-nav-btn active">
        <svg class="nav-icon-v2" viewBox="0 0 24 24">
          <path d="M4 11.5 12 4l8 7.5V20a1 1 0 0 1-1 1h-4v-7H9v7H5a1 1 0 0 1-1-1v-8.5z"/>
        </svg>
        <span class="nav-label-v2">홈</span>
      </button>
      <button type="button" data-tab="history" class="bottom-nav-btn">
        <svg class="nav-icon-v2" viewBox="0 0 24 24">
          <path d="M17 3a2.828 2.828 0 1 1 4 4L7.5 20.5 2 22l1.5-5.5L17 3z"/>
        </svg>
        <span class="nav-label-v2">기록</span>
      </button>
      <button type="button" id="moreMenuBtn" data-tab="more" class="bottom-nav-btn">
        <svg class="nav-icon-v2" viewBox="0 0 24 24">
          <rect x="3" y="3" width="7" height="7" rx="1.5"/>
          <rect x="14" y="3" width="7" height="7" rx="1.5"/>
          <rect x="14" y="14" width="7" height="7" rx="1.5"/>
          <rect x="3" y="14" width="7" height="7" rx="1.5"/>
        </svg>
        <span class="nav-label-v2">서비스</span>
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

    // 웰컴 화면 "시작하기" -> 앱 진입 (온보딩 위저드 1단계부터 시작)
    function enterApp() {
      document.getElementById('screen-welcome').classList.add('hidden');
      const app = document.getElementById('appContainer');
      app.classList.remove('hidden');
      try {
        playScreenTransition(app);
      } catch (e) {
        console.error('enterApp 전환 중 오류:', e);
      }
    }
    document.getElementById('welcomeStartBtn').addEventListener('click', enterApp);

    // 하단 메뉴바 전환 (메인/기록/부가서비스)
    const bottomNavButtons = document.querySelectorAll('.bottom-nav-btn');

    // 활성 탭 배경(pill)을 활성 버튼 위치로 슬라이드 (버튼이 전부 flex:1 동일 너비라 인덱스 * 100%로 정확히 맞춰짐)
    function updateBottomNavPill() {
      const buttons = Array.from(bottomNavButtons);
      const activeIndex = buttons.findIndex((b) => b.classList.contains('active'));
      const pill = document.getElementById('bottomNavActivePill');
      if (activeIndex === -1) {
        pill.style.opacity = '0';
      } else {
        pill.style.opacity = '1';
        pill.style.transform = `translateX(${activeIndex * 100}%)`;
      }
    }

    const screens = {
      register: document.getElementById('screen-register'),
      inuse: document.getElementById('screen-inuse'),
      history: document.getElementById('screen-history'),
      skinReport: document.getElementById('screen-afteruse'),
      community: document.getElementById('screen-community'),
      settings: document.getElementById('screen-settings'),
      countryPopular: document.getElementById('screen-country-popular'),
    };
    let onboardingComplete = false;
    let lastActiveNavTab = 'inuse';
    let pouchCaptureForceOpen = false;

    // 탭 전환(hidden 토글) 자체는 항상 먼저 실행하고, 화면별 렌더링 로직은
    // try/catch로 감싸서 그 안에서 오류가 나더라도 탭 전환 자체는 항상 되게 함

    // 지도 탭: MapLibre GL JS (globe projection) — 처음 지도 탭을 열 때 한 번만 초기화
    let mapInstance = null;
    let cityMarkers = [];
    let currentCityStores = [];
    let lastFlownMapDestination = null;

    // 초기 지구본 화면의 아주 느린 자동 회전 (거의 느껴지지 않을 정도) - 사용자 조작이나
    // 내 위치 확인 flyTo가 시작되면 멈춤
    let globeAutoRotateFrame = null;
    function startGlobeAutoRotate() {
      stopGlobeAutoRotate();
      function step() {
        if (!mapInstance) return;
        mapInstance.setBearing(mapInstance.getBearing() + 0.008);
        globeAutoRotateFrame = requestAnimationFrame(step);
      }
      globeAutoRotateFrame = requestAnimationFrame(step);
    }
    function stopGlobeAutoRotate() {
      if (globeAutoRotateFrame) {
        cancelAnimationFrame(globeAutoRotateFrame);
        globeAutoRotateFrame = null;
      }
    }

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
        startGlobeAutoRotate();
      });

      // 사용자가 직접 드래그/줌으로 조작하면 자동 회전을 멈춤
      mapInstance.on('dragstart', stopGlobeAutoRotate);
      mapInstance.on('zoomstart', stopGlobeAutoRotate);

      window.addEventListener('resize', () => {
        if (mapInstance) mapInstance.resize();
      });

      // 검색창: 나라/도시 이름(한글 또는 영어 일부)으로 weatherData를 찾아 지도를 그 위치로 flyTo
      document.getElementById('globeSearchInput').addEventListener('keydown', (e) => {
        if (e.key !== 'Enter') return;
        searchCityOnMap();
      });

      showMyLocationMock();
    }

    // "내 위치" mock: 실제 Geolocation API는 쓰지 않고, 잠깐 로딩 후 판교 위치로 이동 + 전용 마커 표시
    const MY_LOCATION_LAT = 37.403549;
    const MY_LOCATION_LNG = 127.102664;
    const MY_LOCATION_LABEL = 'Gyeonggi-do Bundang-gu Pangyo-ro 255beon-gil';

    function showMyLocationMock() {
      const loadingEl = document.getElementById('myLocationLoading');
      loadingEl.classList.remove('hidden');
      setTimeout(() => {
        loadingEl.classList.add('hidden');
        stopGlobeAutoRotate();
        mapInstance.flyTo({ center: [MY_LOCATION_LNG, MY_LOCATION_LAT], zoom: 13, duration: 1800, essential: true });

        const el = document.createElement('div');
        el.className = 'my-location-marker';
        el.innerHTML = `
          <div class="my-location-pulse"></div>
          <div class="my-location-dot"></div>
          <div class="my-location-label">📍 ${MY_LOCATION_LABEL}</div>
        `;
        new maplibregl.Marker({ element: el, anchor: 'center' })
          .setLngLat([MY_LOCATION_LNG, MY_LOCATION_LAT])
          .addTo(mapInstance);

        // 내 위치 확인 애니메이션이 끝난 직후: 내 위치(판교) 기준 매장 마커/리스트를 채움
        mapInstance.once('moveend', () => {
          renderCityStoreMarkers('판교', weatherData['판교']);
        });
      }, 1000);
    }

    // 나라/도시 이름(한글 또는 영어 일부)으로 weatherData에서 일치하는 항목 찾기
    function findCityMatch(query) {
      const q = query.trim().toLowerCase();
      if (!q) return null;
      const matchKey = Object.keys(weatherData).find((key) => {
        const entry = weatherData[key];
        return key.toLowerCase().includes(q) || (entry.en && entry.en.toLowerCase().includes(q));
      });
      if (!matchKey) return null;
      const weather = weatherData[matchKey];
      if (weather.lat == null || weather.lng == null) return null;
      return { key: matchKey, weather };
    }

    function searchCityOnMap() {
      const input = document.getElementById('globeSearchInput');
      const notFound = document.getElementById('globeSearchNotFound');
      const match = findCityMatch(input.value);
      if (match) {
        notFound.classList.add('hidden');
        flyToCity(match.key, match.weather);
        document.getElementById('mapSearchBar').classList.add('hidden');
      } else {
        notFound.classList.remove('hidden');
      }
    }

    // 지도 위 검색 아이콘: 평소엔 접혀 있다가 눌렀을 때만 검색바가 펼쳐짐
    document.getElementById('mapSearchToggleBtn').addEventListener('click', () => {
      const bar = document.getElementById('mapSearchBar');
      const willShow = bar.classList.contains('hidden');
      bar.classList.toggle('hidden');
      if (willShow) {
        document.getElementById('globeSearchInput').focus();
      } else {
        document.getElementById('globeSearchNotFound').classList.add('hidden');
      }
    });

    // 검색바 안의 인기 여행지 칩: 눌러도 바로 그 도시로 flyTo
    document.querySelectorAll('.trip-destination-chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        const match = findCityMatch(chip.dataset.city);
        if (!match) return;
        flyToCity(match.key, match.weather);
        document.getElementById('mapSearchBar').classList.add('hidden');
      });
    });

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
      document.getElementById('mapStoreListSubtitle').textContent = '지도에 표시된 마커를 눌러도 위치를 확인할 수 있어요';
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
      updateBottomNavPill();
      Object.entries(screens).forEach(([key, el]) => el.classList.toggle('hidden', key !== tabName));
      try {
        playScreenTransition(screens[tabName]);
        if (tabName === 'inuse') {
          refreshAdjustedRoutine();
          initMapIfNeeded();
        } else if (tabName === 'skinReport') {
          renderSkinReport();
        } else if (tabName === 'settings') {
          renderProfileSummary();
        } else if (tabName === 'community') {
          if (!communityDefaultApplied) {
            applyDefaultCommunityFilter();
            communityDefaultApplied = true;
          }
          renderCommunityFeed();
        }
      } catch (e) {
        console.error(`switchTab('${tabName}') 렌더링 중 오류:`, e);
      }
      if (tabName === 'inuse' || tabName === 'history') {
        lastActiveNavTab = tabName;
      }
    }

    // 등록 완료 전에는 하단 메뉴바 자체를 숨김 (등록 흐름 중에는 이전/다음 버튼으로만 이동)
    function updateTabLockUI() {
      const bottomNav = document.getElementById('bottomNav');
      bottomNav.classList.toggle('hidden', !onboardingComplete);
      // 온보딩 위저드 중에는 로고 헤더를 숨겨 질문 화면이 정중앙에 오도록 함
      document.getElementById('appHeader').classList.toggle('hidden', !onboardingComplete);
      // 하단 메뉴바가 보이는 동안에는 앱 셸을 고정 높이로 만들어 본문만 스크롤되게 함
      document.getElementById('appContainer').classList.toggle('app-shell-fixed', onboardingComplete);
    }

    document.getElementById('settingsEditBtn').addEventListener('click', () => {
      switchTab('register');
      showWizardStep('reg-skintype');
    });

    document.getElementById('goToAfterUseBtn').addEventListener('click', () => {
      switchTab('skinReport');
    });

    // 메인 대시보드의 바로가기 카드/버튼
    document.getElementById('mainProfileBtn').addEventListener('click', () => {
      switchTab('settings');
    });
    document.getElementById('mainRegisterTripBtn').addEventListener('click', () => {
      expandTripSegmentsForm();
    });
    document.getElementById('tripSegmentsSaveBtn').addEventListener('click', () => {
      tripSegmentsExpanded = false;
      updateTripSegmentsUI();
    });

    bottomNavButtons.forEach((btn) => {
      if (btn.id === 'moreMenuBtn') return;
      btn.addEventListener('click', () => switchTab(btn.dataset.tab));
    });

    // 부가서비스 메뉴 패널 (슬라이드업 오버레이) - 화면 전환이 아니라 토글이므로 switchTab을 쓰지 않음
    const moreMenuBtn = document.getElementById('moreMenuBtn');
    const moreMenuModal = document.getElementById('moreMenuModal');
    const moreMenuBackdrop = document.getElementById('moreMenuBackdrop');
    let moreMenuOpen = false;

    function openMoreMenu() {
      moreMenuOpen = true;
      moreMenuModal.classList.remove('hidden');
      moreMenuBackdrop.classList.remove('hidden');
      playScreenTransition(moreMenuModal);
      bottomNavButtons.forEach((b) => b.classList.toggle('active', b === moreMenuBtn));
      updateBottomNavPill();
    }

    function closeMoreMenu() {
      moreMenuOpen = false;
      moreMenuModal.classList.add('hidden');
      moreMenuBackdrop.classList.add('hidden');
      bottomNavButtons.forEach((b) => b.classList.toggle('active', b.dataset.tab === lastActiveNavTab));
      updateBottomNavPill();
    }

    moreMenuBtn.addEventListener('click', () => {
      if (moreMenuOpen) {
        closeMoreMenu();
      } else {
        openMoreMenu();
      }
    });
    document.getElementById('moreMenuCloseBtn').addEventListener('click', closeMoreMenu);
    moreMenuBackdrop.addEventListener('click', closeMoreMenu);

    document.querySelectorAll('.more-menu-item').forEach((item) => {
      item.addEventListener('click', () => {
        closeMoreMenu();
        switchTab(item.dataset.target);
      });
    });

    // 하단 네비에 없는 화면들의 뒤로가기 버튼 - 이전에 있던 메인/기록 탭으로 복귀
    document.querySelectorAll('.back-to-nav-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        switchTab(lastActiveNavTab);
      });
    });

    function showWarning(id, message) {
      const warning = document.getElementById(id);
      warning.textContent = message;
      warning.classList.remove('hidden');
    }

    function hideWarning(id) {
      document.getElementById(id).classList.add('hidden');
    }

    // ===== 온보딩 위저드: 화면 전환 + 진행 상태 =====
    const WIZARD_STEP_ORDER = ['reg-name', 'reg-nickname', 'reg-gender', 'reg-age', 'reg-tone', 'reg-skintype', 'reg-concerns'];

    // 온보딩에서 수집한 기본 정보 (이후 프로필/커뮤니티 화면에서 활용)
    let userProfile = { name: '', nickname: '', gender: '', birthDate: '', tone: '' };

    function showWizardStep(stepId) {
      document.querySelectorAll('.wizard-step').forEach((el) => el.classList.toggle('hidden', el.id !== stepId));
      const progressTrack = document.getElementById('wizardProgressTrack');
      const stepIndex = WIZARD_STEP_ORDER.indexOf(stepId);
      if (stepIndex === -1) {
        progressTrack.classList.add('hidden');
      } else {
        progressTrack.classList.remove('hidden');
        document.getElementById('wizardProgressFill').style.width = `${((stepIndex + 1) / WIZARD_STEP_ORDER.length) * 100}%`;
      }
      playScreenTransition(document.getElementById(stepId));
    }

    // 여행지 국기 이모지 (커뮤니티에 큐레이션된 주요 여행지 위주, 나머지는 📍로 대체)
    const destinationFlags = {
      이탈리아: '🇮🇹', 일본: '🇯🇵', 태국: '🇹🇭', 아랍에미리트: '🇦🇪', 프랑스: '🇫🇷', 싱가포르: '🇸🇬',
      대한민국: '🇰🇷', 미국: '🇺🇸', 영국: '🇬🇧', 스페인: '🇪🇸', 독일: '🇩🇪', 베트남: '🇻🇳', 중국: '🇨🇳',
    };

    // "피부 변화 리포트" 화면: 활성 여행 구간을 바탕으로 헤더와 사진 비교 날짜를 채움 (수치는 mock 고정값)
    function renderSkinReport() {
      const segment = getActiveSegment();
      const start = segment ? segment.start : '';
      const end = segment ? segment.end : '';
      const totalDays = start && end
        ? Math.round((new Date(`${end}T00:00:00`) - new Date(`${start}T00:00:00`)) / (24 * 60 * 60 * 1000)) + 1
        : 1;
      const destination = segment ? segment.country : null;
      const flag = destinationFlags[destination] || '📍';
      document.getElementById('skinReportDayLabel').textContent = `여행 ${totalDays}일차 · 마지막날`;
      document.getElementById('skinReportDestinationChip').textContent = `${flag} ${destination || '여행지'}`;
      document.getElementById('skinReportStartDate').textContent = start || '-';
      document.getElementById('skinReportEndDate').textContent = end || '-';
    }

    // ===== 피부 변화 리포트: 사진 업로드/촬영 → Canvas 픽셀 분석 → 항목별 카드 자동 갱신 =====
    // 외부 API/라이브러리 없이 순수 JS + Canvas로 계산하는 "근사 스크리닝"입니다.
    // 실제 피부과적 진단이 아니라, 두 사진의 픽셀 패턴을 비교해 변화 추이만 보여주는 목적입니다.

    const SKIN_ANALYSIS_SIZE = 96; // 분석용 캔버스 한 변 크기(px). 클수록 정교하지만 느려짐
    const skinPhotoImages = { start: null, end: null }; // 업로드/촬영된 두 장의 <img> 엘리먼트 보관
    let skinScanTimeoutId = null; // 스캔 연출 타이머 핸들 (사진 재등록 시 중복 실행 방지용)

    // 0~100 사이로 값을 잘라내는 유틸
    function clampSkinScore(value, min, max) {
      return Math.max(min, Math.min(max, value));
    }

    // 원본 이미지를 정사각형으로 중앙 크롭해 고정 크기 캔버스에 그린 뒤 픽셀 데이터를 반환
    // (사진의 크기·비율이 달라도 항상 같은 조건으로 분석하기 위함)
    function drawImageToAnalysisCanvas(imgEl) {
      const canvas = document.createElement('canvas');
      canvas.width = SKIN_ANALYSIS_SIZE;
      canvas.height = SKIN_ANALYSIS_SIZE;
      const ctx = canvas.getContext('2d');
      const srcW = imgEl.naturalWidth || imgEl.width;
      const srcH = imgEl.naturalHeight || imgEl.height;
      const side = Math.min(srcW, srcH);
      const sx = (srcW - side) / 2;
      const sy = (srcH - side) / 2;
      ctx.drawImage(imgEl, sx, sy, side, side, 0, 0, SKIN_ANALYSIS_SIZE, SKIN_ANALYSIS_SIZE);
      return ctx.getImageData(0, 0, SKIN_ANALYSIS_SIZE, SKIN_ANALYSIS_SIZE);
    }

    // 격자 블록(8x8px) 단위로 "주변 평균보다 붉고 어두운" 블록을 표시한 뒤,
    // 인접한 블록끼리 4방향 flood fill로 묶어 트러블 반점(blob) 개수를 근사 카운트
    // ※ avgRedness/avgBrightness는 같은 이미지 내부의 평균값이므로, 여기서는 lightingFactor를
    //   따로 곱하지 않고 블록 값과 같은 단위(원본 픽셀값)로 그대로 비교해야 함
    function countBlemishBlobs(data, width, height, avgRedness, avgBrightness) {
      const blockSize = 8;
      const cols = Math.floor(width / blockSize);
      const rows = Math.floor(height / blockSize);
      const flagged = new Array(cols * rows).fill(false);

      for (let by = 0; by < rows; by++) {
        for (let bx = 0; bx < cols; bx++) {
          let rSum = 0, gSum = 0, bSum = 0, n = 0;
          for (let y = by * blockSize; y < by * blockSize + blockSize; y++) {
            for (let x = bx * blockSize; x < bx * blockSize + blockSize; x++) {
              const o = (y * width + x) * 4;
              rSum += data[o]; gSum += data[o + 1]; bSum += data[o + 2];
              n++;
            }
          }
          const r = rSum / n, g = gSum / n, b = bSum / n;
          const blockRedness = r - (g + b) / 2;
          const blockBrightness = (r + g + b) / 3;
          // 주변보다 붉은기가 뚜렷이 높으면서 밝기는 오히려 낮은(홍조성 반점) 블록만 이상 블록으로 표시
          if (blockRedness > avgRedness + 14 && blockBrightness < avgBrightness - 4) {
            flagged[by * cols + bx] = true;
          }
        }
      }

      const visited = new Array(cols * rows).fill(false);
      let blobCount = 0;
      for (let idx = 0; idx < flagged.length; idx++) {
        if (!flagged[idx] || visited[idx]) continue;
        blobCount++;
        const stack = [idx];
        while (stack.length) {
          const cur = stack.pop();
          if (visited[cur] || !flagged[cur]) continue;
          visited[cur] = true;
          const cx = cur % cols, cy = Math.floor(cur / cols);
          if (cx > 0) stack.push(cur - 1);
          if (cx < cols - 1) stack.push(cur + 1);
          if (cy > 0) stack.push(cur - cols);
          if (cy < rows - 1) stack.push(cur + cols);
        }
      }
      return clampSkinScore(blobCount, 0, 12);
    }

    // 사진 한 장을 분석해 수분/톤·홍조/유분 점수(0~100)와 트러블 반점 개수를 반환
    function analyzeSkinPhoto(imgEl) {
      const { data, width, height } = drawImageToAnalysisCanvas(imgEl);
      const pixelCount = width * height;

      let brightnessSum = 0;
      let rednessSum = 0;
      let oilyPixelCount = 0;
      const brightness = new Float32Array(pixelCount);

      for (let i = 0; i < pixelCount; i++) {
        const o = i * 4;
        const r = data[o], g = data[o + 1], b = data[o + 2];
        const bright = (r + g + b) / 3;
        brightness[i] = bright;
        brightnessSum += bright;
        // 톤·홍조 지표: R이 G·B 평균보다 얼마나 높은지 (양수일수록 붉은기가 강함)
        rednessSum += r - (g + b) / 2;

        // 유분 지표: 밝고(반사광) 채도가 낮은(번들거리는) 픽셀 비율
        const maxC = Math.max(r, g, b);
        const minC = Math.min(r, g, b);
        const saturation = maxC === 0 ? 0 : (maxC - minC) / maxC;
        if (bright > 190 && saturation < 0.18) oilyPixelCount++;
      }

      const avgBrightness = brightnessSum / pixelCount;
      const avgRedness = rednessSum / pixelCount;
      // 조명(전체 밝기) 편차를 보정하기 위한 정규화 비율 (기준 밝기 128 대비)
      const lightingFactor = clampSkinScore(128 / Math.max(avgBrightness, 1), 0.6, 1.6);

      // 수분(hydration): 인접 픽셀 간 밝기 변화(엣지 밀도)로 표면 질감을 근사.
      // 요철·각질이 많을수록 엣지가 많아져 매끈함(수분감) 점수는 낮아짐
      let edgeSum = 0;
      let edgeSamples = 0;
      for (let y = 1; y < height - 1; y++) {
        for (let x = 1; x < width - 1; x++) {
          const idx = y * width + x;
          const dx = brightness[idx + 1] - brightness[idx - 1];
          const dy = brightness[idx + width] - brightness[idx - width];
          edgeSum += Math.sqrt(dx * dx + dy * dy);
          edgeSamples++;
        }
      }
      const avgEdge = (edgeSum / edgeSamples) * lightingFactor;
      const hydration = clampSkinScore(100 - avgEdge * 3.2, 0, 100); // 경험적 스케일링 상수

      // 대부분의 피부는 원래 R값이 G·B보다 높으므로(자연스러운 살빛), 배율을 과하게 주면
      // 거의 모든 사진이 100점에 붙어버려 비교가 무의미해짐 → 완만한 배율로 조정
      const redness = clampSkinScore(avgRedness * lightingFactor * 1.6, 0, 100);
      const oiliness = clampSkinScore((oilyPixelCount / pixelCount) * 260, 0, 100);
      const blemish = countBlemishBlobs(data, width, height, avgRedness, avgBrightness);

      return { hydration, redness, oiliness, blemish };
    }

    // dataURL(카메라 캡처 또는 파일 선택 결과)을 미리보기에 채우고, 양쪽 사진이 모두 채워지면 자동 분석 실행
    function applySkinPhoto(kind, dataUrl) {
      const img = new Image();
      img.onload = () => {
        skinPhotoImages[kind] = img;
        const previewEl = document.getElementById(kind === 'start' ? 'skinPhotoStartPreview' : 'skinPhotoEndPreview');
        const placeholderEl = document.getElementById(kind === 'start' ? 'skinPhotoStartPlaceholder' : 'skinPhotoEndPlaceholder');
        previewEl.src = dataUrl;
        previewEl.classList.remove('hidden');
        placeholderEl.classList.add('hidden');
        updateSkinPhotoHint();
        updateSkinChangeEmptyState();
        if (skinPhotoImages.start && skinPhotoImages.end) {
          runSkinPhotoAnalysis();
        }
      };
      img.src = dataUrl;
    }

    // (폴백 경로) 파일 선택창에서 고른 파일을 읽어 applySkinPhoto로 전달
    function loadSkinPhoto(kind, file) {
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => applySkinPhoto(kind, reader.result);
      reader.readAsDataURL(file);
    }

    function updateSkinPhotoHint() {
      const hintEl = document.getElementById('skinPhotoHint');
      const count = (skinPhotoImages.start ? 1 : 0) + (skinPhotoImages.end ? 1 : 0);
      if (count >= 2) {
        hintEl.textContent = '✓ 두 사진을 비교해 아래 리포트를 갱신했어요';
      } else if (count === 1) {
        hintEl.textContent = '나머지 한 장을 더 등록해 주세요';
      } else {
        hintEl.textContent = '→ 카메라 아이콘을 누르면 촬영 후 AI가 두 사진을 비교해 분석해드려요';
      }
    }

    // "항목별 변화" 빈 상태 안내: 등록된 사진 개수(0/1/2장)에 따라 문구를 갱신.
    // 두 장이 모두 채워지면 이 안내는 숨기고 스캔 연출(beginSkinScan)로 넘어감
    function updateSkinChangeEmptyState() {
      const emptyEl = document.getElementById('skinChangeEmptyState');
      const count = (skinPhotoImages.start ? 1 : 0) + (skinPhotoImages.end ? 1 : 0);
      if (count >= 2) {
        emptyEl.classList.add('hidden');
        return;
      }
      emptyEl.classList.remove('hidden');
      emptyEl.innerHTML = count === 1
        ? '나머지 한 장을 더 등록해 주세요'
        : '1일차 사진과 마지막날 사진을 등록하면<br />항목별 분석 결과가 여기에 표시됩니다.';
    }

    document.getElementById('skinPhotoStartInput').addEventListener('change', (e) => {
      loadSkinPhoto('start', e.target.files[0]);
    });
    document.getElementById('skinPhotoEndInput').addEventListener('change', (e) => {
      loadSkinPhoto('end', e.target.files[0]);
    });

    // ===== 실제 카메라 촬영 (getUserMedia 라이브 프리뷰 + 셔터) =====
    // 카메라 아이콘 박스를 탭하면 이 모달이 열려 실시간 카메라 화면을 보여줌.
    // getUserMedia를 지원하지 않거나(구형 브라우저) 권한이 거부된 경우에는
    // 숨겨진 file input(capture="user")을 대신 열어 OS 카메라/갤러리로 자연스럽게 대체됨
    let skinCameraStream = null;
    let skinCameraTargetKind = null; // 현재 촬영 대상: 'start' | 'end'

    async function openSkinCamera(kind) {
      skinCameraTargetKind = kind;
      if (!navigator.mediaDevices || !navigator.mediaDevices.getUserMedia) {
        document.getElementById(kind === 'start' ? 'skinPhotoStartInput' : 'skinPhotoEndInput').click();
        return;
      }
      try {
        skinCameraStream = await navigator.mediaDevices.getUserMedia({ video: { facingMode: 'user' }, audio: false });
        document.getElementById('skinCameraVideo').srcObject = skinCameraStream;
        document.getElementById('skinCameraModal').classList.remove('hidden');
      } catch (err) {
        console.error('카메라 접근 실패, 파일 선택으로 대체합니다:', err);
        document.getElementById(kind === 'start' ? 'skinPhotoStartInput' : 'skinPhotoEndInput').click();
      }
    }

    function closeSkinCamera() {
      if (skinCameraStream) {
        skinCameraStream.getTracks().forEach((track) => track.stop());
        skinCameraStream = null;
      }
      document.getElementById('skinCameraModal').classList.add('hidden');
    }

    // 셔터 탭: 현재 비디오 프레임을 캔버스에 그려 이미지로 캡처 → 기존 미리보기/분석 파이프라인으로 전달
    function captureSkinPhoto() {
      const video = document.getElementById('skinCameraVideo');
      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth || SKIN_ANALYSIS_SIZE;
      canvas.height = video.videoHeight || SKIN_ANALYSIS_SIZE;
      canvas.getContext('2d').drawImage(video, 0, 0, canvas.width, canvas.height);
      applySkinPhoto(skinCameraTargetKind, canvas.toDataURL('image/png'));
      closeSkinCamera();
    }

    document.getElementById('skinPhotoStartBox').addEventListener('click', () => openSkinCamera('start'));
    document.getElementById('skinPhotoEndBox').addEventListener('click', () => openSkinCamera('end'));
    document.getElementById('skinCameraShutterBtn').addEventListener('click', captureSkinPhoto);
    document.getElementById('skinCameraCancelBtn').addEventListener('click', closeSkinCamera);

    // 배지(개선됨/주의 필요/변화 없음) 색상 ↔ Tailwind 클래스 매핑
    const skinBadgeColorClasses = {
      green: 'text-green-600 bg-green-50',
      amber: 'text-amber-600 bg-amber-50',
      gray: 'text-gray-500 bg-gray-100',
      red: 'text-red-600 bg-red-50',
    };
    const skinTextColorClasses = {
      green: 'text-green-600',
      amber: 'text-amber-600',
      gray: 'text-gray-500',
      red: 'text-red-600',
    };

    function setSkinBadge(id, label, colorKey) {
      const el = document.getElementById(id);
      el.className = `text-xs font-bold rounded-full px-2 py-0.5 ${skinBadgeColorClasses[colorKey]}`;
      el.textContent = label;
    }

    // 점수(0~100)형 지표의 배지를 계산. higherIsBetter=false인 지표(홍조·유분)는 오를수록 "주의 필요".
    // threshold 이내의 변화는 "변화 없음"으로 간주
    function computeScoreBadge(delta, higherIsBetter, threshold = 3) {
      if (Math.abs(delta) <= threshold) return { label: '변화 없음', color: 'gray' };
      const improved = higherIsBetter ? delta > 0 : delta < 0;
      return improved ? { label: '개선됨', color: 'green' } : { label: '주의 필요', color: 'amber' };
    }

    // 건수(트러블)형 지표는 배지 자체에 증감 건수를 표시
    function computeBlemishBadge(delta) {
      if (delta === 0) return { label: '변화 없음', color: 'gray' };
      if (delta > 0) return { label: `${delta}건 증가`, color: 'red' };
      return { label: `${Math.abs(delta)}건 감소`, color: 'green' };
    }

    function formatPercentDelta(start, end) {
      if (start <= 0) return end > 0 ? '+100%' : '±0%';
      const pct = Math.round(((end - start) / start) * 100);
      if (pct === 0) return '±0%';
      return pct > 0 ? `+${pct}%` : `${pct}%`;
    }

    // 두 사진이 모두 준비되면 실제 픽셀 분석은 여기서 즉시 끝내고 값만 보관함.
    // 결과를 바로 보여주지 않고 beginSkinScan()으로 넘겨 스캔 연출(3초) 뒤에 표시함 —
    // 즉, 3초 동안 무거운 연산을 도는 게 아니라 순전히 연출용 지연임
    function runSkinPhotoAnalysis() {
      const startScores = analyzeSkinPhoto(skinPhotoImages.start);
      const endScores = analyzeSkinPhoto(skinPhotoImages.end);
      beginSkinScan(startScores, endScores);
    }

    // 사진 두 장 위에 스캔 라인 오버레이 + "분석 중" 상태를 3초간 보여준 뒤 결과 카드를 드러냄.
    // 이미 결과가 표시된 상태에서 사진을 다시 등록해도 이 함수가 다시 호출되므로 스캔 연출부터 재생됨
    function beginSkinScan(startScores, endScores) {
      if (skinScanTimeoutId) {
        clearTimeout(skinScanTimeoutId); // 기존 타이머가 남아있으면 정리해 중복 실행 방지
      }

      document.getElementById('skinChangeEmptyState').classList.add('hidden');
      const cardsEl = document.getElementById('skinChangeCards');
      cardsEl.classList.add('hidden');
      cardsEl.classList.remove('skin-fade-in');
      document.getElementById('skinChangeScanningState').classList.remove('hidden');
      document.getElementById('skinPhotoStartScanOverlay').classList.remove('hidden');
      document.getElementById('skinPhotoEndScanOverlay').classList.remove('hidden');

      skinScanTimeoutId = setTimeout(() => {
        document.getElementById('skinPhotoStartScanOverlay').classList.add('hidden');
        document.getElementById('skinPhotoEndScanOverlay').classList.add('hidden');
        document.getElementById('skinChangeScanningState').classList.add('hidden');
        renderSkinChangeCards(startScores, endScores);
        cardsEl.classList.remove('hidden');
        cardsEl.classList.add('skin-fade-in');
        skinScanTimeoutId = null;
      }, 3000);
    }

    // 분석된 1일차/마지막날 점수로 "항목별 변화" 카드 4개 + 종합 요약을 동적으로 갱신
    function renderSkinChangeCards(startScores, endScores) {
      const s = {
        hydration: Math.round(startScores.hydration),
        redness: Math.round(startScores.redness),
        oiliness: Math.round(startScores.oiliness),
        blemish: Math.round(startScores.blemish),
      };
      const e = {
        hydration: Math.round(endScores.hydration),
        redness: Math.round(endScores.redness),
        oiliness: Math.round(endScores.oiliness),
        blemish: Math.round(endScores.blemish),
      };

      // 수분: 오를수록 좋음(초록)
      const hydrationBadge = computeScoreBadge(e.hydration - s.hydration, true);
      setSkinBadge('hydrationBadge', hydrationBadge.label, hydrationBadge.color);
      document.getElementById('hydrationScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.hydration}</span> → 마지막날 <span class="font-bold text-gray-900">${e.hydration}</span>/100 <span class="${skinTextColorClasses[hydrationBadge.color]} font-semibold ml-1">${formatPercentDelta(s.hydration, e.hydration)}</span>`;
      document.getElementById('hydrationDesc').textContent = hydrationBadge.label === '개선됨'
        ? '사진 비교 결과 표면이 매끈해져 수분감이 올라간 것으로 보여요.'
        : hydrationBadge.label === '주의 필요'
          ? '표면 텍스처가 거칠어져 수분감이 떨어진 것으로 보여요. 수분크림을 더 챙겨보세요.'
          : '수분감은 1일차와 큰 차이가 없어요.';

      // 톤·홍조: 오를수록 나쁨(빨강/주황)
      const rednessBadge = computeScoreBadge(e.redness - s.redness, false);
      setSkinBadge('rednessBadge', rednessBadge.label, rednessBadge.color);
      document.getElementById('rednessScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.redness}</span> → 마지막날 <span class="font-bold text-gray-900">${e.redness}</span>/100 <span class="${skinTextColorClasses[rednessBadge.color]} font-semibold ml-1">${formatPercentDelta(s.redness, e.redness)}</span>`;
      document.getElementById('rednessDesc').textContent = rednessBadge.label === '주의 필요'
        ? '사진 속 붉은 영역이 넓어졌어요. 강한 자외선 노출과 관련 있을 수 있어요.'
        : rednessBadge.label === '개선됨'
          ? '붉은기가 가라앉아 톤이 안정된 것으로 보여요.'
          : '톤·홍조는 1일차와 큰 차이가 없어요.';

      // 유분: 오를수록 나쁨(번들거림)
      const oilinessBadge = computeScoreBadge(e.oiliness - s.oiliness, false);
      setSkinBadge('oilinessBadge', oilinessBadge.label, oilinessBadge.color);
      document.getElementById('oilinessScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.oiliness}</span> → 마지막날 <span class="font-bold text-gray-900">${e.oiliness}</span>/100 T존 <span class="${skinTextColorClasses[oilinessBadge.color]} font-semibold ml-1">${formatPercentDelta(s.oiliness, e.oiliness)}</span>`;
      document.getElementById('oilinessDesc').textContent = oilinessBadge.label === '주의 필요'
        ? 'T존 반사광이 늘어 유분이 증가한 것으로 보여요.'
        : oilinessBadge.label === '개선됨'
          ? 'T존 번들거림이 줄어 유분이 안정된 것으로 보여요.'
          : 'T존 유분은 1일차와 큰 차이가 없어요.';

      // 트러블: 반점(blob) 개수 차이를 "건수"로 표시
      const blemishDelta = e.blemish - s.blemish;
      const blemishBadge = computeBlemishBadge(blemishDelta);
      setSkinBadge('blemishBadge', blemishBadge.label, blemishBadge.color);
      const blemishDiffText = blemishDelta === 0 ? '±0건' : blemishDelta > 0 ? `+${blemishDelta}건` : `${blemishDelta}건`;
      document.getElementById('blemishScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.blemish}건</span> → 마지막날 <span class="font-bold text-gray-900">${e.blemish}건</span> <span class="${skinTextColorClasses[blemishBadge.color]} font-semibold ml-1">${blemishDiffText}</span>`;
      document.getElementById('blemishDesc').textContent = blemishDelta > 0
        ? '새로운 트러블이 감지됐어요. 세안과 보습 루틴을 다시 점검해보세요.'
        : blemishDelta < 0
          ? '트러블이 줄어들어 피부가 안정된 것으로 보여요.'
          : '트러블 개수는 1일차와 같아요.';

      // 종합 요약: 홍조·트러블 악화 여부에 따라 조언 문구를 조건 분기
      const worsenedRedness = rednessBadge.label === '주의 필요';
      const worsenedBlemish = blemishDelta > 0;
      const improvedHydration = hydrationBadge.label === '개선됨';
      let summary;
      if (worsenedRedness && worsenedBlemish) {
        summary = '여행 중 자외선 노출이 늘면서 홍조와 트러블이 조금 생겼어요. 자외선 차단제를 2~3시간마다 다시 발라주면 다음 여행에서 더 편안한 피부를 유지할 수 있을 거예요.';
      } else if (worsenedRedness) {
        summary = '홍조가 도드라진 편이에요. 자외선 차단제를 자주 덧발라 톤을 관리해보세요.';
      } else if (worsenedBlemish) {
        summary = '트러블이 새로 생겼어요. 자기 전 세안과 보습을 조금 더 신경 써보세요.';
      } else if (improvedHydration) {
        summary = '전반적으로 피부가 편안해졌어요. 지금의 수분 관리 루틴을 계속 유지해보세요.';
      } else {
        summary = '전체적으로 여행 전과 비슷한 상태를 유지했어요.';
      }
      document.getElementById('skinReportSummary').textContent = summary;
    }

    // 카드별 "상세보기" 아코디언 토글. 카드마다 독립적으로 펼침/접힘 가능(동시 펼침 허용)
    function toggleSkinDetail(key) {
      const detailEl = document.getElementById(`${key}Detail`);
      const willExpand = detailEl.classList.contains('hidden');
      detailEl.classList.toggle('hidden', !willExpand);
      document.getElementById(`${key}ToggleBtn`).setAttribute('aria-expanded', String(willExpand));
      document.getElementById(`${key}ToggleArrow`).textContent = willExpand ? '▴' : '▾';
    }
    ['hydration', 'redness', 'oiliness', 'blemish'].forEach((key) => {
      document.getElementById(`${key}ToggleBtn`).addEventListener('click', () => toggleSkinDetail(key));
    });

    function updateWizardNextButton(stepId, enabled) {
      const btn = document.querySelector(`#${stepId} .wizard-next-btn`);
      if (btn) btn.disabled = !enabled;
    }

    document.querySelectorAll('.wizard-back-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        const prev = btn.dataset.prev;
        if (prev === 'welcome') {
          document.getElementById('appContainer').classList.add('hidden');
          document.getElementById('screen-welcome').classList.remove('hidden');
        } else {
          showWizardStep(prev);
        }
      });
    });

    document.querySelectorAll('.wizard-next-btn[data-next]').forEach((btn) => {
      btn.addEventListener('click', () => {
        if (btn.disabled) return;
        showWizardStep(btn.dataset.next);
      });
    });

    // 온보딩 1단계: 이름 입력 - 값이 있어야 "다음" 버튼 활성화, 입력하는 대로 프로필/인사말에도 반영
    const regNameInput = document.getElementById('regNameInput');
    regNameInput.addEventListener('input', () => {
      const value = regNameInput.value.trim();
      updateWizardNextButton('reg-name', value.length > 0);
      userProfile.name = value;
      document.getElementById('nameInput').value = regNameInput.value;
      refreshGreetings();
    });

    // 온보딩 2단계: 닉네임 입력 - 값이 있어야 "다음" 버튼 활성화
    const regNicknameInput = document.getElementById('regNicknameInput');
    regNicknameInput.addEventListener('input', () => {
      const value = regNicknameInput.value.trim();
      updateWizardNextButton('reg-nickname', value.length > 0);
      userProfile.nickname = value;
      document.getElementById('nicknameInput').value = regNicknameInput.value;
      refreshGreetings();
    });

    // 온보딩 3단계: 성별 버튼 (단일 선택 - 선택 즉시 다음 단계로 자동 진행)
    document.querySelectorAll('.onboard-gender-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.onboard-gender-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        userProfile.gender = btn.dataset.gender;
        // 개인설정 화면의 성별 버튼도 함께 반영 (여성/남성일 때만, "선택 안 함"은 둘 다 비활성)
        document.querySelectorAll('.gender-btn').forEach((b) => b.classList.toggle('active', b.dataset.gender === btn.dataset.gender));
        setTimeout(() => showWizardStep('reg-age'), 200);
      });
    });

    // 생년월일로 만 나이 계산 (개인설정 화면의 숫자 나이 입력칸에 그대로 반영하기 위함)
    function calculateAge(birthDateStr) {
      const birth = new Date(`${birthDateStr}T00:00:00`);
      const today = new Date();
      let age = today.getFullYear() - birth.getFullYear();
      const hasHadBirthdayThisYear =
        today.getMonth() > birth.getMonth() ||
        (today.getMonth() === birth.getMonth() && today.getDate() >= birth.getDate());
      if (!hasHadBirthdayThisYear) age -= 1;
      return age;
    }

    // 온보딩 4단계: 생년월일 입력 - 값이 있어야 "다음" 버튼 활성화, 계산한 나이를 개인설정에도 반영
    const regBirthdateInput = document.getElementById('regBirthdateInput');
    regBirthdateInput.max = new Date().toISOString().slice(0, 10);
    regBirthdateInput.addEventListener('input', () => {
      const value = regBirthdateInput.value;
      updateWizardNextButton('reg-age', value.length > 0);
      if (value) {
        userProfile.birthDate = value;
        document.getElementById('ageInput').value = calculateAge(value);
      }
    });

    // 온보딩 5단계: 퍼스널컬러 버튼 (단일 선택 - 선택 즉시 다음 단계로 자동 진행)
    document.querySelectorAll('.onboard-tone-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.onboard-tone-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        userProfile.tone = btn.dataset.tone;
        // 개인설정 화면의 퍼스널컬러 버튼도 함께 반영
        document.querySelectorAll('.tone-btn').forEach((b) => b.classList.toggle('active', b.dataset.tone === btn.dataset.tone));
        setTimeout(() => showWizardStep('reg-skintype'), 200);
      });
    });

    // 피부 타입 버튼 토글 (온보딩 6단계, 단일 선택 - 선택 즉시 다음 단계로 자동 진행)
    document.querySelectorAll('.skin-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.skin-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        setTimeout(() => showWizardStep('reg-concerns'), 200);
      });
    });

    // 성별 버튼 토글 (개인설정, 선택 항목)
    document.querySelectorAll('.gender-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.gender-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // 퍼스널컬러 버튼 토글 (개인설정, 선택 항목)
    document.querySelectorAll('.tone-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.tone-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
      });
    });

    // 피부 고민 칩 토글 (중복 선택 가능, 온보딩 2단계)
    document.querySelectorAll('.concern-chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        chip.classList.toggle('active');
        updateWizardNextButton('reg-concerns', document.querySelectorAll('.concern-chip.active').length > 0);
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

    // 화장품이 추가/삭제될 때마다 카운트 배지 + 메인 화면 파우치 칩 목록 갱신
    const cosmeticCountBadge = document.getElementById('cosmeticCountBadge');
    function updateCosmeticCountBadge() {
      const count = cosmeticRows.querySelectorAll('.cosmetic-row').length;
      cosmeticCountBadge.textContent = count > 0 ? `(${count})` : '';
      // 화장품이 등록되면 촬영/입력 UI를 접고 카드 그리드로 보여줌
      if (getMyProducts().length > 0) {
        pouchCaptureForceOpen = false;
      }
      updatePouchSectionView();
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

    // 등록 페이지에 입력된 보유 화장품을 { name, category } 배열로 읽어옴
    function getMyProducts() {
      return Array.from(cosmeticRows.querySelectorAll('.cosmetic-row'))
        .map((row) => ({
          name: row.querySelector('input').value.trim(),
          category: row.querySelector('select').value,
        }))
        .filter((product) => product.name);
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
    function checkImportBan(destinationKey) {
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

    document.getElementById('importBanCloseBtn').addEventListener('click', () => {
      document.getElementById('importBanModal').classList.add('hidden');
    });

    document.getElementById('pouchPromptYesBtn').addEventListener('click', () => {
      document.getElementById('pouchPromptModal').classList.add('hidden');
      expandPouchSection();
    });

    document.getElementById('pouchPromptLaterBtn').addEventListener('click', () => {
      document.getElementById('pouchPromptModal').classList.add('hidden');
    });

    updateTabLockUI();

    // ===== 여행 일정 등록 (다중 구간) =====
    // 등록 2단계에서 쓰던 curated 국가 목록을 그대로 재사용
    const ALL_COUNTRIES = [
      '가나', '가봉', '가이아나', '감비아', '과테말라', '그레나다', '그리스', '기니', '기니비사우', '나미비아',
      '나우루', '나이지리아', '남수단', '남아프리카공화국', '네덜란드', '네팔', '노르웨이', '뉴질랜드', '니제르', '니카라과',
      '대만', '대한민국', '덴마크', '도미니카', '도미니카공화국', '독일', '동티모르', '라오스', '라이베리아', '라트비아',
      '러시아', '레바논', '레소토', '루마니아', '룩셈부르크', '르완다', '리비아', '리투아니아', '리히텐슈타인', '마다가스카르',
      '마셜제도', '말라위', '말레이시아', '말리', '멕시코', '모나코', '모로코', '모리셔스', '모리타니', '모잠비크',
      '몬테네그로', '몰도바', '몰디브', '몰타', '몽골', '미국', '미얀마', '미크로네시아', '바누아투', '바레인',
      '바베이도스', '바티칸', '바하마', '방글라데시', '베냉', '베네수엘라', '베트남', '벨기에', '벨라루스', '벨리즈',
      '보스니아헤르체고비나', '보츠와나', '볼리비아', '부룬디', '부르키나파소', '부탄', '북마케도니아', '북한', '불가리아', '브라질',
      '브루나이', '사모아', '사우디아라비아', '산마리노', '상투메프린시페', '세네갈', '세르비아', '세이셸', '세인트루시아', '세인트빈센트그레나딘',
      '세인트키츠네비스', '소말리아', '솔로몬제도', '수단', '수리남', '스리랑카', '스웨덴', '스위스', '스페인', '슬로바키아',
      '슬로베니아', '시리아', '시에라리온', '싱가포르', '아랍에미리트', '아르메니아', '아르헨티나', '아이슬란드', '아이티', '아일랜드',
      '아제르바이잔', '아프가니스탄', '안도라', '알바니아', '알제리', '앙골라', '앤티가바부다', '에리트레아', '에스와티니', '에스토니아',
      '에콰도르', '에티오피아', '엘살바도르', '영국', '예멘', '오만', '오스트리아', '온두라스', '요르단', '우간다',
      '우루과이', '우즈베키스탄', '우크라이나', '이라크', '이란', '이스라엘', '이집트', '이탈리아', '인도', '인도네시아',
      '일본', '자메이카', '잠비아', '적도기니', '조지아', '중국', '중앙아프리카공화국', '지부티', '짐바브웨', '차드',
      '체코', '칠레', '카메룬', '카보베르데', '카자흐스탄', '카타르', '캄보디아', '캐나다', '케냐', '코모로',
      '코스타리카', '코트디부아르', '콜롬비아', '콩고공화국', '콩고민주공화국', '쿠바', '쿠웨이트', '크로아티아', '키르기스스탄', '키리바시',
      '키프로스', '타지키스탄', '탄자니아', '태국', '토고', '통가', '투르크메니스탄', '투발루', '튀니지', '튀르키예',
      '트리니다드토바고', '파나마', '파라과이', '파키스탄', '파푸아뉴기니', '팔라우', '팔레스타인', '페루', '포르투갈', '폴란드',
      '프랑스', '피지', '핀란드', '필리핀', '헝가리', '호주',
    ];

    let tripSegments = [];
    let tripSegmentsExpanded = false;
    let prevValidSegmentCount = 0;

    // container: 이 행이 들어갈 컨테이너 (구간 번호를 그 안의 기존 행 수로 계산)
    // onChange: 필드가 바뀔 때마다 호출할 콜백 (메인 화면/온보딩 화면이 각자 다른 콜백을 전달)
    // initial: 값을 미리 채워야 할 때 사용 (온보딩에서 완료한 구간을 메인 화면으로 옮길 때)
    function buildTripSegmentRow(container, onChange, initial) {
      initial = initial || {};
      const segmentNumber = container.querySelectorAll('.trip-segment-row').length + 1;
      const row = document.createElement('div');
      row.className = 'trip-segment-row border border-gray-100 rounded-xl p-3 space-y-2';
      const countryOptions = ALL_COUNTRIES
        .map((c) => `<option value="${c}" ${c === initial.country ? 'selected' : ''}>${c}</option>`)
        .join('');
      row.innerHTML = `
        <div class="flex items-center justify-between">
          <p class="text-xs font-semibold text-gray-400">구간 ${segmentNumber}</p>
          <button type="button" class="remove-segment-btn text-gray-300 hover:text-gray-500 text-sm px-1">✕</button>
        </div>
        <div class="grid grid-cols-2 gap-2">
          <input type="date" value="${initial.start || ''}" class="segment-start-input w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
          <input type="date" value="${initial.end || ''}" class="segment-end-input w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500" />
        </div>
        <select class="segment-country-select w-full border border-gray-200 rounded-xl px-3 py-2 text-sm focus:outline-none focus:border-brand-500">
          <option value="">국가를 선택해주세요</option>
          ${countryOptions}
        </select>
      `;
      row.querySelector('.remove-segment-btn').addEventListener('click', () => {
        row.remove();
        onChange();
      });
      row.querySelector('.segment-start-input').addEventListener('change', onChange);
      row.querySelector('.segment-end-input').addEventListener('change', onChange);
      row.querySelector('.segment-country-select').addEventListener('change', () => {
        onChange();
        const country = row.querySelector('.segment-country-select').value;
        if (country && getMyProducts().length > 0) {
          checkImportBan(country);
        }
      });
      return row;
    }

    const tripSegmentRowsEl = document.getElementById('tripSegmentRows');

    document.getElementById('addTripSegmentBtn').addEventListener('click', () => {
      tripSegmentRowsEl.appendChild(buildTripSegmentRow(tripSegmentRowsEl, syncTripSegmentsFromDOM));
    });

    // 시작일/종료일/국가가 모두 채워진 구간만 유효한 여행 구간으로 인정
    function readTripSegmentsFromDOM() {
      const filled = Array.from(tripSegmentRowsEl.querySelectorAll('.trip-segment-row'))
        .map((row) => ({
          start: row.querySelector('.segment-start-input').value,
          end: row.querySelector('.segment-end-input').value,
          country: row.querySelector('.segment-country-select').value,
        }))
        .filter((seg) => seg.start && seg.end && seg.country);

      const invalid = filled.some((seg) => seg.end < seg.start);
      if (invalid) {
        showWarning('tripSegmentWarning', '종료일은 시작일보다 늦어야 해요');
        return filled.filter((seg) => seg.end >= seg.start);
      }
      hideWarning('tripSegmentWarning');
      return filled;
    }

    function formatSegmentRange(seg) {
      const shorten = (d) => d.slice(5).replace('-', '/');
      return `${shorten(seg.start)}~${shorten(seg.end)}`;
    }

    // 화면 최상단 "어디로 여행가시나요?" 아래 링크: 미등록 시 "여행지 등록하기 →",
    // 등록 후엔 "이탈리아 8/15~19 · 수정하기" 같은 요약으로 바뀌고 같은 폼을 다시 열어줌
    function updateTripSegmentsUI() {
      const hasSegments = tripSegments.length > 0;
      document.getElementById('tripSegmentsSection').classList.toggle('hidden', !tripSegmentsExpanded);
      const registerBtn = document.getElementById('mainRegisterTripBtn');
      if (hasSegments) {
        const seg = getActiveSegment() || tripSegments[0];
        const moreNote = tripSegments.length > 1 ? ` 외 ${tripSegments.length - 1}건` : '';
        registerBtn.textContent = `${seg.country} ${formatSegmentRange(seg)}${moreNote} · 수정하기`;
      } else {
        registerBtn.textContent = '여행지 등록하기 →';
      }
    }

    // 여행지 수정하기 클릭 시 이 섹션으로 스크롤 + 펼치기
    function expandTripSegmentsForm() {
      tripSegmentsExpanded = true;
      updateTripSegmentsUI();
      document.getElementById('tripSegmentsSection').scrollIntoView({ behavior: 'smooth' });
    }

    // 파우치 섹션으로 스크롤 + 촬영/입력 UI를 펼침 (메인 화면 상단으로 이동한 파우치 진입점들이 공유)
    function expandPouchSection() {
      pouchCaptureForceOpen = true;
      updatePouchSectionView();
      document.getElementById('pouchSection').scrollIntoView({ behavior: 'smooth' });
    }

    function syncTripSegmentsFromDOM() {
      tripSegments = readTripSegmentsFromDOM();
      updateTripSegmentsUI();
      if (tripSegments.length > 0 && prevValidSegmentCount === 0 && getMyProducts().length === 0) {
        document.getElementById('pouchPromptModal').classList.remove('hidden');
      }
      prevValidSegmentCount = tripSegments.length;
      refreshAdjustedRoutine();
      renderHistoryRecords();
    }

    // 오늘 날짜가 속한 구간 → 없으면 가장 가까운 미래 구간 → 없으면 가장 최근 지난 구간
    function getActiveSegment() {
      if (tripSegments.length === 0) return null;
      const today = new Date();
      const todayDate = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const withDates = tripSegments.map((seg) => ({
        ...seg,
        startDate: new Date(`${seg.start}T00:00:00`),
        endDate: new Date(`${seg.end}T00:00:00`),
      }));
      const current = withDates.find((seg) => todayDate >= seg.startDate && todayDate <= seg.endDate);
      if (current) return current;
      const future = withDates.filter((seg) => seg.startDate > todayDate).sort((a, b) => a.startDate - b.startDate);
      if (future.length > 0) return future[0];
      const past = withDates.filter((seg) => seg.endDate < todayDate).sort((a, b) => b.endDate - a.endDate);
      if (past.length > 0) return past[0];
      return null;
    }

    function getCurrentTripDestination() {
      const seg = getActiveSegment();
      return seg ? seg.country : null;
    }

    tripSegmentRowsEl.appendChild(buildTripSegmentRow(tripSegmentRowsEl, syncTripSegmentsFromDOM));
    updateTripSegmentsUI();

    document.getElementById('wizardFinishBtn').addEventListener('click', () => {
      onboardingComplete = true;
      updateTabLockUI();
      switchTab('inuse');
    });

    // ===== 내 파우치 (메인 화면 상단, 촬영 UI ↔ 등록된 화장품 카드 그리드 토글) =====
    // 화장품 카드 1장을 만드는 공통 로직 (대시보드의 내 화장품 루틴 그리드와 공유)
    function buildProductCard(product) {
      const category = cosmeticCategories.find((c) => c.value === product.category);
      const card = document.createElement('div');
      card.className = 'bg-white border border-gray-100 rounded-2xl p-3';
      card.innerHTML = `
        <div class="w-10 h-10 rounded-xl bg-brand-50 flex items-center justify-center text-lg mb-2">${category ? category.icon : '🧴'}</div>
        <p class="text-sm font-semibold truncate">${product.name}</p>
        <p class="text-xs text-gray-400">${category ? category.label : ''}</p>
      `;
      return card;
    }

    // 화장품이 1개 이상이면 카드 그리드를 보여주고 촬영/입력 UI는 접음("+ 추가"로 다시 펼침)
    function updatePouchSectionView() {
      const products = getMyProducts();
      const count = products.length;
      const grid = document.getElementById('pouchProductGrid');
      grid.innerHTML = '';
      products.forEach((product) => grid.appendChild(buildProductCard(product)));

      const showCapture = count === 0 || pouchCaptureForceOpen;
      grid.classList.toggle('hidden', count === 0 || showCapture);
      document.getElementById('pouchCaptureUI').classList.toggle('hidden', !showCapture);
      document.getElementById('pouchAddMoreBtn').classList.toggle('hidden', count === 0);
      document.getElementById('pouchSectionSubtitle').classList.toggle('hidden', count > 0);
    }

    document.getElementById('pouchAddMoreBtn').addEventListener('click', () => {
      pouchCaptureForceOpen = true;
      updatePouchSectionView();
    });

    updatePouchSectionView();

    // 국가별 기후 데이터 (전세계 196개국, '리뷰, 국가_수질 추가 DB' 원본의 체감온도·습도·기후·수질 평균값을 반영)
    // 여행 구간(tripSegments)의 country 값이 국가명 그대로이므로 키도 국가명을 그대로 사용
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
      판교: { temp: 30, humidity: 70, uvi: 8, climate: `열대기후`, waterQuality: `연수`, en: `Pangyo`, lat: 37.403549, lng: 127.102664 },
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
      이탈리아: { temp: 26, humidity: 47, uvi: 6, climate: `온대기후`, waterQuality: `경수`, en: `Italy`, lat: 41.9028, lng: 12.4964 },
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
      const destinationLabel = tripSegments.length > 0 ? tripSegments.map((s) => s.country).join(', ') : '미선택';
      const scheduleLabel =
        tripSegments.length > 0 ? tripSegments.map((s) => `${s.start}~${s.end}`).join(' / ') : '-';

      const rows = [
        ['나이', `${age}세`],
        ['성별', gender],
        ['피부 타입', skinLabel],
        ['퍼스널컬러', toneLabel],
        ['피부 고민', `${concernCount}개 선택`],
        ['보유 화장품', `${productCount}개`],
        ['여행지', destinationLabel],
        ['여행 기간', scheduleLabel],
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
        document.getElementById('myRoutineEmptyCard').addEventListener('click', expandPouchSection);
        return;
      }

      products.forEach((product) => grid.appendChild(buildProductCard(product)));
    }

    // 다른 여행자 리뷰(communityReviews)에서 내 여행지·피부타입에 맞는 추천 루틴을 찾아 보여줌
    function renderRecommendedRoutine() {
      const section = document.getElementById('recommendedRoutineSection');
      const activeSkinBtn = document.querySelector('.skin-btn.active');
      const skinTypeMap = { dry: '건성', normal: '중성', oily: '지성', combination: '복합성', dehydrated: '수부지' };
      const skinType = skinTypeMap[activeSkinBtn ? activeSkinBtn.dataset.skin : 'dry'];

      const destination = getCurrentTripDestination();
      const byCountry = communityReviews.filter((r) => r.country === destination);
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
        ? `${destination}을 다녀온 여행자 ${pick.id}님의 추천이에요`
        : `나와 같은 ${skinType} 피부의 ${pick.id}님이 ${destination}에서 추천한 루틴이에요`;
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

    // 날씨 원인(습도/자외선)과 뷰티 행동을 한 문장으로 연결하는 오늘의 인사이트
    function getTodayInsight(weather) {
      if (weather.humidity <= 30) {
        return { cause: '건조한 날씨', action: '오늘은 고보습 크림을 두 겹 발라주세요', highlight: 'humidity' };
      }
      if (weather.humidity >= 70) {
        return { cause: '습도 높은 날씨', action: '가벼운 토너 위주로 산뜻하게 마무리하세요', highlight: 'humidity' };
      }
      if (weather.uvi >= 8) {
        return { cause: '자외선이 강한 날씨', action: '2~3시간마다 선크림을 덧발라주세요', highlight: 'uvi' };
      }
      return { cause: '맑고 쾌적한 날씨', action: '가벼운 데일리 선크림 하나면 충분해요', highlight: 'temp' };
    }

    function formatTodayDate() {
      const now = new Date();
      return `${now.getMonth() + 1}월 ${now.getDate()}일`;
    }

    // 날씨 요약 + 오늘의 뷰티 인사이트 통합 카드 렌더링
    function renderTodayInsightCard(label, weather, start, end) {
      const insight = getTodayInsight(weather);
      const highlightClass = 'text-yellow-200 underline underline-offset-2 decoration-2';
      const metricClass = (key) => (insight.highlight === key ? highlightClass : '');

      document.getElementById('todayInsightLocation').textContent = `📍 ${label}`;
      document.getElementById('todayInsightDate').textContent =
        start && end ? `${formatTodayDate()} · ${getTripScheduleLabel(start, end)}` : formatTodayDate();
      document.getElementById('todayInsightMetrics').innerHTML = `
        <span class="${metricClass('temp')}">🌡️ ${weather.temp}°C</span>
        <span class="${metricClass('humidity')}">💧 습도 ${weather.humidity}%</span>
        <span class="${metricClass('uvi')}">☀️ 자외선 ${weather.uvi}</span>
      `;
      document.getElementById('todayInsightText').innerHTML =
        `<span class="${highlightClass} font-bold">${insight.cause}</span>예요. ${insight.action}`;
    }

    function renderTripOverview() {
      const activeSegment = getActiveSegment();
      const destinationKey = activeSegment ? activeSegment.country : null;

      if (!destinationKey) {
        document.getElementById('mainDashboard').classList.add('hidden');
        document.getElementById('todayInsightCard').classList.add('hidden');
        return;
      }

      document.getElementById('mainDashboard').classList.remove('hidden');
      document.getElementById('todayInsightCard').classList.remove('hidden');
      renderMyRoutineGrid();

      const label = destinationKey;
      const start = activeSegment.start;
      const end = activeSegment.end;

      const weather = weatherData[destinationKey];
      let todayCondition = '쾌적한 날씨';
      if (weather.humidity >= 70) {
        todayCondition = '습도 상승 주의';
      } else if (weather.humidity <= 30) {
        todayCondition = '건조 주의';
      } else if (weather.uvi >= 8) {
        todayCondition = '자외선 주의';
      }

      // 오늘 날짜가 속한 여행 구간의 국가가 바뀌면 지도도 그 국가로 자동 flyTo (좌표가 있는 국가만 가능)
      if (mapInstance && weather.lat != null && lastFlownMapDestination !== destinationKey) {
        lastFlownMapDestination = destinationKey;
        stopGlobeAutoRotate();
        flyToCity(destinationKey, weather);
      }

      renderTodayInsightCard(label, weather, start, end);

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

    // 사용중 탭의 여행지 기준으로 조정 제안 계산 (오늘 날짜가 속한 여행 구간의 국가로 갱신됨)
    function refreshAdjustedRoutine() {
      renderTripOverview();
      const destination = getCurrentTripDestination();
      if (!destination) return;
      const activeSkinBtn = document.querySelector('.skin-btn.active');
      const skinType = activeSkinBtn ? activeSkinBtn.dataset.skin : 'oily';
      const result = getAdjustedRoutine(destination, skinType, getMyProducts());
      renderAdjustedRoutine(result);
    }
    refreshAdjustedRoutine();

    // ===== 기록 화면: 달력별 기록 / 지구본 기록 =====
    function getSegmentStatus(seg) {
      const today = new Date();
      const todayDate = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const startDate = new Date(`${seg.start}T00:00:00`);
      const endDate = new Date(`${seg.end}T00:00:00`);
      if (todayDate < startDate) return { label: '예정', className: 'text-brand-500' };
      if (todayDate > endDate) return { label: '다녀옴', className: 'text-gray-400' };
      return { label: '진행중', className: 'text-green-600' };
    }

    function buildHistoryRecordCard(seg) {
      const status = getSegmentStatus(seg);
      const card = document.createElement('div');
      card.className = 'flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3';
      card.innerHTML = `
        <div class="w-10 h-10 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-lg shrink-0">📍</div>
        <div class="flex-1 min-w-0">
          <p class="text-sm font-semibold">${seg.country}</p>
          <p class="text-xs text-gray-400">${seg.start} ~ ${seg.end}</p>
        </div>
        <span class="text-xs font-semibold shrink-0 ${status.className}">${status.label}</span>
      `;
      return card;
    }

    function renderHistoryRecords() {
      const sorted = [...tripSegments].sort((a, b) => new Date(a.start) - new Date(b.start));

      const calendarList = document.getElementById('historyCalendarList');
      calendarList.innerHTML = '';
      sorted.forEach((seg) => calendarList.appendChild(buildHistoryRecordCard(seg)));
      document.getElementById('historyCalendarEmpty').classList.toggle('hidden', sorted.length > 0);

      const globeList = document.getElementById('historyGlobeList');
      globeList.innerHTML = '';
      sorted.forEach((seg) => globeList.appendChild(buildHistoryRecordCard(seg)));
      document.getElementById('historyGlobeEmpty').classList.toggle('hidden', sorted.length > 0);

      updateHistoryGlobeMarkers();
    }

    document.querySelectorAll('.history-view-toggle-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.history-view-toggle-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        const view = btn.dataset.view;
        document.getElementById('historyCalendarView').classList.toggle('hidden', view !== 'calendar');
        document.getElementById('historyGlobeView').classList.toggle('hidden', view !== 'globe');
        if (view === 'globe') {
          initHistoryGlobeIfNeeded();
        }
      });
    });

    // 지구본 기록: 좌표가 있는 국가(mock 데이터 일부)만 지구본에 마커로 표시, 전체 목록은 텍스트로 항상 표시
    let historyMapInstance = null;
    let historyMapMarkers = [];

    function initHistoryGlobeIfNeeded() {
      if (historyMapInstance) {
        updateHistoryGlobeMarkers();
        return;
      }
      const el = document.getElementById('historyGlobeViz');
      if (!el || typeof maplibregl === 'undefined') return;

      historyMapInstance = new maplibregl.Map({
        container: el,
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [20, 15],
        zoom: 1.3,
        attributionControl: false,
      });

      historyMapInstance.on('load', () => {
        try {
          historyMapInstance.setProjection({ type: 'globe' });
        } catch (e) {
          console.error('기록 지구본 setProjection 오류:', e);
        }
        try {
          historyMapInstance.setSky({
            'sky-color': '#eaf6ff',
            'sky-horizon-blend': 0.8,
            'horizon-color': '#ffffff',
            'horizon-fog-blend': 0.6,
            'fog-color': '#eaf6ff',
            'fog-ground-blend': 0.5,
          });
        } catch (e) {
          console.error('기록 지구본 setSky 오류:', e);
        }
        updateHistoryGlobeMarkers();
      });

      window.addEventListener('resize', () => {
        if (historyMapInstance) historyMapInstance.resize();
      });
    }

    function updateHistoryGlobeMarkers() {
      if (!historyMapInstance) return;
      historyMapMarkers.forEach((m) => m.remove());
      historyMapMarkers = [];
      tripSegments.forEach((seg) => {
        const weather = weatherData[seg.country];
        if (!weather || weather.lat == null || weather.lng == null) return;
        const el = document.createElement('div');
        el.className = 'store-marker';
        const marker = new maplibregl.Marker({ element: el })
          .setLngLat([weather.lng, weather.lat])
          .setPopup(
            new maplibregl.Popup({ offset: 16 }).setHTML(
              `<div style="font-size:12px;font-weight:700;">${seg.country}</div><div style="font-size:11px;color:#6b7280;">${seg.start} ~ ${seg.end}</div>`
            )
          )
          .addTo(historyMapInstance);
        historyMapMarkers.push(marker);
      });
    }

    renderHistoryRecords();
  </script>

</body>
</html>
"""

HTML_PAGE = (
    HTML_PAGE.replace("__EARTH_BG_URI__", EARTH_BG_URI)
    .replace("__LOGO_URI__", LOGO_URI)
    .replace("__AVATAR_URI_1__", AVATAR_URIS[0])
    .replace("__AVATAR_URI_2__", AVATAR_URIS[1])
    .replace("__AVATAR_URI_3__", AVATAR_URIS[2])
    .replace("__AVATAR_URI_4__", AVATAR_URIS[3])
)

components.html(HTML_PAGE, height=852, scrolling=True)