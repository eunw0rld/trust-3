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
  .tab-btn {
    color: #9ca3af;
    border-bottom: 2px solid transparent;
  }
  .tab-btn.active {
    color: #111827;
    border-bottom-color: #f97316;
  }
  .tab-btn.locked {
    opacity: 0.4;
    cursor: not-allowed;
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
      <button id="skipStartBtn" type="button" class="w-full text-center text-xs text-gray-400 underline mt-4">
        둘러보기
      </button>
    </div>

  </div>

  <!-- ============ 앱 화면 ============ -->
  <div id="appContainer" class="hidden max-w-md mx-auto min-h-screen bg-white border-x border-gray-100">

    <!-- 상단 로고 -->
    <header class="px-5 pt-6 pb-4">
      <p class="text-lg font-bold tracking-tight">Skin<span class="text-orange-500">Trip</span></p>
    </header>

    <!-- 상단 탭 (등록 완료 전에는 표시하지 않음) -->
    <nav id="tabNav" class="hidden border-b border-gray-100 px-5">
      <button type="button" data-tab="register" data-label="등록" class="tab-btn active flex-1 py-3 text-sm font-semibold text-center">등록</button>
      <button type="button" data-tab="inuse" data-label="사용중" class="tab-btn flex-1 py-3 text-sm font-semibold text-center">사용중</button>
      <button type="button" data-tab="afteruse" data-label="사용후" class="tab-btn flex-1 py-3 text-sm font-semibold text-center">사용후</button>
    </nav>

    <main class="px-5">

      <!-- ============ 1. 등록 페이지 ============ -->
      <section id="screen-register" class="py-6">

        <!-- 등록 (1): 내 피부 프로필 -->
        <div id="register-step1" class="space-y-8">

          <div>
            <h2 class="text-base font-bold mb-1">내 피부 프로필</h2>
            <p class="text-sm text-gray-400 mb-4">여행 루틴을 조정할 때 기준이 되는 정보예요</p>

            <div class="grid grid-cols-2 gap-3 mb-5">
              <div>
                <p class="text-xs font-semibold text-gray-400 mb-2">나이</p>
                <input id="ageInput" type="number" min="1" max="120" placeholder="예: 27" class="w-full border border-gray-200 rounded-lg px-3 py-2 text-sm focus:outline-none focus:border-orange-400" />
              </div>
              <div>
                <p class="text-xs font-semibold text-gray-400 mb-2">성별</p>
                <div class="grid grid-cols-2 gap-2">
                  <button type="button" data-gender="여성" class="gender-btn rounded-lg py-2.5 text-sm font-semibold">여성</button>
                  <button type="button" data-gender="남성" class="gender-btn rounded-lg py-2.5 text-sm font-semibold">남성</button>
                </div>
              </div>
            </div>

            <p class="text-xs font-semibold text-gray-400 mb-2">피부 타입</p>
            <div class="grid grid-cols-4 gap-2">
              <button type="button" data-skin="oily" class="skin-btn active rounded-lg py-2.5 text-sm font-semibold">지성</button>
              <button type="button" data-skin="dry" class="skin-btn rounded-lg py-2.5 text-sm font-semibold">건성</button>
              <button type="button" data-skin="combination" class="skin-btn rounded-lg py-2.5 text-sm font-semibold">복합성</button>
              <button type="button" data-skin="sensitive" class="skin-btn rounded-lg py-2.5 text-sm font-semibold">민감성</button>
            </div>
          </div>

          <!-- 피부 고민 -->
          <div>
            <p class="text-xs font-semibold text-gray-400 mb-2">피부 고민 <span class="text-gray-300 font-normal">(중복 선택 가능)</span></p>
            <div class="flex flex-wrap gap-2">
              <button type="button" data-concern="trouble" class="concern-chip rounded-full px-3 py-1.5 text-xs font-medium">트러블</button>
              <button type="button" data-concern="dryness" class="concern-chip rounded-full px-3 py-1.5 text-xs font-medium">건조함</button>
              <button type="button" data-concern="oiliness" class="concern-chip rounded-full px-3 py-1.5 text-xs font-medium">유분과다</button>
              <button type="button" data-concern="sensitivity" class="concern-chip rounded-full px-3 py-1.5 text-xs font-medium">민감성</button>
              <button type="button" data-concern="pigmentation" class="concern-chip rounded-full px-3 py-1.5 text-xs font-medium">색소침착</button>
            </div>
          </div>

          <!-- 보유 화장품 -->
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">보유 화장품</h3>
            <div id="cosmeticRows" class="space-y-2 mb-3"></div>
            <button id="addCosmeticRowBtn" type="button" class="w-full border border-dashed border-gray-300 rounded-lg py-2.5 text-sm font-semibold text-gray-500 hover:border-orange-400 hover:text-orange-500 transition">
              + 화장품 추가
            </button>
          </div>

          <div>
            <p id="step1Warning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-lg px-3 py-2 mb-3"></p>
            <button id="toStep2Btn" type="button" class="w-full py-3.5 rounded-lg bg-orange-500 text-white text-sm font-bold">
              다음
            </button>
          </div>

        </div>

        <!-- 등록 (2): 여행지·여행 계획 입력 -->
        <div id="register-step2" class="hidden space-y-8">

          <div>
            <button id="toStep1Btn" type="button" class="text-xs text-gray-400 mb-3">← 이전</button>
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
          <p class="text-xs font-semibold text-gray-400 mb-1">DAY 2 · 도쿄</p>
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
          <div class="border border-gray-100 rounded-xl divide-y divide-gray-100">
            <div class="flex items-center justify-between px-4 py-3">
              <div>
                <p class="text-sm font-semibold">Day 1 · 도쿄</p>
                <p class="text-xs text-gray-400">맑음</p>
              </div>
              <p class="text-sm text-gray-600">28°C · 습도 65%</p>
            </div>
            <div class="flex items-center justify-between px-4 py-3 bg-orange-50">
              <div>
                <p class="text-sm font-semibold">Day 2 · 도쿄 (오늘)</p>
                <p class="text-xs text-orange-500 font-semibold">습도 상승 주의</p>
              </div>
              <p class="text-sm text-gray-600">29°C · 습도 78%</p>
            </div>
            <div class="flex items-center justify-between px-4 py-3">
              <div>
                <p class="text-sm font-semibold">Day 3 · 도쿄</p>
                <p class="text-xs text-gray-400">흐림</p>
              </div>
              <p class="text-sm text-gray-600">27°C · 습도 70%</p>
            </div>
          </div>
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

    </main>

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

    // 랜딩 페이지 → 앱 화면 전환
    function enterApp() {
      document.getElementById('screen-landing').classList.add('hidden');
      document.getElementById('appContainer').classList.remove('hidden');
    }
    document.getElementById('startBtn').addEventListener('click', enterApp);
    document.getElementById('skipStartBtn').addEventListener('click', enterApp);

    // 상단 탭 전환
    const tabButtons = document.querySelectorAll('.tab-btn');
    const screens = {
      register: document.getElementById('screen-register'),
      inuse: document.getElementById('screen-inuse'),
      afteruse: document.getElementById('screen-afteruse'),
    };
    let onboardingComplete = false;

    function switchTab(tabName) {
      tabButtons.forEach((b) => b.classList.toggle('active', b.dataset.tab === tabName));
      Object.entries(screens).forEach(([key, el]) => el.classList.toggle('hidden', key !== tabName));
      if (tabName === 'inuse') {
        refreshAdjustedRoutine();
      }
    }

    // 등록 완료 전에는 상단 탭(등록/사용중/사용후) 자체를 숨김
    function updateTabLockUI() {
      tabButtons.forEach((btn) => {
        const locked = btn.dataset.tab !== 'register' && !onboardingComplete;
        btn.classList.toggle('locked', locked);
        btn.textContent = locked ? `🔒 ${btn.dataset.label}` : btn.dataset.label;
      });
      const tabNav = document.getElementById('tabNav');
      tabNav.classList.toggle('hidden', !onboardingComplete);
      tabNav.classList.toggle('flex', onboardingComplete);
    }

    function showWarning(id, message) {
      const warning = document.getElementById(id);
      warning.textContent = message;
      warning.classList.remove('hidden');
    }

    function hideWarning(id) {
      document.getElementById(id).classList.add('hidden');
    }

    // 등록 1/2 단계 중 현재 보이는 쪽에 경고 메시지를 띄움
    function showRegisterWarning(message) {
      const step1Visible = !document.getElementById('register-step1').classList.contains('hidden');
      showWarning(step1Visible ? 'step1Warning' : 'step2Warning', message);
    }

    function showRegisterStep(stepName) {
      document.getElementById('register-step1').classList.toggle('hidden', stepName !== 'step1');
      document.getElementById('register-step2').classList.toggle('hidden', stepName !== 'step2');
    }

    tabButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        if (btn.dataset.tab !== 'register' && !onboardingComplete) {
          showRegisterWarning('등록 페이지를 먼저 완료해야 다음 단계로 넘어갈 수 있어요');
          return;
        }
        switchTab(btn.dataset.tab);
      });
    });

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

    document.getElementById('toStep2Btn').addEventListener('click', () => {
      const result = validateStep1();
      if (!result.valid) {
        showWarning('step1Warning', `${result.missing.join(', ')}을(를) 먼저 입력해주세요`);
        return;
      }
      hideWarning('step1Warning');
      showRegisterStep('step2');
    });

    document.getElementById('toStep1Btn').addEventListener('click', () => {
      showRegisterStep('step1');
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
    const mockCosmetics = [
      { name: '이니스프리 그린티 클렌징폼', category: 'cleanser' },
      { name: '라운드랩 자작나무 수분 토너', category: 'toner' },
      { name: '라네즈 워터뱅크 에멀전', category: 'emulsion' },
      { name: '닥터자르트 세라마이딘 크림', category: 'cream' },
    ];
    mockCosmetics.forEach(({ name, category }) => {
      cosmeticRows.appendChild(buildCosmeticRow(name, category));
    });

    document.getElementById('addCosmeticRowBtn').addEventListener('click', () => {
      cosmeticRows.appendChild(buildCosmeticRow('', cosmeticCategories[0].value));
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

    // 도시별 mock 기후 데이터
    const weatherData = {
      singapore: { temp: 32, humidity: 85, uvi: 9 },
      tokyo: { temp: 29, humidity: 78, uvi: 8 },
      bangkok: { temp: 34, humidity: 78, uvi: 10 },
      dubai: { temp: 40, humidity: 25, uvi: 11 },
      paris: { temp: 22, humidity: 55, uvi: 4 },
    };

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

    // 사용중 탭의 여행지 기준으로 조정 제안 계산 (등록 2단계에서 선택한 여행지로 갱신됨)
    let currentTripDestination = 'tokyo';
    function refreshAdjustedRoutine() {
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
