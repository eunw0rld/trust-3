import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SkinTrip", layout="centered")

st.markdown(
    """
    <style>
      .block-container { padding-top: 1.5rem; }
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
</style>
</head>
<body class="font-sans text-gray-900">

  <!-- ============ 랜딩 페이지 ============ -->
  <div id="screen-landing" class="max-w-md mx-auto min-h-screen bg-gray-50 border-x border-gray-100 flex flex-col px-6 pt-12 pb-8">

    <div>
      <h1 class="text-2xl font-bold leading-snug mb-3">
        여행 갈 때마다,<br />피부도 함께 챙겨봐요
      </h1>
      <p class="text-sm text-gray-400 leading-relaxed">
        여행지 기후에 맞춰 스킨케어 루틴을 조정해주는<br />SkinTrip과 함께 떠나볼까요
      </p>
    </div>

    <div class="flex-1 flex items-center justify-center gap-8 my-8">
      <span class="text-7xl">☀️</span>
      <span class="text-7xl">🧴</span>
    </div>

    <div>
      <button id="startBtn" type="button" class="w-full py-4 rounded-2xl bg-brand-500 text-white text-base font-bold">
        처음 시작해요
      </button>
      <button id="googleLoginBtn" type="button" class="w-full py-3.5 rounded-2xl border border-gray-200 text-gray-700 text-sm font-semibold flex items-center justify-center gap-2 mt-3">
        <svg width="18" height="18" viewBox="0 0 18 18" xmlns="http://www.w3.org/2000/svg">
          <path fill="#4285F4" d="M17.64 9.2c0-.637-.057-1.251-.164-1.84H9v3.481h4.844a4.14 4.14 0 0 1-1.796 2.716v2.259h2.908c1.702-1.567 2.684-3.874 2.684-6.615z"/>
          <path fill="#34A853" d="M9 18c2.43 0 4.467-.806 5.956-2.184l-2.908-2.259c-.806.54-1.837.86-3.048.86-2.344 0-4.328-1.584-5.036-3.711H.957v2.332A8.997 8.997 0 0 0 9 18z"/>
          <path fill="#FBBC05" d="M3.964 10.706A5.41 5.41 0 0 1 3.682 9c0-.593.102-1.17.282-1.706V4.962H.957A8.996 8.996 0 0 0 0 9c0 1.452.348 2.827.957 4.038l3.007-2.332z"/>
          <path fill="#EA4335" d="M9 3.58c1.321 0 2.508.454 3.44 1.345l2.582-2.58C13.463.891 11.426 0 9 0A8.997 8.997 0 0 0 .957 4.962L3.964 7.294C4.672 5.167 6.656 3.58 9 3.58z"/>
        </svg>
        구글로 로그인하기
      </button>
      <button id="skipStartBtn" type="button" class="w-full text-center text-xs text-gray-400 underline mt-4">
        둘러보기
      </button>
    </div>

  </div>

  <!-- 구글 로그인 후 일정 연동 여부를 묻는 팝업 -->
  <div id="calendarSyncModal" class="hidden fixed inset-0 bg-black/40 px-6 z-50">
    <div class="flex items-center justify-center h-full">
      <div class="bg-white rounded-2xl p-5 w-full max-w-xs">
        <p class="text-base font-bold mb-1">여행 일정 연동</p>
        <p class="text-sm text-gray-500 mb-5">구글 캘린더와 연동하면 여행지와 일정을 자동으로 채워드려요. 지금 연동하시겠어요?</p>
        <div class="space-y-2">
          <button id="syncYesBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">네, 연동할게요</button>
          <button id="syncNoBtn" type="button" class="w-full py-3 rounded-xl border border-gray-200 text-gray-600 text-sm font-semibold">아니오</button>
          <button id="syncLaterBtn" type="button" class="w-full py-2 text-xs text-gray-400 underline">조금 이따가 할게요</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ 앱 화면 ============ -->
  <div id="appContainer" class="hidden max-w-md mx-auto min-h-screen bg-gray-50 border-x border-gray-100">

    <!-- 상단 로고 -->
    <header class="px-5 pt-6 pb-4">
      <p class="text-lg font-bold tracking-tight">Skin<span class="text-brand-500">Trip</span></p>
    </header>

    <main class="px-5 pb-24">

      <!-- ============ 1. 등록 페이지 ============ -->
      <section id="screen-register" class="py-6">

        <!-- 등록 (1): 내 정보 등록 (온보딩에서 유일하게 필수인 단계) -->
        <div id="register-step1">

          <!-- 상단 바: 뒤로가기 · 제목 · 다음 -->
          <div class="flex items-center justify-between mb-4">
            <button id="step1ToLandingBtn" type="button" class="text-lg text-gray-400 w-8">←</button>
            <p class="text-base font-bold">내 정보 등록</p>
            <button id="step1ToStep2Btn" type="button" class="text-sm font-bold text-brand-500 w-8 text-right">완료</button>
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
              <option value="tokyo">일본</option>
              <option value="bangkok">태국</option>
              <option value="dubai">아랍에미리트</option>
              <option value="paris">프랑스</option>
              <option value="singapore">싱가포르</option>
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

          <!-- 여행 요약 배너 -->
          <div id="tripSummaryBanner" class="bg-white border border-gray-100 rounded-2xl p-4"></div>

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

          <!-- 일정 기반 기후 안내 -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">일정 기반 기후 안내</h3>
            <div id="climateTable" class="bg-white border border-gray-100 rounded-xl divide-y divide-gray-100"></div>
          </div>

          <!-- 오늘의 루틴 조정 제안 -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">오늘의 루틴 조정 제안</h3>
            <div id="adjustmentWarnings" class="space-y-2 mb-2"></div>
            <div id="adjustmentTips" class="space-y-2 mb-2"></div>
            <div id="adjustmentList" class="space-y-2"></div>
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
          <h2 class="text-base font-bold mb-1">내 주위 화장품 매장</h2>
          <p class="text-sm text-gray-400 mb-4">현재 위치 기준으로 가까운 매장을 보여드려요 (mock)</p>
        </div>

        <div class="relative h-40 rounded-2xl border border-gray-100" style="background-image: repeating-linear-gradient(0deg, transparent, transparent 19px, #e5e7eb 20px), repeating-linear-gradient(90deg, transparent, transparent 19px, #e5e7eb 20px); background-color: #f3f4f6;">
          <span class="absolute text-2xl" style="left: 28%; top: 30%;">📍</span>
          <span class="absolute text-2xl" style="left: 62%; top: 22%;">📍</span>
          <span class="absolute text-2xl" style="left: 70%; top: 60%;">📍</span>
          <span class="absolute text-2xl -translate-x-1/2 -translate-y-1/2" style="left: 50%; top: 55%;">🧍</span>
        </div>

        <div class="space-y-2">
          <div class="flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">올리브영 강남역점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 3분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">250m</p>
          </div>
          <div class="flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">시코르 강남점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 5분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">410m</p>
          </div>
          <div class="flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-xl bg-brand-50 text-brand-500 flex items-center justify-center text-lg shrink-0">🏬</div>
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

        <div id="communityFeed" class="space-y-3"></div>
      </section>

      <!-- ============ 6. 개인설정 페이지 ============ -->
      <section id="screen-settings" class="hidden py-6 space-y-6">
        <div>
          <h2 class="text-base font-bold mb-1">개인설정</h2>
          <p class="text-sm text-gray-400 mb-4">내 프로필과 여행 정보를 확인하고 수정할 수 있어요</p>
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

      </section>

    </main>

    <!-- 하단 메뉴바 (등록 완료 후에만 표시) -->
    <nav id="bottomNav" class="hidden fixed bottom-0 inset-x-0 max-w-md mx-auto bg-white border-t border-gray-100 z-40">
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
      try {
        if (window.frameElement) {
          window.frameElement.style.height = `${document.documentElement.scrollHeight}px`;
        }
      } catch (e) {
        // 프레임에 접근할 수 없는 환경이면 무시
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

    // 랜딩 페이지 ↔ 앱 화면 전환
    // 온보딩은 피부 정보(1단계)만 필수이고, 화장품·여행지 등록은 이후 개인설정 메뉴에서 진행
    function enterApp() {
      document.getElementById('screen-landing').classList.add('hidden');
      const app = document.getElementById('appContainer');
      app.classList.remove('hidden');
      showRegisterStep('step1');
      playScreenTransition(app);
    }
    function exitToLanding() {
      document.getElementById('appContainer').classList.add('hidden');
      const landing = document.getElementById('screen-landing');
      landing.classList.remove('hidden');
      playScreenTransition(landing);
    }
    document.getElementById('startBtn').addEventListener('click', enterApp);
    document.getElementById('skipStartBtn').addEventListener('click', enterApp);

    // 구글 로그인 → 여행 일정 연동 여부를 묻는 팝업
    function formatDateInput(date) {
      const yyyy = date.getFullYear();
      const mm = String(date.getMonth() + 1).padStart(2, '0');
      const dd = String(date.getDate()).padStart(2, '0');
      return `${yyyy}-${mm}-${dd}`;
    }

    document.getElementById('googleLoginBtn').addEventListener('click', () => {
      document.getElementById('calendarSyncModal').classList.remove('hidden');
    });

    function closeCalendarSyncModal() {
      document.getElementById('calendarSyncModal').classList.add('hidden');
    }

    document.getElementById('syncYesBtn').addEventListener('click', () => {
      closeCalendarSyncModal();
      // mock: 구글 캘린더 일정에서 가져온 여행지·기간으로 자동 채움
      const start = new Date();
      start.setDate(start.getDate() + 7);
      const end = new Date();
      end.setDate(end.getDate() + 11);
      document.getElementById('destinationSelect').value = 'tokyo';
      document.getElementById('tripStartDate').value = formatDateInput(start);
      document.getElementById('tripEndDate').value = formatDateInput(end);
      currentTripDestination = 'tokyo';
      enterApp();
    });

    document.getElementById('syncNoBtn').addEventListener('click', () => {
      closeCalendarSyncModal();
      enterApp();
    });

    document.getElementById('syncLaterBtn').addEventListener('click', () => {
      closeCalendarSyncModal();
      enterApp();
    });

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

    function switchTab(tabName) {
      bottomNavButtons.forEach((b) => b.classList.toggle('active', b.dataset.tab === tabName));
      Object.entries(screens).forEach(([key, el]) => el.classList.toggle('hidden', key !== tabName));
      playScreenTransition(screens[tabName]);
      if (tabName === 'inuse') {
        refreshAdjustedRoutine();
      } else if (tabName === 'settings') {
        renderProfileSummary();
      }
    }

    // 등록 완료 전에는 하단 메뉴바 자체를 숨김 (등록 흐름 중에는 이전/다음 버튼으로만 이동)
    function updateTabLockUI() {
      const bottomNav = document.getElementById('bottomNav');
      bottomNav.classList.toggle('hidden', !onboardingComplete);
      bottomNav.classList.toggle('flex', onboardingComplete);
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

    document.getElementById('step1ToLandingBtn').addEventListener('click', exitToLanding);

    // 피부 고민 칩 토글 (중복 선택 가능)
    document.querySelectorAll('.concern-chip').forEach((chip) => {
      chip.addEventListener('click', () => {
        chip.classList.toggle('active');
      });
    });

    // 보유 화장품 - 제품명 + 카테고리 행 추가
    const cosmeticCategories = [
      { value: 'cleanser', label: '클렌저' },
      { value: 'toner', label: '토너' },
      { value: 'essence', label: '에센스' },
      { value: 'lotion', label: '로션' },
      { value: 'cream', label: '크림' },
      { value: 'emulsion', label: '에멀전' },
      { value: 'sunscreen', label: '선크림' },
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
      return { valid: missing.length === 0, missing };
    }

    document.getElementById('completeOnboardingBtn').addEventListener('click', () => {
      const result = validateOnboarding();
      if (!result.valid) {
        showWarning('step2Warning', `${result.missing.join(', ')}을(를) 먼저 입력해주세요`);
        return;
      }
      onboardingComplete = true;
      updateTabLockUI();
      hideWarning('step2Warning');
      switchTab('inuse');
    });

    updateTabLockUI();

    // 국가별 기후 데이터 ('리뷰, 국가 DB' 원본의 체감온도·습도·기후·수질 평균값을 반영)
    const weatherData = {
      singapore: { temp: 34, humidity: 83, uvi: 9, climate: '열대기후', waterQuality: '연수' },
      tokyo: { temp: 20, humidity: 54, uvi: 6, climate: '온대기후', waterQuality: '연수' },
      bangkok: { temp: 33, humidity: 82, uvi: 10, climate: '열대기후', waterQuality: '연수' },
      dubai: { temp: 36, humidity: 24, uvi: 11, climate: '건조기후', waterQuality: '경수' },
      paris: { temp: 22, humidity: 56, uvi: 5, climate: '온대기후', waterQuality: '경수' },
    };
    const destinationLabels = {
      singapore: '싱가포르',
      tokyo: '일본',
      bangkok: '태국',
      dubai: '아랍에미리트',
      paris: '프랑스',
    };

    // 커뮤니티 피드 ('리뷰, 국가 DB' 원본에서 5개 지원 국가별 2건씩 발췌)
    const communityReviews = [
      { id: `glowup_diary`, gender: `여성`, age: 26, rating: 3, skinType: `건성`, country: `일본`, cosmetics: `고보습 크림, 립밤, 수분 앰플`, makeup: `촉촉한 쿠션과 크림 블러셔로 생기 있는 룩 연출.`, skincare: `건조한 날씨라 고보습 크림과 앰플로 수분 층 강화.`, review: `가을 날씨라 입술이 자주 텄어요. 립밤 없이는 하루도 못 버텼습니다.` },
      { id: `coolbreeze07`, gender: `남성`, age: 29, rating: 3, skinType: `복합성`, country: `일본`, cosmetics: `올인원 로션, 선크림, 미스트`, makeup: `가벼운 톤업로션 정도로 자연스럽게.`, skincare: `환절기 피부라 올인원 로션으로 간편하게 보습 유지.`, review: `일교차가 커서 아침저녁으로 피부 컨디션이 달랐어요.` },
      { id: `sunnytraveler23`, gender: `여성`, age: 54, rating: 3, skinType: `복합성`, country: `태국`, cosmetics: `가벼운 수분 선크림, 쿠션, 미스트`, makeup: `워터프루프 아이라이너와 마스카라로 땀과 습기에 대비하는 것이 좋습니다.`, skincare: `저녁에 이중세안을 꼭 하고 산뜻한 젤 타입 제품으로 유수분 밸런스를 유지하세요.`, review: `생각보다 더 더워서 땀 때문에 끈적임이 심했는데 가벼운 수분 선크림이 정말 큰 도움이 됐습니다.` },
      { id: `dahye_life`, gender: `남성`, age: 21, rating: 5, skinType: `복합성`, country: `태국`, cosmetics: `워터프루프 아이라이너, 피지 흡수 패드, 쿨링 젤`, makeup: `얇은 베이스에 워터프루프 제품 위주로 메이크업하고 픽싱 스프레이로 마무리하는 것을 추천합니다.`, skincare: `외출 중 블로팅 페이퍼로 피지를 자주 관리하고 쿨링 토너로 진정시켜 주세요.`, review: `야외 일정이 많았는데 자외선이 강해서 워터프루프 아이라이너을 자주 덧발라야 했어요.` },
      { id: `desertrose99`, gender: `여성`, age: 22, rating: 1, skinType: `건성`, country: `아랍에미리트`, cosmetics: `저자극 선크림, 진정 젤, 수분 세럼`, makeup: `가벼운 수분 쿠션으로 건조함을 커버하며 자연스러운 룩을 연출하세요.`, skincare: `낮은 습도로 인한 수분 손실을 막기 위해 고보습 크림을 겹겹이 발라주세요.`, review: `사막성 기후라 그런지 평소보다 피부가 훨씬 건조해지는 걸 느꼈어요.` },
      { id: `hana99`, gender: `남성`, age: 29, rating: 4, skinType: `건성`, country: `아랍에미리트`, cosmetics: `수분 로션, 선크림, 핸드크림`, makeup: `고보습 베이스 제품으로 들뜸 없이 매끈한 피부 표현이 가능합니다.`, skincare: `입술과 손이 트기 쉬우므로 립밤과 핸드크림을 항상 휴대하는 것이 좋습니다.`, review: `낮은 습도 때문에 피부가 계속 당기고 화장이 들떴어요. 수분 로션이 필수였습니다.` },
      { id: `wanderlust_log`, gender: `여성`, age: 34, rating: 3, skinType: `복합성`, country: `프랑스`, cosmetics: `산뜻한 로션, 선크림, 블로팅 페이퍼`, makeup: `촉촉한 선쿠션과 립틴트로 화사한 인상을 연출할 수 있습니다.`, skincare: `일교차가 크므로 수분 크림으로 아침저녁 보습을 꼼꼼히 챙겨주세요.`, review: `날씨는 선선했는데 실내 난방 때문에 오히려 피부가 건조하고 번들거렸어요.` },
      { id: `tropicalgirl_official`, gender: `남성`, age: 41, rating: 5, skinType: `복합성`, country: `프랑스`, cosmetics: `수분 크림, 립틴트, 선쿠션`, makeup: `촉촉한 쿠션과 크림 블러셔로 생기 있는 룩을 연출하는 것을 추천합니다.`, skincare: `환절기 피부 컨디션 변화에 대비해 올인원 로션으로 간편하게 보습을 유지하세요.`, review: `사계절이 뚜렷한 곳이라 그런지 여행 기간 내내 온도 변화에 신경 써야 했어요.` },
      { id: `yeji_life`, gender: `여성`, age: 27, rating: 5, skinType: `지성`, country: `싱가포르`, cosmetics: `피지 컨트롤 파우더, 워터프루프 선크림, 미스트`, makeup: `베이스는 얇게, 픽싱 스프레이로 마무리해 번들거림 방지. 아이라이너는 워터프루프 필수.`, skincare: `저녁에 이중세안 필수, 가벼운 젤 타입 로션 위주로 유수분 밸런스 유지.`, review: `습도가 높아서 파운데이션이 계속 뜨더라고요. 워터프루프 제품 없이는 3시간도 못 버텼어요.` },
      { id: `funtraveler_world`, gender: `남성`, age: 34, rating: 3, skinType: `복합성`, country: `싱가포르`, cosmetics: `선크림 SPF50+, 블로팅 페이퍼, 쿨링 토너`, makeup: `남성용 톤업크림 정도만 가볍게, 유분 많은 제품은 피하기.`, skincare: `외출 전후 블로팅 페이퍼로 피지 제거, 쿨링 토너로 진정.`, review: `야외 일정이 많았는데 선크림 안 바르면 바로 붉어졌어요. 자주 덧발라야 합니다.` },
    ];

    function renderStars(rating) {
      const filled = '★'.repeat(rating);
      const empty = '★'.repeat(5 - rating);
      return `<span class="text-brand-500">${filled}</span><span class="text-gray-300">${empty}</span>`;
    }

    function renderCommunityFeed() {
      const communityFeed = document.getElementById('communityFeed');
      communityFeed.innerHTML = '';
      communityReviews.forEach((post) => {
        const card = document.createElement('div');
        card.className = 'bg-white border border-gray-100 rounded-xl p-4';
        card.innerHTML = `
          <div class="flex items-center gap-2 mb-2">
            <div class="w-8 h-8 rounded-full bg-brand-50 text-brand-600 text-xs font-bold flex items-center justify-center shrink-0">${post.id.charAt(0).toUpperCase()}</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold truncate">${post.id}</p>
              <span class="text-[10px] text-gray-400">${post.country} 여행 · ${post.gender} · ${post.age}세</span>
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
    renderCommunityFeed();

    // 개인설정 탭에 등록된 내 정보를 요약해서 보여줌
    function renderProfileSummary() {
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
      const destinationLabel = destinationLabels[destinationKey] || '미선택';
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
        tips.push('이 지역은 경수(센물) 지역이에요. 두피·모발에 미네랄이 쌓이기 쉬우니 클래리파잉 샴푸나 헤어팩을 챙겨보세요');
      } else {
        tips.push('이 지역은 연수(단물) 지역이에요. 세안 후 당김이 적은 편이라 순한 클렌저로도 충분해요');
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

    // 등록 2단계에서 선택한 여행지를 사용중 탭의 알림/기후 안내에도 동일하게 반영
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

      // 여행지는 등록했지만 파우치가 비어있으면 살짝 눈에 띄는 알림 스타일로 표시
      const pouchCard = document.getElementById('mainPouchCardFilled');
      const pouchIcon = document.getElementById('mainPouchIcon');
      const pouchText = document.getElementById('mainPouchFilledText');
      const pouchEmpty = productCount === 0;
      pouchCard.className = `w-full flex items-center gap-3 border rounded-2xl p-4 text-left ${pouchEmpty ? 'bg-red-50 border-red-100' : 'bg-white border-gray-100'}`;
      pouchIcon.className = `w-11 h-11 rounded-xl flex items-center justify-center text-xl shrink-0 ${pouchEmpty ? 'bg-red-100 text-red-500' : 'bg-brand-50 text-brand-500'}`;
      pouchText.className = pouchEmpty ? 'text-xs font-medium text-red-500' : 'text-xs text-gray-400';
      pouchText.textContent = pouchEmpty ? '파우치가 비어있어요! 화장품을 등록해주세요' : `화장품 ${productCount}개 등록됨`;

      const label = destinationLabels[currentTripDestination] || '여행지';
      const start = document.getElementById('tripStartDate').value;
      const end = document.getElementById('tripEndDate').value;
      document.getElementById('tripSummaryBanner').innerHTML = `
        <div class="flex items-center justify-between">
          <div>
            <p class="text-xs text-gray-400 mb-0.5">이번 여행</p>
            <p class="text-base font-bold">📍 ${label}</p>
            ${start && end ? `<p class="text-xs text-gray-400 mt-0.5">${start} ~ ${end}</p>` : ''}
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

      const days = [
        { dayLabel: 'Day 1', suffix: '', temp: weather.temp - 1, humidity: weather.humidity - 13, condition: '맑음', highlight: false },
        { dayLabel: 'Day 2', suffix: ' (오늘)', temp: weather.temp, humidity: weather.humidity, condition: todayCondition, highlight: true },
        { dayLabel: 'Day 3', suffix: '', temp: weather.temp - 2, humidity: weather.humidity - 8, condition: '흐림', highlight: false },
      ];

      const climateTable = document.getElementById('climateTable');
      climateTable.innerHTML = '';
      days.forEach((day) => {
        const row = document.createElement('div');
        row.className = `flex items-center justify-between px-4 py-3${day.highlight ? ' bg-brand-50' : ''}`;
        row.innerHTML = `
          <div>
            <p class="text-sm font-semibold">${day.dayLabel} · ${label}${day.suffix}</p>
            <p class="text-xs ${day.highlight ? 'text-brand-500 font-semibold' : 'text-gray-400'}">${day.condition}</p>
          </div>
          <p class="text-base font-bold text-gray-800">${day.temp}°C <span class="text-xs font-normal text-gray-400">· 습도 ${day.humidity}%</span></p>
        `;
        climateTable.appendChild(row);
      });
    }

    // 사용중 탭의 여행지 기준으로 조정 제안 계산 (등록 2단계에서 선택한 여행지로 갱신됨)
    let currentTripDestination = 'tokyo';
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


components.html(HTML_PAGE, height=700, scrolling=False)
