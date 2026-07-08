import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SkinTrip", layout="centered")

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

  <div class="max-w-md mx-auto min-h-screen bg-white border-x border-gray-100">

    <!-- 상단 로고 -->
    <header class="px-5 pt-6 pb-4">
      <p class="text-lg font-bold tracking-tight">Skin<span class="text-orange-500">Trip</span></p>
    </header>

    <!-- 상단 탭 -->
    <nav class="flex border-b border-gray-100 px-5">
      <button type="button" data-tab="register" class="tab-btn active flex-1 py-3 text-sm font-semibold text-center">등록</button>
      <button type="button" data-tab="inuse" class="tab-btn flex-1 py-3 text-sm font-semibold text-center">사용중</button>
      <button type="button" data-tab="afteruse" class="tab-btn flex-1 py-3 text-sm font-semibold text-center">사용후</button>
    </nav>

    <main class="px-5">

      <!-- ============ 1. 등록 페이지 ============ -->
      <section id="screen-register" class="py-6 space-y-8">

        <!-- 피부 타입 -->
        <div>
          <h2 class="text-base font-bold mb-1">내 피부 프로필</h2>
          <p class="text-sm text-gray-400 mb-4">여행 루틴을 조정할 때 기준이 되는 정보예요</p>
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

        <!-- 비슷한 피부타입 리뷰 -->
        <div>
          <h3 class="text-sm font-semibold text-gray-700 mb-3">나와 비슷한 피부타입 사용자 리뷰</h3>
          <div id="reviewList" class="space-y-3"></div>
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
    // 상단 탭 전환
    const tabButtons = document.querySelectorAll('.tab-btn');
    const screens = {
      register: document.getElementById('screen-register'),
      inuse: document.getElementById('screen-inuse'),
      afteruse: document.getElementById('screen-afteruse'),
    };
    tabButtons.forEach((btn) => {
      btn.addEventListener('click', () => {
        tabButtons.forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        Object.values(screens).forEach((s) => s.classList.add('hidden'));
        screens[btn.dataset.tab].classList.remove('hidden');
        if (btn.dataset.tab === 'inuse') {
          refreshAdjustedRoutine();
        }
      });
    });

    // 나와 비슷한 피부타입 사용자 리뷰 (피부타입별 mock 데이터)
    const skinReviews = {
      oily: [
        { nickname: 'jiyeon_92', rating: 5, destination: '방콕', text: '습한 나라 갈 때 로션 대신 젤 크림 쓰니까 훨씬 나았어요' },
        { nickname: 'sunny_k', rating: 4, destination: '싱가포르', text: '자외선 강한 날엔 선크림 재도포가 진짜 필수예요' },
        { nickname: 'oilyskin_life', rating: 4, destination: '두바이', text: '건조한 곳에서도 지성 피부는 가벼운 제형 유지하는 게 낫더라고요' },
      ],
      dry: [
        { nickname: 'dryday_min', rating: 5, destination: '두바이', text: '건조한 지역 갈 땐 크림 타입 모이스처라이저 꼭 챙기세요, 수분 부족 걱정 없었어요' },
        { nickname: 'hana.trip', rating: 4, destination: '파리', text: '비행기 안에서부터 미스트 자주 뿌려주니 도착해서도 당김이 덜했어요' },
      ],
      combination: [
        { nickname: 'balance_yj', rating: 5, destination: '싱가포르', text: '습도 높은 곳에서는 T존만 가볍게, 나머지는 보습 신경 쓰니 밸런스가 잘 맞았어요' },
        { nickname: 'travel_mix', rating: 4, destination: '도쿄', text: '토너 패딩만 늘렸는데도 트러블이 확실히 줄었어요' },
        { nickname: 'jeju_mix', rating: 4, destination: '파리', text: '일교차 큰 곳에서는 로션-크림 번갈아 쓰는 게 편했어요' },
      ],
      sensitive: [
        { nickname: 'calm_skin22', rating: 5, destination: '방콕', text: '자외선 지수 높은 날 무기자차로 바꾸니 트러블이 훨씬 덜했어요' },
        { nickname: 'soothing_ny', rating: 5, destination: '두바이', text: '건조한 여행 중엔 진정 팩을 매일 밤 챙겼더니 편안했어요' },
      ],
    };

    function renderStars(rating) {
      const filled = '★'.repeat(rating);
      const empty = '★'.repeat(5 - rating);
      return `<span class="text-orange-500">${filled}</span><span class="text-gray-300">${empty}</span>`;
    }

    function renderReviews(skinType) {
      const reviewList = document.getElementById('reviewList');
      reviewList.innerHTML = '';
      (skinReviews[skinType] || []).forEach((review) => {
        const card = document.createElement('div');
        card.className = 'border border-gray-100 rounded-xl p-4';
        card.innerHTML = `
          <div class="flex items-center gap-2 mb-2">
            <div class="w-8 h-8 rounded-full bg-orange-50 text-orange-600 text-xs font-bold flex items-center justify-center">${review.nickname.charAt(0).toUpperCase()}</div>
            <div class="flex-1">
              <p class="text-sm font-semibold">${review.nickname}</p>
              <span class="inline-block text-[10px] text-gray-400">${review.destination} 여행</span>
            </div>
            <p class="text-xs">${renderStars(review.rating)}</p>
          </div>
          <p class="text-sm text-gray-600 leading-relaxed">${review.text}</p>
        `;
        reviewList.appendChild(card);
      });
    }

    // 피부 타입 버튼 토글 (등록 페이지) → 선택에 따라 리뷰도 갱신
    document.querySelectorAll('.skin-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.skin-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        renderReviews(btn.dataset.skin);
      });
    });
    renderReviews('oily');

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

    // 사용중 탭의 여행지 기준으로 조정 제안 계산 (현재 목업 일정: 도쿄)
    const currentTripDestination = 'tokyo';
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


components.html(HTML_PAGE, height=900, scrolling=True)
