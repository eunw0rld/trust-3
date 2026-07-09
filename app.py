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
      },
    },
  };
</script>
<style>
  body {
    background: #f7f7f7;
  }
  .bottom-nav-btn {
    color: #9ca3af;
  }
  .bottom-nav-btn.active {
    color: #f97316;
  }
  .skin-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .skin-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #ea580c;
  }
  .gender-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .gender-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #ea580c;
  }
  .feedback-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .feedback-btn.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #ea580c;
  }
  .concern-chip {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .concern-chip.active {
    border-color: #f97316;
    background: #fff7ed;
    color: #ea580c;
  }
</style>
</head>
<body class="font-sans text-gray-900">

  <!-- ============ 랜딩 페이지 ============ -->
  <div id="screen-landing" class="max-w-md mx-auto min-h-screen bg-white border-x border-gray-100 flex flex-col px-6 pt-12 pb-8">

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
      <button id="startBtn" type="button" class="w-full py-4 rounded-2xl bg-orange-500 text-white text-base font-bold shadow-lg shadow-orange-200">
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
          <button id="syncYesBtn" type="button" class="w-full py-3 rounded-lg bg-orange-500 text-white text-sm font-bold">네, 연동할게요</button>
          <button id="syncNoBtn" type="button" class="w-full py-3 rounded-lg border border-gray-200 text-gray-600 text-sm font-semibold">아니오</button>
          <button id="syncLaterBtn" type="button" class="w-full py-2 text-xs text-gray-400 underline">조금 이따가 할게요</button>
        </div>
      </div>
    </div>
  </div>

  <!-- ============ 앱 화면 ============ -->
  <div id="appContainer" class="hidden max-w-md mx-auto min-h-screen bg-white border-x border-gray-100">

    <!-- 상단 로고 -->
    <header class="px-5 pt-6 pb-4">
      <p class="text-lg font-bold tracking-tight">Skin<span class="text-orange-500">Trip</span></p>
    </header>

    <main class="px-5 pb-24">

      <!-- ============ 1. 등록 페이지 ============ -->
      <section id="screen-register" class="py-6">

        <!-- 등록 (0): 보유 화장품 촬영 -->
        <div id="register-step0" class="space-y-8">

          <div>
            <button id="step0ToLandingBtn" type="button" class="text-xs text-gray-400 mb-3">← 이전</button>
            <h2 class="text-base font-bold mb-1">보유 화장품을 촬영해주세요</h2>
            <p class="text-sm text-gray-400 mb-4">사진 한 장이면 화장품 이름과 종류를 자동으로 인식해드려요</p>

            <label for="cosmeticPhotoInput" class="flex flex-col items-center justify-center gap-1.5 border-2 border-dashed border-gray-300 rounded-2xl py-10 text-gray-400 cursor-pointer hover:border-orange-400 hover:text-orange-500 transition">
              <span class="text-3xl">📷</span>
              <span class="text-sm font-semibold">탭해서 촬영하기</span>
              <span class="text-xs text-gray-300">또는 앨범에서 사진 선택</span>
            </label>
            <input id="cosmeticPhotoInput" type="file" accept="image/*" capture="environment" class="hidden" />

            <!-- 인식 중 -->
            <div id="scanningState" class="hidden border border-gray-100 rounded-2xl p-3 mt-3">
              <div class="flex items-center gap-3">
                <img id="scanningThumb" src="" alt="촬영한 화장품" class="w-14 h-14 rounded-lg object-cover shrink-0" />
                <div class="flex-1 min-w-0">
                  <p class="text-sm font-semibold text-gray-700">화장품 정보를 인식하고 있어요...</p>
                  <div class="h-1.5 bg-gray-100 rounded-full mt-2 overflow-hidden">
                    <div id="scanningBar" class="h-full bg-orange-400 rounded-full" style="width: 0%;"></div>
                  </div>
                </div>
              </div>
            </div>

            <!-- 인식 결과 확인 -->
            <div id="scanResult" class="hidden border border-orange-200 bg-orange-50 rounded-2xl p-3 mt-3">
              <div class="flex items-center gap-3 mb-3">
                <img id="scanResultThumb" src="" alt="촬영한 화장품" class="w-14 h-14 rounded-lg object-cover shrink-0" />
                <div class="flex-1 min-w-0">
                  <p class="text-[10px] font-semibold text-orange-500 mb-1">인식 완료 · 맞는지 확인해주세요</p>
                  <input id="scanResultName" type="text" class="w-full bg-white border border-gray-200 rounded-lg px-2 py-1.5 text-sm font-semibold focus:outline-none focus:border-orange-400" />
                </div>
              </div>
              <div class="flex gap-2">
                <select id="scanResultCategory" class="flex-1 border border-gray-200 rounded-lg px-2 py-2 text-sm text-gray-600 bg-white focus:outline-none focus:border-orange-400"></select>
                <button id="confirmScanBtn" type="button" class="px-4 rounded-lg bg-orange-500 text-white text-sm font-bold">추가</button>
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
            <p id="step0Warning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-lg px-3 py-2 mb-3"></p>
            <button id="step0ToStep1Btn" type="button" class="w-full py-3.5 rounded-lg bg-orange-500 text-white text-sm font-bold">
              다음
            </button>
          </div>

        </div>

        <!-- 등록 (1): 내 정보 등록 -->
        <div id="register-step1" class="hidden">

          <!-- 상단 바: 뒤로가기 · 제목 · 다음 -->
          <div class="flex items-center justify-between mb-4">
            <button id="step1ToStep0Btn" type="button" class="text-lg text-gray-400 w-8">←</button>
            <p class="text-base font-bold">내 정보 등록</p>
            <button id="step1ToStep2Btn" type="button" class="text-sm font-bold text-orange-500 w-8 text-right">다음</button>
          </div>

          <p id="step1Warning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-lg px-3 py-2 mb-4"></p>

          <div class="space-y-6">

            <!-- 기본 정보 -->
            <div>
              <div class="bg-gray-50 rounded-xl px-4 py-2.5 mb-3">
                <p class="text-sm font-bold text-gray-700">기본 정보</p>
              </div>
              <div class="px-1 space-y-4">
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">나이</p>
                  <input id="ageInput" type="number" min="1" max="120" placeholder="예: 27" class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-orange-400" />
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
              <div class="bg-gray-50 rounded-xl px-4 py-2.5 mb-3">
                <p class="text-sm font-bold text-gray-700">피부 정보</p>
                <p class="text-xs text-gray-400 mt-0.5">맞춤 루틴을 위해 꼭 선택해주세요</p>
              </div>
              <div class="px-1 space-y-4">
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">피부 타입 <span class="text-gray-300 font-normal">(1개)</span></p>
                  <div class="flex flex-wrap gap-2">
                    <button type="button" data-skin="oily" class="skin-btn active rounded-full px-4 py-2 text-sm font-semibold">지성</button>
                    <button type="button" data-skin="dry" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">건성</button>
                    <button type="button" data-skin="combination" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">복합성</button>
                    <button type="button" data-skin="sensitive" class="skin-btn rounded-full px-4 py-2 text-sm font-semibold">민감성</button>
                  </div>
                </div>
                <div>
                  <p class="text-xs font-semibold text-gray-400 mb-2">피부 고민 <span class="text-gray-300 font-normal">(중복 선택 가능)</span></p>
                  <div class="flex flex-wrap gap-2">
                    <button type="button" data-concern="trouble" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">트러블</button>
                    <button type="button" data-concern="dryness" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">건조함</button>
                    <button type="button" data-concern="oiliness" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">유분과다</button>
                    <button type="button" data-concern="sensitivity" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">민감성</button>
                    <button type="button" data-concern="pigmentation" class="concern-chip rounded-full px-4 py-2 text-sm font-medium">색소침착</button>
                  </div>
                </div>
              </div>
            </div>

          </div>

        </div>

        <!-- 등록 (2): 여행지·여행 계획 입력 -->
        <div id="register-step2" class="hidden space-y-8">

          <div>
            <button id="step2ToStep1Btn" type="button" class="text-xs text-gray-400 mb-3">← 이전</button>
            <h2 class="text-base font-bold mb-1">여행지와 여행 계획을 알려주세요</h2>
            <p class="text-sm text-gray-400 mb-4">입력한 여행지 기후에 맞춰 루틴을 조정해드려요</p>

            <p class="text-xs font-semibold text-gray-400 mb-2">여행지</p>
            <select id="destinationSelect" class="w-full border border-gray-200 rounded-lg px-3 py-2.5 text-sm mb-4 focus:outline-none focus:border-orange-400">
              <option value="">여행지를 선택해주세요</option>
              <option value="tokyo">일본</option>
              <option value="bangkok">태국</option>
              <option value="dubai">아랍에미리트</option>
              <option value="paris">프랑스</option>
              <option value="singapore">싱가포르</option>
            </select>

            <p class="text-xs font-semibold text-gray-400 mb-2">여행 계획</p>
            <div class="grid grid-cols-2 gap-2">
              <input id="tripStartDate" type="date" class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-orange-400" />
              <input id="tripEndDate" type="date" class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-orange-400" />
            </div>
          </div>

          <div>
            <p id="step2Warning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-lg px-3 py-2 mb-3"></p>
            <button id="completeOnboardingBtn" type="button" class="w-full py-3.5 rounded-lg bg-orange-500 text-white text-sm font-bold">
              완료하고 시작하기
            </button>
          </div>

        </div>

      </section>

      <!-- ============ 2. 사용중 페이지 ============ -->
      <section id="screen-inuse" class="hidden py-6 space-y-8">

        <!-- 알림 목업 -->
        <div>
          <p id="tripDayLabel" class="text-xs font-semibold text-gray-400 mb-1">DAY 2 · 도쿄</p>
          <h2 class="text-base font-bold mb-1">여행 중 알림</h2>
          <p class="text-xs text-gray-400 mb-3">실제 앱에서는 푸시 알림으로 도착해요. 아래는 미리보기예요</p>
          <div class="space-y-3">
            <div class="border border-gray-100 rounded-2xl p-3 shadow-sm">
              <div class="flex gap-3">
                <div class="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center text-sm shrink-0">🧴</div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <p class="text-xs font-bold text-gray-500">SkinTrip</p>
                    <p class="text-[10px] text-gray-400">지금</p>
                  </div>
                  <p class="text-sm font-semibold text-gray-900 mt-0.5">습도가 오늘 밤부터 오를 예정이에요</p>
                  <p class="text-xs text-gray-500 mt-0.5">보유 중인 <span class="text-orange-500 font-semibold">에멀전</span>은 오늘 저녁 루틴에서 빼는 걸 추천해요</p>
                </div>
              </div>
            </div>
            <div class="border border-gray-100 rounded-2xl p-3 shadow-sm">
              <div class="flex gap-3">
                <div class="w-9 h-9 rounded-xl bg-gray-900 text-white flex items-center justify-center text-sm shrink-0">☀️</div>
                <div class="flex-1 min-w-0">
                  <div class="flex items-center justify-between">
                    <p class="text-xs font-bold text-gray-500">SkinTrip</p>
                    <p class="text-[10px] text-gray-400">3시간 전</p>
                  </div>
                  <p class="text-sm font-semibold text-gray-900 mt-0.5">오늘 자외선 지수 매우 높음</p>
                  <p class="text-xs text-gray-500 mt-0.5">2~3시간마다 <span class="text-orange-500 font-semibold">선크림</span> 재도포를 잊지 마세요</p>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- 일정 기반 기후 안내 -->
        <div>
          <h3 class="text-sm font-semibold text-gray-700 mb-3">일정 기반 기후 안내</h3>
          <div id="climateTable" class="border border-gray-100 rounded-xl divide-y divide-gray-100"></div>
        </div>

        <!-- 오늘의 루틴 조정 제안 -->
        <div>
          <h3 class="text-sm font-semibold text-gray-700 mb-3">오늘의 루틴 조정 제안</h3>
          <div id="adjustmentWarnings" class="space-y-2 mb-2"></div>
          <div id="adjustmentList" class="space-y-2"></div>
        </div>

      </section>

      <!-- ============ 3. 사용후 페이지 (입국신고서 컨셉) ============ -->
      <section id="screen-afteruse" class="hidden py-6 space-y-6">

        <button id="afterUseToSettingsBtn" type="button" class="text-xs text-gray-400">← 이전</button>

        <div class="border border-gray-200 rounded-2xl p-5">
          <div class="flex items-center justify-between mb-1">
            <p class="text-[10px] font-semibold tracking-widest text-gray-400 uppercase">Arrival Skin Declaration</p>
            <span class="text-[10px] font-bold text-orange-500 border border-orange-200 rounded-full px-2 py-0.5">DAY 5</span>
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
              <button type="button" data-feedback="good" class="feedback-btn rounded-lg py-2 text-xs font-semibold">좋음</button>
              <button type="button" data-feedback="normal" class="feedback-btn rounded-lg py-2 text-xs font-semibold">보통</button>
              <button type="button" data-feedback="trouble" class="feedback-btn rounded-lg py-2 text-xs font-semibold">트러블 있었음</button>
            </div>
            <textarea rows="3" placeholder="자유롭게 남겨주세요 (선택)" class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-orange-400"></textarea>
          </div>

          <!-- 추가 케어 제안 -->
          <div class="border-t border-dashed border-gray-200 pt-4">
            <p class="text-xs font-semibold text-gray-500 mb-2">귀국 후 추가 케어 제안</p>
            <ul class="space-y-2 text-sm text-gray-700">
              <li class="flex gap-2"><span class="text-orange-500">•</span>장시간 비행 후 진정 마스크팩으로 수분 보충</li>
              <li class="flex gap-2"><span class="text-orange-500">•</span>건조해진 각질 정리를 위한 약산성 필링</li>
              <li class="flex gap-2"><span class="text-orange-500">•</span>2~3일간 저자극 로션으로 피부 장벽 회복</li>
            </ul>
          </div>
        </div>

        <button type="button" class="w-full py-3.5 rounded-lg bg-orange-500 text-white text-sm font-bold">신고서 제출</button>

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
          <div class="flex items-center gap-3 border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-lg bg-orange-50 text-orange-500 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">올리브영 강남역점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 3분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">250m</p>
          </div>
          <div class="flex items-center gap-3 border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-lg bg-orange-50 text-orange-500 flex items-center justify-center text-lg shrink-0">🏬</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">시코르 강남점</p>
              <p class="text-xs text-gray-400">헬스&뷰티 · 도보 5분</p>
            </div>
            <p class="text-xs text-gray-500 shrink-0">410m</p>
          </div>
          <div class="flex items-center gap-3 border border-gray-100 rounded-xl p-3">
            <div class="w-10 h-10 rounded-lg bg-orange-50 text-orange-500 flex items-center justify-center text-lg shrink-0">🏬</div>
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

        <div class="border border-gray-100 rounded-xl p-4">
          <div class="flex items-center gap-2 mb-2">
            <div class="w-8 h-8 rounded-full bg-orange-50 text-orange-600 text-xs font-bold flex items-center justify-center shrink-0">J</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">jiyeon_life</p>
              <span class="text-[10px] text-gray-400">일본 여행</span>
            </div>
            <p class="text-xs shrink-0"><span class="text-orange-500">★★★★★</span></p>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed">날씨는 선선했는데 실내 난방 때문에 오히려 피부가 건조하고 번들거렸어요.</p>
        </div>

        <div class="border border-gray-100 rounded-xl p-4">
          <div class="flex items-center gap-2 mb-2">
            <div class="w-8 h-8 rounded-full bg-orange-50 text-orange-600 text-xs font-bold flex items-center justify-center shrink-0">B</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">backpacklife_daily</p>
              <span class="text-[10px] text-gray-400">싱가포르 여행</span>
            </div>
            <p class="text-xs shrink-0"><span class="text-orange-500">★★★★</span><span class="text-gray-300">★</span></p>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed">실내는 에어컨 때문에 건조하고 밖은 습해서 피부가 오락가락했어요.</p>
        </div>

        <div class="border border-gray-100 rounded-xl p-4">
          <div class="flex items-center gap-2 mb-2">
            <div class="w-8 h-8 rounded-full bg-orange-50 text-orange-600 text-xs font-bold flex items-center justify-center shrink-0">H</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">hana99</p>
              <span class="text-[10px] text-gray-400">아랍에미리트 여행</span>
            </div>
            <p class="text-xs shrink-0"><span class="text-orange-500">★★★★</span><span class="text-gray-300">★</span></p>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed">낮은 습도 때문에 피부가 계속 당기고 화장이 들떴어요. 수분 로션이 필수였습니다.</p>
        </div>

        <div class="border border-gray-100 rounded-xl p-4">
          <div class="flex items-center gap-2 mb-2">
            <div class="w-8 h-8 rounded-full bg-orange-50 text-orange-600 text-xs font-bold flex items-center justify-center shrink-0">D</div>
            <div class="flex-1 min-w-0">
              <p class="text-sm font-semibold">dewyskin_k</p>
              <span class="text-[10px] text-gray-400">프랑스 여행</span>
            </div>
            <p class="text-xs shrink-0"><span class="text-orange-500">★★★★★</span></p>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed">일교차가 커서 아침저녁으로 피부 컨디션이 완전히 달랐어요. 저자극 크림이 도움이 됐어요.</p>
        </div>
      </section>

      <!-- ============ 6. 개인설정 페이지 ============ -->
      <section id="screen-settings" class="hidden py-6 space-y-6">
        <div>
          <h2 class="text-base font-bold mb-1">개인설정</h2>
          <p class="text-sm text-gray-400 mb-4">내 프로필과 여행 정보를 확인하고 수정할 수 있어요</p>
        </div>

        <div id="profileSummaryCard" class="border border-gray-100 rounded-2xl p-4 space-y-2"></div>

        <div class="space-y-2">
          <button id="settingsEditBtn" type="button" class="w-full py-3 rounded-lg border border-gray-200 text-gray-700 text-sm font-semibold">
            정보 수정하기
          </button>
          <button id="goToAfterUseBtn" type="button" class="w-full py-3 rounded-lg bg-orange-500 text-white text-sm font-bold">
            여행 후 피부 신고서 작성하기
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
      <button type="button" data-tab="settings" class="bottom-nav-btn flex-1 flex flex-col items-center gap-0.5 py-2.5 text-[11px] font-medium">
        <span class="text-xl">👤</span>
        <span>개인설정</span>
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

    // 랜딩 페이지 ↔ 앱 화면 전환
    function enterApp() {
      document.getElementById('screen-landing').classList.add('hidden');
      document.getElementById('appContainer').classList.remove('hidden');
    }
    function exitToLanding() {
      document.getElementById('appContainer').classList.add('hidden');
      document.getElementById('screen-landing').classList.remove('hidden');
    }
    document.getElementById('startBtn').addEventListener('click', enterApp);
    document.getElementById('skipStartBtn').addEventListener('click', enterApp);
    document.getElementById('step0ToLandingBtn').addEventListener('click', exitToLanding);

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

    // 하단 메뉴바 전환 (지도/메인/커뮤니티/개인설정)
    const bottomNavButtons = document.querySelectorAll('.bottom-nav-btn');
    const screens = {
      register: document.getElementById('screen-register'),
      inuse: document.getElementById('screen-inuse'),
      afteruse: document.getElementById('screen-afteruse'),
      map: document.getElementById('screen-map'),
      community: document.getElementById('screen-community'),
      settings: document.getElementById('screen-settings'),
    };
    let onboardingComplete = false;

    function switchTab(tabName) {
      bottomNavButtons.forEach((b) => b.classList.toggle('active', b.dataset.tab === tabName));
      Object.entries(screens).forEach(([key, el]) => el.classList.toggle('hidden', key !== tabName));
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
      ['step0', 'step1', 'step2'].forEach((key) => {
        document.getElementById(`register-${key}`).classList.toggle('hidden', key !== stepName);
      });
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

    // 등록 1단계 → 2단계 이동 조건: 나이 입력 + 성별 선택
    function validateStep1() {
      const missing = [];
      if (!document.getElementById('ageInput').value.trim()) {
        missing.push('나이');
      }
      if (!document.querySelector('.gender-btn.active')) {
        missing.push('성별');
      }
      return { valid: missing.length === 0, missing };
    }

    document.getElementById('step1ToStep2Btn').addEventListener('click', () => {
      const result = validateStep1();
      if (!result.valid) {
        showWarning('step1Warning', `${result.missing.join(', ')}을(를) 먼저 입력해주세요`);
        return;
      }
      hideWarning('step1Warning');
      showRegisterStep('step2');
    });

    document.getElementById('step2ToStep1Btn').addEventListener('click', () => {
      showRegisterStep('step1');
    });

    document.getElementById('step1ToStep0Btn').addEventListener('click', () => {
      showRegisterStep('step0');
    });

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
        <input type="text" value="${productName}" placeholder="제품명" class="flex-1 min-w-0 border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-orange-400" />
        <select class="border border-gray-200 rounded-lg px-2 py-2 text-sm text-gray-600 focus:outline-none focus:border-orange-400">${options}</select>
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
          hideWarning('step0Warning');
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

    // 등록 0단계 → 1단계 이동 조건: 화장품 1개 이상 등록
    function validateStep0() {
      const missing = [];
      if (getMyProducts().length === 0) {
        missing.push('보유 화장품');
      }
      return { valid: missing.length === 0, missing };
    }

    document.getElementById('step0ToStep1Btn').addEventListener('click', () => {
      const result = validateStep0();
      if (!result.valid) {
        showWarning('step0Warning', `${result.missing.join(', ')}을(를) 먼저 등록해주세요`);
        return;
      }
      hideWarning('step0Warning');
      showRegisterStep('step1');
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

    // 등록(온보딩) 완료 조건: 피부 고민 1개 이상, 보유 화장품 1개 이상, 여행지 선택
    function validateOnboarding() {
      const missing = [];
      if (document.querySelectorAll('.concern-chip.active').length === 0) {
        missing.push('피부 고민');
      }
      if (getMyProducts().length === 0) {
        missing.push('보유 화장품');
      }
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

    // 도시별 mock 기후 데이터 (등록 2단계 여행지 선택값과 동일한 key 사용)
    const weatherData = {
      singapore: { temp: 32, humidity: 85, uvi: 9 },
      tokyo: { temp: 29, humidity: 78, uvi: 8 },
      bangkok: { temp: 34, humidity: 78, uvi: 10 },
      dubai: { temp: 40, humidity: 25, uvi: 11 },
      paris: { temp: 22, humidity: 55, uvi: 4 },
    };
    const destinationLabels = {
      singapore: '싱가포르',
      tokyo: '일본',
      bangkok: '태국',
      dubai: '아랍에미리트',
      paris: '프랑스',
    };

    // 개인설정 탭에 등록된 내 정보를 요약해서 보여줌
    function renderProfileSummary() {
      const age = document.getElementById('ageInput').value.trim() || '-';
      const genderBtn = document.querySelector('.gender-btn.active');
      const gender = genderBtn ? genderBtn.dataset.gender : '-';
      const skinBtn = document.querySelector('.skin-btn.active');
      const skinLabel = skinBtn ? skinBtn.textContent : '-';
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

      return { adjustments, warnings };
    }

    // 조정 제안 카드 렌더링 (remove: 빨강 취소선 / modify: 주황 / add: 파랑)
    function renderAdjustedRoutine(result) {
      const actionStyle = {
        remove: { label: '빼기', badge: 'bg-red-50 text-red-600', bar: 'border-red-400', text: 'text-red-600 line-through' },
        modify: { label: '조정', badge: 'bg-orange-50 text-orange-600', bar: 'border-orange-400', text: 'text-orange-600' },
        add: { label: '추가', badge: 'bg-blue-50 text-blue-600', bar: 'border-blue-400', text: 'text-blue-600' },
      };

      const adjustmentList = document.getElementById('adjustmentList');
      adjustmentList.innerHTML = '';
      result.adjustments.forEach((item) => {
        const style = actionStyle[item.action];
        const card = document.createElement('div');
        card.className = `border-l-4 ${style.bar} bg-gray-50 rounded-r-xl p-3 flex items-start gap-3`;
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
    }

    // 등록 2단계에서 선택한 여행지를 사용중 탭의 알림/기후 안내에도 동일하게 반영
    function renderTripOverview() {
      const label = destinationLabels[currentTripDestination] || '여행지';
      document.getElementById('tripDayLabel').textContent = `DAY 2 · ${label}`;

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
        row.className = `flex items-center justify-between px-4 py-3${day.highlight ? ' bg-orange-50' : ''}`;
        row.innerHTML = `
          <div>
            <p class="text-sm font-semibold">${day.dayLabel} · ${label}${day.suffix}</p>
            <p class="text-xs ${day.highlight ? 'text-orange-500 font-semibold' : 'text-gray-400'}">${day.condition}</p>
          </div>
          <p class="text-sm text-gray-600">${day.temp}°C · 습도 ${day.humidity}%</p>
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
