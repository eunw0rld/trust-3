import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="SkinTrip", layout="centered")

# 웰컴 화면에 쓰이는 로컬 이미지들을 base64 data URI로 인코딩
# (components.html은 srcdoc 기반 sandbox iframe이라 상대경로로 로컬 파일을 못 읽어옴)
_ASSET_DIR = Path(__file__).parent / "01 landing page"
_AVATAR_DIR = _ASSET_DIR / "사람 이미지_v2"


def _data_uri(path: Path, mime: str) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:{mime};base64,{encoded}"


EARTH_BG_URI = _data_uri(_ASSET_DIR / "bg.png", "image/png")
LOGO_URI = _data_uri(_ASSET_DIR / "landing_logo.png", "image/png")
AVATAR_URIS = [
    _data_uri(_AVATAR_DIR / "3.png", "image/png"),
    _data_uri(_AVATAR_DIR / "1.png", "image/png"),
    _data_uri(_AVATAR_DIR / "5.png", "image/png"),
    _data_uri(_AVATAR_DIR / "2.png", "image/png"),
    _data_uri(_AVATAR_DIR / "4.png", "image/png"),
]

# "들고 가면 좋을 제품" 추천 카드에 쓰는 실제 제품 사진 (기후별 추천화장품 DB 기준)
_CARE_DIR = Path(__file__).parent / "추천 화장품"
CARE_IMG_TORRIDEN_BALANCEFUL = _data_uri(_CARE_DIR / "토리든 패드 밸런스풀.png", "image/png")
CARE_IMG_BANILA_PRIMER = _data_uri(_CARE_DIR / "바닐라코 프라임 프라이머 피니쉬 파우더.png", "image/png")
CARE_IMG_KISSME_EYELINER = _data_uri(_CARE_DIR / "키스미 스무스 리퀴드 아이라이너.png", "image/png")
CARE_IMG_ISNTREE_SUNCREAM = _data_uri(_CARE_DIR / "이즈앤트리 히알루론산 에어리 바디 선크림.png", "image/png")
CARE_IMG_SONATURAL_FIXER = _data_uri(_CARE_DIR / "쏘내추럴 올 데이 타이트 메이크업 세팅 픽서.png", "image/png")
CARE_IMG_GOODAL_VITAC = _data_uri(_CARE_DIR / "구달 청귤 비타C 잡티케어 세럼마스크 알파.png", "image/png")
CARE_IMG_DERMATORY_AMPOULE = _data_uri(_CARE_DIR / "더마토리 프로 앰플 마스크- 미백.png", "image/png")
CARE_IMG_BIODANCE_MASK = _data_uri(_CARE_DIR / "바이오던스 리얼 딥 마스크  - 래디언트 비타 나이아신.png", "image/png")
CARE_IMG_ABIB_AQUAFIT = _data_uri(_CARE_DIR / "아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏.png", "image/png")
CARE_IMG_TORRIDEN_DIVEIN = _data_uri(_CARE_DIR / "토리든 패드 다이브인.png", "image/png")
CARE_IMG_ABIB_SERUM = _data_uri(_CARE_DIR / "아비브 히알루로닉 붐 세럼 워터드롭.png", "image/png")
CARE_IMG_TORRIDEN_LIP = _data_uri(_CARE_DIR / "토리든 솔리드인 세라마이드 립 에센스.png", "image/png")
CARE_IMG_HAIRPLUS_ESSENCE = _data_uri(_CARE_DIR / "헤어플러스 단백질본드 워터에센스.png", "image/png")
CARE_IMG_ROUNDLAB_TONIC = _data_uri(_CARE_DIR / "라운드랩 소나무 진정 시카 두피 토닉.png", "image/png")
CARE_IMG_BRINGGREEN_ALOE = _data_uri(_CARE_DIR / "브링그린 알로에 97% 수딩젤.png", "image/png")

# 내 파우치 카드/상세 모달에서 이모지 아이콘 대신 쓰는 실제 제품 사진
_POUCH_CARD_DIR = Path(__file__).parent / "파우치 속 화장품"
CARD_IMG_TONER = _data_uri(_POUCH_CARD_DIR / "넘버즈인 1번 진정 맑게담은 청초토너 토너.png", "image/png")
CARD_IMG_SERUM = _data_uri(_POUCH_CARD_DIR / "넘버즈인 1번 판토텐산 액티브업 수딩세럼.png", "image/png")
CARD_IMG_SUNCREAM = _data_uri(_POUCH_CARD_DIR / "넘버즈인 1번 청초 진정맑은 물막선크림.png", "image/png")
CARD_IMG_DRG_CREAM = _data_uri(_POUCH_CARD_DIR / "닥터지 레드 블레미쉬 클리어 수딩 크림.png", "image/png")
CARD_IMG_CUSHION = _data_uri(_POUCH_CARD_DIR / "비디비치 블랙 퍼펙션 커버 핏 쿠션.png", "image/png")
CARD_IMG_EYEPALETTE = _data_uri(_POUCH_CARD_DIR / "웨이크메이크 소프트 블러링 아이팔레트 10호 레이지 핑크 블러링.png", "image/png")
CARD_IMG_CONTOUR = _data_uri(_POUCH_CARD_DIR / "롬앤 베러 댄 컨투어 02 그레이 쿨.png", "image/png")
CARD_IMG_TINT = _data_uri(_POUCH_CARD_DIR / "롬앤 더 쥬시 래스팅 틴트 03 베어그레이프.png", "image/png")
CARD_IMG_BROW = _data_uri(_POUCH_CARD_DIR / "에스쁘아 더브로우.png", "image/png")
CARD_IMG_HIGHLIGHTER = _data_uri(_POUCH_CARD_DIR / "글린트 하이라이터 듀이 문.png", "image/png")

# 여행 아카이빙(달력 콜라주) 배경/스탬프 사진 - 개수가 많아 딕셔너리로 일괄 로딩
_ARCHIVE_DIR = Path(__file__).parent / "여행 아카이빙"
_ARCHIVE_FILES = {
    "ARCHIVE_JAN_BASE": ("jan_base.webp", "image/webp"),
    "ARCHIVE_JAN_SUN": ("jan_sun.webp", "image/webp"),
    "ARCHIVE_JAN_STREET": ("jan_street.webp", "image/webp"),
    "ARCHIVE_JAN_MAP": ("jan_map.webp", "image/webp"),
    "ARCHIVE_JAN_SELFIE": ("jan_selfie.webp", "image/webp"),
    "ARCHIVE_JAN_IZAKAYA": ("jan_izakaya.webp", "image/webp"),
    "ARCHIVE_JAN_PLATE": ("jan_plate.webp", "image/webp"),
    "ARCHIVE_JAN_FLAG": ("jan_flag.webp", "image/webp"),
    "ARCHIVE_JAN_PLAYER": ("jan_player.webp", "image/webp"),
    "ARCHIVE_FEB_BASE": ("feb_base.webp", "image/webp"),
    "ARCHIVE_FEB_CUSHION": ("feb_cushion.webp", "image/webp"),
    "ARCHIVE_FEB_CAFE": ("feb_cafe.webp", "image/webp"),
    "ARCHIVE_FEB_MAP": ("feb_map.webp", "image/webp"),
    "ARCHIVE_FEB_SELFIE": ("feb_selfie.webp", "image/webp"),
    "ARCHIVE_FEB_EIFFEL": ("feb_eiffel.webp", "image/webp"),
    "ARCHIVE_FEB_PLATE": ("feb_plate.webp", "image/webp"),
    "ARCHIVE_FEB_FLAG": ("feb_flag.webp", "image/webp"),
    "ARCHIVE_FEB_PLAYER": ("feb_player.webp", "image/webp"),
    "ARCHIVE_MAR_BASE": ("mar_base.webp", "image/webp"),
    "ARCHIVE_MAR_CREAM": ("mar_cream.webp", "image/webp"),
    "ARCHIVE_MAR_SIGN": ("mar_sign.webp", "image/webp"),
    "ARCHIVE_MAR_MAP": ("mar_map.webp", "image/webp"),
    "ARCHIVE_MAR_SELFIE": ("mar_selfie.webp", "image/webp"),
    "ARCHIVE_MAR_GROUP": ("mar_group.webp", "image/webp"),
    "ARCHIVE_MAR_PLATE": ("mar_plate.webp", "image/webp"),
    "ARCHIVE_MAR_FLAG": ("mar_flag.webp", "image/webp"),
    "ARCHIVE_MAR_PLAYER": ("mar_player.webp", "image/webp"),
    "ARCHIVE_APR_BASE": ("apr_base.webp", "image/webp"),
    "ARCHIVE_APR_COLLAGEN": ("apr_collagen.webp", "image/webp"),
    "ARCHIVE_APR_MEETING": ("apr_meeting.webp", "image/webp"),
    "ARCHIVE_APR_MAP": ("apr_map.webp", "image/webp"),
    "ARCHIVE_APR_SELFIE": ("apr_selfie.webp", "image/webp"),
    "ARCHIVE_APR_BEER": ("apr_beer.webp", "image/webp"),
    "ARCHIVE_APR_PLATE": ("apr_plate.webp", "image/webp"),
    "ARCHIVE_APR_FLAG": ("apr_flag.webp", "image/webp"),
    "ARCHIVE_APR_PLAYER": ("apr_player.webp", "image/webp"),
    "ARCHIVE_JUN_BASE": ("jun_base.webp", "image/webp"),
    "ARCHIVE_JUN_CLEANSER": ("jun_cleanser.webp", "image/webp"),
    "ARCHIVE_JUN_SELFIE": ("jun_selfie.webp", "image/webp"),
    "ARCHIVE_JUN_MEETING": ("jun_meeting.webp", "image/webp"),
    "ARCHIVE_JUN_MAP": ("jun_map.webp", "image/webp"),
    "ARCHIVE_JUN_PLATE": ("jun_plate.webp", "image/webp"),
    "ARCHIVE_JUN_FLAG": ("jun_flag.webp", "image/webp"),
    "ARCHIVE_JUN_SUNSET": ("jun_sunset.webp", "image/webp"),
    "ARCHIVE_JUN_PLAYER": ("jun_player.webp", "image/webp"),
    "ARCHIVE_MAY_BASE": ("may_base.webp", "image/webp"),
    "ARCHIVE_MAY_MEETING1": ("may_meeting1.webp", "image/webp"),
    "ARCHIVE_MAY_SERUM": ("may_serum.webp", "image/webp"),
    "ARCHIVE_MAY_MAP1": ("may_map1.webp", "image/webp"),
    "ARCHIVE_MAY_PLATE1": ("may_plate1.webp", "image/webp"),
    "ARCHIVE_MAY_THMAP": ("may_thmap.webp", "image/webp"),
    "ARCHIVE_MAY_SELFIE": ("may_selfie.webp", "image/webp"),
    "ARCHIVE_MAY_GOAT": ("may_goat.webp", "image/webp"),
    "ARCHIVE_MAY_MEETING2": ("may_meeting2.webp", "image/webp"),
    "ARCHIVE_MAY_PLATE2": ("may_plate2.webp", "image/webp"),
    "ARCHIVE_MAY_AUMAP": ("may_aumap.webp", "image/webp"),
    "ARCHIVE_MAY_MAP2": ("may_map2.webp", "image/webp"),
    "ARCHIVE_MAY_PLAYER": ("may_player.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_BASE": ("maystack_base.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_PERFUME": ("maystack_perfume.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_MEETING": ("maystack_meeting.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_MAP": ("maystack_map.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_SELFIE": ("maystack_selfie.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_DINNER": ("maystack_dinner.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_PLATE": ("maystack_plate.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_COLISEUM": ("maystack_coliseum.webp", "image/webp"),
    "ARCHIVE_MAYSTACK_PLAYER": ("maystack_player.webp", "image/webp"),
}
ARCHIVE_URIS = {name: _data_uri(_ARCHIVE_DIR / fname, mime) for name, (fname, mime) in _ARCHIVE_FILES.items()}

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
<script>
  window.onerror = function (msg, url, line, col, err) {
    window.__lastError = { msg: msg, url: url, line: line, col: col };
    console.error('__DIAG__', JSON.stringify(window.__lastError));
  };
</script>
<script src="https://cdn.tailwindcss.com"></script>
<link href="https://unpkg.com/maplibre-gl@5.24.0/dist/maplibre-gl.css" rel="stylesheet" />
<script src="https://unpkg.com/maplibre-gl@5.24.0/dist/maplibre-gl.js"></script>
<!-- 파우치 화장품 사진 인식용 물체 감지 모델 (실제 제품명 판별은 안 하고, 사진 속 물체 위치만 감지) -->
<script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs"></script>
<script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd"></script>
<!-- 국기 이모지가 OS/브라우저에 따라 알파벳 코드로만 보이는 문제(특히 Windows) 방지용:
     이모지를 일관된 국기 그림(svg)으로 렌더링해주는 twemoji -->
<script src="https://cdn.jsdelivr.net/npm/twemoji@14.0.2/dist/twemoji.min.js" crossorigin="anonymous"></script>
<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          sans: ['"Pretendard"', '"Apple SD Gothic Neo"', '"Malgun Gothic"', 'sans-serif'],
        },
        colors: {
          // 포인트 레드 체계 (구 파스텔 블루→퍼플 brand 팔레트를 대체)
          brand: {
            50: '#FDE7EA',
            100: '#FAC7CE',
            400: '#F14F62',
            500: '#EB0029',
            600: '#B4001F',
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

    /* [베이스] 배경은 밝은 화이트, 카드 층 구분용 연회색 */
    --bg-base: #ffffff;
    --bg-surface: #f4f4f6;

    /* [포인트 레드] 검색/저장/확인 등 핵심 액션 CTA 버튼에만 사용 (tailwind brand-500과 동일) */
    --accent-red: #eb0029;

    /* [그라데이션] 강조 카드용 4-stop 그라데이션 */
    --accent-gradient: linear-gradient(135deg, #6cacdf 0%, #d1e6f5 50%, #d6dadf 59%, #f2a074 100%);
  }
  body {
    background: var(--bg-base);
  }
  /* ===== 새 디자인 시스템: 공통 pill/카드/버튼/타이포 토큰 (개별 화면 적용은 이후 별도 작업) ===== */
  /* [타이포] 핵심 정보(제목/큰 숫자/코드)는 크고 굵게 검정, 보조 텍스트는 작은 회색 */
  .text-display {
    font-weight: 800;
    color: #111111;
  }
  .text-heading {
    font-weight: 700;
    color: #111111;
  }
  .text-secondary {
    font-size: 12px;
    color: #888888;
  }
  /* [pill] 선택 가능한 알약형 토글 - 기본은 흰 배경 + 얇은 회색 테두리, 활성 시 검정 반전 */
  .pill {
    display: inline-flex;
    align-items: center;
    border-radius: 999px;
    background: #ffffff;
    border: 1px solid #e5e5e5;
    color: #111111;
  }
  .pill-active {
    background: #111111;
    color: #ffffff;
    border-color: #111111;
  }
  /* [버튼] 검색/저장/확인 등 핵심 액션 전용 - 포인트 레드 */
  .btn-primary {
    background: var(--accent-red);
    color: #ffffff;
    border-radius: 16px;
    font-weight: 700;
  }
  /* [카드] 흰 배경 + 아주 얕은 그림자로만 층을 구분 */
  .card {
    background: #ffffff;
    border-radius: 20px;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.06);
  }
  .card-gradient {
    background: var(--accent-gradient);
    border-radius: 20px;
  }
  /* [여백] 카드를 세로로 쌓을 때 넉넉한 간격을 주는 공용 래퍼 */
  .card-stack {
    display: flex;
    flex-direction: column;
    gap: 20px;
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
    background: var(--accent-red);
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
    border-color: var(--accent-red);
    background: #fde7ea;
    color: #b4001f;
  }
  .wizard-progress-track {
    height: 4px;
    background: #e5e7eb;
    border-radius: 9999px;
    overflow: hidden;
  }
  .wizard-progress-fill {
    height: 100%;
    background: var(--accent-red);
    border-radius: 9999px;
    transition: width 0.25s ease;
  }
  .wizard-cta-btn {
    height: 54px;
    border-radius: 16px;
    background: var(--accent-red);
    color: #ffffff;
    font-weight: 600;
    font-size: 15px;
    transition: background 0.15s ease;
  }
  .wizard-cta-btn:disabled {
    background: #d1d5db;
  }
  /* 내 파우치 "+ 추가" 1단계: 사진/직접입력 선택 카드 - 사진 쪽을 더 크고 진하게 강조 */
  .pouch-add-choice-btn {
    width: 100%;
    display: flex;
    align-items: center;
    gap: 12px;
    border-radius: 16px;
    border: 1px solid #e5e7eb;
    background: #ffffff;
    text-align: left;
  }
  .pouch-add-choice-btn.primary {
    padding: 20px 18px;
    border-color: var(--accent-red);
    background: #fde7ea;
  }
  .pouch-add-choice-btn.secondary {
    padding: 12px 18px;
  }
  .pouch-add-choice-title {
    font-size: 15px;
    font-weight: 700;
    color: #111827;
  }
  .pouch-add-choice-btn.secondary .pouch-add-choice-title {
    font-size: 13px;
    font-weight: 600;
    color: #6b7280;
  }
  .pouch-add-choice-desc {
    font-size: 11px;
    color: #9ca3af;
    margin-top: 1px;
  }
  /* 등록된 나라 칩 리스트: 가로 스크롤, 스크롤바는 숨김 */
  #tripCountryChipsRow {
    scrollbar-width: none;
  }
  #tripCountryChipsRow::-webkit-scrollbar {
    display: none;
  }
  .trip-country-chip {
    transition: box-shadow 0.15s ease, transform 0.1s ease;
  }
  .trip-country-chip.active {
    box-shadow: 0 0 0 1.5px currentColor inset;
  }
  /* 여행 계획 수정 모달: 구간이 많아지거나 날짜 선택 트리거가 늘어나 내용이 길어질 수 있어
     내부만 스크롤되게 하고, 저장 버튼은 모달 하단에 고정 */
  #tripSegmentsModal {
    max-height: calc(var(--app-height) - 96px);
    overflow-y: auto;
    -webkit-overflow-scrolling: touch;
  }
  #tripSegmentsModal #tripSegmentsSaveBtn {
    position: sticky;
    bottom: 0;
    margin-top: 12px;
  }
  #tripSegmentsSaveBtn:disabled {
    background: #d1d5db;
  }
  /* 여행 날짜 선택(달력) 팝업 */
  .trip-date-cell {
    position: relative;
    display: flex;
    align-items: center;
    justify-content: center;
    height: 36px;
    font-size: 13px;
    font-weight: 600;
    color: #374151;
  }
  .trip-date-cell.muted {
    color: #d1d5db;
    font-weight: 400;
  }
  .trip-date-cell .trip-date-cell-inner {
    position: relative;
    z-index: 1;
    display: flex;
    align-items: center;
    justify-content: center;
    width: 30px;
    height: 30px;
    border-radius: 9999px;
  }
  .trip-date-cell.in-range::before {
    content: '';
    position: absolute;
    inset: 3px 0;
    background: var(--range-bg, #fdf0f8);
  }
  .trip-date-cell.range-start::before {
    left: 50%;
  }
  .trip-date-cell.range-end::before {
    right: 50%;
  }
  .trip-date-cell.range-start.range-end::before {
    display: none;
  }
  #tripDateRangeConfirmBtn:disabled {
    background: #d1d5db;
  }
  /* ===== 여행 기록 아카이빙: 도장(stamp) 애니메이션 (03 calendar_archive_pkg 통합) ===== */
  .archive-modal {
    animation: archiveModalFade 0.25s ease;
  }
  @keyframes archiveModalFade {
    from { opacity: 0; }
    to { opacity: 1; }
  }
  /* 각 오마주 요소가 "탁" 하고 도장처럼 찍히는 효과: 크게 나타나 살짝 회전하며 안착 */
  .stamp-el {
    opacity: 0;
    transform: scale(1.6) rotate(var(--stamp-rot, -6deg));
    transform-origin: center;
  }
  .stamp-el.stamped {
    animation: stampIn 0.45s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  }
  /* 콜라주 사진: 탭 가능함을 보여주는 커서 + 살짝 눌리는 피드백(밝기로만, transform은
     스탬프 등장 애니메이션이 이미 점유하고 있어 건드리지 않음) */
  .archive-tappable {
    cursor: pointer;
    transition: filter 0.12s ease;
  }
  .archive-tappable.tap-flash {
    filter: brightness(0.85) !important;
  }
  /* 음악 플레이어 스탬프를 탭하면 "재생 중" 느낌으로 은은하게 펄스 */
  .archive-tappable[data-stamp-name="player"].is-playing {
    animation: archivePlayerPulse 1.6s ease-in-out infinite;
  }
  @keyframes archivePlayerPulse {
    0%, 100% { filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.45)) brightness(1); }
    50% { filter: drop-shadow(0 4px 14px rgba(235, 0, 41, 0.55)) brightness(1.05); }
  }
  @keyframes stampIn {
    0%   { opacity: 0; transform: scale(1.6) rotate(var(--stamp-rot, -6deg)); }
    60%  { opacity: 1; transform: scale(0.92) rotate(calc(var(--stamp-rot, -6deg) * 0.4)); }
    100% { opacity: 1; transform: scale(1) rotate(var(--stamp-tilt, 0deg)); }
  }
  /* 도장이 찍힐 때 잠깐 번지는 잉크 링 효과 */
  .stamp-el.stamped::after {
    content: '';
    position: absolute;
    inset: -6px;
    border-radius: 14px;
    border: 2px solid rgba(49, 130, 246, 0.45);
    opacity: 0;
    animation: stampRing 0.5s ease forwards;
    pointer-events: none;
  }
  @keyframes stampRing {
    0%   { opacity: 0.7; transform: scale(0.85); }
    100% { opacity: 0; transform: scale(1.15); }
  }
  /* 국기 이모지 흔들림 */
  .flag-wave {
    display: inline-block;
    transform-origin: 0% 60%;
    animation: flagWave 1.4s ease-in-out infinite;
  }
  @keyframes flagWave {
    0%   { transform: rotate(0deg)   skewX(0deg); }
    25%  { transform: rotate(-9deg)  skewX(6deg); }
    50%  { transform: rotate(0deg)   skewX(0deg); }
    75%  { transform: rotate(9deg)   skewX(-6deg); }
    100% { transform: rotate(0deg)   skewX(0deg); }
  }
  .archive-day-cell {
    position: relative;
    font-size: 13px;
    font-weight: 600;
    color: #1f2937;
    text-align: left;
    padding: 6px 8px;
  }
  .archive-day-cell.faded { color: #d1d5db; }
  /* 12~15일 하이라이트: 핵심 구간 표시 */
  .archive-day-cell.key-day {
    color: #1B64DA;
    font-weight: 800;
  }
  .archive-day-dot {
    display: block;
    width: 6px;
    height: 6px;
    border-radius: 9999px;
    margin-top: 3px;
    background: #3182F6;
  }
  .archive-day-dot.muted { background: #d1d5db; }
  .archive-history-card {
    transition: transform 0.12s ease, box-shadow 0.15s ease;
  }
  .archive-history-card:active {
    transform: scale(0.97);
  }
  /* twemoji가 국기 이모지를 <img>로 치환한 결과물 - 주변 텍스트/폰트 크기에 맞춰 보이도록
     (twemoji 공식 권장 스타일) */
  img.emoji {
    height: 1em;
    width: 1em;
    margin: 0 0.02em 0 0.02em;
    vertical-align: -0.1em;
  }
  /* 커뮤니티 화면: [리뷰] / [나라별 인기템] 서브탭 */
  .community-subtab-btn {
    color: #6b7280;
    transition: background 0.15s ease, color 0.15s ease;
  }
  .community-subtab-btn.active {
    background: #ffffff;
    color: var(--accent-red);
    box-shadow: 0 1px 2px rgba(0, 0, 0, 0.08);
  }
  /* 국가 선택 바: 스크롤해도 항상 최상단에 고정되어 어떤 나라를 보고 있는지 인지되게 함 */
  .community-country-bar {
    position: sticky;
    top: 0;
    z-index: 10;
    background: #f9fafb;
  }
  .popular-item-card.rank-1 {
    border-color: var(--accent-red);
    box-shadow: 0 0 0 1px rgba(235, 0, 41, 0.12);
  }
  @keyframes popularItemHighlight {
    0%, 100% { box-shadow: 0 0 0 0 rgba(235, 0, 41, 0); }
    30% { box-shadow: 0 0 0 4px rgba(235, 0, 41, 0.35); }
  }
  .popular-item-flash {
    animation: popularItemHighlight 1.2s ease;
  }
  .skin-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .skin-btn.active {
    border-color: var(--accent-red);
    background: #fde7ea;
    color: #b4001f;
  }
  .gender-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .gender-btn.active {
    border-color: var(--accent-red);
    background: #fde7ea;
    color: #b4001f;
  }
  .tone-btn {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .tone-btn.active {
    border-color: var(--accent-red);
    background: #fde7ea;
    color: #b4001f;
  }
  .concern-chip {
    border: 1px solid #e5e7eb;
    color: #6b7280;
    background: #ffffff;
  }
  .concern-chip.active {
    border-color: var(--accent-red);
    background: #fde7ea;
    color: #b4001f;
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
    z-index: 2;
    width: 46px;
    animation: landingFloat 3.2s ease-in-out infinite;
    filter: drop-shadow(0 4px 10px rgba(0, 0, 0, 0.35));
  }
  .landing-bubble img {
    display: block;
    width: 100%;
    height: auto;
  }
  @keyframes landingFloat {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-7px); }
  }
  /* 웰컴 화면: 지구.jpg 자체에 검은 우주 배경이 포함돼 있어서, 원형으로 잘라 쓰는 대신
     화면 전체 배경으로 깔고 background-position/size로 지구 위치·크기를 맞춤
     (실제 배경 설정은 #screen-welcome 인라인 스타일에 있음) */
  .welcome-logo-icon {
    height: 52px;
    width: auto;
    display: block;
    filter: drop-shadow(0 1px 6px rgba(255, 255, 255, 0.35));
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
    padding: 11px 0;
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
  /* 매장 찾기 지도: 기본 파란 핀 대신 보라색 원형 커스텀 마커 */
  .store-marker {
    width: 22px;
    height: 22px;
    border-radius: 9999px;
    background: var(--accent-red);
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
    border-top-color: var(--accent-red);
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
    background: #fde7ea;
    color: #b4001f;
    font-size: 12px;
    font-weight: 600;
    border: 1px solid #fac7ce;
  }
  /* 리스트 아이템이 지도로 flyTo되는 동안 살짝 강조 */
  .map-store-list-item.active-store-item {
    background-color: #fde7ea;
    border-color: #f5919e;
  }

  /* 피부 변화 리포트: 두 사진이 모두 등록된 직후 재생되는 "스캔 중" 연출.
     얼굴 위에 랜드마크 노드 + 삼각망을 순차적으로 점등시키는 페이스 스캔 애니메이션.
     opacity/transform만 애니메이션해 레이아웃 리플로우 없이 60fps에 가깝게 동작함 */
  .skin-scan-overlay {
    background: transparent; /* 사진이 그대로 비치도록 어둡게 덮지 않음 */
  }
  .skin-scan-mesh-mount,
  .skin-scan-mesh-svg {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
  }
  .skin-scan-mesh-svg {
    animation: skinMeshFlash var(--mesh-cycle, 2400ms) ease-in-out infinite;
  }
  .skin-scan-node {
    fill: #22d3ee;
    filter: drop-shadow(0 0 3px rgba(34, 211, 238, 0.95));
    opacity: 0;
    transform-box: fill-box;
    transform-origin: center;
    animation-name: skinMeshNodeAppear;
    animation-duration: var(--mesh-cycle, 2400ms);
    animation-timing-function: ease-out;
    animation-iteration-count: infinite;
  }
  .skin-scan-ring {
    fill: none;
    stroke: #67e8f9;
    stroke-width: 1;
    opacity: 0;
    transform-box: fill-box;
    transform-origin: center;
    animation-name: skinMeshRingPulse;
    animation-duration: var(--mesh-cycle, 2400ms);
    animation-timing-function: ease-out;
    animation-iteration-count: infinite;
  }
  .skin-scan-edge {
    stroke: #67e8f9;
    stroke-width: 0.6;
    opacity: 0;
    animation-name: skinMeshEdgeAppear;
    animation-duration: var(--mesh-cycle, 2400ms);
    animation-timing-function: ease-out;
    animation-iteration-count: infinite;
  }
  @keyframes skinMeshNodeAppear {
    0% { opacity: 0; transform: scale(0.3); }
    6% { opacity: 1; transform: scale(1.35); }
    12% { transform: scale(1); }
    88% { opacity: 1; }
    96%, 100% { opacity: 0; }
  }
  @keyframes skinMeshRingPulse {
    0% { opacity: 0; transform: scale(0.5); }
    8% { opacity: 0.9; transform: scale(0.7); }
    35% { opacity: 0; transform: scale(2.4); }
    100% { opacity: 0; }
  }
  @keyframes skinMeshEdgeAppear {
    0% { opacity: 0; }
    8% { opacity: 0.85; }
    90% { opacity: 0.85; }
    97%, 100% { opacity: 0; }
  }
  @keyframes skinMeshFlash {
    0%, 78% { filter: brightness(1); }
    87% { filter: brightness(1.9) drop-shadow(0 0 8px rgba(34, 211, 238, 0.9)); }
    97%, 100% { filter: brightness(1); }
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
    background: linear-gradient(90deg, #f14f62, #eb0029);
    border-radius: 9999px;
    transform-origin: left;
    animation: skinScanProgress var(--scan-duration, 3s) linear forwards;
  }
  @keyframes skinScanProgress {
    from { transform: scaleX(0); }
    to { transform: scaleX(1); }
  }
  /* ===== 파우치 화장품 사진 인식: 전체화면 물체 감지 스캔 연출 ===== */
  .cosmetic-scan-box {
    position: absolute;
    border: 2px solid var(--accent-red);
    border-radius: 10px;
    overflow: hidden;
    opacity: 0;
    box-shadow: 0 0 12px 1px rgba(235, 0, 41, 0.5);
    animation: cosmeticScanBoxIn 0.35s ease forwards;
  }
  @keyframes cosmeticScanBoxIn {
    from { opacity: 0; transform: scale(0.92); }
    to { opacity: 1; transform: scale(1); }
  }
  .cosmetic-scan-box-line {
    position: absolute;
    left: 0;
    right: 0;
    top: -30%;
    height: 30%;
    background: linear-gradient(180deg, rgba(235, 0, 41, 0) 0%, rgba(235, 0, 41, 0.75) 50%, rgba(235, 0, 41, 0) 100%);
    filter: blur(2px);
    box-shadow: 0 0 14px 3px rgba(235, 0, 41, 0.6);
    animation: cosmeticScanLineMove 1.4s ease-in-out infinite;
  }
  @keyframes cosmeticScanLineMove {
    0% { top: -30%; }
    100% { top: 100%; }
  }
  /* 분석 연출 페이지: 1일차 사진 → 마지막날 사진 크로스페이드 오버레이 (opacity만 애니메이션) */
  .skin-scan-fade {
    opacity: 0;
    transition: opacity 700ms ease;
  }
  .skin-scan-fade.skin-scan-fade-in {
    opacity: 1;
  }
  /* 스캔 중: 마지막날 사진을 반투명하게 오가게(왕복) 해서 1일차 사진과 겹쳐 비쳐 보이게 함.
     min/max 투명도(0.45~0.65)와 왕복 여부는 초기값 — 필요시 숫자만 조정 */
  .skin-scan-fade.skin-scan-overlay-active {
    animation: skinScanOverlayPulse 1.6s ease-in-out infinite;
  }
  @keyframes skinScanOverlayPulse {
    0%, 100% { opacity: 0.45; }
    50% { opacity: 0.65; }
  }
  /* 스캔이 끝나갈 무렵 다시 또렷하게(불투명) 정리 */
  .skin-scan-fade.skin-scan-settle {
    animation: none;
    opacity: 1;
  }

  /* ===== 정교한 얼굴 스캔 모션: 격자 + 스캔 라인(잔상) + 코너 프레임 =====
     모두 skinScanMeshOverlay 안에서 같이 켜지고 꺼짐(기존 mesh 노드/삼각망과 레이어로 겹침) */

  /* 은은한 스캔 격자: 영역별로 훑는 느낌만 주는 용도라 아주 옅게(opacity) 처리 */
  .skin-scan-grid {
    position: absolute;
    inset: 0;
    background-image:
      repeating-linear-gradient(0deg, rgba(103, 232, 249, 0.5) 0, rgba(103, 232, 249, 0.5) 1px, transparent 1px, transparent 12.5%),
      repeating-linear-gradient(90deg, rgba(103, 232, 249, 0.5) 0, rgba(103, 232, 249, 0.5) 1px, transparent 1px, transparent 12.5%);
    opacity: 0.18;
    animation: skinScanGridPulse 2.4s ease-in-out infinite;
  }
  @keyframes skinScanGridPulse {
    0%, 100% { opacity: 0.12; }
    50% { opacity: 0.26; }
  }

  /* 가로 스캔 라인: brand(보라) 글로우, 위→아래→위로 왕복. 뒤에 옅고 흐릿한 잔상 한 겹을 살짝
     지연시켜 겹쳐두면 "trail" 느낌이 남 (트레일 전용 레이어: .skin-scan-sweep-trail) */
  .skin-scan-sweep,
  .skin-scan-sweep-trail {
    position: absolute;
    left: 0;
    right: 0;
    top: -22%;
    height: 22%;
    background: linear-gradient(180deg, rgba(235, 0, 41, 0) 0%, rgba(235, 0, 41, 0.7) 50%, rgba(235, 0, 41, 0) 100%);
    animation: skinScanSweepMove 2.2s ease-in-out infinite;
  }
  .skin-scan-sweep {
    filter: blur(1.5px);
    box-shadow: 0 0 14px 4px rgba(235, 0, 41, 0.55);
  }
  .skin-scan-sweep-trail {
    filter: blur(6px);
    opacity: 0.5;
    animation-delay: 160ms; /* 본 라인보다 살짝 늦게 따라와 잔상처럼 보임 */
  }
  @keyframes skinScanSweepMove {
    0% { top: -22%; }
    50% { top: 100%; }
    100% { top: -22%; }
  }

  /* 카메라 초점 코너 마커: 4모서리에 ㄱ자 브래킷을 둬 "스캐닝 중" 인상을 강화 */
  .skin-scan-corner {
    position: absolute;
    width: 18px;
    height: 18px;
    border: 2px solid #67e8f9;
    opacity: 0.85;
  }
  .skin-scan-corner-tl { top: 8px; left: 8px; border-right: none; border-bottom: none; }
  .skin-scan-corner-tr { top: 8px; right: 8px; border-left: none; border-bottom: none; }
  .skin-scan-corner-bl { bottom: 8px; left: 8px; border-right: none; border-top: none; }
  .skin-scan-corner-br { bottom: 8px; right: 8px; border-left: none; border-top: none; }
  /* 스캔 연출이 끝나고 결과 카드가 나타날 때 부드럽게 페이드인 */
  @keyframes skinFadeIn {
    from { opacity: 0; transform: translateY(4px); }
    to { opacity: 1; transform: translateY(0); }
  }
  .skin-fade-in {
    animation: skinFadeIn 0.4s ease-out;
  }
  /* "내 파우치" 등록 완료 후 뜨는 바구니 애니메이션 페이지 */
  .pouch-basket-stage {
    position: relative;
    width: 345px;
    aspect-ratio: 1122 / 1402;
    margin: 0 auto;
  }
  /* 유리 선반 사진(02 pouch/glass bg.png)을 배경으로 사용. 스테이지 종횡비를
     이미지 원본 비율과 동일하게 맞춰서 cover/contain 어느 쪽이든 잘리거나
     여백 없이 선반이 그대로 보이게 함 */
  .pouch-basket {
    position: absolute;
    inset: 0;
    opacity: 0;
    transform: scale(0.92);
    animation: pouchBasketFadeIn 0.4s ease-out 0.05s forwards;
    background-color: #eef4f3;
    background-image: none;
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  /* 파우치 격자무늬 채도가 너무 높아 제품과 함께 시끄러워 보이는 것을 완화하는 옅은 흰색 오버레이 */
  .pouch-basket::after {
    display: none;
  }
  /* 유리 선반 사진은 선반이 2단으로 고정돼 있어 3단으로 늘릴 수 없어서,
     사진 대신 CSS로 3단 유리 선반을 다시 그림 (제품도 훨씬 크게) */
  .pouch-basket-stage {
    height: 460px !important;
  }
  .pouch-basket {
    background-image: none !important;
    background: linear-gradient(180deg, #eef5f4 0%, #e2eeec 100%) !important;
  }
  .pouch-glass-shelf-line {
    position: absolute;
    left: 6%;
    right: 6%;
    height: 3px;
    border-radius: 2px;
    background: linear-gradient(90deg, rgba(150, 214, 208, 0.1), rgba(122, 199, 192, 0.65) 12%, rgba(122, 199, 192, 0.65) 88%, rgba(150, 214, 208, 0.1));
    box-shadow: 0 3px 6px rgba(96, 168, 162, 0.28), 0 -1px 1px rgba(255, 255, 255, 0.7);
  }
  .pouch-basket-items {
    position: absolute;
    inset: 0;
    z-index: 2;
  }
  .pouch-item {
    position: absolute;
    opacity: 0;
    transform: translate(var(--from-x, 0px), var(--from-y, -240px)) rotate(var(--from-rot, -30deg)) scale(0.85);
    animation: pouchItemFlyIn 0.65s cubic-bezier(0.2, 0.8, 0.25, 1) forwards;
    animation-delay: var(--delay, 0s);
    filter: drop-shadow(0 6px 8px rgba(0, 0, 0, 0.18));
  }
  @keyframes pouchItemFlyIn {
    0% { opacity: 0; transform: translate(var(--from-x, 0px), var(--from-y, -240px)) rotate(var(--from-rot, -30deg)) scale(0.8); }
    70% { opacity: 1; transform: translate(0, 0) rotate(calc(var(--rot, 0deg) + 4deg)) scale(1.05); }
    100% { opacity: 1; transform: translate(0, 0) rotate(var(--rot, 0deg)) scale(1); }
  }
  .pouch-item-label {
    position: absolute;
    left: 50%;
    bottom: -14px;
    transform: translateX(-50%);
    font-size: 7px;
    font-weight: 700;
    text-align: center;
    white-space: nowrap;
    color: rgba(0, 0, 0, 0.55);
  }
  @keyframes pouchBasketFadeIn {
    to { opacity: 1; transform: scale(1); }
  }
  /* 완료 화면: 체크 아이콘이 팝(scale 0→1 바운스)으로 등장 */
  .pouch-complete-check-mini {
    width: 20px;
    height: 20px;
    border-radius: 9999px;
    background: linear-gradient(135deg, #f14f62 0%, #eb0029 100%);
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
    transform: scale(0);
    animation: pouchCheckPop 0.45s cubic-bezier(0.34, 1.56, 0.64, 1) forwards;
  }
  @keyframes pouchCheckPop {
    0% { transform: scale(0); }
    60% { transform: scale(1.15); }
    100% { transform: scale(1); }
  }
  /* 제품을 탭하면 이름을 보여주는 말풍선 (긴 목록 대신 필요할 때만 확인) */
  .pouch-item {
    cursor: pointer;
  }
  .pouch-item:active {
    filter: brightness(0.96) drop-shadow(0 6px 8px rgba(0, 0, 0, 0.18));
  }
  /* 제품이 유리 선반 위에 서 있는 느낌을 주는 아주 옅은 접지 그림자 */
  .pouch-item::after {
    content: '';
    position: absolute;
    left: 50%;
    bottom: -3px;
    transform: translateX(-50%);
    width: 65%;
    height: 5px;
    background: rgba(15, 23, 42, 0.14);
    filter: blur(2.5px);
    border-radius: 50%;
    pointer-events: none;
  }
  .pouch-item-tooltip {
    position: absolute;
    z-index: 5;
    max-width: 160px;
    background: rgba(31, 41, 55, 0.92);
    color: #fff;
    font-size: 11px;
    font-weight: 600;
    line-height: 1.35;
    text-align: center;
    padding: 6px 10px;
    border-radius: 10px;
    white-space: normal;
    opacity: 0;
    transform: translate(-50%, 4px) scale(0.95);
    transition: opacity 0.15s ease-out, transform 0.15s ease-out;
    pointer-events: none;
  }
  .pouch-item-tooltip.visible {
    opacity: 1;
    transform: translate(-50%, 0) scale(1);
  }
  /* 선반 위 제품 좌측 상단 번호 배지 - 위 선반 왼쪽부터 1,2,3... 순서로,
     하단 리스트의 같은 번호 배지와 1:1로 대응됨 */
  .pouch-item-badge {
    position: absolute;
    top: -6px;
    left: -6px;
    width: 20px;
    height: 20px;
    border-radius: 9999px;
    background: var(--accent-red);
    color: #fff;
    font-size: 10px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.25);
    z-index: 3;
  }
  .pouch-chip-badge {
    width: 22px;
    height: 22px;
    border-radius: 9999px;
    background: var(--accent-red);
    color: #fff;
    font-size: 11px;
    font-weight: 800;
    display: flex;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
  }
  /* 하단 제품 리스트 */
  .pouch-chip {
    position: relative;
    display: flex;
    align-items: center;
    gap: 8px;
    width: 100%;
    background: #ffffff;
    border: 1px solid #f3f4f6;
    border-radius: 16px;
    box-shadow: 0 1px 3px rgba(0, 0, 0, 0.06);
    padding: 10px 12px;
    font-size: 13px;
    font-weight: 600;
    color: #1f2937;
    opacity: 0;
    transform: translateY(6px);
    animation: pouchChipFadeIn 0.3s ease-out forwards;
    animation-delay: var(--chip-delay, 0s);
  }
  .pouch-chip::before {
    content: '';
    position: absolute;
    inset: 0;
    background: linear-gradient(180deg, rgba(255, 255, 255, 0.5) 0%, rgba(255, 255, 255, 0) 50%);
    pointer-events: none;
  }
  @keyframes pouchChipFadeIn {
    to { opacity: 1; transform: translateY(0); }
  }
  .pouch-shape-bottle {
    width: 46px;
    height: 78px;
    border-radius: 10px 10px 16px 16px;
    background: linear-gradient(180deg, #d8f3ee 0%, #a9e3d8 100%);
    border: 1px solid rgba(0, 0, 0, 0.06);
  }
  .pouch-shape-bottle::after {
    content: '';
    position: absolute;
    top: -10px;
    left: 50%;
    transform: translateX(-50%);
    width: 22px;
    height: 12px;
    border-radius: 4px;
    background: #4fb3a5;
  }
  .pouch-shape-tube {
    width: 34px;
    height: 82px;
    border-radius: 8px 8px 14px 14px;
    background: linear-gradient(180deg, #cdeee8 0%, #8fd6c8 100%);
  }
  .pouch-shape-tube::after {
    content: '';
    position: absolute;
    top: -8px;
    left: 50%;
    transform: translateX(-50%);
    width: 14px;
    height: 10px;
    border-radius: 3px 3px 6px 6px;
    background: #5fc2af;
  }
  .pouch-shape-cushion {
    width: 68px;
    height: 68px;
    border-radius: 50%;
    background: radial-gradient(circle at 35% 30%, #3a3a3a 0%, #0d0d0d 70%);
    border: 4px solid #cdae7d;
  }
  .pouch-shape-palette-pink {
    width: 66px;
    height: 52px;
    border-radius: 8px;
    background:
      repeating-linear-gradient(90deg, rgba(255, 255, 255, 0.5) 0 1px, transparent 1px 16.5px),
      repeating-linear-gradient(0deg, rgba(255, 255, 255, 0.5) 0 1px, transparent 1px 13px),
      linear-gradient(160deg, #f7d3e6 0%, #f2a9cf 100%);
    border: 3px solid #ffffff;
    box-shadow: 0 0 0 1px rgba(0, 0, 0, 0.08);
  }
  .pouch-shape-palette-brown {
    width: 52px;
    height: 74px;
    border-radius: 6px;
    background: linear-gradient(160deg, #8a6a52 0%, #4a3527 100%);
    border: 3px solid #d8bd93;
  }
  .pouch-shape-lip {
    width: 22px;
    height: 62px;
    border-radius: 8px 8px 10px 10px;
    background: linear-gradient(180deg, #f5b9c9 0%, #e8709a 100%);
  }
  .pouch-shape-pencil {
    width: 62px;
    height: 16px;
    border-radius: 4px;
    background: linear-gradient(90deg, #c0392b, #8e2317);
  }
  .pouch-shape-highlighter {
    width: 40px;
    height: 40px;
    border-radius: 8px;
    background: linear-gradient(160deg, #fff2e6 0%, #f5cdd8 100%);
    border: 2px solid #ffffff;
    box-shadow: inset 0 0 10px rgba(255, 255, 255, 0.9);
  }
  /* 내 파우치: 등록된 화장품 카드를 세로 그리드 대신 가로 캐러셀로 스와이프 */
  #pouchProductGrid.pouch-carousel {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
    gap: 12px;
    scroll-snap-type: x proximity;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  /* .hidden 유틸리티보다 위 규칙의 명시도가 높아서(#id.class) display:flex가 이겨버리는 문제 방지 */
  #pouchProductGrid.pouch-carousel.hidden {
    display: none;
  }
  #pouchProductGrid.pouch-carousel::-webkit-scrollbar {
    display: none;
  }
  #pouchProductGrid.pouch-carousel > .pouch-card {
    flex: 0 0 124px;
    width: 124px;
    scroll-snap-align: start;
  }
  #pouchProductGrid.pouch-carousel > .pouch-card p {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
  }
  /* 실제 제품 사진이 있는 경우 일러스트 대신 사진을 그대로, 라벨 없이 크게 보여줌 (등록하기 바구니 애니메이션).
     너비/높이는 제품별로 buildPouchItemEl에서 인라인으로 지정 */
  .pouch-item-photo {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .pouch-item-photo img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
  }
  /* 들고 가면 좋을 제품 추천: 내 파우치 카드와 동일한 가로 스와이프 캐러셀 */
  #careRecommendGrid {
    display: flex;
    flex-wrap: nowrap;
    overflow-x: auto;
    overflow-y: hidden;
    gap: 12px;
    scroll-snap-type: x proximity;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  #careRecommendGrid::-webkit-scrollbar {
    display: none;
  }
  #careRecommendGrid > .care-card {
    flex: 0 0 108px;
    width: 108px;
    scroll-snap-align: start;
  }
  #careRecommendGrid > .care-card p {
    display: -webkit-box;
    -webkit-line-clamp: 2;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }
  #careRecommendGrid > .care-card img {
    width: 100%;
    height: 84px;
    object-fit: contain;
  }
</style>
</head>
<body class="font-sans text-gray-900">

  <!-- ============ 랜딩 페이지 (웰컴 화면) ============ -->
  <div id="screen-welcome" class="relative mx-auto overflow-hidden" style="width: var(--app-width); height: var(--app-height); background-color: #000; background-image: url('__EARTH_BG_URI__'); background-size: cover; background-position: center;">

    <div class="relative z-10 pt-8 px-6 text-left">
      <img src="__LOGO_URI__" alt="GlowTrip" class="welcome-logo-icon" />
      <p class="mt-2 text-sm text-white/90 leading-relaxed font-normal">
        <span class="font-bold">글로우트립</span>과 함께,<br />피부 걱정 없이 어디든
      </p>
    </div>

    <div class="landing-bubble" style="top: 36%; left: 30%;"><img src="__AVATAR_URI_1__" alt="" /></div>
    <div class="landing-bubble" style="top: 43%; left: 13%;"><img src="__AVATAR_URI_2__" alt="" /></div>
    <div class="landing-bubble" style="top: 56%; left: 60%;"><img src="__AVATAR_URI_3__" alt="" /></div>
    <div class="landing-bubble" style="top: 60%; left: 76%;"><img src="__AVATAR_URI_4__" alt="" /></div>
    <div class="landing-bubble" style="top: 69%; left: 30%;"><img src="__AVATAR_URI_5__" alt="" /></div>

    <div class="absolute inset-x-0 bottom-9 z-10 flex justify-center">
      <button id="welcomeStartBtn" type="button" class="welcome-cta-btn" style="width: 60%;">시작하기</button>
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

  <!-- 내 파우치 제품 카드를 탭했을 때 뜨는 상세 정보(가격/용량/전성분) 팝업 -->
  <div id="productDetailModal" class="hidden fixed inset-0 bg-black/40 px-6 z-50">
    <div class="flex items-center justify-center h-full">
      <div class="bg-white rounded-2xl p-5 w-full max-w-xs max-h-[80vh] overflow-y-auto">
        <div class="flex items-start justify-between gap-2 mb-1">
          <div class="w-11 h-11 rounded-xl bg-brand-50 flex items-center justify-center text-xl shrink-0" id="productDetailIcon"></div>
          <button id="productDetailCloseBtn" type="button" class="text-gray-300 text-lg leading-none px-1">✕</button>
        </div>
        <p id="productDetailName" class="text-base font-bold mt-2"></p>
        <p id="productDetailMeta" class="text-xs text-gray-400 mb-3"></p>
        <div class="bg-brand-50 rounded-xl p-3 mb-3">
          <p class="text-[11px] font-semibold text-brand-500 mb-0.5">가격</p>
          <p id="productDetailPrice" class="text-lg font-bold"></p>
        </div>
        <div>
          <p class="text-[11px] font-semibold text-gray-500 mb-1.5">전성분</p>
          <p id="productDetailIngredients" class="text-xs text-gray-500 leading-relaxed"></p>
        </div>
        <p class="text-[10px] text-gray-300 mt-3">* 예시 데이터로, 실제 제품 정보와 다를 수 있어요</p>
        <button id="productDetailDeleteBtn" type="button" class="w-full mt-4 py-2.5 rounded-xl border border-red-200 text-red-500 text-sm font-semibold">파우치에서 삭제</button>
      </div>
    </div>
  </div>

  <!-- ============ 앱 화면 ============ -->
  <div id="appContainer" class="hidden mx-auto bg-gray-50 border-x border-gray-100" style="width: var(--app-width); position: relative;">

    <!-- 상단 로고 (온보딩 위저드 중에는 화면 정중앙 배치를 위해 숨김) -->
    <header id="appHeader" class="hidden px-5 pt-6 pb-3 flex items-center justify-between">
      <img src="__LOGO_URI__" alt="GlowTrip" class="app-header-logo" />
      <button id="mainProfileBtn" type="button" class="hidden text-xs font-semibold text-gray-500 bg-white border border-gray-200 rounded-full px-3 py-1.5">프로필 설정</button>
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
            <div class="flex gap-2 w-full max-w-xs">
              <select id="regBirthYearSelect" class="flex-1 min-w-0 border border-gray-200 rounded-xl px-1 py-3 text-sm text-center focus:outline-none focus:border-brand-500">
                <option value="">년</option>
              </select>
              <select id="regBirthMonthSelect" class="flex-1 min-w-0 border border-gray-200 rounded-xl px-1 py-3 text-sm text-center focus:outline-none focus:border-brand-500">
                <option value="">월</option>
              </select>
              <select id="regBirthDaySelect" class="flex-1 min-w-0 border border-gray-200 rounded-xl px-1 py-3 text-sm text-center focus:outline-none focus:border-brand-500">
                <option value="">일</option>
              </select>
            </div>
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
      <section id="screen-inuse" class="hidden pt-3 pb-6 space-y-6">

        <!-- 상단 헤더 블록: 인사말 → 국가 스위처(칩) → 선택된 여행 요약을 한 덩어리로 묶어서
             "지금 어떤 여행 기준으로 보고 있는지"를 처방/카드를 보기 전에 먼저 인지하게 함.
             미등록 시엔 바로 아래 폼이 펼쳐져 있어 별도 안내 링크가 없고,
             등록 후에만 칩/"[국가] ... · 수정하기" 요약 링크가 나타나 폼을 다시 열 수 있음 -->
        <div>
          <p id="mainGreeting" class="text-sm text-gray-400 mb-2">안녕하세요!</p>
          <!-- 등록된 나라 칩: 탭하면 아래 요약/카드가 그 나라 기준으로 전환됨 -->
          <div id="tripCountryChipsRow" class="hidden flex items-center gap-2 overflow-x-auto mb-3" style="scrollbar-width: none;"></div>
          <h2 id="mainTripHeadline" class="text-2xl font-bold leading-snug mb-1">어디로<br />여행가시나요?</h2>
          <button id="mainRegisterTripBtn" type="button" class="hidden text-sm font-semibold text-brand-500">여행지 등록하기 →</button>
        </div>

        <!-- 오늘의 처방(또는 이미 다녀온 여행이면 회고) 히어로 카드: "정보 나열"이 아니라 오늘 뭘 하면
             되는지(혹은 그때 날씨가 어땠는지) 한 문장으로 안내. 여행지 등록 후에만 표시,
             인사말/칩/여행 요약 바로 아래(여행 폼/파우치/지도보다 위)에 노출 -->
        <div id="todayInsightCard" class="hidden bg-white border border-gray-100 rounded-2xl p-5">
          <p id="todayInsightWeatherLine" class="text-xs font-semibold text-gray-400 mb-2"></p>
          <p id="todayInsightMain" class="text-lg font-extrabold text-gray-900 leading-snug mb-1.5"></p>
          <p id="todayInsightSub" class="text-xs text-gray-500 mb-4"></p>
          <div id="todayInsightMetrics" class="flex items-center gap-3 text-[11px] font-semibold text-gray-400"></div>
        </div>

        <!-- 예측 경고 배너: 처방 카드가 주인공이 되도록 카드 아래에 작게, 여행지 등록 후에만
             노출 (단, 이미 다녀온 과거 여행이면 더 이상 의미가 없으므로 숨김) -->
        <button id="predictiveWarningBanner" type="button" class="hidden w-full flex items-center gap-2 text-left rounded-xl px-3 py-2.5" style="background: #fde7ea; border-left: 3px solid #eb0029;">
          <span class="text-xs font-semibold leading-snug" style="color: #b4001f;">⚠️ 이틀 뒤 습도가 급격히 떨어져요. 지금 루틴이면 각질이 올라올 수 있어요.</span>
        </button>

        <!-- 여행 계획 입력: 여행지 미등록 시엔 이 인라인 카드 안에 항상 펼쳐져 있고,
             등록 후에는 아래 팝업(바텀시트)으로 옮겨져서 "수정하기" 클릭 시에만 열림 -->
        <div id="tripSegmentsInlineSlot" class="bg-white border border-gray-100 rounded-2xl p-4">
          <div id="tripSegmentsSection" class="space-y-3">
            <div id="tripSegmentRows" class="space-y-3"></div>
            <button id="addTripSegmentBtn" type="button" class="w-full py-2.5 rounded-xl border border-dashed border-gray-300 text-gray-500 text-sm font-semibold">+ 구간 추가</button>
            <p id="tripSegmentWarning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2"></p>
            <button id="tripSegmentsSaveBtn" type="button" class="w-full py-2.5 rounded-xl bg-brand-500 text-white text-sm font-bold">저장하기</button>
          </div>
        </div>

        <!-- 내 파우치 (촬영/직접입력 UI가 클릭 없이 항상 바로 노출) -->
        <div id="pouchSection" class="bg-white border border-gray-100 rounded-2xl p-4">
          <div class="flex items-center justify-between mb-1">
            <h2 class="text-base font-bold">내 파우치</h2>
            <button id="pouchAddMoreBtn" type="button" class="hidden text-xs font-semibold text-brand-500">+ 추가</button>
          </div>
          <p id="pouchSectionSubtitle" class="text-sm text-gray-400 mb-4">사진 한 장이면 화장품 이름과 종류를 자동으로 인식해드려요</p>

          <!-- 여행지에 반입 금지된 성분이 파우치 제품에서 발견되면 노출되는 인라인 경고 -->
          <p id="pouchIngredientWarning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2 mb-3 leading-relaxed"></p>

          <!-- 등록된 화장품 카드 그리드 (1개 이상 등록되면 노출) -->
          <div id="pouchProductGrid" class="hidden pouch-carousel"></div>

          <!-- 촬영/직접입력 UI (비어있을 때 기본 노출, "+ 추가" 클릭 시 다시 노출) -->
          <div id="pouchCaptureUI">
            <!-- 1단계: 어떻게 추가할지 먼저 선택 -->
            <div id="pouchAddChoiceView" class="pouch-add-step">
              <button id="pouchAddChoiceBackBtn" type="button" class="hidden text-xs text-gray-400 mb-3">← 이전</button>
              <p class="text-sm text-gray-500 text-center mb-3">어떻게 추가할까요?</p>
              <div class="space-y-2.5">
                <button id="pouchChoosePhotoBtn" type="button" class="pouch-add-choice-btn primary">
                  <span class="text-3xl">📷</span>
                  <span class="flex flex-col items-start">
                    <span class="pouch-add-choice-title">사진으로 추가</span>
                    <span class="pouch-add-choice-desc">한 장이면 이름·종류 자동 인식</span>
                  </span>
                </button>
                <button id="pouchChooseTextBtn" type="button" class="pouch-add-choice-btn secondary">
                  <span class="text-lg">✏️</span>
                  <span class="pouch-add-choice-title">직접 입력</span>
                </button>
              </div>
            </div>

            <!-- 2-a단계: 사진으로 추가 (기존 촬영/인식 흐름 그대로) -->
            <div id="pouchAddPhotoView" class="pouch-add-step hidden">
              <button type="button" class="pouch-add-back-btn text-xs text-gray-400 mb-3">← 이전</button>
              <label for="cosmeticPhotoInput" class="flex flex-col items-center justify-center gap-1.5 border-2 border-dashed border-gray-300 rounded-2xl py-10 text-gray-400 cursor-pointer hover:border-brand-500 hover:text-brand-500 transition">
                <span class="text-3xl">📷</span>
                <span class="text-sm font-semibold">탭해서 촬영하기</span>
                <span class="text-xs text-gray-300">또는 앨범에서 사진 선택</span>
              </label>
              <input id="cosmeticPhotoInput" type="file" accept="image/*" capture="environment" class="hidden" />

              <!-- 인식된(또는 직접 추가한) 화장품 검토 리스트 -->
              <div class="mt-3">
                <h3 class="text-sm font-semibold text-gray-700 mb-3">갖고 있는 화장품 <span id="cosmeticCountBadge" class="text-gray-400 font-normal"></span></h3>
                <div id="cosmeticRows" class="space-y-2 mb-3"></div>
                <button id="addCosmeticRowBtn" type="button" class="w-full text-center text-xs text-gray-400 underline">
                  직접 입력하기
                </button>
                <button id="pouchRegisterBtn" type="button" class="hidden w-full mt-3 py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">
                  등록하기
                </button>
              </div>
            </div>

            <!-- 2-b단계: 직접 입력 (제품 1개만 빠르게 추가) -->
            <div id="pouchAddTextView" class="pouch-add-step hidden">
              <button type="button" class="pouch-add-back-btn text-xs text-gray-400 mb-3">← 이전</button>
              <div class="space-y-2">
                <input id="pouchAddTextName" type="text" placeholder="제품명" class="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm focus:outline-none focus:border-brand-500" />
                <select id="pouchAddTextCategory" class="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-gray-600 focus:outline-none focus:border-brand-500"></select>
                <button id="pouchAddTextSaveBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">추가하기</button>
              </div>
            </div>
          </div>
        </div>

        <!-- 들고 가면 좋을 제품: 등록된 여행지의 기후에 맞춰 추천 (여행지 등록 전에는 숨김) -->
        <div id="careRecommendSection" class="hidden bg-white border border-gray-100 rounded-2xl p-4">
          <h2 class="text-base font-bold mb-1">들고 가면 좋을 제품</h2>
          <p id="careRecommendMent" class="text-sm text-gray-400 mb-4"></p>
          <div id="careRecommendGrid"></div>
        </div>

        <!-- 내 주위 화장품 매장 (기존 지도 탭 내용을 메인 화면 안으로 흡수) -->
        <div id="mapStoreSection" class="space-y-4">
          <div>
            <h2 class="text-base font-bold mb-1">내 주위 화장품 매장</h2>
            <p class="text-sm text-gray-400 mb-1">지도에 표시된 마커를 눌러도 위치를 확인할 수 있어요</p>
            <p id="mapStoreLocationLabel" class="hidden text-xs font-semibold text-brand-500 mb-3"></p>
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
                <input id="globeSearchInput" type="text" placeholder="나라 또는 도시를 검색해보세요" class="w-full py-2 px-3 rounded-full bg-gray-50 border-2 border-transparent text-sm text-gray-900 placeholder-gray-400 focus:outline-none focus:border-brand-400 transition-colors" />
                <p id="globeSearchNotFound" class="hidden mt-1.5 ml-1 inline-block text-[11px] font-medium text-brand-500 bg-brand-50 px-2 py-1 rounded-full">찾을 수 없어요</p>
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
          <h2 class="text-base font-bold mb-1">기록</h2>
          <p class="text-sm text-gray-400 mb-4">등록한 여행 일정을 확인해보세요</p>
        </div>

        <!-- 여행 요약 히어로: 지금까지의 여행을 국가/도시/연도로 집계 + 방문 국기 나열 -->
        <div id="historySummaryHero" class="hidden rounded-2xl p-5" style="background: linear-gradient(135deg, #fde7ea 0%, #fac7ce 100%); border: 1px solid #fac7ce;">
          <p id="summaryMainSentence" class="text-lg font-extrabold text-gray-900 leading-snug mb-1"></p>
          <p id="summarySubSentence" class="text-xs text-gray-500 mb-3"></p>
          <div id="summaryFlagsRow" class="flex flex-wrap gap-1.5" style="font-size: 20px;"></div>
        </div>

        <div class="space-y-2">
          <p id="historyCalendarEmpty" class="hidden text-sm text-gray-400 text-center py-10">아직 등록된 여행 일정이 없어요</p>
          <div id="historyCalendarList" class="space-y-2"></div>
        </div>
      </section>

      <!-- ============ 4. 피부 변화 리포트 ============ -->
      <section id="screen-afteruse" class="hidden py-6 space-y-6">

        <button id="afterUseToSettingsBtn" type="button" class="back-to-nav-btn text-xs text-gray-400">← 이전</button>

        <!-- 사진 등록 페이지 전용: 여권(패스포트) 컨셉 헤더 + 출국(1일차)·입국(마지막날) 도장 카드.
             두 사진이 모두 등록되기 전까지만 노출. 리포트 화면(skinReportPageLayout)은 완전히 분리되어
             그대로 유지되므로 이 영역의 변경은 리포트 표시에 영향을 주지 않음 -->
        <div id="skinRegisterPageLayout">
          <div class="rounded-2xl p-5 mb-3 bg-emerald-950">
            <div class="flex items-center justify-between mb-2">
              <p class="text-[10px] font-bold tracking-widest text-emerald-300">SKIN CONDITION PASSPORT</p>
              <span class="text-emerald-300 text-lg inline-block" style="transform: rotate(-45deg);">✈</span>
            </div>
            <h2 class="text-lg font-bold text-white mb-1">피부 변화 리포트</h2>
            <p id="skinPassportSubtitle" class="text-xs text-emerald-100/80"></p>
          </div>

          <div id="skinPhotoRegisterLayout" class="space-y-2 mb-2">
            <button type="button" id="skinPhotoStartRegBox" class="relative overflow-hidden w-full min-h-[160px] border border-gray-200 rounded-2xl py-8 flex flex-col items-center justify-center gap-2 cursor-pointer bg-white">
              <!-- 사진이 등록되면 카드 전체를 채우는 미리보기로 표시(center-crop은 object-cover가 처리).
                   글자가 사진 위에서도 잘 보이도록 어두운 스크림을 함께 깔고 아이콘은 숨김 -->
              <img id="skinPhotoStartRegPreview" class="hidden absolute inset-0 w-full h-full object-cover" alt="1일차 피부 사진" />
              <div id="skinPhotoStartRegScrim" class="hidden absolute inset-0 bg-black/50"></div>
              <span class="absolute top-3 right-3 z-10 text-[10px] font-bold text-gray-400 border border-gray-200 rounded px-1.5 py-0.5 bg-white/85">DEP</span>
              <div id="skinPhotoStartRegIcon" class="w-16 h-16 rounded-full border-2 border-brand-500 flex items-center justify-center text-2xl text-brand-500" style="transform: rotate(-45deg);">✈</div>
              <p id="skinPhotoStartRegTitle" class="text-base font-bold text-gray-900">출국 · 1일차</p>
              <p id="skinPhotoStartRegHint" class="text-xs text-gray-400">탭해서 사진 등록하기</p>
            </button>
            <div class="flex justify-center text-gray-300">↓</div>
            <button type="button" id="skinPhotoEndRegBox" class="relative overflow-hidden w-full min-h-[160px] border border-blue-200 rounded-2xl py-8 flex flex-col items-center justify-center gap-2 cursor-pointer bg-blue-50">
              <img id="skinPhotoEndRegPreview" class="hidden absolute inset-0 w-full h-full object-cover" alt="마지막날 피부 사진" />
              <div id="skinPhotoEndRegScrim" class="hidden absolute inset-0 bg-black/50"></div>
              <span class="absolute top-3 right-3 z-10 text-[10px] font-bold text-blue-500 border border-blue-200 rounded px-1.5 py-0.5 bg-white/85">ARR</span>
              <div id="skinPhotoEndRegIcon" class="w-16 h-16 rounded-full border-2 border-blue-500 flex items-center justify-center text-2xl text-blue-500" style="transform: rotate(135deg);">✈</div>
              <p id="skinPhotoEndRegTitle" class="text-base font-bold text-gray-900">입국 · 마지막날</p>
              <p id="skinPhotoEndRegHint" class="text-xs text-gray-400">탭해서 사진 등록하기</p>
            </button>
          </div>
          <p id="skinPhotoRegisterHint" class="text-xs text-gray-400 mt-1">출국·입국 도장을 찍으면 <span class="font-semibold text-gray-600">피부 여정 심사</span>가 시작돼요</p>
        </div>

        <!-- 리포트 화면(피부 변화 리포트): 두 사진이 모두 등록된 뒤에만 노출. 기존 그대로 변경 없음 -->
        <div id="skinReportPageLayout" class="hidden border border-gray-200 rounded-2xl p-5">
          <div class="flex items-center justify-between mb-1">
            <p id="skinReportDayLabel" class="text-xs text-gray-400"></p>
            <span id="skinReportDestinationChip" class="text-[10px] font-bold text-brand-500 border border-brand-100 rounded-full px-2 py-0.5"></span>
          </div>
          <h2 class="text-base font-bold mb-4">피부 변화 리포트</h2>

          <div class="grid grid-cols-2 gap-3 mb-2">
            <div>
              <button type="button" id="skinPhotoStartBox" class="relative overflow-hidden block w-full border-2 border-dashed border-gray-200 rounded-xl h-[38vh] flex flex-col items-center justify-center text-gray-400 gap-1 cursor-pointer">
                <img id="skinPhotoStartPreview" class="hidden absolute inset-0 w-full h-full object-cover" alt="1일차 피부 사진" />
                <div id="skinPhotoStartPlaceholder" class="flex flex-col items-center gap-1">
                  <span class="text-xl">🖼️</span>
                  <span class="text-xs">1일차 사진</span>
                </div>
                <!-- 사진이 이미 등록된 뒤에도 이 버튼을 누르면 파일 선택창이 다시 열려 사진을 교체할 수 있음.
                     탭하면 상위 버튼(라이트박스 확대)으로 클릭이 전달되지 않도록 별도 핸들러에서 stopPropagation 처리 -->
                <span id="skinPhotoStartRetakeBtn" class="hidden absolute bottom-1.5 right-1.5 z-10 text-[11px] font-semibold text-white bg-black/50 rounded-full px-2.5 py-1">다시 선택</span>
              </button>
              <input id="skinPhotoStartInput" type="file" accept="image/*" class="hidden" />
              <p id="skinReportStartDate" class="text-xs text-gray-400 text-center mt-2"></p>
            </div>
            <div>
              <button type="button" id="skinPhotoEndBox" class="relative overflow-hidden block w-full border-2 border-brand-500 rounded-xl h-[38vh] flex flex-col items-center justify-center text-brand-500 gap-1 cursor-pointer">
                <img id="skinPhotoEndPreview" class="hidden absolute inset-0 w-full h-full object-cover" alt="마지막날 피부 사진" />
                <div id="skinPhotoEndPlaceholder" class="flex flex-col items-center gap-1">
                  <span class="text-xl">🖼️</span>
                  <span class="text-xs">마지막날 사진</span>
                </div>
                <span id="skinPhotoEndRetakeBtn" class="hidden absolute bottom-1.5 right-1.5 z-10 text-[11px] font-semibold text-white bg-black/50 rounded-full px-2.5 py-1">다시 선택</span>
              </button>
              <input id="skinPhotoEndInput" type="file" accept="image/*" class="hidden" />
              <p id="skinReportEndDate" class="text-xs text-gray-400 text-center mt-2"></p>
            </div>
          </div>
          <p id="skinPhotoHint" class="text-xs text-gray-400 mt-1">→ 사진을 첨부하면 AI가 두 사진을 비교해 분석해드려요</p>
        </div>

        <!-- 항목별 변화: 두 사진이 모두 등록되기 전에는 제목·안내·버튼을 DOM에서 숨김(조건부 렌더링) -->
        <div>
          <h3 id="skinChangeSectionTitle" class="hidden text-sm font-semibold text-gray-700 mb-3">항목별 변화</h3>

          <!-- 초기 빈 상태 / 사진 등록 안내: 분석 전에는 mock 점수 대신 이 안내만 노출 -->
          <div id="skinChangeEmptyState" class="hidden text-center text-sm text-gray-400 py-10 leading-relaxed">
            1일차 사진과 마지막날 사진을 등록하면<br />항목별 분석 결과가 여기에 표시됩니다.
          </div>

          <!-- 분석 결과 카드: 별도의 "분석 연출 페이지"(screen-skin-scan)를 거친 뒤에만 노출.
               카드별로 "상세보기"를 누르면 세부 피드백이 펼쳐짐 -->
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

        <!-- 종합 요약: 사진이 모두 등록되어 분석이 끝나기 전에는 숨김 (항목별 카드와 함께 노출) -->
        <div id="skinReportSummaryBox" class="hidden bg-brand-50 border border-brand-100 rounded-2xl p-4">
          <p id="skinReportSummary" class="text-sm text-brand-700 leading-relaxed">여행 중 자외선 노출이 늘면서 홍조와 트러블이 조금 생겼어요. 자외선 차단제를 2~3시간마다 다시 발라주면 다음 여행에서 더 편안한 피부를 유지할 수 있을 거예요.</p>
          <p class="text-[11px] text-brand-400 mt-2 leading-relaxed">※ 사진 기반 근사 분석 결과로, 의학적 진단이 아닌 참고용 정보예요. 정확한 진단은 피부과 상담을 권장해요.</p>
        </div>

        <p id="aftercareMissingPhotosWarning" class="hidden text-xs font-medium text-red-500 bg-red-50 border border-red-100 rounded-xl px-3 py-2">먼저 1일차·마지막날 사진을 등록해 주세요</p>
        <!-- 리포트 저장하기: 항목별 변화·종합 요약이 준비된 뒤(두 사진 등록 후)에만 노출.
             기존 "내 피부 사후관리하기" 버튼과 동일한 스타일(색상·모서리·크기) 유지 -->
        <button id="saveSkinReportBtn" type="button" class="hidden w-full py-3.5 rounded-xl bg-brand-500 text-white text-sm font-bold">리포트 저장하기</button>
        <button id="goToAftercareBtn" type="button" class="hidden w-full py-3.5 rounded-xl bg-brand-500 text-white text-sm font-bold">내 피부 사후관리하기</button>

        <!-- 사진 확대 라이트박스: 결과 페이지의 1일차/마지막날 사진을 탭하면 원본 비율로 크게 표시 -->
        <div id="skinPhotoLightbox" class="hidden absolute inset-0 z-[70] bg-black/85 flex items-center justify-center p-6">
          <button id="skinPhotoLightboxCloseBtn" type="button" class="absolute top-4 right-4 w-9 h-9 rounded-full bg-white/15 text-white text-lg flex items-center justify-center" aria-label="닫기">✕</button>
          <img id="skinPhotoLightboxImage" class="max-w-full max-h-full object-contain rounded-xl" alt="확대된 피부 사진" />
        </div>

      </section>

      <!-- 피부 변화 리포트 흐름: 사진 입력 → 분석 연출(신규) → 분석 결과.
           두 사진이 모두 등록되면 이 화면으로 전환해 약 5초간 스캔 연출을 재생한 뒤 결과로 넘어감 -->
      <section id="screen-skin-scan" class="hidden py-6 flex flex-col items-center justify-center" style="min-height: 60vh;">
        <!-- overflow-hidden으로 감싸 아래 스캔 라인 등의 연출이 사진 영역 밖으로 넘치지 않게 클리핑 -->
        <div class="relative w-full max-w-[280px] aspect-square rounded-2xl overflow-hidden shadow-lg bg-gray-100">
          <img id="skinScanDay1Image" class="skin-scan-fade absolute inset-0 w-full h-full object-cover" alt="1일차 사진" />
          <img id="skinScanDay2Image" class="skin-scan-fade absolute inset-0 w-full h-full object-cover" alt="마지막날 사진" />
          <!-- 스캔 연출 스택: 격자 → 얼굴 mesh(노드+삼각망) → 스캔 라인(잔상 포함) 순으로 겹쳐 쌓음 -->
          <div id="skinScanMeshOverlay" class="hidden absolute inset-0 skin-scan-overlay">
            <div class="skin-scan-grid"></div>
            <div class="skin-scan-mesh-mount"></div>
            <div class="skin-scan-sweep-trail"></div>
            <div class="skin-scan-sweep"></div>
            <span class="skin-scan-corner skin-scan-corner-tl"></span>
            <span class="skin-scan-corner skin-scan-corner-tr"></span>
            <span class="skin-scan-corner skin-scan-corner-bl"></span>
            <span class="skin-scan-corner skin-scan-corner-br"></span>
          </div>
        </div>
        <p class="text-sm text-gray-500 mt-6">피부를 분석하고 있어요<span class="skin-scan-dots"><span></span><span></span><span></span></span></p>
        <p id="skinScanStatusText" class="text-xs text-brand-500 font-semibold mt-1">&nbsp;</p>
        <div class="skin-scan-progress mt-3"><div id="skinScanProgressBar" class="skin-scan-progress-bar"></div></div>
      </section>

      <!-- 피부 변화 리포트 하위 화면: 트러블 유무·유형에 따른 사후케어 제품 추천 -->
      <section id="screen-aftercare" class="hidden py-6 space-y-6">

        <button id="aftercareBackBtn" type="button" class="text-xs text-gray-400">← 이전</button>

        <h2 class="text-lg font-bold leading-snug">여행은 즐거웠으나<br />내 피부는 힘들었어요 😭</h2>

        <!-- 케어 필요 항목: 트러블이 있을 때만 노출 -->
        <div id="aftercareNeedsSection" class="hidden border border-gray-200 rounded-2xl p-5">
          <p class="text-xs font-semibold text-gray-400 mb-2">케어가 필요해요</p>
          <div class="flex items-center justify-between mb-2">
            <p class="text-sm font-semibold">🦠 <span id="aftercareTypeLabel">트러블</span></p>
            <span id="aftercareCountLine" class="text-xs text-gray-500"></span>
          </div>
          <p id="aftercareReasonText" class="text-xs text-gray-500 leading-relaxed"></p>
        </div>

        <!-- 트러블 없음 안내: 트러블이 없거나 분석 결과가 아직 없을 때 노출 -->
        <div id="aftercareEmptyState" class="hidden text-center text-sm text-gray-500 leading-relaxed bg-brand-50 border border-brand-100 rounded-2xl p-6"></div>

        <!-- 제품 추천: 트러블이 있을 때만 노출 -->
        <div id="aftercareProductSection" class="hidden">
          <h3 class="text-sm font-semibold text-gray-700 mb-3">추천 제품</h3>
          <div class="bg-white border border-gray-100 rounded-2xl p-4 space-y-3">
            <div>
              <p id="aftercareProductBrand" class="text-xs font-semibold text-brand-600"></p>
              <p id="aftercareProductName" class="text-base font-bold text-gray-900"></p>
            </div>
            <p id="aftercareProductBenefit" class="text-xs text-gray-500 leading-relaxed"></p>
            <div class="grid grid-cols-2 gap-2">
              <a id="aftercareOliveyoungLink" href="#" target="_blank" rel="noopener" class="text-center text-xs font-semibold text-gray-700 border border-gray-200 rounded-xl py-2.5">올리브영에서 보기</a>
              <a id="aftercareCoupangLink" href="#" target="_blank" rel="noopener" class="text-center text-xs font-semibold text-white bg-brand-500 rounded-xl py-2.5">쿠팡에서 보기</a>
            </div>
          </div>
          <p class="text-[11px] text-gray-400 mt-2 leading-relaxed">※ 참고용 추천이며 실제 피부 고민은 전문가 상담을 권장해요.</p>
        </div>

        <!-- 배달의뷰티 서비스 종료 안내 팝업: 사후케어 화면에 들어올 때마다 노출 -->
        <div id="deliveryBeautyEndModal" class="hidden absolute inset-0 z-50 bg-black/40 px-6 flex items-center justify-center">
          <div class="bg-white rounded-2xl p-5 w-full max-w-xs">
            <p class="text-base font-bold mb-3">배달의뷰티 서비스 종료 안내</p>
            <p class="text-sm text-gray-500 leading-relaxed mb-5">그동안 배달의뷰티를 아껴주신 모든 분들께 진심으로 감사드립니다.<br /><br />배달의뷰티 서비스는 종료되었지만, 여러분의 뷰티 라이프는 계속됩니다. 앞으로는 2개의 플랫폼에서 더욱 다양한 뷰티 상품으로 찾아뵙겠습니다.<br />감사합니다.</p>
            <button id="deliveryBeautyEndCloseBtn" type="button" class="w-full py-3 rounded-xl bg-brand-500 text-white text-sm font-bold">확인했어요</button>
          </div>
        </div>

      </section>

      <!-- 피부 변화 리포트 하위 화면: "리포트 저장하기"로 저장해둔 리포트 목록.
           하단 네비 탭이 아니므로 뒤로가기는 항상 피부 변화 리포트 화면으로 복귀 (aftercare와 동일 패턴) -->
      <section id="screen-saved-reports" class="hidden py-6 space-y-6">

        <button id="savedReportsBackBtn" type="button" class="text-xs text-gray-400">← 이전</button>

        <div>
          <h2 class="text-base font-bold mb-1">저장된 피부 리포트</h2>
          <p class="text-sm text-gray-400">저장해둔 여행별 피부 변화 리포트를 다시 볼 수 있어요</p>
        </div>

        <!-- 저장된 리포트가 하나도 없을 때 안내 -->
        <p id="savedReportsEmptyNote" class="hidden text-sm text-gray-400 text-center py-10">아직 저장된 리포트가 없어요</p>

        <!-- 저장된 리포트 목록: 각 행 = [여행지 | 날짜 | 리포트 조회하기] -->
        <div id="savedReportsList" class="space-y-3"></div>

        <!-- 리포트 조회 팝업(모달): 배경 탭 또는 X 버튼으로 닫힘 -->
        <div id="savedReportViewModal" class="hidden absolute inset-0 z-50 bg-black/40 px-6 flex items-center justify-center">
          <div class="bg-white rounded-2xl p-5 w-full max-w-xs max-h-[80vh] overflow-y-auto">
            <div class="flex items-center justify-between mb-3">
              <p id="savedReportViewTitle" class="text-sm font-bold"></p>
              <button id="savedReportViewCloseBtn" type="button" class="text-gray-400 text-lg leading-none" aria-label="닫기">✕</button>
            </div>
            <p id="savedReportViewDateRange" class="text-xs text-gray-400 mb-4"></p>
            <!-- 저장 당시 등록했던 1일차·마지막날 사진 (예전에 사진 없이 저장된 리포트는 이 영역을 숨김) -->
            <div id="savedReportViewPhotos" class="hidden grid grid-cols-2 gap-2 mb-4">
              <div>
                <img id="savedReportViewStartPhoto" class="w-full aspect-square object-cover rounded-xl" alt="1일차 사진" />
                <p class="text-[11px] text-gray-400 text-center mt-1">1일차</p>
              </div>
              <div>
                <img id="savedReportViewEndPhoto" class="w-full aspect-square object-cover rounded-xl" alt="마지막날 사진" />
                <p class="text-[11px] text-gray-400 text-center mt-1">마지막날</p>
              </div>
            </div>
            <div id="savedReportViewItems" class="space-y-2 mb-4"></div>
            <div class="bg-brand-50 border border-brand-100 rounded-2xl p-4">
              <p id="savedReportViewSummary" class="text-sm text-brand-700 leading-relaxed"></p>
            </div>
          </div>
        </div>

      </section>

      <!-- ============ 5. 커뮤니티 페이지 ============ -->
      <section id="screen-community" class="hidden py-6 space-y-3">
        <button type="button" class="back-to-nav-btn text-xs text-gray-400" data-back-target="inuse">← 이전</button>
        <div>
          <h2 class="text-base font-bold mb-1">커뮤니티</h2>
          <p class="text-sm text-gray-400 mb-4">다른 여행자들의 스킨케어 이야기를 둘러보세요</p>
        </div>

        <!-- 국가 선택 + [리뷰]/[나라별 인기템] 서브탭 (두 탭이 공유, 스크롤해도 항상 보이도록 고정) -->
        <div class="community-country-bar space-y-2 pb-2">
          <select id="communitySharedCountrySelect" class="w-full border border-gray-200 rounded-xl px-3 py-2.5 text-sm font-semibold bg-white focus:outline-none focus:border-brand-500">
            <option value="이탈리아">🇮🇹 이탈리아</option>
            <option value="일본">🇯🇵 일본</option>
            <option value="프랑스">🇫🇷 프랑스</option>
            <option value="태국">🇹🇭 태국</option>
            <option value="한국">🇰🇷 한국</option>
            <option value="독일">🇩🇪 독일</option>
            <option value="미국">🇺🇸 미국</option>
            <option value="호주">🇦🇺 호주</option>
            <option value="그리스">🇬🇷 그리스</option>
          </select>
          <div class="flex bg-gray-100 rounded-full p-1">
            <button type="button" class="community-subtab-btn active flex-1 py-2 rounded-full text-sm font-semibold" data-subtab="review">리뷰</button>
            <button type="button" class="community-subtab-btn flex-1 py-2 rounded-full text-sm font-semibold" data-subtab="popular">나라별 인기템</button>
          </div>
        </div>

        <!-- [리뷰] 탭: 기존 커뮤니티 리뷰 기능 그대로 -->
        <div id="communityReviewTab" class="space-y-3">
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
        </div>

        <!-- [나라별 인기템] 탭: 지도+매장 → 인기 아이템 TOP3 → 매장 연결 순으로 배치 -->
        <div id="communityPopularTab" class="hidden space-y-5">
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">📍 <span id="popularStoreCountryLabel">이탈리아</span>에서 갈 만한 매장</h3>
            <div id="communityPopularMapViz" class="relative w-full rounded-2xl overflow-hidden mb-3" style="height: 220px; background: linear-gradient(180deg, #eaf6ff 0%, #cfeeff 100%);"></div>
            <div id="communityPopularStoreList" class="space-y-2"></div>
            <p id="communityPopularStoreEmpty" class="hidden text-sm text-gray-400 text-center py-6">아직 이 나라의 매장 정보가 없어요</p>
          </div>
          <div>
            <h3 class="text-sm font-semibold text-gray-700 mb-3">🏆 <span id="popularItemsCountryLabel">이탈리아</span> 인기 아이템 TOP3</h3>
            <div id="communityPopularItemsList" class="space-y-3"></div>
            <p id="communityPopularItemsEmpty" class="hidden text-sm text-gray-400 text-center py-8">아직 준비 중이에요</p>
          </div>
        </div>
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

    </main>

    <!-- 여행 계획 수정 팝업: 여행지 등록 후 "수정하기" 클릭 시에만 바텀시트로 열림 (미등록 시엔 인라인 카드로 별도 노출) -->
    <div id="tripSegmentsBackdrop" class="hidden absolute inset-0 z-[52] bg-black/40"></div>
    <div id="tripSegmentsModal" class="trip-destination-sheet hidden absolute left-0 right-0 bottom-0 z-[55] bg-white rounded-t-3xl px-5 pt-4 pb-6">
      <div class="flex items-center justify-between mb-3">
        <p class="text-sm font-bold">여행 계획 수정</p>
        <button id="tripSegmentsCloseBtn" type="button" class="text-gray-400 text-lg leading-none">✕</button>
      </div>
    </div>

    <!-- 여행 날짜 선택(월간 달력, 범위 선택): 구간 카드의 날짜 필드를 탭하면 이 위에 열림 -->
    <div id="tripDateRangeBackdrop" class="hidden absolute inset-0 z-[60] bg-black/40"></div>
    <div id="tripDateRangeModal" class="trip-destination-sheet hidden absolute left-0 right-0 bottom-0 z-[60] bg-white rounded-t-3xl px-5 pt-4 pb-6">
      <div class="flex items-center justify-between mb-3">
        <p class="text-sm font-bold">여행 날짜 선택</p>
        <button id="tripDateRangeCloseBtn" type="button" class="text-gray-400 text-lg leading-none">✕</button>
      </div>
      <div class="flex items-center justify-between mb-2">
        <p id="tripDateRangeMonthLabel" class="text-sm font-bold"></p>
        <div class="flex items-center gap-1">
          <button id="tripDateRangePrevBtn" type="button" aria-label="이전 달" class="w-7 h-7 rounded-full bg-gray-100 text-gray-500 flex items-center justify-center text-xs">▲</button>
          <button id="tripDateRangeNextBtn" type="button" aria-label="다음 달" class="w-7 h-7 rounded-full bg-gray-100 text-gray-500 flex items-center justify-center text-xs">▼</button>
        </div>
      </div>
      <div class="grid grid-cols-7 text-center text-[11px] text-gray-400 mb-1">
        <span>일</span><span>월</span><span>화</span><span>수</span><span>목</span><span>금</span><span>토</span>
      </div>
      <div id="tripDateRangeGrid" class="grid grid-cols-7"></div>
      <p id="tripDateRangeHint" class="text-xs text-gray-400 text-center mt-3"></p>
      <button id="tripDateRangeConfirmBtn" type="button" class="w-full mt-3 py-3 rounded-xl bg-brand-500 text-white text-sm font-bold" disabled>확인</button>
    </div>

    <!-- 부가서비스 메뉴 패널 (하단 네비 위로 올라오는 오버레이) -->
    <div id="moreMenuBackdrop" class="hidden absolute inset-0 z-[52] bg-black/40"></div>
    <div id="moreMenuModal" class="trip-destination-sheet hidden absolute left-0 right-0 bottom-0 z-[55] bg-white rounded-t-3xl px-5 pt-4 pb-6">
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

    <!-- 파우치 화장품 사진 인식: 전체화면 물체 감지 스캔 -->
    <div id="cosmeticScanModal" class="hidden absolute inset-0 z-[60] flex flex-col" style="background: #0d0d0f;">
      <div class="p-4 flex items-center justify-end">
        <button id="cosmeticScanCloseBtn" type="button" aria-label="닫기" class="w-8 h-8 rounded-full bg-white/15 text-white text-base leading-none flex items-center justify-center">✕</button>
      </div>
      <div class="flex-1 flex items-center justify-center px-6 overflow-hidden">
        <div id="cosmeticScanImageWrap" class="relative inline-block">
          <img id="cosmeticScanImage" src="" alt="촬영한 화장품" class="block rounded-2xl" style="max-width: 100%; max-height: 55vh; width: auto; height: auto;" />
          <div id="cosmeticScanBoxLayer" class="absolute inset-0 pointer-events-none"></div>
        </div>
      </div>
      <div class="px-6 pb-10 pt-4 text-center">
        <p id="cosmeticScanStatusText" class="text-white text-sm font-semibold mb-3">준비 중...</p>
        <div class="h-1.5 bg-white/15 rounded-full overflow-hidden max-w-[220px] mx-auto">
          <div id="cosmeticScanProgressBar" class="h-full bg-brand-400 rounded-full" style="width: 0%;"></div>
        </div>
      </div>
    </div>

    <!-- "등록하기" 클릭 시 열리는 새 페이지: 내 파우치에 담긴 화장품들이 하나씩
         바구니 안으로 날아들어오는 연출 -->
    <div id="pouchBasketModal" class="hidden absolute inset-0 z-[60] flex flex-col" style="background-color: #eef4f3;">
      <div class="p-4 flex items-center justify-end shrink-0">
        <button id="pouchBasketCloseBtn" type="button" aria-label="닫기" class="w-8 h-8 rounded-full bg-white/80 text-gray-500 text-base leading-none flex items-center justify-center shadow-sm">✕</button>
      </div>
      <div class="flex-1 flex flex-col items-center overflow-y-auto">
        <div class="flex-1 flex flex-col items-center px-6 pt-1 pb-4 w-full">
          <div class="w-full flex items-center gap-2 mb-4">
            <span id="pouchCompleteCheck" class="pouch-complete-check-mini">
              <svg viewBox="0 0 24 24" width="12" height="12" fill="none"><path d="M5 12.5l4.5 4.5L19 7" stroke="white" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
            </span>
            <p id="pouchCompleteMsg" class="text-xl font-bold text-gray-900 leading-snug"><span id="pouchCompleteCount">0</span>개 제품을 선반에 정리했어요</p>
          </div>
          <div class="pouch-basket-stage">
            <div class="pouch-basket">
              <div class="pouch-glass-shelf-line" style="top: 35.2%;"></div>
              <div class="pouch-glass-shelf-line" style="top: 64.3%;"></div>
              <div class="pouch-glass-shelf-line" style="top: 93.5%;"></div>
            </div>
            <div id="pouchBasketItems" class="pouch-basket-items"></div>
            <div id="pouchItemTooltip" class="pouch-item-tooltip"></div>
          </div>
          <div id="pouchChipsRow" class="flex flex-col gap-2 mt-5 px-1 w-full"></div>
        </div>
      </div>
      <div class="px-6 pt-3 pb-8 shrink-0">
        <button id="pouchBasketConfirmBtn" type="button" class="w-full py-3.5 rounded-2xl bg-brand-500 text-white text-sm font-bold shadow-md active:scale-[0.98] transition">확인</button>
      </div>
    </div>

    <!-- 여행 기록 상세: 달력 콜라주 + 순차 도장 애니메이션 (03 calendar_archive_pkg 통합) -->
    <div id="archiveModal" class="hidden absolute inset-0 z-[60]">
      <div id="archiveBackdrop" class="absolute inset-0 bg-black/50"></div>
      <div class="archive-modal absolute inset-0 flex flex-col">
        <div id="archiveCanvas" class="absolute inset-0 z-10 overflow-hidden"></div>
        <div id="archiveHeader" class="absolute top-0 left-0 right-0 z-20 flex items-center justify-between px-5 pt-6 pb-4 text-white pointer-events-none">
          <button id="archiveCloseBtn" type="button" class="w-10 h-10 rounded-full bg-white/15 backdrop-blur ring-1 ring-white/25 flex items-center justify-center text-xl text-white active:scale-95 transition pointer-events-auto" aria-label="뒤로 가기">←</button>
          <div class="text-center" style="text-shadow: 0 1px 6px rgba(0, 0, 0, 0.5);">
            <p id="archiveHeaderTitle" class="text-sm font-bold leading-tight"></p>
            <p id="archiveHeaderSub" class="text-[11px] opacity-90"></p>
          </div>
          <div class="w-10 h-10"></div>
        </div>
        <!-- 콜라주 사진을 탭하면 확대해서 보여주는 라이트박스 -->
        <div id="archivePhotoLightbox" class="hidden absolute inset-0 z-30 flex items-center justify-center px-8" style="background: rgba(0, 0, 0, 0.75);">
          <img id="archivePhotoLightboxImg" src="" alt="" class="max-w-full max-h-[70vh] rounded-2xl" style="box-shadow: 0 12px 40px rgba(0, 0, 0, 0.5);" />
        </div>
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
    // Tailwind CDN(JIT)이 이 페이지 전체(용량이 매우 큼)를 스캔해서 스타일을 주입하는 데
    // 300ms보다 오래 걸리면, 그 사이에 계산된 iframe 높이가 실제 레이아웃보다 작게 고정돼
    // 화면 하단 버튼(예: 웰컴 화면 "시작하기")이 iframe 클릭 가능 영역 밖으로 밀려나는
    // 문제가 생길 수 있어 여러 지연 시간으로 반복 재계산함
    [300, 800, 1500, 3000, 5000].forEach((delay) => setTimeout(scheduleResize, delay));
    scheduleResize();

    // 화면이 바뀔 때마다 살짝 페이드인되도록 애니메이션 클래스를 다시 걸어줌
    function playScreenTransition(el) {
      el.classList.remove('screen-transition');
      void el.offsetWidth; // 리플로우를 강제로 일으켜 애니메이션을 재시작
      el.classList.add('screen-transition');
    }

    // 웰컴 화면 "시작하기" -> 앱 진입 (온보딩 위저드 1단계부터 시작)
    function enterApp() {
      try {
        const welcome = document.getElementById('screen-welcome');
        const app = document.getElementById('appContainer');
        if (!welcome || !app) {
          console.error('enterApp: 화면 요소를 찾을 수 없음', { welcome: !!welcome, app: !!app });
          return;
        }
        welcome.classList.add('hidden');
        app.classList.remove('hidden');
        playScreenTransition(app);
      } catch (e) {
        console.error('enterApp 전환 중 오류:', e);
      }
    }
    // 일부 모바일 브라우저는 컴포넌트가 srcdoc iframe 안에 있을 때 iframe에 처음
    // 탭하는 동작이 포커스 이동으로만 소모되고 click 이벤트가 발생하지 않는 경우가
    // 있어(:active 프레스 효과는 보이지만 다음 화면으로 안 넘어가는 증상과 일치),
    // touchend에도 동일하게 걸어 click이 먹지 않는 경우를 보완함
    (function bindWelcomeStart() {
      const btn = document.getElementById('welcomeStartBtn');
      if (!btn) {
        console.error('welcomeStartBtn을 찾을 수 없음');
        return;
      }
      let handled = false;
      function handleStart() {
        if (handled) return;
        handled = true;
        enterApp();
        setTimeout(() => { handled = false; }, 600);
      }
      btn.addEventListener('click', handleStart);
      btn.addEventListener('touchend', handleStart);
    })();

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
      skinScan: document.getElementById('screen-skin-scan'),
      aftercare: document.getElementById('screen-aftercare'),
      savedReports: document.getElementById('screen-saved-reports'),
      community: document.getElementById('screen-community'),
      settings: document.getElementById('screen-settings'),
    };
    let onboardingComplete = false;
    let lastActiveNavTab = 'inuse';
    let pouchCaptureForceOpen = false;
    let pouchAddStep = 'choice'; // 'choice' | 'photo' | 'text'

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
      const storeKey = weather.cityKey || (weather.en ? weather.en.toLowerCase() : '');
      const baseStores = storeData[storeKey] || [];
      const offsets = [
        [0.008, 0.006], [-0.009, 0.004], [0.004, -0.009], [-0.006, -0.007], [0.011, -0.002],
      ];
      currentCityStores = baseStores.map((store, i) => {
        // 구글 맵 기준 실제 좌표가 있는 매장(예: 로마 세포라)은 그대로 쓰고,
        // 없는 mock 매장만 여행지 중심 좌표에서 살짝 흩어지게 배치
        if (store.lat != null && store.lng != null) return { ...store };
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
            <span style="display:inline-block;font-size:10px;padding:2px 8px;border-radius:9999px;background:#fac7ce;color:#b4001f;font-weight:600;">${store.category}</span>
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
      renderMapStoreList(weather.cityLabel || cityKey, currentCityStores);
    }

    // 지도 아래 매장 리스트 카드: 클릭 시 지도가 해당 매장 마커로 다시 flyTo
    // 타이틀/부제는 고정 문구를 유지하고, 위치 정보만 작은 라벨로 표시
    function renderMapStoreList(displayLabel, stores) {
      const locationLabel = document.getElementById('mapStoreLocationLabel');
      locationLabel.textContent = `📍 ${displayLabel}`;
      locationLabel.classList.remove('hidden');
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
      // 분석 연출 페이지에서 다른 탭으로 벗어나면(뒤로가기/하단 네비 탭 등) 예약된 타이머를 즉시 정리해
      // 메모리 누수나 다른 화면에서 엉뚱하게 전환/카드 갱신이 발생하는 것을 막음
      if (tabName !== 'skinScan') {
        clearSkinScanTimers();
      }
      bottomNavButtons.forEach((b) => b.classList.toggle('active', b.dataset.tab === tabName));
      updateBottomNavPill();
      Object.entries(screens).forEach(([key, el]) => el.classList.toggle('hidden', key !== tabName));
      // 프로필 설정 버튼은 로고와 한 줄에 있는 전역 헤더 소속이라, 홈 화면일 때만 보여줌
      document.getElementById('mainProfileBtn').classList.toggle('hidden', tabName !== 'inuse');
      try {
        playScreenTransition(screens[tabName]);
        if (tabName === 'inuse') {
          refreshAdjustedRoutine();
          initMapIfNeeded();
        } else if (tabName === 'skinReport') {
          renderSkinReport();
        } else if (tabName === 'aftercare') {
          renderAftercare();
        } else if (tabName === 'savedReports') {
          renderSavedSkinReportsList();
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
      commitTripSegments();
      tripSegmentsExpanded = false;
      applyTripSegmentsFormMode();
    });
    document.getElementById('tripSegmentsCloseBtn').addEventListener('click', () => {
      resetDraftFormToConfirmed(); // 저장 없이 닫기 - 편집 중이던 값은 버리고 마지막 확정값으로 되돌림
      tripSegmentsExpanded = false;
      applyTripSegmentsFormMode();
    });
    document.getElementById('tripSegmentsBackdrop').addEventListener('click', () => {
      resetDraftFormToConfirmed(); // 저장 없이 닫기 - 편집 중이던 값은 버리고 마지막 확정값으로 되돌림
      tripSegmentsExpanded = false;
      applyTripSegmentsFormMode();
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
      // 사진 등록 페이지(여권 컨셉 헤더)의 부제 문구도 같은 데이터로 함께 채움
      document.getElementById('skinPassportSubtitle').textContent = `여행 ${totalDays}일차 · 마지막날 / 출입국 기록`;
    }

    // ===== 피부 변화 리포트: 사진 업로드/촬영 → Canvas 픽셀 분석 → 항목별 카드 자동 갱신 =====
    // 외부 API/라이브러리 없이 순수 JS + Canvas로 계산하는 "근사 스크리닝"입니다.
    // 실제 피부과적 진단이 아니라, 두 사진의 픽셀 패턴을 비교해 변화 추이만 보여주는 목적입니다.

    const SKIN_ANALYSIS_SIZE = 128; // 분석용 캔버스 한 변 크기(px). 클수록 정교하지만 느려짐

    // ===== 피부타입별 분석 기준값 설정 =====
    // 아래 값은 모두 "초기 경험값"입니다. 실제 사진으로 결과를 보면서 이 객체 안의 숫자만
    // 조정하면 되도록 모든 타입별 기준값을 여기 한 곳에 모아둡니다(로직 코드는 건드릴 필요 없음).
    // - hydration.optimalMin/optimalMax: 이 범위 "안"에 있을 때 가장 좋은 상태로 판정(무조건 높다고 좋은 게 아님)
    //
    // blemish(트러블 감지)는 "누가 봐도 명백한, 치료가 필요할 수준"만 잡도록 매우 엄격하게 설계됨.
    // 아래 4개 조건을 모두(AND) 만족해야만 트러블 1건으로 카운트:
    //   1) minBlobBlocks   — 크기: 이 개수(8px 블록 기준) 이상 뭉쳐야 "명백히 큰 병변"으로 인정
    //   2) rednessMargin / brightnessMargin — 색상 대비: 국소 이웃보다 얼마나 더 붉고/어두워야 하는지
    //   3) maxAspectRatio  — 형태: 뭉친 영역의 가로/세로 비율이 이 배수를 넘으면 "띠 모양"(그림자·주름·홍조 번짐)으로
    //                        보고 제외 — 진짜 병변은 둥글게 뭉친 형태, 그림자는 길게 늘어진 형태이기 때문
    //   4) minAbsoluteRedness / minSaturation — 채도·강도: 국소 대비뿐 아니라 그 블록 자체가 "확실한 염증성
    //                        붉은색"이어야 함(그림자는 R·G·B가 고르게 어두워질 뿐 붉은기·채도 자체는 낮음)
    const SKIN_TYPE_PROFILES = {
      dry: { // 건성: 유분·수분 모두 부족 → 수분 하한을 낮게 잡아 "조금만 올라도" 개선으로 인정
        hydration: { optimalMin: 15, optimalMax: 45 },
        blemish: {
          minBlobBlocks: 6, rednessMargin: 4, brightnessMargin: -10,
          maxAspectRatio: 2.0, minAbsoluteRedness: 60, minSaturation: 0.30,
        },
      },
      normal: { // 중성: 유분·수분 균형 → 표준 범위(트러블 감지 기준값의 기본 베이스라인).
                // ※ 아래 값은 실사용자가 제공한 기준 사진(볼에 난 뚜렷한 빨간 뾰루지 1개)에 맞춰
                //   보정한 값 — 그 병변이 "정확히 1건"으로 잡히는 최소 기준선. 실제 병변은 볼록하게
                //   솟아 빛을 받아 오히려 주변보다 살짝 밝게 나올 수 있어(brightnessMargin이 음수인
                //   이유) "무조건 더 어두워야 한다"는 가정을 버리고 밝기 조건은 느슨하게 둠
        hydration: { optimalMin: 20, optimalMax: 55 },
        blemish: {
          minBlobBlocks: 6, rednessMargin: 4, brightnessMargin: -10,
          maxAspectRatio: 2.0, minAbsoluteRedness: 60, minSaturation: 0.30,
        },
      },
      oily: { // 지성: 유분 과다가 핵심 문제라 수분은 보통~높게 유지되면 충분 → 상한을 넉넉히.
              // 모공·피지·트러블이 잘 도드라지는 타입이라 트러블 감지는 가장 엄격하게(과잉 감지 방지 최우선).
              // ※ minBlobBlocks·rednessMargin은 기준 사진의 병변이 계속 잡히도록 dry/normal과 동일하게
              //   두고, 채도 기준만 살짝 더 엄격하게 두어 지성 특유의 잦은 오탐만 추가로 걸러냄
        hydration: { optimalMin: 15, optimalMax: 60 },
        blemish: {
          minBlobBlocks: 6, rednessMargin: 4, brightnessMargin: -10,
          maxAspectRatio: 1.8, minAbsoluteRedness: 62, minSaturation: 0.33,
        },
      },
      combination: { // 복합성: T존은 지성, 볼은 건성 → 볼(cheek) 수치를 함께 반영해 판단(judgeHydrationBySkinType에서 평균 사용).
                      // T존 유분·트러블 경향이 있어 기본보다는 살짝 엄격하게, 지성만큼 극단적이진 않게
        hydration: { optimalMin: 18, optimalMax: 50 },
        blemish: {
          minBlobBlocks: 6, rednessMargin: 4, brightnessMargin: -10,
          maxAspectRatio: 1.9, minAbsoluteRedness: 61, minSaturation: 0.32,
        },
      },
      dehydrated: { // 수부지(수분부족지성): 유분은 많아도 수분이 부족한 타입 → 하한을 상대적으로 높게 잡아
                    // "겉은 번들거려도 속수분이 낮으면" 바로 경고가 뜨도록 함(개선 1의 핵심 케이스).
                    // 지성처럼 유분·트러블이 잘 생기는 타입이라 트러블 감지는 가장 엄격한 축에 둠
        hydration: { optimalMin: 25, optimalMax: 55 },
        blemish: {
          minBlobBlocks: 6, rednessMargin: 4, brightnessMargin: -10,
          maxAspectRatio: 1.8, minAbsoluteRedness: 62, minSaturation: 0.33,
        },
      },
    };
    const DEFAULT_SKIN_TYPE = 'normal'; // 피부타입 미선택/알 수 없는 값일 때 기본으로 사용

    // 블록 단위 노이즈 제거(모폴로지 유사 효과): 이웃 블록끼리 값을 섞어(3x3 박스 블러) 모공·잡티·
    // 미세 질감처럼 "한두 블록만 튀는" 노이즈를 뭉갠다. 진짜 큰 병변은 여러 블록에 걸쳐 이미 붉고
    // 어두우므로 블러 후에도 살아남지만, 국소 잡음은 주변 값에 섞여 옅어져 걸러진다.
    const BLEMISH_BLUR_PASSES = 2; // 블러 반복 횟수(클수록 더 많이 뭉개짐 → 더 보수적)

    // 선택된 피부타입에 맞는 기준값 묶음을 반환(없으면 DEFAULT_SKIN_TYPE 기준으로 폴백)
    function getSkinTypeProfile(skinType) {
      return SKIN_TYPE_PROFILES[skinType] || SKIN_TYPE_PROFILES[DEFAULT_SKIN_TYPE];
    }

    const skinPhotoImages = { start: null, end: null }; // 업로드/촬영된 두 장의 <img> 엘리먼트 보관
    // 분석 완료된 점수 보관 (사후케어 화면에서 재계산 없이 그대로 사용): { hydration, redness, oiliness, blemishCount }
    const skinPhotoScores = { start: null, end: null };
    let skinScanTimers = []; // 분석 연출 페이지에서 예약된 모든 타이머(단계 전환용) 핸들 모음
    let skinScanStatusIntervalId = null; // "수분 분석 중…" 등 문구 로테이션 인터벌 핸들

    // 예약된 스캔 연출 타이머(+ 문구 로테이션 인터벌)를 전부 취소. 뒤로가기/다른 탭 이동/사진 재등록 시
    // 호출해 메모리 누수나 엉뚱한 시점의 화면 전환·카드 갱신을 막음
    function clearSkinScanTimers() {
      skinScanTimers.forEach((id) => clearTimeout(id));
      skinScanTimers = [];
      if (skinScanStatusIntervalId) {
        clearInterval(skinScanStatusIntervalId);
        skinScanStatusIntervalId = null;
      }
    }

    // 스캔 중 "수분 분석 중…" 같은 짧은 문구를 0.7초 간격으로 순환 표시 (과하지 않게 항목명만 교체)
    const SKIN_SCAN_STATUS_MESSAGES = ['수분 분석 중…', '톤 분석 중…', '유분 확인 중…', '트러블 확인 중…'];
    const SKIN_SCAN_STATUS_INTERVAL_MS = 700;
    function startSkinScanStatusRotation() {
      const el = document.getElementById('skinScanStatusText');
      let idx = 0;
      el.textContent = SKIN_SCAN_STATUS_MESSAGES[idx];
      skinScanStatusIntervalId = setInterval(() => {
        idx = (idx + 1) % SKIN_SCAN_STATUS_MESSAGES.length;
        el.textContent = SKIN_SCAN_STATUS_MESSAGES[idx];
      }, SKIN_SCAN_STATUS_INTERVAL_MS);
    }

    // ===== 얼굴 랜드마크 mesh 스캔 연출 (SVG) =====
    // 실제 얼굴 검출은 하지 않고, 얼굴형 사진 위에 자연스럽게 겹치도록 상대좌표(%)로
    // 미리 배치해둔 포인트들을 순차 점등시켜 "AI가 얼굴을 스캔하는" 느낌만 낸다.
    const SKIN_MESH_POINTS = [
      [50, 8], [30, 14], [70, 14],           // 0-2  이마
      [22, 26], [40, 24], [60, 24], [78, 26], // 3-6  눈썹
      [26, 38], [74, 38],                     // 7-8  눈 바깥 코너
      [50, 34],                                // 9    콧대 위
      [50, 48],                                // 10   코끝
      [34, 46], [66, 46],                     // 11-12 광대
      [50, 58],                                // 13   인중
      [36, 64], [64, 64],                     // 14-15 입꼬리
      [50, 68],                                // 16   입술 아래
      [50, 84],                                // 17   턱끝
    ];
    const SKIN_MESH_EDGES = [
      [0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 4], [4, 5], [5, 6],
      [3, 7], [6, 8], [4, 9], [5, 9], [7, 9], [8, 9], [7, 11], [8, 12],
      [9, 10], [10, 11], [10, 12], [11, 13], [12, 13], [10, 13],
      [13, 14], [13, 15], [14, 16], [15, 16], [14, 17], [15, 17], [16, 17],
      [11, 14], [12, 15],
    ];
    const SKIN_MESH_CYCLE_MS = 2400; // CSS --mesh-cycle과 일치시켜야 딜레이 계산이 맞음
    const SKIN_MESH_NODE_STEP_MS = 90; // 노드가 하나씩 점등되는 간격

    // 노드/링/엣지에 순차 딜레이를 부여한 SVG 마크업 문자열을 생성 (두 사진 오버레이에 동일하게 재사용)
    function buildFaceMeshScanSVG() {
      const nodeDelays = SKIN_MESH_POINTS.map((_, i) => i * SKIN_MESH_NODE_STEP_MS);

      const edgeMarkup = SKIN_MESH_EDGES.map(([a, b]) => {
        const [x1, y1] = SKIN_MESH_POINTS[a];
        const [x2, y2] = SKIN_MESH_POINTS[b];
        const delay = Math.max(nodeDelays[a], nodeDelays[b]) + 30;
        return `<line class="skin-scan-edge" x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" style="animation-delay:${delay}ms" />`;
      }).join('');

      const nodeMarkup = SKIN_MESH_POINTS.map(([x, y], i) => {
        const delay = nodeDelays[i];
        return (
          `<circle class="skin-scan-ring" cx="${x}" cy="${y}" r="3.2" style="animation-delay:${delay}ms" />` +
          `<circle class="skin-scan-node" cx="${x}" cy="${y}" r="1.1" style="animation-delay:${delay}ms" />`
        );
      }).join('');

      return (
        `<svg class="skin-scan-mesh-svg" viewBox="0 0 100 100" preserveAspectRatio="none" style="--mesh-cycle:${SKIN_MESH_CYCLE_MS}ms">` +
        edgeMarkup + nodeMarkup +
        `</svg>`
      );
    }

    // 두 사진 박스의 스캔 오버레이 마운트 지점에 동일한 mesh SVG를 한 번씩 심어둠
    document.querySelectorAll('.skin-scan-mesh-mount').forEach((mount) => {
      mount.innerHTML = buildFaceMeshScanSVG();
    });

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

    // ===== 피부(얼굴) 영역만 골라내는 마스킹 =====
    // 사진 전체(배경·머리카락·의류 등)를 그대로 분석하면 피부가 아닌 픽셀이 통계를 오염시켜
    // 두 사진 사이의 실제 변화가 잘 드러나지 않는다. 그래서
    // 1) 널리 쓰이는 RGB 기반 규칙으로 "피부색 후보" 픽셀을 골라내고
    // 2) 그중 가장 큰 연결 영역(=얼굴로 추정)만 남겨 이후 모든 지표 계산에 사용한다.
    function isSkinColorPixel(r, g, b) {
      const maxC = Math.max(r, g, b);
      const minC = Math.min(r, g, b);
      return (
        r > 95 && g > 40 && b > 20 &&
        maxC - minC > 15 &&
        Math.abs(r - g) > 15 &&
        r > g && r > b
      );
    }

    // 피부색 후보 픽셀 중 가장 큰 연결 성분만 1로 표시한 마스크를 반환.
    // 후보 영역이 너무 작으면(오탐 가능성이 높은 경우) 전체 이미지를 그대로 분석하는 것으로 폴백
    function extractFaceSkinMask(data, width, height) {
      const pixelCount = width * height;
      const candidate = new Uint8Array(pixelCount);
      for (let i = 0; i < pixelCount; i++) {
        const o = i * 4;
        if (isSkinColorPixel(data[o], data[o + 1], data[o + 2])) candidate[i] = 1;
      }

      const floodFill = (startIdx, visited, onVisit) => {
        const stack = [startIdx];
        visited[startIdx] = 1;
        let size = 0;
        while (stack.length) {
          const cur = stack.pop();
          size++;
          if (onVisit) onVisit(cur);
          const cx = cur % width;
          if (cx > 0 && candidate[cur - 1] && !visited[cur - 1]) { visited[cur - 1] = 1; stack.push(cur - 1); }
          if (cx < width - 1 && candidate[cur + 1] && !visited[cur + 1]) { visited[cur + 1] = 1; stack.push(cur + 1); }
          if (cur - width >= 0 && candidate[cur - width] && !visited[cur - width]) { visited[cur - width] = 1; stack.push(cur - width); }
          if (cur + width < pixelCount && candidate[cur + width] && !visited[cur + width]) { visited[cur + width] = 1; stack.push(cur + width); }
        }
        return size;
      };

      const visited = new Uint8Array(pixelCount);
      let bestStart = -1;
      let bestSize = 0;
      for (let start = 0; start < pixelCount; start++) {
        if (!candidate[start] || visited[start]) continue;
        const size = floodFill(start, visited);
        if (size > bestSize) { bestSize = size; bestStart = start; }
      }

      const mask = new Uint8Array(pixelCount);
      if (bestStart < 0 || bestSize < pixelCount * 0.03) {
        mask.fill(1); // 얼굴로 추정되는 영역을 찾지 못하면 전체 이미지를 그대로 분석(폴백)
        return { mask, bounds: { minX: 0, maxX: width - 1, minY: 0, maxY: height - 1 } };
      }
      let minX = width, maxX = 0, minY = height, maxY = 0;
      floodFill(bestStart, new Uint8Array(pixelCount), (idx) => {
        mask[idx] = 1;
        const x = idx % width, y = Math.floor(idx / width);
        if (x < minX) minX = x;
        if (x > maxX) maxX = x;
        if (y < minY) minY = y;
        if (y > maxY) maxY = y;
      });
      // 마스크 자체(엄격한 피부색 규칙)와 별도로 얼굴 영역의 대략적인 사각 범위(bounds)도 함께 반환.
      // 유분(반사광) 픽셀은 밝고 채도가 낮아 정작 "피부색" 규칙(|r-g|>15)에는 걸리지 않는 경우가 많아,
      // T존/유분 계산은 이 bounds를 기준으로 하고 엄격한 마스크에 얽매이지 않아야 함
      return { mask, bounds: { minX, maxX, minY, maxY } };
    }

    // 블록 값 배열(redness 또는 brightness)에 3x3 박스 블러를 N회 적용해 반환.
    // 모공·잡티처럼 한두 블록만 튀는 노이즈를 이웃 값과 섞어 뭉개는 전처리(노이즈 제거) 단계
    function blurBlockGrid(values, valid, cols, rows, passes) {
      let current = values;
      for (let pass = 0; pass < passes; pass++) {
        const next = new Float32Array(current.length);
        for (let by = 0; by < rows; by++) {
          for (let bx = 0; bx < cols; bx++) {
            const bi = by * cols + bx;
            if (!valid[bi]) continue;
            let sum = current[bi], count = 1;
            for (let dy = -1; dy <= 1; dy++) {
              for (let dx = -1; dx <= 1; dx++) {
                if (dx === 0 && dy === 0) continue;
                const nx = bx + dx, ny = by + dy;
                if (nx < 0 || nx >= cols || ny < 0 || ny >= rows) continue;
                const ni = ny * cols + nx;
                if (!valid[ni]) continue;
                sum += current[ni];
                count++;
              }
            }
            next[bi] = sum / count;
          }
        }
        current = next;
      }
      return current;
    }

    // 격자 블록(8x8px) 단위로 "누가 봐도 명백한, 치료가 필요할 수준"의 트러블만 매우 엄격하게 카운트.
    // 아래 4개 조건을 모두(AND) 만족하는 블록만 후보로 남기고, 이어서 인접한 블록끼리 4방향
    // flood fill로 묶어 병변 1개 단위(blob)를 구성한다.
    //   1) 크기(minBlobBlocks): 뭉친 블록 수가 이 값 이상이어야 "명백히 큰 병변"으로 인정
    //   2) 색상 대비(rednessMargin/brightnessMargin): 국소 이웃보다 뚜렷이 붉고 어두워야 함
    //   3) 형태(maxAspectRatio): 뭉친 영역의 가로/세로 비율이 이 배수를 넘으면 그림자·주름처럼
    //      "띠 모양"으로 퍼진 영역으로 보고 제외(진짜 병변은 둥글게 뭉친 형태)
    //   4) 채도·강도(minAbsoluteRedness/minSaturation): 국소 대비뿐 아니라 그 블록 자체가 절대적으로도
    //      "확실한 염증성 붉은색"이어야 함(그림자는 R·G·B가 고르게 어두워질 뿐 붉은기·채도는 낮음)
    // 판정 전, 블록 단위로 블러(blurBlockGrid)를 먼저 적용해 모공·잡티 수준의 노이즈를 제거한다.
    // blemishProfile(SKIN_TYPE_PROFILES[...].blemish)로 위 5개 기준값을 피부타입별로 조정.
    function countBlemishBlobs(data, width, height, skinMask, blemishProfile) {
      // 블록 크기 4px(기존 8px에서 축소): 작은 병변 하나가 근처의 넓은 미온성 홍조/조명 영역과
      // 4방향 인접으로 맞닿아 하나의 길쭉한 덩어리로 합쳐지는 것을 막기 위해 더 촘촘한 격자를 사용.
      // 국소 이웃 반경(neighborRadius)도 6블록(=24px)으로 늘려 기존과 동일한 물리적 이웃 범위를 유지.
      const blockSize = 4;
      const cols = Math.floor(width / blockSize);
      const rows = Math.floor(height / blockSize);
      const rawRedness = new Float32Array(cols * rows);
      const rawBrightness = new Float32Array(cols * rows);
      const blockSaturation = new Float32Array(cols * rows);
      const blockValid = new Uint8Array(cols * rows);

      for (let by = 0; by < rows; by++) {
        for (let bx = 0; bx < cols; bx++) {
          let rSum = 0, gSum = 0, bSum = 0, n = 0;
          for (let y = by * blockSize; y < by * blockSize + blockSize; y++) {
            for (let x = bx * blockSize; x < bx * blockSize + blockSize; x++) {
              const idx = y * width + x;
              if (!skinMask[idx]) continue; // 배경/머리카락 등 피부가 아닌 픽셀은 집계에서 제외
              const o = idx * 4;
              rSum += data[o]; gSum += data[o + 1]; bSum += data[o + 2];
              n++;
            }
          }
          if (n < (blockSize * blockSize) / 2) continue; // 블록 절반 이상이 피부가 아니면 신뢰하지 않고 건너뜀
          const r = rSum / n, g = gSum / n, b = bSum / n;
          const bi = by * cols + bx;
          rawRedness[bi] = r - (g + b) / 2;
          rawBrightness[bi] = (r + g + b) / 3;
          const maxC = Math.max(r, g, b), minC = Math.min(r, g, b);
          blockSaturation[bi] = maxC > 0 ? (maxC - minC) / maxC : 0; // 채도는 노이즈 제거 목적이 아니라 판정 기준이므로 블러하지 않음
          blockValid[bi] = 1;
        }
      }

      // 노이즈 제거: 모공·잡티·미세 질감 수준의 블록 단위 노이즈를 이웃과 섞어 뭉갬
      const blockRedness = blurBlockGrid(rawRedness, blockValid, cols, rows, BLEMISH_BLUR_PASSES);
      const blockBrightness = blurBlockGrid(rawBrightness, blockValid, cols, rows, BLEMISH_BLUR_PASSES);

      const neighborRadius = 6; // 반경 6블록(4px 기준 약 24px) 이내의 유효 블록들을 "국소 이웃"으로 삼음
      const flagged = new Array(cols * rows).fill(false);
      for (let by = 0; by < rows; by++) {
        for (let bx = 0; bx < cols; bx++) {
          const bi = by * cols + bx;
          if (!blockValid[bi]) continue;
          // 조건 4(채도·강도): 절대적으로도 확실한 염증성 붉은색이 아니면 이 블록은 더 볼 것도 없이 제외
          if (blockRedness[bi] < blemishProfile.minAbsoluteRedness || blockSaturation[bi] < blemishProfile.minSaturation) continue;

          let neighborRedSum = 0, neighborBrightSum = 0, neighborCount = 0;
          for (let dy = -neighborRadius; dy <= neighborRadius; dy++) {
            for (let dx = -neighborRadius; dx <= neighborRadius; dx++) {
              if (dx === 0 && dy === 0) continue;
              const nx = bx + dx, ny = by + dy;
              if (nx < 0 || nx >= cols || ny < 0 || ny >= rows) continue;
              const ni = ny * cols + nx;
              if (!blockValid[ni]) continue;
              neighborRedSum += blockRedness[ni];
              neighborBrightSum += blockBrightness[ni];
              neighborCount++;
            }
          }
          if (neighborCount < 6) continue; // 얼굴 가장자리 등 주변 정보가 너무 적으면 판정하지 않음
          const localAvgRedness = neighborRedSum / neighborCount;
          const localAvgBrightness = neighborBrightSum / neighborCount;
          // 조건 2(색상 대비): 주변보다 붉은기가 뚜렷이 높으면서 밝기는 오히려 낮은 블록만 후보로 표시
          if (blockRedness[bi] > localAvgRedness + blemishProfile.rednessMargin
            && blockBrightness[bi] < localAvgBrightness - blemishProfile.brightnessMargin) {
            flagged[bi] = true;
          }
        }
      }

      const visited = new Array(cols * rows).fill(false);
      let blobCount = 0;
      for (let idx = 0; idx < flagged.length; idx++) {
        if (!flagged[idx] || visited[idx]) continue;
        const stack = [idx];
        const region = [];
        let minBx = cols, maxBx = 0, minBy = rows, maxBy = 0;
        while (stack.length) {
          const cur = stack.pop();
          if (visited[cur] || !flagged[cur]) continue;
          visited[cur] = true;
          region.push(cur);
          const cx = cur % cols, cy = Math.floor(cur / cols);
          if (cx < minBx) minBx = cx;
          if (cx > maxBx) maxBx = cx;
          if (cy < minBy) minBy = cy;
          if (cy > maxBy) maxBy = cy;
          if (cx > 0) stack.push(cur - 1);
          if (cx < cols - 1) stack.push(cur + 1);
          if (cy > 0) stack.push(cur - cols);
          if (cy < rows - 1) stack.push(cur + cols);
        }
        // 조건 1(크기): 뭉친 블록 수가 minBlobBlocks 미만이면(작은 점) 제외
        if (region.length < blemishProfile.minBlobBlocks) continue;
        // 조건 3(형태): 뭉친 영역의 바운딩박스 가로/세로 비율이 너무 길쭉하면(그림자·주름) 제외
        const regionWidth = maxBx - minBx + 1;
        const regionHeight = maxBy - minBy + 1;
        const aspectRatio = Math.max(regionWidth, regionHeight) / Math.max(Math.min(regionWidth, regionHeight), 1);
        if (aspectRatio > blemishProfile.maxAspectRatio) continue;

        blobCount++;
      }
      return clampSkinScore(blobCount, 0, 12);
    }

    // 사진 한 장을 분석해 수분/톤·홍조/유분 점수(0~100)와 트러블 반점 개수를 반환.
    // skinType(피부타입)은 트러블 감지 민감도(countBlemishBlobs)를 타입별로 다르게 적용하는 데 사용
    function analyzeSkinPhoto(imgEl, skinType) {
      const blemishProfile = getSkinTypeProfile(skinType).blemish;
      const { data, width, height } = drawImageToAnalysisCanvas(imgEl);
      const pixelCount = width * height;
      // 배경/머리카락/의류 등을 제외한 얼굴(피부) 영역만 이후 수분·톤/홍조·트러블 지표 계산에 사용
      const { mask: skinMask, bounds } = extractFaceSkinMask(data, width, height);

      // 유분(T존) 측정 대상 영역: 얼굴로 추정된 사각 범위(bounds) 안에서 이마+콧대를 근사한
      // 상단·중앙 영역 (실제 얼굴 landmark가 없으므로 얼굴 bounds 대비 위치 비율로 근사).
      // ※ 반사광(번들거림) 픽셀은 밝고 채도가 낮아 정작 엄격한 "피부색" 규칙(|r-g|>15)에는
      //   걸리지 않는 경우가 많으므로, 여기서는 skinMask가 아니라 이 bounds만 기준으로 삼는다
      const faceWidth = Math.max(bounds.maxX - bounds.minX, 1);
      const faceHeight = Math.max(bounds.maxY - bounds.minY, 1);
      const tZoneTop = bounds.minY + faceHeight * 0.08;
      const tZoneBottom = bounds.minY + faceHeight * 0.55;
      const tZoneLeft = bounds.minX + faceWidth * 0.2;
      const tZoneRight = bounds.minX + faceWidth * 0.8;

      // 볼(cheeks) 측정 대상 영역: T존 아래쪽, 좌우 양볼 부분을 근사(코·입 주변 중앙은 제외).
      // 피부타입별 유분 판정(judgeOilinessBySkinType)에서 "T존은 번들거려도 볼은 촉촉/건조한지"를
      // 함께 봐야 하는 복합성·수부지 규칙에 사용
      const cheekTop = bounds.minY + faceHeight * 0.45;
      const cheekBottom = bounds.minY + faceHeight * 0.75;
      const cheekLeftMin = bounds.minX + faceWidth * 0.05;
      const cheekLeftMax = bounds.minX + faceWidth * 0.32;
      const cheekRightMin = bounds.minX + faceWidth * 0.68;
      const cheekRightMax = bounds.minX + faceWidth * 0.95;
      const isInCheekZone = (x, y) => y >= cheekTop && y <= cheekBottom
        && ((x >= cheekLeftMin && x <= cheekLeftMax) || (x >= cheekRightMin && x <= cheekRightMax));

      let brightnessSum = 0;
      let rNormSum = 0;
      let skinPixelCount = 0;
      let oilyPixelCount = 0;
      let tZonePixelCount = 0;
      let cheekOilyPixelCount = 0;
      let cheekPixelCount = 0;
      const brightness = new Float32Array(pixelCount);

      for (let y = 0; y < height; y++) {
        for (let x = 0; x < width; x++) {
          const i = y * width + x;
          const o = i * 4;
          const r = data[o], g = data[o + 1], b = data[o + 2];
          const bright = (r + g + b) / 3;
          brightness[i] = bright; // 경계 그레디언트 계산을 위해 마스크 여부와 무관하게 전체를 채워둠

          // 유분 지표: 밝고(반사광) 채도가 낮은(번들거리는) 픽셀 비율 — T존·볼 각각 집계
          const maxC = Math.max(r, g, b);
          const minC = Math.min(r, g, b);
          const saturation = maxC === 0 ? 0 : (maxC - minC) / maxC;
          const isOilyPixel = bright > 190 && saturation < 0.18;

          if (x >= tZoneLeft && x <= tZoneRight && y >= tZoneTop && y <= tZoneBottom) {
            tZonePixelCount++;
            if (isOilyPixel) oilyPixelCount++;
          }
          if (isInCheekZone(x, y)) {
            cheekPixelCount++;
            if (isOilyPixel) cheekOilyPixelCount++;
          }

          if (!skinMask[i]) continue; // 수분·톤/홍조·트러블 통계는 피부(얼굴) 영역만 집계
          skinPixelCount++;
          brightnessSum += bright;
          // 톤·홍조 지표: R 채널의 상대 비중(r-chromaticity, r/(r+g+b)).
          // 밝기(노출)가 달라져도 채널 "비율"은 거의 변하지 않아, 사진마다 밝기가 다른
          // 두 장을 비교할 때도 광원 보정 없이 안정적으로 붉은기만 비교할 수 있음
          const channelSum = r + g + b;
          if (channelSum > 0) rNormSum += r / channelSum;
        }
      }

      const avgBrightness = brightnessSum / Math.max(skinPixelCount, 1);
      const avgRNorm = rNormSum / Math.max(skinPixelCount, 1);
      // 조명(전체 밝기) 편차를 보정하기 위한 정규화 비율 (기준 밝기 128 대비) — 수분(질감) 지표에만 사용
      const lightingFactor = clampSkinScore(128 / Math.max(avgBrightness, 1), 0.6, 1.6);

      // 수분(hydration): 인접 픽셀 간 밝기 변화(엣지 밀도)로 표면 질감을 근사.
      // 요철·각질이 많을수록 엣지가 많아져 매끈함(수분감) 점수는 낮아짐.
      // 얼굴 윤곽선(피부↔배경/머리카락 경계)이 만드는 가짜 엣지가 섞이지 않도록,
      // 자기 자신과 4방향 이웃이 모두 피부 영역인 픽셀만 집계 대상으로 삼음.
      // 같은 루프에서 볼 영역만의 엣지 밀도도 함께 집계해 "볼 건조도"(cheekHydration)를 구함
      let edgeSum = 0;
      let edgeSamples = 0;
      let cheekEdgeSum = 0;
      let cheekEdgeSamples = 0;
      for (let y = 1; y < height - 1; y++) {
        for (let x = 1; x < width - 1; x++) {
          const idx = y * width + x;
          if (!skinMask[idx] || !skinMask[idx - 1] || !skinMask[idx + 1] || !skinMask[idx - width] || !skinMask[idx + width]) continue;
          const dx = brightness[idx + 1] - brightness[idx - 1];
          const dy = brightness[idx + width] - brightness[idx - width];
          const edge = Math.sqrt(dx * dx + dy * dy);
          edgeSum += edge;
          edgeSamples++;
          if (isInCheekZone(x, y)) {
            cheekEdgeSum += edge;
            cheekEdgeSamples++;
          }
        }
      }
      const avgEdge = edgeSamples > 0 ? (edgeSum / edgeSamples) * lightingFactor : 0;
      const hydration = clampSkinScore(100 - avgEdge * 3.2, 0, 100); // 경험적 스케일링 상수
      const cheekAvgEdge = cheekEdgeSamples > 0 ? (cheekEdgeSum / cheekEdgeSamples) * lightingFactor : 0;
      const cheekHydration = clampSkinScore(100 - cheekAvgEdge * 3.2, 0, 100);

      // 톤·홍조 점수: r-chromaticity 기준 baseline(0.36, 중립 살빛 하한 근처)보다 얼마나 붉은 쪽으로
      // 치우쳤는지를 0~100으로 스케일링. (이전에는 원본 R 우세치에 조명 보정 배율을 곱했는데, 사진이
      // 조금만 어두워도 배율이 겹쳐 거의 모든 사진이 100점에 붙어버려 비교가 무의미했음)
      const redness = clampSkinScore((avgRNorm - 0.36) * 400, 0, 100);
      const oiliness = clampSkinScore((oilyPixelCount / Math.max(tZonePixelCount, 1)) * 150, 0, 100);
      const cheekOiliness = clampSkinScore((cheekOilyPixelCount / Math.max(cheekPixelCount, 1)) * 150, 0, 100);
      const blemish = countBlemishBlobs(data, width, height, skinMask, blemishProfile);

      return { hydration, redness, oiliness, blemish, cheekOiliness, cheekHydration };
    }

    // dataURL(카메라 캡처 또는 파일 선택 결과)을 미리보기에 채우고, 양쪽 사진이 모두 채워지면 자동 분석 실행
    function applySkinPhoto(kind, dataUrl) {
      const img = new Image();
      img.onload = () => {
        skinPhotoImages[kind] = img;
        const boxEl = document.getElementById(kind === 'start' ? 'skinPhotoStartBox' : 'skinPhotoEndBox');
        const previewEl = document.getElementById(kind === 'start' ? 'skinPhotoStartPreview' : 'skinPhotoEndPreview');
        const placeholderEl = document.getElementById(kind === 'start' ? 'skinPhotoStartPlaceholder' : 'skinPhotoEndPlaceholder');
        const retakeBtnEl = document.getElementById(kind === 'start' ? 'skinPhotoStartRetakeBtn' : 'skinPhotoEndRetakeBtn');
        previewEl.src = dataUrl;
        previewEl.classList.remove('hidden');
        placeholderEl.classList.add('hidden');
        retakeBtnEl.classList.remove('hidden'); // 사진 등록 후에는 "다시 선택" 버튼을 노출해 재등록 가능하게 함
        // 사진이 등록되면 등록 전의 세로로 긴 칸(h-[38vh]) 대신 정사각형으로 표시(center-crop은 object-cover가 처리)
        boxEl.classList.remove('h-[38vh]');
        boxEl.classList.add('aspect-square');
        updateSkinPhotoRegCardState(kind);
        updateSkinPhotoLayoutPhase();
        updateSkinPhotoHint();
        updateSkinChangeEmptyState();
        updateSkinChangeSectionVisibility();
        if (skinPhotoImages.start && skinPhotoImages.end) {
          runSkinPhotoAnalysis();
        }
      };
      img.src = dataUrl;
    }

    // 사진 등록 페이지(출국·입국 도장 카드)의 각 카드 상태를 등록 여부에 따라 갱신.
    // 사진이 등록되면 아이콘 대신 실제 사진을 카드 전체에 채워 보여주고(center-crop),
    // 제목·안내 문구는 사진 위에서도 잘 보이도록 어두운 스크림 + 흰 글자로 전환
    function updateSkinPhotoRegCardState(kind) {
      const hintEl = document.getElementById(kind === 'start' ? 'skinPhotoStartRegHint' : 'skinPhotoEndRegHint');
      const titleEl = document.getElementById(kind === 'start' ? 'skinPhotoStartRegTitle' : 'skinPhotoEndRegTitle');
      const iconEl = document.getElementById(kind === 'start' ? 'skinPhotoStartRegIcon' : 'skinPhotoEndRegIcon');
      const previewEl = document.getElementById(kind === 'start' ? 'skinPhotoStartRegPreview' : 'skinPhotoEndRegPreview');
      const scrimEl = document.getElementById(kind === 'start' ? 'skinPhotoStartRegScrim' : 'skinPhotoEndRegScrim');
      const hasPhoto = !!skinPhotoImages[kind];

      hintEl.textContent = hasPhoto ? '등록 완료 · 다시 탭하면 변경' : '탭해서 사진 등록하기';
      iconEl.classList.toggle('hidden', hasPhoto);
      previewEl.classList.toggle('hidden', !hasPhoto);
      scrimEl.classList.toggle('hidden', !hasPhoto);
      if (hasPhoto) previewEl.src = skinPhotoImages[kind].src;

      titleEl.classList.toggle('text-gray-900', !hasPhoto);
      titleEl.classList.toggle('text-white', hasPhoto);
      hintEl.classList.toggle('text-gray-400', !hasPhoto);
      hintEl.classList.toggle('text-white/90', hasPhoto);
    }

    // 두 사진이 모두 등록되기 전에는 "사진 등록 페이지"(여권 헤더 + 출국·입국 도장 카드)를,
    // 모두 등록된 뒤에는 "리포트" 화면(기존 그대로)을 노출 — 서로 배타적으로 전환
    function updateSkinPhotoLayoutPhase() {
      const bothRegistered = !!(skinPhotoImages.start && skinPhotoImages.end);
      document.getElementById('skinRegisterPageLayout').classList.toggle('hidden', bothRegistered);
      document.getElementById('skinReportPageLayout').classList.toggle('hidden', !bothRegistered);
    }

    // (폴백 경로) 파일 선택창에서 고른 파일을 읽어 applySkinPhoto로 전달
    function loadSkinPhoto(kind, file) {
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => applySkinPhoto(kind, reader.result);
      reader.readAsDataURL(file);
    }

    function updateSkinPhotoHint() {
      // 리포트 화면(skinReportPageLayout) 안내 문구 — 두 사진이 모두 등록됐을 때만 노출되므로 그대로 유지
      const hintEl = document.getElementById('skinPhotoHint');
      const count = (skinPhotoImages.start ? 1 : 0) + (skinPhotoImages.end ? 1 : 0);
      if (count >= 2) {
        hintEl.textContent = '✓ 두 사진을 비교해 아래 리포트를 갱신했어요';
      } else if (count === 1) {
        hintEl.textContent = '나머지 한 장을 더 등록해 주세요';
      } else {
        hintEl.textContent = '→ 사진을 첨부하면 AI가 두 사진을 비교해 분석해드려요';
      }

      // 사진 등록 페이지(여권 헤더 + 출국·입국 도장 카드) 하단 안내 문구
      const registerHintEl = document.getElementById('skinPhotoRegisterHint');
      if (count === 1) {
        registerHintEl.textContent = '나머지 한 장을 더 등록해 주세요';
      } else {
        registerHintEl.innerHTML = '출국·입국 도장을 찍으면 <span class="font-semibold text-gray-600">피부 여정 심사</span>가 시작돼요';
      }
    }

    // "항목별 변화" 빈 상태 안내: 등록된 사진 개수(0/1/2장)에 따라 문구를 갱신.
    // 두 장이 모두 채워지면 이 안내는 숨기고 스캔 연출(beginSkinScan)로 넘어감
    function updateSkinChangeEmptyState() {
      // 두 사진이 모두 등록되기 전에는 이 안내 자체를 숨김 — "나머지 한 장" 안내는
      // 바로 위 #skinPhotoHint가 이미 하고 있어 중복 표시하지 않음
      const emptyEl = document.getElementById('skinChangeEmptyState');
      const count = (skinPhotoImages.start ? 1 : 0) + (skinPhotoImages.end ? 1 : 0);
      if (count < 2) {
        emptyEl.classList.add('hidden');
        return;
      }
      emptyEl.classList.remove('hidden');
      emptyEl.innerHTML = '1일차 사진과 마지막날 사진을 등록하면<br />항목별 분석 결과가 여기에 표시됩니다.';
    }

    // "항목별 변화" 제목, "리포트 저장하기"·"내 피부 사후관리하기" 버튼은 두 사진이 모두
    // 등록되기 전에는 DOM에서 숨김
    function updateSkinChangeSectionVisibility() {
      const bothRegistered = !!(skinPhotoImages.start && skinPhotoImages.end);
      document.getElementById('skinChangeSectionTitle').classList.toggle('hidden', !bothRegistered);
      document.getElementById('saveSkinReportBtn').classList.toggle('hidden', !bothRegistered);
      document.getElementById('goToAftercareBtn').classList.toggle('hidden', !bothRegistered);
    }

    document.getElementById('skinPhotoStartInput').addEventListener('change', (e) => {
      loadSkinPhoto('start', e.target.files[0]);
    });
    document.getElementById('skinPhotoEndInput').addEventListener('change', (e) => {
      loadSkinPhoto('end', e.target.files[0]);
    });

    // 사진 등록 페이지(출국·입국 도장 카드) 탭: 등록 전/후 관계없이 항상 파일 선택창을 염
    // (다시 탭하면 사진을 바로 교체할 수 있음 — 별도의 "다시 선택" 버튼이 필요 없는 단순한 등록 전용 화면)
    document.getElementById('skinPhotoStartRegBox').addEventListener('click', () => {
      document.getElementById('skinPhotoStartInput').click();
    });
    document.getElementById('skinPhotoEndRegBox').addEventListener('click', () => {
      document.getElementById('skinPhotoEndInput').click();
    });

    // 사진 박스 탭: 아직 등록 전이면 파일 선택창을, 이미 등록된 사진이 있으면 라이트박스(확대)를 염
    document.getElementById('skinPhotoStartBox').addEventListener('click', () => {
      if (skinPhotoImages.start) {
        openSkinPhotoLightbox('start');
      } else {
        document.getElementById('skinPhotoStartInput').click();
      }
    });
    document.getElementById('skinPhotoEndBox').addEventListener('click', () => {
      if (skinPhotoImages.end) {
        openSkinPhotoLightbox('end');
      } else {
        document.getElementById('skinPhotoEndInput').click();
      }
    });

    // "다시 선택" 버튼: 이미 등록된 사진이어도 파일 선택창을 다시 열어 교체할 수 있게 함.
    // 상위 사진 박스 버튼(라이트박스 확대)으로 클릭이 전달되지 않도록 stopPropagation 처리
    document.getElementById('skinPhotoStartRetakeBtn').addEventListener('click', (e) => {
      e.stopPropagation();
      document.getElementById('skinPhotoStartInput').click();
    });
    document.getElementById('skinPhotoEndRetakeBtn').addEventListener('click', (e) => {
      e.stopPropagation();
      document.getElementById('skinPhotoEndInput').click();
    });

    // 결과 페이지 사진 확대 라이트박스: 원본 비율 그대로(object-contain) 크게 표시
    function openSkinPhotoLightbox(kind) {
      document.getElementById('skinPhotoLightboxImage').src = skinPhotoImages[kind].src;
      document.getElementById('skinPhotoLightbox').classList.remove('hidden');
    }
    function closeSkinPhotoLightbox() {
      document.getElementById('skinPhotoLightbox').classList.add('hidden');
    }
    document.getElementById('skinPhotoLightboxCloseBtn').addEventListener('click', closeSkinPhotoLightbox);
    document.getElementById('skinPhotoLightbox').addEventListener('click', (e) => {
      // 배경(빈 공간) 탭으로도 닫히게 하되, 사진/닫기 버튼 자체를 누른 경우는 그대로 둠
      if (e.target.id === 'skinPhotoLightbox') {
        closeSkinPhotoLightbox();
      }
    });

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

    // 온보딩 1단계에서 선택한 피부타입을 그대로 읽어옴('.skin-btn.active'의 data-skin 값).
    // 이미 정해진 값을 그대로 신뢰하며, 사진을 보고 재판정하지 않음
    function getSelectedSkinType() {
      const btn = document.querySelector('.skin-btn.active');
      return btn ? btn.dataset.skin : null; // 'dry' | 'normal' | 'oily' | 'combination' | 'dehydrated' | null(미선택)
    }

    // ===== 유분(T존·볼) 판정: 피부타입을 "절대 기준"으로 삼아 해석 =====
    // 유분은 "오르면 무조건 나쁨"이 아니라 피부타입별 목표 범위에 가까워졌는지로 판단해야 함.
    // 예) 건성은 유분이 늘어야 개선, 지성은 줄어야 개선. 복합성·수부지는 T존과 볼을 따로 봐야
    // (T존만 좋아지고 볼이 건조해지면 오히려 관리가 필요한 상태) 두 부위를 함께 참고해 판정한다.
    function judgeOilinessBySkinType(skinType, s, e) {
      const THRESHOLD = 5; // 이 범위 이내 변화는 "변화 없음"으로 간주
      const noChange = (delta) => Math.abs(delta) <= THRESHOLD;
      const tzoneDelta = e.oiliness - s.oiliness; // T존 유분 변화(+면 번들거림 증가)
      const cheekHydrationDelta = e.cheekHydration - s.cheekHydration; // -면 볼이 더 건조해짐(과교정 신호)

      if (skinType === 'dry') {
        // 건성: 유분 부족이 문제 → 유분이 올라야 개선, 그대로거나 더 줄면 악화
        if (noChange(tzoneDelta)) return { status: '유지', color: 'gray', desc: '유분감은 1일차와 큰 차이가 없어요. 건성 피부는 유분이 조금 더 올라오면 훨씬 편안해질 거예요.' };
        if (tzoneDelta > 0) return { status: '개선', color: 'green', desc: '유분과 윤기가 살아나 건성 피부 특유의 푸석함이 줄어든 것으로 보여요.' };
        return { status: '악화', color: 'red', desc: '유분이 더 줄어 건조함이 심해진 것으로 보여요. 고보습 크림과 오일류 제품을 더 챙겨보세요.' };
      }

      if (skinType === 'oily') {
        // 지성: 유분 과다가 문제 → T존 유분이 내려가면 개선. 단, 볼까지 매트/건조해지는 과교정은 주의
        if (tzoneDelta < -THRESHOLD) {
          if (cheekHydrationDelta < -THRESHOLD) {
            return { status: '주의', color: 'amber', desc: 'T존 번들거림은 줄었지만 볼까지 건조해진 과교정 신호가 보여요. 유수분 밸런스 제품으로 조절해보세요.' };
          }
          return { status: '개선', color: 'green', desc: 'T존 번들거림이 가라앉아 지성 피부의 유분이 안정된 것으로 보여요.' };
        }
        if (noChange(tzoneDelta)) return { status: '유지', color: 'gray', desc: 'T존 유분은 1일차와 큰 차이가 없어요.' };
        return { status: '악화', color: 'red', desc: 'T존 번들거림이 늘었어요. 피지 흡수 시트나 매트 선크림을 사용해 유분을 관리해보세요.' };
      }

      if (skinType === 'normal') {
        // 중성: 이미 균형 잡힌 상태 → 유지가 목표, 큰 변화 자체가 오히려 악화 신호
        if (noChange(tzoneDelta)) return { status: '유지', color: 'gray', desc: '유분 밸런스가 1일차와 비슷하게 잘 유지됐어요.' };
        return { status: '악화', color: 'red', desc: '유분 밸런스가 여행 전보다 크게 흔들렸어요. 평소 스킨케어 루틴으로 되돌아가 보세요.' };
      }

      if (skinType === 'combination') {
        // 복합성: T존과 볼을 따로 판단 — T존이 좋아져도 볼이 건조해지면 전체적으론 악화로 봄
        if (cheekHydrationDelta < -THRESHOLD) {
          return { status: '악화', color: 'red', desc: 'T존은 안정됐지만 볼이 건조해진 것으로 보여요. 복합성 피부는 볼 위주로 수분크림을 더 챙겨보세요.' };
        }
        if (tzoneDelta < -THRESHOLD) return { status: '개선', color: 'green', desc: 'T존 번들거림이 줄고 볼은 촉촉함을 유지해 유분 밸런스가 좋아졌어요.' };
        if (noChange(tzoneDelta)) return { status: '유지', color: 'gray', desc: 'T존·볼 유분 모두 1일차와 큰 차이가 없어요.' };
        return { status: '악화', color: 'red', desc: 'T존 번들거림이 늘었어요. T존 위주로 피지 관리를 해보세요.' };
      }

      if (skinType === 'dehydrated') {
        // 수부지: 겉은 번들거려도 속은 수분 부족 → T존 유분만 보지 말고 볼 수분도 함께 확인
        if (tzoneDelta < -THRESHOLD && cheekHydrationDelta < -THRESHOLD) {
          return { status: '주의', color: 'amber', desc: 'T존은 안정됐지만 볼까지 당길 만큼 건조해졌어요. 유분보다 수분 보충이 더 필요해 보여요.' };
        }
        if (tzoneDelta < -THRESHOLD) return { status: '개선', color: 'green', desc: 'T존 번들거림은 가라앉고 볼 수분은 유지돼 속당김 없이 편안해진 것으로 보여요.' };
        if (noChange(tzoneDelta)) return { status: '유지', color: 'gray', desc: 'T존 유분은 1일차와 큰 차이가 없어요.' };
        return { status: '악화', color: 'red', desc: 'T존 번들거림이 늘었어요. 수분을 먼저 채운 뒤 가벼운 유분 제품으로 마무리해보세요.' };
      }

      // 피부타입이 선택되지 않은 경우(온보딩을 건너뛴 예외 상황)의 폴백: 단순 증감으로만 판단
      if (noChange(tzoneDelta)) return { status: '유지', color: 'gray', desc: 'T존 유분은 1일차와 큰 차이가 없어요.' };
      if (tzoneDelta > 0) return { status: '악화', color: 'red', desc: 'T존 반사광이 늘어 유분이 증가한 것으로 보여요.' };
      return { status: '개선', color: 'green', desc: 'T존 번들거림이 줄어 유분이 안정된 것으로 보여요.' };
    }

    // 값이 [min, max] 적정 범위의 어느 쪽에 있는지와 범위 밖이라면 얼마나 벗어났는지(gap)를 반환
    function classifyHydrationZone(value, min, max) {
      if (value < min) return { zone: 'low', gap: min - value };
      if (value > max) return { zone: 'high', gap: value - max };
      return { zone: 'optimal', gap: 0 };
    }

    // ===== 수분 판정: "높을수록 좋음"이 아니라 피부타입별 "적정 범위"에 가까울수록 좋음 =====
    // 너무 건조해도, 너무 과수분(끈적임에 가까운 상태)이어도 좋지 않다는 전제로 판정.
    // 복합성은 T존/볼 부위 편차가 특징이므로 전체 얼굴 수치와 볼(cheek) 수치의 평균으로 판단.
    // 수부지는 "유분↑ + 수분↓" 조합을 별도로 감지해 수분 보충을 핵심 안내로 강조(개선 1의 핵심 케이스)
    function judgeHydrationBySkinType(skinType, s, e) {
      const profile = getSkinTypeProfile(skinType).hydration;
      const GAP_THRESHOLD = 3; // 적정 범위 밖에서의 거리(gap) 변화가 이 이내면 "변화 없음"으로 간주

      // 복합성: 전체 얼굴 수치만으로는 "T존 지성·볼 건성"의 부위별 편차를 반영할 수 없으므로
      // 얼굴 전체 수치와 볼(cheek) 수치의 평균을 대표값으로 사용(부위별 샘플링 평균)
      const pickValue = (v) => (skinType === 'combination' ? (v.hydration + v.cheekHydration) / 2 : v.hydration);
      const startVal = pickValue(s);
      const endVal = pickValue(e);

      // 수부지 전용: 유분은 늘고 수분은 뚜렷이 줄어드는 "수분 부족형" 조합을 최우선으로 감지
      if (skinType === 'dehydrated') {
        const oilinessUp = (e.oiliness - s.oiliness) > GAP_THRESHOLD;
        const hydrationDown = (endVal - startVal) < -GAP_THRESHOLD;
        if (oilinessUp && hydrationDown) {
          return {
            status: '주의',
            color: 'amber',
            desc: '유분은 늘고 수분은 줄어드는 "수분 부족형" 신호가 보여요. 유분 케어보다 수분 보충(수분크림·수분 미스트)을 먼저 챙겨보세요.',
          };
        }
      }

      const startZone = classifyHydrationZone(startVal, profile.optimalMin, profile.optimalMax);
      const endZone = classifyHydrationZone(endVal, profile.optimalMin, profile.optimalMax);

      if (endZone.zone === 'optimal') {
        if (startZone.zone === 'optimal') {
          return { status: '유지', color: 'gray', desc: '수분감이 적정 범위 안에서 안정적으로 유지되고 있어요.' };
        }
        return { status: '개선', color: 'green', desc: '수분감이 적정 범위 안으로 들어와 훨씬 편안해진 상태예요.' };
      }

      // 적정 범위 밖: 방향(건조/과수분)에 따라 문구를 다르게 하고, 범위에 더 가까워졌는지(개선)
      // 더 멀어졌는지(악화)를 gap(범위와의 거리) 변화로 판단
      const direction = endZone.zone === 'low' ? '건조' : '과수분';
      const tip = endZone.zone === 'low' ? '보습 케어(수분크림·팩)를 늘려보세요.' : '가벼운 제형으로 바꾸고 유수분 밸런스를 맞춰보세요.';

      if (startZone.zone !== endZone.zone) {
        // 반대쪽(건조↔과수분)으로 범위를 넘나든 경우는 gap 비교가 무의미하므로 악화로 간주
        return { status: '악화', color: 'red', desc: `${direction} 쪽으로 상태가 바뀌었어요. ${tip}` };
      }
      if (endZone.gap < startZone.gap - GAP_THRESHOLD) {
        return { status: '개선', color: 'green', desc: `아직 적정 범위는 아니지만 ${direction} 상태에서 벗어나며 좋아지고 있어요.` };
      }
      if (endZone.gap > startZone.gap + GAP_THRESHOLD) {
        return { status: '악화', color: 'red', desc: `${direction} 상태가 더 심해졌어요. ${tip}` };
      }
      return { status: '주의', color: 'amber', desc: `${direction} 상태가 계속되고 있어요. ${tip}` };
    }

    // 여러 항목명을 자연스러운 한국어 나열로 합침 (예: ['수분','유분'] → "수분·유분")
    function joinKoreanList(labels) {
      return labels.join('·');
    }

    // 수분/톤·홍조/유분/트러블 4가지 항목의 배지 판정 결과를 종합해 최종 "종합 요약" 문구를 생성.
    // 개별 카드 설명은 항목별로 따로 있으므로, 여기서는 4개 항목을 한 번에 놓고 본 전체 총평만 담당함
    function buildSkinReportSummary(hydrationBadge, rednessBadge, oilinessBadge, blemishBadge) {
      const improved = [];
      const worsened = [];
      if (hydrationBadge.label === '개선됨') improved.push('수분');
      else if (hydrationBadge.label === '주의 필요' || hydrationBadge.label === '악화') worsened.push('수분');
      if (rednessBadge.label === '개선됨') improved.push('톤·홍조');
      else if (rednessBadge.label === '주의 필요') worsened.push('톤·홍조');
      if (oilinessBadge.label === '개선됨') improved.push('유분');
      else if (oilinessBadge.label === '주의 필요' || oilinessBadge.label === '악화') worsened.push('유분');
      if (blemishBadge.color === 'green') improved.push('트러블');
      else if (blemishBadge.color === 'red') worsened.push('트러블');

      if (improved.length === 0 && worsened.length === 0) {
        return '수분·톤/홍조·유분·트러블 4가지 항목 모두 1일차와 큰 차이 없이 안정적인 상태를 유지했어요.';
      }
      if (worsened.length === 0) {
        return `${joinKoreanList(improved)} 항목이 좋아지며 전반적으로 피부 컨디션이 개선됐어요. 지금 하고 있는 관리 루틴을 여행 후에도 계속 이어가 보세요.`;
      }
      if (improved.length === 0) {
        return `${joinKoreanList(worsened)} 항목에서 다소 신경 쓰이는 변화가 감지됐어요. 자외선 차단과 보습 위주로 관리해보면 좋을 것 같아요.`;
      }
      return `${joinKoreanList(improved)} 항목은 좋아졌지만 ${joinKoreanList(worsened)} 항목은 아직 신경 쓰이는 변화가 있어요. 좋아진 루틴은 유지하면서 나머지 항목 위주로 관리해보세요.`;
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
      // 선택된 피부타입을 한 번만 읽어 두 사진 분석에 동일하게 적용(트러블 감지 민감도 등)
      const skinType = getSelectedSkinType();
      const startScores = analyzeSkinPhoto(skinPhotoImages.start, skinType);
      const endScores = analyzeSkinPhoto(skinPhotoImages.end, skinType);
      // 사후케어 화면(#screen-aftercare)에서 그대로 쓸 수 있도록 반올림해 보관 (blemish → blemishCount로 이름만 맞춤)
      skinPhotoScores.start = { hydration: Math.round(startScores.hydration), redness: Math.round(startScores.redness), oiliness: Math.round(startScores.oiliness), blemishCount: Math.round(startScores.blemish) };
      skinPhotoScores.end = { hydration: Math.round(endScores.hydration), redness: Math.round(endScores.redness), oiliness: Math.round(endScores.oiliness), blemishCount: Math.round(endScores.blemish) };
      beginSkinScan(startScores, endScores);
    }

    // 사진 두 장 위에 스캔 연출(반투명 오버레이 + 격자/mesh/스캔라인/코너)을 재생한 뒤 결과 카드를 드러냄.
    // 이미 결과가 표시된 상태에서 사진을 다시 등록해도 이 함수가 다시 호출되므로 스캔 연출부터 재생됨
    // 분석 연출 페이지 타이밍 상수 (필요시 조절) — 분석 로직·결과 렌더링과 무관, 연출 타이밍만 담당
    const SCAN_DURATION_MS = 5000; // 연출 페이지 진입 ~ 결과 페이지 전환까지 총 시간
    const SCAN_DAY1_HOLD_MS = 1200; // 1일차 사진이 혼자 보이는 시간(이후 마지막날 사진이 반투명하게 오버레이됨)
    const SCAN_SETTLE_MS = 600; // 결과 전환 직전, 반투명 오버레이를 다시 또렷하게 정리하는 시간

    // 두 사진이 모두 등록되면 "분석 연출 페이지"로 전환해 1일차 사진 페이드인 → 마지막날 사진가
    // 반투명하게 겹쳐(비교 느낌) 오버레이 → 격자/얼굴 mesh/스캔 라인/코너 프레임 스캔 연출 →
    // 종료 직전 또렷하게 정리 → 결과 페이지로 전환. 실제 분석(analyzeSkinPhoto)은 이미 끝난 상태이므로
    // 이 함수는 순전히 연출/타이밍만 담당.
    function beginSkinScan(startScores, endScores) {
      clearSkinScanTimers(); // 이미 결과가 표시된 상태에서 사진을 다시 등록해도 처음부터 재생되도록 기존 타이머 정리

      const day1El = document.getElementById('skinScanDay1Image');
      const day2El = document.getElementById('skinScanDay2Image');
      const meshOverlay = document.getElementById('skinScanMeshOverlay');
      const progressBar = document.getElementById('skinScanProgressBar');

      day1El.src = skinPhotoImages.start.src;
      day2El.src = skinPhotoImages.end.src;
      day1El.classList.remove('skin-scan-fade-in');
      day2El.classList.remove('skin-scan-fade-in', 'skin-scan-overlay-active', 'skin-scan-settle');
      meshOverlay.classList.add('hidden');
      document.getElementById('skinScanStatusText').textContent = ' ';
      progressBar.style.setProperty('--scan-duration', `${SCAN_DURATION_MS}ms`);
      // 진행바 애니메이션을 처음부터 다시 재생하기 위해 강제로 리플로우시켜 재시작을 보장
      progressBar.style.animation = 'none';
      void progressBar.offsetWidth;
      progressBar.style.animation = '';

      switchTab('skinScan');

      skinScanTimers.push(setTimeout(() => {
        day1El.classList.add('skin-scan-fade-in');
      }, 30));

      skinScanTimers.push(setTimeout(() => {
        // 1일차 사진 위에 마지막날 사진을 반투명하게 오버레이(왕복 pulse)해 두 시점이 겹쳐 비쳐 보이게 함
        day2El.classList.add('skin-scan-overlay-active');
        meshOverlay.classList.remove('hidden'); // 격자 + mesh + 스캔라인 + 코너 프레임 스캔 연출 시작
        startSkinScanStatusRotation();
      }, SCAN_DAY1_HOLD_MS));

      skinScanTimers.push(setTimeout(() => {
        // 결과로 넘어가기 직전, 반투명 왕복을 멈추고 마지막날 사진을 다시 또렷하게 정리
        day2El.classList.remove('skin-scan-overlay-active');
        day2El.classList.add('skin-scan-settle');
      }, SCAN_DURATION_MS - SCAN_SETTLE_MS));

      skinScanTimers.push(setTimeout(() => {
        switchTab('skinReport');
        showSkinReportResults(startScores, endScores);
      }, SCAN_DURATION_MS));
    }

    // 분석 연출이 끝난 뒤 "피부 변화 리포트" 화면에 결과 카드 + 종합 요약을 바로 노출
    function showSkinReportResults(startScores, endScores) {
      document.getElementById('skinChangeEmptyState').classList.add('hidden');
      renderSkinChangeCards(startScores, endScores);
      const cardsEl = document.getElementById('skinChangeCards');
      cardsEl.classList.remove('hidden');
      cardsEl.classList.add('skin-fade-in');
      const summaryBoxEl = document.getElementById('skinReportSummaryBox');
      summaryBoxEl.classList.remove('hidden');
      summaryBoxEl.classList.add('skin-fade-in');
    }

    // 분석된 1일차/마지막날 점수로 "항목별 변화" 카드 4개 + 종합 요약을 동적으로 갱신
    // 피부타입(건성/지성 등)에 따라 문구를 다르게 서술하는 설명 생성기.
    // 판정(배지) 자체는 공통 임계값 로직을 그대로 쓰되, 설명 문구만 선택된 피부타입 맥락에 맞게 조정
    function buildHydrationDesc(skinType, badge) {
      if (badge.label === '개선됨') {
        return skinType === 'dry'
          ? '표면이 매끈해지고 수분감이 올라갔어요. 건성 피부에서는 특히 반가운 변화예요.'
          : '사진 비교 결과 표면이 매끈해져 수분감이 올라간 것으로 보여요.';
      }
      if (badge.label === '주의 필요') {
        if (skinType === 'dry') return '표면 텍스처가 거칠어져 수분감이 더 떨어졌어요. 건성 피부는 수분 손실에 특히 취약하니 고보습 크림을 꼭 챙겨보세요.';
        if (skinType === 'oily') return '표면 결이 거칠어졌어요. 유분과는 별개로 속수분이 부족해진 신호일 수 있어요.';
        return '표면 텍스처가 거칠어져 수분감이 떨어진 것으로 보여요. 수분크림을 더 챙겨보세요.';
      }
      return skinType === 'dry'
        ? '수분감은 1일차와 큰 차이가 없어요. 건성 피부는 유지만으로는 부족할 수 있으니 수분 케어를 꾸준히 더해보세요.'
        : '수분감은 1일차와 큰 차이가 없어요.';
    }

    function buildRednessDesc(skinType, badge) {
      if (badge.label === '주의 필요') {
        if (skinType === 'dry') return '붉은 영역이 넓어졌어요. 건조로 인한 자극성 홍조일 수 있어 저자극 진정 크림과 보습을 함께 챙겨보세요.';
        if (skinType === 'oily' || skinType === 'combination') return '붉은 영역이 넓어졌어요. 피지·트러블성 자극일 수 있어 진정 성분 위주로 관리해보세요.';
        return '사진 속 붉은 영역이 넓어졌어요. 강한 자외선 노출과 관련 있을 수 있어요.';
      }
      if (badge.label === '개선됨') return '붉은기가 가라앉아 톤이 안정된 것으로 보여요.';
      return '톤·홍조는 1일차와 큰 차이가 없어요.';
    }

    function buildBlemishDesc(skinType, blemishDelta) {
      if (blemishDelta > 0) {
        return skinType === 'oily' || skinType === 'combination'
          ? '새로운 트러블이 감지됐어요. T존·코 주변 모공에 피지가 쌓이지 않도록 세안과 각질 케어를 다시 점검해보세요.'
          : '새로운 트러블이 감지됐어요. 세안과 보습 루틴을 다시 점검해보세요.';
      }
      if (blemishDelta < 0) return '트러블이 줄어들어 피부가 안정된 것으로 보여요.';
      return '트러블 개수는 1일차와 같아요.';
    }

    // 유분·수분처럼 4단계 판정('개선'/'유지'/'악화'/'주의')을 쓰는 항목들을 다른 카드와
    // 통일된 배지 라벨로 변환
    const SKIN_JUDGMENT_STATUS_LABEL = { 개선: '개선됨', 유지: '변화 없음', 악화: '악화', 주의: '주의 필요' };

    function renderSkinChangeCards(startScores, endScores) {
      const s = {
        hydration: Math.round(startScores.hydration),
        redness: Math.round(startScores.redness),
        oiliness: Math.round(startScores.oiliness),
        cheekOiliness: Math.round(startScores.cheekOiliness),
        cheekHydration: Math.round(startScores.cheekHydration),
        blemish: Math.round(startScores.blemish),
      };
      const e = {
        hydration: Math.round(endScores.hydration),
        redness: Math.round(endScores.redness),
        oiliness: Math.round(endScores.oiliness),
        cheekOiliness: Math.round(endScores.cheekOiliness),
        cheekHydration: Math.round(endScores.cheekHydration),
        blemish: Math.round(endScores.blemish),
      };
      // 온보딩에서 선택한 피부타입을 "절대 기준"으로 삼아 4개 항목 모두 그 맥락에 맞게 해석
      const skinType = getSelectedSkinType();

      // 수분: 높을수록 좋은 게 아니라 피부타입별 "적정 범위"에 가까울수록 좋음 → judgeHydrationBySkinType로 판정
      const hydrationJudgment = judgeHydrationBySkinType(skinType, s, e);
      const hydrationBadge = { label: SKIN_JUDGMENT_STATUS_LABEL[hydrationJudgment.status], color: hydrationJudgment.color };
      setSkinBadge('hydrationBadge', hydrationBadge.label, hydrationBadge.color);
      document.getElementById('hydrationScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.hydration}</span> → 마지막날 <span class="font-bold text-gray-900">${e.hydration}</span>/100 <span class="${skinTextColorClasses[hydrationBadge.color]} font-semibold ml-1">${formatPercentDelta(s.hydration, e.hydration)}</span>`;
      document.getElementById('hydrationDesc').textContent = hydrationJudgment.desc;

      // 톤·홍조: 오를수록 나쁨(빨강/주황) — 판정은 공통 로직, 설명만 피부타입별로 다르게
      const rednessBadge = computeScoreBadge(e.redness - s.redness, false);
      setSkinBadge('rednessBadge', rednessBadge.label, rednessBadge.color);
      document.getElementById('rednessScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.redness}</span> → 마지막날 <span class="font-bold text-gray-900">${e.redness}</span>/100 <span class="${skinTextColorClasses[rednessBadge.color]} font-semibold ml-1">${formatPercentDelta(s.redness, e.redness)}</span>`;
      document.getElementById('rednessDesc').textContent = buildRednessDesc(skinType, rednessBadge);

      // 유분: 피부타입에 따라 "오르면 개선"일 수도 "내려야 개선"일 수도 있음 → judgeOilinessBySkinType로 판정
      const oilinessJudgment = judgeOilinessBySkinType(skinType, s, e);
      const oilinessBadge = { label: SKIN_JUDGMENT_STATUS_LABEL[oilinessJudgment.status], color: oilinessJudgment.color };
      setSkinBadge('oilinessBadge', oilinessBadge.label, oilinessBadge.color);
      document.getElementById('oilinessScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.oiliness}</span> → 마지막날 <span class="font-bold text-gray-900">${e.oiliness}</span>/100 T존 <span class="${skinTextColorClasses[oilinessBadge.color]} font-semibold ml-1">${formatPercentDelta(s.oiliness, e.oiliness)}</span>`;
      document.getElementById('oilinessDesc').textContent = oilinessJudgment.desc;

      // 트러블: 반점(blob) 개수 차이를 "건수"로 표시
      const blemishDelta = e.blemish - s.blemish;
      const blemishBadge = computeBlemishBadge(blemishDelta);
      setSkinBadge('blemishBadge', blemishBadge.label, blemishBadge.color);
      const blemishDiffText = blemishDelta === 0 ? '±0건' : blemishDelta > 0 ? `+${blemishDelta}건` : `${blemishDelta}건`;
      document.getElementById('blemishScoreLine').innerHTML =
        `1일차 <span class="font-bold text-gray-900">${s.blemish}건</span> → 마지막날 <span class="font-bold text-gray-900">${e.blemish}건</span> <span class="${skinTextColorClasses[blemishBadge.color]} font-semibold ml-1">${blemishDiffText}</span>`;
      document.getElementById('blemishDesc').textContent = buildBlemishDesc(skinType, blemishDelta);

      // 종합 요약: 수분·톤/홍조·유분·트러블 4개 항목의 배지 판정을 모두 종합해 최종 총평 생성
      const summary = buildSkinReportSummary(hydrationBadge, rednessBadge, oilinessBadge, blemishBadge);
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

    // ===== "내 피부 사후관리하기": 트러블 유형 자동 판정 + 제품 추천 =====

    // 트러블 유형 판정: 붉은기 우선 → 건조 → 기본 염증성
    // 임계값은 초기값이며, 실제 데이터 보고 조정 가능
    function classifyBlemishType(start, end) {
      const rednessRise = end.redness - start.redness; // 홍조 증가폭
      const hydrationDrop = start.hydration - end.hydration; // 수분 감소폭

      // 1) 자극성/민감성: 붉은기가 높거나 뚜렷이 증가 → 화끈거림·붉어짐
      if (end.redness >= 45 || rednessRise >= 10) return 'irritant';
      // 2) 건조성: 수분이 낮거나 뚜렷이 감소 → 건조로 인한 트러블
      if (end.hydration <= 45 || hydrationDrop >= 10) return 'dry';
      // 3) 그 외: 염증성(뾰루지·여드름·화농성) 기본값
      return 'inflammatory';
    }

    // 트러블 유형별 추천 제품
    const BLEMISH_PRODUCTS = {
      dry: { // 건조 트러블
        brand: '메디힐(MEDIHEAL)',
        name: '티트리 에센셜 마스크',
        benefit: '티트리 성분으로 진정하며 수분을 채워 건조로 예민해진 트러블 피부를 달래는 시트 마스크',
        query: '메디힐 티트리 에센셜 마스크',
      },
      inflammatory: { // 염증성 트러블(뾰루지·여드름·화농성)
        brand: '파티온(PADION)',
        name: '노스카나인 트러블 세럼 마스크팩',
        benefit: '트러블·화이트헤드 집중 케어 성분을 담아 염증성 트러블을 진정시키는 세럼 마스크팩',
        query: '파티온 노스카나인 트러블 세럼 마스크팩',
      },
      irritant: { // 자극성/민감성 트러블(자극·환절기·마스크 등으로 화끈거리고 붉어짐)
        brand: '아비브(ABIB)',
        name: '약산성 pH 시트 마스크 어성초 핏',
        benefit: '어성초 성분의 약산성 시트로 자극·환절기·마스크 마찰로 화끈거리고 붉어진 피부를 진정',
        query: '아비브 약산성 pH 시트 마스크 어성초 핏',
      },
    };

    const BLEMISH_TYPE_LABEL = {
      dry: '건조 트러블',
      inflammatory: '염증성 트러블',
      irritant: '자극성·민감성 트러블',
    };

    // 트러블은 없지만 사진 분석 점수상 "그래도 케어하면 좋은" 항목이 있을 때 추천할 제품.
    // 수분/유분은 분석 항목과 그대로 매칭하고, 톤·홍조는 가장 가까운 "미백/톤 케어" 카테고리로 매핑.
    // (제공된 목록 중 카테고리별 대표 1개만 사용, 픽서·헤어 카테고리는 대응되는 분석 지표가 없어 제외)
    const CARE_TIP_PRODUCTS = {
      hydration: {
        brand: '아비브(ABIB)',
        name: '약산성 pH 시트 마스크 핏 - 부활초 핏',
        benefit: '약산성 시트에 부활초 성분을 더해 수분과 진정을 함께 채워주는 마스크',
        query: '아비브 약산성 pH 시트 마스크 핏 부활초 핏',
      },
      tone: {
        brand: '구달(goodal)',
        name: '청귤 비타C 잡티케어 세럼마스크 알파',
        benefit: '비타민C 성분으로 칙칙해진 톤을 환하게 정돈해주는 세럼 마스크',
        query: '구달 청귤 비타C 잡티케어 세럼마스크 알파',
      },
      oiliness: {
        brand: '토리든(TORRIDEN)',
        name: '패드 밸런스풀',
        benefit: '유수분 밸런스를 맞춰 번들거림을 가라앉혀주는 저자극 패드',
        query: '토리든 패드 밸런스풀',
      },
    };

    // 트러블이 없을 때, 마지막날 점수 기준으로 "그래도 케어하면 좋은" 항목을 하나 고름 (없으면 null)
    // 기준선(65/30/40)보다 부족한 정도(margin)가 가장 큰 항목을 우선 추천
    function pickCareTipCategory(end) {
      const candidates = [
        { key: 'hydration', margin: 65 - end.hydration },
        { key: 'tone', margin: end.redness - 30 },
        { key: 'oiliness', margin: end.oiliness - 40 },
      ].filter((c) => c.margin > 0);
      if (candidates.length === 0) return null;
      candidates.sort((a, b) => b.margin - a.margin);
      return candidates[0].key;
    }

    // 구매 링크 생성기: 특정 상품 페이지가 아닌 검색 결과 URL이라 품절·개편에도 안 깨짐
    function makeBuyLinks(query) {
      const q = encodeURIComponent(query);
      return {
        oliveyoung: `https://www.oliveyoung.co.kr/store/search/getSearchMain.do?query=${q}`,
        coupang: `https://www.coupang.com/np/search?q=${q}`,
      };
    }

    // "내 피부 사후관리하기" 화면: 트러블 유무에 따라 내용을 채움 (트러블 있을 때만 유형 판정 + 제품 추천)
    function renderAftercare() {
      // 배달의뷰티 서비스 종료 안내 팝업: 이 화면에 들어올 때마다 노출
      document.getElementById('deliveryBeautyEndModal').classList.remove('hidden');

      const start = skinPhotoScores.start;
      const end = skinPhotoScores.end;
      const needsSection = document.getElementById('aftercareNeedsSection');
      const productSection = document.getElementById('aftercareProductSection');
      const emptyState = document.getElementById('aftercareEmptyState');

      if (!start || !end) {
        // 버튼 클릭 시 이미 막지만, 방어적으로 한 번 더 체크
        needsSection.classList.add('hidden');
        productSection.classList.add('hidden');
        emptyState.classList.remove('hidden');
        emptyState.textContent = '먼저 1일차·마지막날 사진을 등록해 주세요.';
        return;
      }

      if (end.blemishCount === 0) {
        // 트러블 없음: 케어가 "필요한" 건 아니므로 aftercareNeedsSection은 계속 숨김.
        // 다만 수분/톤·홍조/유분 중 아쉬운 항목이 있으면 선택적으로 제품 하나를 추천
        needsSection.classList.add('hidden');
        const careTipKey = pickCareTipCategory(end);
        if (careTipKey) {
          emptyState.classList.remove('hidden');
          emptyState.textContent = '잘 관리하고 있어요! 혹시 그래도 여행 중 부족한 부분을 케어하고 싶으면 아래와 같은 제품을 추천드려요';
          productSection.classList.remove('hidden');
          const tip = CARE_TIP_PRODUCTS[careTipKey];
          document.getElementById('aftercareProductBrand').textContent = tip.brand;
          document.getElementById('aftercareProductName').textContent = tip.name;
          document.getElementById('aftercareProductBenefit').textContent = tip.benefit;
          const tipLinks = makeBuyLinks(tip.query);
          document.getElementById('aftercareOliveyoungLink').href = tipLinks.oliveyoung;
          document.getElementById('aftercareCoupangLink').href = tipLinks.coupang;
        } else {
          emptyState.classList.remove('hidden');
          emptyState.innerHTML = '이번 여행에서는 눈에 띄는 트러블이 발견되지 않았어요.<br />지금 루틴을 잘 유지해 주세요 👍';
          productSection.classList.add('hidden');
        }
        return;
      }

      // 트러블 있음: 유형 판정 후 케어 필요 항목 + 제품 1개 노출
      emptyState.classList.add('hidden');
      needsSection.classList.remove('hidden');
      productSection.classList.remove('hidden');

      const type = classifyBlemishType(start, end);
      document.getElementById('aftercareTypeLabel').textContent = BLEMISH_TYPE_LABEL[type];
      document.getElementById('aftercareCountLine').textContent = `1일차 ${start.blemishCount}건 → 마지막날 ${end.blemishCount}건`;

      // 판정 근거를 "피부 변화 리포트" 하단 요약과 동일한 방식(1일차 → 마지막날 + 증감률)으로 제시
      let reason;
      if (type === 'irritant') {
        reason = `톤·홍조가 1일차 ${start.redness} → 마지막날 ${end.redness}로 뚜렷하게 늘어(${formatPercentDelta(start.redness, end.redness)}) 자극성·민감성 트러블로 보여요.`;
      } else if (type === 'dry') {
        reason = `수분이 1일차 ${start.hydration} → 마지막날 ${end.hydration}로 줄어(${formatPercentDelta(start.hydration, end.hydration)}) 건조 트러블로 보여요.`;
      } else {
        reason = `톤·홍조(${start.redness}→${end.redness})와 수분(${start.hydration}→${end.hydration})은 큰 변화가 없지만, 트러블이 1일차 ${start.blemishCount}건 → 마지막날 ${end.blemishCount}건으로 나타나 염증성 트러블로 보여요.`;
      }
      document.getElementById('aftercareReasonText').textContent = reason;

      const product = BLEMISH_PRODUCTS[type];
      document.getElementById('aftercareProductBrand').textContent = product.brand;
      document.getElementById('aftercareProductName').textContent = product.name;
      document.getElementById('aftercareProductBenefit').textContent = product.benefit;
      const links = makeBuyLinks(product.query);
      document.getElementById('aftercareOliveyoungLink').href = links.oliveyoung;
      document.getElementById('aftercareCoupangLink').href = links.coupang;
    }

    // "내 피부 사후관리하기" 버튼: 분석 결과가 없으면 이동하지 않고 안내만 표시
    document.getElementById('goToAftercareBtn').addEventListener('click', () => {
      if (!skinPhotoScores.start || !skinPhotoScores.end) {
        showWarning('aftercareMissingPhotosWarning', '먼저 1일차·마지막날 사진을 등록해 주세요');
        return;
      }
      hideWarning('aftercareMissingPhotosWarning');
      switchTab('aftercare');
    });

    // 사후케어 화면의 뒤로가기: 하단 네비 탭이 아니므로 항상 피부 변화 리포트로 복귀 (lastActiveNavTab을 쓰는
    // 공용 .back-to-nav-btn과 달리 이 화면은 전용 핸들러로 skinReport 탭에 직접 복귀시킴)
    document.getElementById('aftercareBackBtn').addEventListener('click', () => {
      switchTab('skinReport');
    });

    // 저장된 리포트 목록 화면도 사후케어 화면과 동일하게 하단 네비 탭이 아닌 피부 변화 리포트의
    // 하위 화면이므로, 뒤로가기는 항상 skinReport 탭으로 복귀시킴
    document.getElementById('savedReportsBackBtn').addEventListener('click', () => {
      switchTab('skinReport');
    });

    // ===== "리포트 저장하기": 피부 변화 리포트를 localStorage에 배열로 누적 저장 =====

    const SKIN_REPORTS_STORAGE_KEY = 'skinTripSavedReports';

    // 저장된 리포트 배열을 읽어옴 (최초 실행/파싱 실패 시 빈 배열로 폴백)
    function loadSavedSkinReports() {
      try {
        const raw = localStorage.getItem(SKIN_REPORTS_STORAGE_KEY);
        const parsed = raw ? JSON.parse(raw) : [];
        return Array.isArray(parsed) ? parsed : [];
      } catch (e) {
        return [];
      }
    }

    function saveSkinReportsToStorage(list) {
      localStorage.setItem(SKIN_REPORTS_STORAGE_KEY, JSON.stringify(list));
    }

    // 저장할 사진을 정사각형으로 center-crop한 뒤 축소한 JPEG dataURL로 변환.
    // 원본 화질 그대로 저장하면 사진 2장만으로도 localStorage 용량을 금방 채우기 때문에
    // "조회 화면에서 보여주는 용도"에 맞는 해상도(320px)로만 줄여서 저장함
    function shrinkPhotoForStorage(imgEl, size = 320) {
      const canvas = document.createElement('canvas');
      canvas.width = size;
      canvas.height = size;
      const ctx = canvas.getContext('2d');
      const srcW = imgEl.naturalWidth || imgEl.width;
      const srcH = imgEl.naturalHeight || imgEl.height;
      const side = Math.min(srcW, srcH);
      const sx = (srcW - side) / 2;
      const sy = (srcH - side) / 2;
      ctx.drawImage(imgEl, sx, sy, side, side, 0, 0, size, size);
      return canvas.toDataURL('image/jpeg', 0.75);
    }

    // "리포트 저장하기" 버튼: 현재 화면에 표시된 항목별 변화·종합 요약·사진을 그대로 스냅샷으로 저장
    document.getElementById('saveSkinReportBtn').addEventListener('click', () => {
      const segment = getActiveSegment();
      const destination = segment ? segment.country : '여행지 미등록';
      const flag = destinationFlags[destination] || '📍';
      const report = {
        id: Date.now(), // 저장 시각을 고유 id로 사용(같은 ms에 두 번 저장될 일은 없다고 가정)
        destination,
        flag,
        startDate: segment ? segment.start : '-',
        endDate: segment ? segment.end : '-',
        scores: {
          start: { ...skinPhotoScores.start },
          end: { ...skinPhotoScores.end },
        },
        summary: document.getElementById('skinReportSummary').textContent,
        photos: {
          start: shrinkPhotoForStorage(skinPhotoImages.start),
          end: shrinkPhotoForStorage(skinPhotoImages.end),
        },
      };
      const list = loadSavedSkinReports();
      list.push(report);
      try {
        saveSkinReportsToStorage(list);
      } catch (e) {
        // localStorage 용량 초과 등으로 저장이 실패해도 화면 전환은 그대로 진행(치명적 오류로 막지 않음)
        console.error('피부 리포트 저장 실패:', e);
      }
      switchTab('savedReports'); // 저장 후 저장된 리포트 목록 화면으로 이동
    });

    // 저장된 리포트 목록 렌더링: 각 행 = [여행지 | 날짜 | 리포트 조회하기 | 삭제(X)]
    function renderSavedSkinReportsList() {
      const list = loadSavedSkinReports();
      const listEl = document.getElementById('savedReportsList');
      const emptyEl = document.getElementById('savedReportsEmptyNote');

      if (list.length === 0) {
        emptyEl.classList.remove('hidden');
        listEl.innerHTML = '';
        return;
      }
      emptyEl.classList.add('hidden');

      // 최근 저장한 리포트가 위로 오도록 역순 정렬
      listEl.innerHTML = [...list].reverse().map((report) => `
        <div class="bg-white border border-gray-100 rounded-2xl p-4 flex items-center justify-between gap-3">
          <div class="min-w-0">
            <p class="text-sm font-semibold truncate">${report.flag} ${report.destination}</p>
            <p class="text-xs text-gray-400 mt-0.5">${report.startDate} ~ ${report.endDate}</p>
          </div>
          <div class="flex items-center gap-2 shrink-0">
            <button type="button" class="view-saved-report-btn text-xs font-semibold text-brand-600 border border-brand-100 rounded-full px-3 py-1.5" data-report-id="${report.id}">리포트 조회하기</button>
            <button type="button" class="delete-saved-report-btn text-gray-300 hover:text-gray-500 text-sm px-1" data-report-id="${report.id}" aria-label="리포트 삭제">✕</button>
          </div>
        </div>
      `).join('');

      listEl.querySelectorAll('.view-saved-report-btn').forEach((btn) => {
        btn.addEventListener('click', () => openSavedReportView(Number(btn.dataset.reportId)));
      });
      // 삭제(X): 확인창 없이 바로 목록에서 제거 (앱 내 다른 ✕ 삭제 버튼들과 동일한 방식)
      listEl.querySelectorAll('.delete-saved-report-btn').forEach((btn) => {
        btn.addEventListener('click', () => deleteSavedSkinReport(Number(btn.dataset.reportId)));
      });
    }

    // 저장된 리포트 삭제 후 목록 다시 렌더링
    function deleteSavedSkinReport(reportId) {
      const list = loadSavedSkinReports().filter((r) => r.id !== reportId);
      saveSkinReportsToStorage(list);
      renderSavedSkinReportsList();
    }

    // 저장된 리포트 항목명·라벨(모달에 표시할 4개 항목)
    const SAVED_REPORT_ITEM_LABELS = [
      { key: 'hydration', label: '💧 수분', unit: '/100' },
      { key: 'redness', label: '☀️ 톤·홍조', unit: '/100' },
      { key: 'oiliness', label: '💧 유분', unit: '/100' },
      { key: 'blemishCount', label: '🦠 트러블', unit: '건' },
    ];

    // 리포트 조회 팝업(모달) 열기: id로 저장된 리포트를 찾아 항목별 수치·종합 요약을 채워 넣음
    function openSavedReportView(reportId) {
      const list = loadSavedSkinReports();
      const report = list.find((r) => r.id === reportId);
      if (!report) return;

      document.getElementById('savedReportViewTitle').textContent = `${report.flag} ${report.destination}`;
      document.getElementById('savedReportViewDateRange').textContent = `${report.startDate} ~ ${report.endDate}`;

      // 저장 당시 등록했던 1일차·마지막날 사진 표시 (사진 없이 저장된 예전 리포트는 이 영역을 숨김)
      const photosEl = document.getElementById('savedReportViewPhotos');
      if (report.photos && report.photos.start && report.photos.end) {
        document.getElementById('savedReportViewStartPhoto').src = report.photos.start;
        document.getElementById('savedReportViewEndPhoto').src = report.photos.end;
        photosEl.classList.remove('hidden');
      } else {
        photosEl.classList.add('hidden');
      }

      document.getElementById('savedReportViewItems').innerHTML = SAVED_REPORT_ITEM_LABELS.map(({ key, label, unit }) => {
        const startVal = report.scores.start ? report.scores.start[key] : '-';
        const endVal = report.scores.end ? report.scores.end[key] : '-';
        return `
          <div class="flex items-center justify-between text-sm">
            <span class="font-semibold text-gray-700">${label}</span>
            <span class="text-gray-500">${startVal}${unit} → <span class="font-bold text-gray-900">${endVal}${unit}</span></span>
          </div>
        `;
      }).join('');
      document.getElementById('savedReportViewSummary').textContent = report.summary || '';

      document.getElementById('savedReportViewModal').classList.remove('hidden');
    }

    function closeSavedReportView() {
      document.getElementById('savedReportViewModal').classList.add('hidden');
    }
    document.getElementById('savedReportViewCloseBtn').addEventListener('click', closeSavedReportView);
    document.getElementById('savedReportViewModal').addEventListener('click', (e) => {
      // 배경(빈 공간) 탭으로도 닫히게 하되, 카드/닫기 버튼 자체를 누른 경우는 그대로 둠
      if (e.target.id === 'savedReportViewModal') {
        closeSavedReportView();
      }
    });

    // 배달의뷰티 서비스 종료 안내 팝업 닫기
    document.getElementById('deliveryBeautyEndCloseBtn').addEventListener('click', () => {
      document.getElementById('deliveryBeautyEndModal').classList.add('hidden');
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

    // 온보딩 4단계: 생년월일 입력(년/월/일 드롭다운 3개) - 셋 다 선택돼야 "다음" 버튼 활성화,
    // 계산한 나이를 개인설정에도 반영. 값은 기존 date input과 동일한 'YYYY-MM-DD' 형식으로
    // userProfile.birthDate에 저장해 calculateAge 등 기존 로직과 호환되게 함
    const regBirthYearSelect = document.getElementById('regBirthYearSelect');
    const regBirthMonthSelect = document.getElementById('regBirthMonthSelect');
    const regBirthDaySelect = document.getElementById('regBirthDaySelect');

    // 년: 1950 ~ 올해, 최근 연도가 위로 오도록 내림차순
    const birthYearNow = new Date().getFullYear();
    for (let y = birthYearNow; y >= 1950; y--) {
      const opt = document.createElement('option');
      opt.value = String(y);
      opt.textContent = `${y}년`;
      regBirthYearSelect.appendChild(opt);
    }
    // 월: 1~12
    for (let m = 1; m <= 12; m++) {
      const opt = document.createElement('option');
      opt.value = String(m).padStart(2, '0');
      opt.textContent = `${m}월`;
      regBirthMonthSelect.appendChild(opt);
    }

    // 일: 선택된 년/월의 말일에 맞춰 옵션을 다시 채움 (년/월 미선택 시엔 기본 31일까지)
    function populateBirthDayOptions() {
      const y = regBirthYearSelect.value;
      const m = regBirthMonthSelect.value;
      const daysInMonth = y && m ? new Date(Number(y), Number(m), 0).getDate() : 31;
      const prevValue = regBirthDaySelect.value;
      regBirthDaySelect.innerHTML = '<option value="">일</option>';
      for (let d = 1; d <= daysInMonth; d++) {
        const opt = document.createElement('option');
        opt.value = String(d).padStart(2, '0');
        opt.textContent = `${d}일`;
        regBirthDaySelect.appendChild(opt);
      }
      // 말일이 줄어들어도 기존에 고른 일자가 여전히 유효하면 유지
      if (prevValue && Number(prevValue) <= daysInMonth) {
        regBirthDaySelect.value = prevValue;
      }
    }
    populateBirthDayOptions();

    function syncBirthDateFromSelects() {
      const y = regBirthYearSelect.value;
      const m = regBirthMonthSelect.value;
      const d = regBirthDaySelect.value;
      const allFilled = !!(y && m && d);
      updateWizardNextButton('reg-age', allFilled);
      if (allFilled) {
        const value = `${y}-${m}-${d}`;
        userProfile.birthDate = value;
        document.getElementById('ageInput').value = calculateAge(value);
      }
    }

    regBirthYearSelect.addEventListener('change', () => {
      populateBirthDayOptions();
      syncBirthDateFromSelects();
    });
    regBirthMonthSelect.addEventListener('change', () => {
      populateBirthDayOptions();
      syncBirthDateFromSelects();
    });
    regBirthDaySelect.addEventListener('change', syncBirthDateFromSelects);

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
      { value: 'serum', label: '세럼', icon: '🧪' },
      { value: 'essence', label: '에센스', icon: '✨' },
      { value: 'lotion', label: '로션', icon: '🧴' },
      { value: 'cream', label: '크림', icon: '🫙' },
      { value: 'emulsion', label: '에멀전', icon: '🧴' },
      { value: 'sunscreen', label: '선크림', icon: '☀️' },
      { value: 'cushion', label: '쿠션 및 파운데이션', icon: '🟤' },
      { value: 'eye', label: '아이 메이크업', icon: '👁️' },
      { value: 'shading', label: '쉐딩', icon: '🌗' },
      { value: 'lip', label: '립 메이크업', icon: '💋' },
      { value: 'highlighter', label: '하이라이터', icon: '🌟' },
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
      // 빈 행을 추가한 뒤 이름을 입력하는 경우, 행 추가/삭제가 아니라 "값 변경"이라
      // MutationObserver(updateCosmeticCountBadge)가 안 걸림 → 등록하기 버튼이 계속 숨어있던 문제를
      // 막기 위해 입력할 때마다 등록하기 버튼 노출 여부도 함께 갱신
      row.querySelector('input').addEventListener('input', () => {
        renderPouchIngredientWarning();
        document.getElementById('pouchRegisterBtn').classList.toggle('hidden', getMyProducts().length === 0);
      });
      return row;
    }

    const cosmeticRows = document.getElementById('cosmeticRows');
    // tripSegments가 선언되기 전(초기 렌더링 중)에 파우치 성분 체크가 돌지 않도록 막는 플래그
    let pouchIngredientCheckReady = false;

    document.getElementById('addCosmeticRowBtn').addEventListener('click', () => {
      cosmeticRows.appendChild(buildCosmeticRow('', cosmeticCategories[0].value));
    });

    // 화장품이 추가/삭제될 때마다 카운트 배지 + 메인 화면 파우치 칩 목록 갱신
    const cosmeticCountBadge = document.getElementById('cosmeticCountBadge');
    // 사진 인식으로 여러 화장품을 한꺼번에 채우는 동안에는, 리스트+등록하기 버튼을
    // 계속 펼쳐서 보여줘야 해서 아래의 "첫 화장품 등록 시 자동 접힘"을 잠깐 막아둠
    let suppressPouchAutoCollapse = false;
    function updateCosmeticCountBadge() {
      const count = cosmeticRows.querySelectorAll('.cosmetic-row').length;
      cosmeticCountBadge.textContent = count > 0 ? `(${count})` : '';
      document.getElementById('pouchRegisterBtn').classList.toggle('hidden', getMyProducts().length === 0);
      // 화장품이 등록되면 촬영/입력 UI를 접고 카드 그리드로 보여줌
      if (!suppressPouchAutoCollapse && getMyProducts().length > 0) {
        pouchCaptureForceOpen = false;
      }
      updatePouchSectionView();
      renderPouchIngredientWarning();
    }
    new MutationObserver(updateCosmeticCountBadge).observe(cosmeticRows, { childList: true });
    updateCosmeticCountBadge();

    // 화장품 사진(파우치 전체) 촬영 → 인식 중 애니메이션 → 갖고 있는 화장품 목록에
    // 한 번에 자동 채워짐 (한 장의 사진으로 파우치 속 여러 화장품을 인식하는 컨셉)
    const pouchScanProducts = [
      { name: '넘버즈인 1번 진정 맑게 담은 청초토너 토너', category: 'toner' },
      { name: '넘버즈인 1번 판토텐산 액티브업 수딩세럼', category: 'serum' },
      { name: '넘버즈인 1번 청초 진정맑은 물막선크림', category: 'sunscreen' },
      { name: '닥터지 레드 블레미쉬 클리어 수딩 크림', category: 'cream' },
      { name: '비디비치 블랙 퍼펙션 커버 핏 쿠션', category: 'cushion' },
      { name: '웨이크메이크 소프트 블러링 아이팔레트 10호 레이지 핑크 블러링', category: 'eye' },
      { name: '롬앤 베러 댄 컨투어 02 그레이 쿨', category: 'shading' },
      { name: '롬앤 더 쥬시 래스팅 틴트 03 베어그레이프', category: 'lip' },
      { name: '에스쁘아 더브로우', category: 'eye' },
      { name: '글린트 하이라이터 듀이 문', category: 'highlighter' },
    ];

    // 내 파우치 카드/상세 모달에서 이모지 아이콘 대신 보여줄 실제 제품 사진
    const POUCH_CARD_IMG = {
      '넘버즈인 1번 진정 맑게 담은 청초토너 토너': '__CARD_IMG_TONER__',
      '넘버즈인 1번 판토텐산 액티브업 수딩세럼': '__CARD_IMG_SERUM__',
      '넘버즈인 1번 청초 진정맑은 물막선크림': '__CARD_IMG_SUNCREAM__',
      '닥터지 레드 블레미쉬 클리어 수딩 크림': '__CARD_IMG_DRG_CREAM__',
      '비디비치 블랙 퍼펙션 커버 핏 쿠션': '__CARD_IMG_CUSHION__',
      '웨이크메이크 소프트 블러링 아이팔레트 10호 레이지 핑크 블러링': '__CARD_IMG_EYEPALETTE__',
      '롬앤 베러 댄 컨투어 02 그레이 쿨': '__CARD_IMG_CONTOUR__',
      '롬앤 더 쥬시 래스팅 틴트 03 베어그레이프': '__CARD_IMG_TINT__',
      '에스쁘아 더브로우': '__CARD_IMG_BROW__',
      '글린트 하이라이터 듀이 문': '__CARD_IMG_HIGHLIGHTER__',
    };

    // 제품 상세 모달용 목업 데이터(가격/용량/전성분) - 실제 성분·가격 DB 연동 전까지
    // 지금 등록되어 있는 제품들에 한해 대표적인 값으로 채워둠
    const PRODUCT_DETAILS = {
      '넘버즈인 1번 진정 맑게 담은 청초토너 토너': {
        brand: '넘버즈인', volume: '200ml', price: 19800,
        ingredients: ['정제수', '부틸렌글라이콜', '나이아신아마이드', '판테놀', '마데카소사이드', '병풀추출물', '알란토인', '소듐하이알루로네이트', '카프릴릴글라이콜', '잔탄검'],
      },
      '넘버즈인 1번 판토텐산 액티브업 수딩세럼': {
        brand: '넘버즈인', volume: '50ml', price: 25000,
        ingredients: ['정제수', '판테놀', '나이아신아마이드', '아데노신', '소듐하이알루로네이트', '병풀추출물', '베타글루칸', '세라마이드엔피', '다이메티콘'],
      },
      '넘버즈인 1번 청초 진정맑은 물막선크림': {
        brand: '넘버즈인', volume: '50ml', price: 22000,
        ingredients: ['정제수', '에칠헥실메톡시신나메이트', '티타늄디옥사이드', '나이아신아마이드', '마데카소사이드', '병풀추출물', '알로에베라잎추출물', '다이메티콘'],
      },
      '비디비치 블랙 퍼펙션 커버 핏 쿠션': {
        brand: '비디비치', volume: '15g', price: 32000,
        ingredients: ['정제수', '사이클로펜타실록세인', '티타늄디옥사이드', '나이아신아마이드', '다이메티콘', '알루미나', '마이카', '페녹시에탄올'],
      },
      '웨이크메이크 소프트 블러링 아이팔레트 10호 레이지 핑크 블러링': {
        brand: '웨이크메이크', volume: '4.5g', price: 21000,
        ingredients: ['탈크', '마이카', '다이메티콘', '나일론-12', '트라이에틸헥사노인', '합성불소플로고파이트', '틴옥사이드', '적색산화철'],
      },
      '롬앤 베러 댄 컨투어 02 그레이 쿨': {
        brand: '롬앤', volume: '4.5g', price: 15000,
        ingredients: ['탈크', '마이카', '다이메티콘', '세틸에틸헥사노에이트', '합성왁스', '흑색산화철', '이산화티타늄'],
      },
      '롬앤 더 쥬시 래스팅 틴트 03 베어그레이프': {
        brand: '롬앤', volume: '5.5g', price: 11000,
        ingredients: ['다이머다이리놀레익애씨드/다이머다이리놀레일알코올코폴리머', '폴리부텐', '트라이에틸헥사노인', '적색산화철', '토코페롤'],
      },
      '에스쁘아 더브로우': {
        brand: '에스쁘아', volume: '0.15g', price: 12000,
        ingredients: ['하이드로제네이티드폴리아이소부텐', '마이크로크리스탈린왁스', '카나우바왁스', '흑색산화철', '토코페롤'],
      },
      '글린트 하이라이터 듀이 문': {
        brand: '글린트', volume: '8g', price: 18000,
        ingredients: ['탈크', '마이카', '다이메티콘', '합성불소플로고파이트', '보론나이트라이드', '틴옥사이드'],
      },
      // 파우치 반입 금지 성분 경고 데모/테스트용 (직접 입력으로 이 제품명을 그대로 입력하면 확인 가능)
      '화이트드롭 인텐시브 톤업크림': {
        brand: '화이트드롭', volume: '50ml', price: 28000,
        ingredients: ['정제수', '글리세린', '하이드로퀴논', '나이아신아마이드', '토코페롤', '다이메티콘'],
      },
    };

    const cosmeticPhotoInput = document.getElementById('cosmeticPhotoInput');

    let cocoSsdModel = null;
    let cocoSsdLoadPromise = null;
    function preloadCocoSsd() {
      if (cocoSsdLoadPromise) return cocoSsdLoadPromise;
      cocoSsdLoadPromise = (typeof cocoSsd !== 'undefined' ? cocoSsd.load() : Promise.reject(new Error('coco-ssd 라이브러리를 불러오지 못함')))
        .then((model) => { cocoSsdModel = model; return model; })
        .catch((e) => { console.error('coco-ssd 모델 로드 실패:', e); return null; });
      return cocoSsdLoadPromise;
    }
    preloadCocoSsd();

    let cosmeticScanCancelled = false;
    let cosmeticScanTimers = [];
    function clearCosmeticScanTimers() {
      cosmeticScanTimers.forEach((t) => clearTimeout(t));
      cosmeticScanTimers = [];
    }

    function renderCosmeticScanBoxes(boxes) {
      const boxLayer = document.getElementById('cosmeticScanBoxLayer');
      boxLayer.innerHTML = '';
      boxes.forEach((box, i) => {
        const el = document.createElement('div');
        el.className = 'cosmetic-scan-box';
        el.style.left = `${box.left}%`;
        el.style.top = `${box.top}%`;
        el.style.width = `${box.width}%`;
        el.style.height = `${box.height}%`;
        el.style.animationDelay = `${i * 0.25}s`;
        const line = document.createElement('div');
        line.className = 'cosmetic-scan-box-line';
        line.style.animationDelay = `${i * 0.25 + 0.2}s`;
        el.appendChild(line);
        boxLayer.appendChild(el);
      });
    }

    // 사진 로드 → 모델 로드 대기 → 물체 감지 → 스캔 연출 → 완료 처리 순으로
    // 반드시 순차 실행되도록 async/await로 구성 (setTimeout으로 미리 닫지 않음)
    async function runCosmeticScan(photoDataUrl) {
      cosmeticScanCancelled = false;
      clearCosmeticScanTimers();
      const modal = document.getElementById('cosmeticScanModal');
      const img = document.getElementById('cosmeticScanImage');
      const statusText = document.getElementById('cosmeticScanStatusText');
      const progressBar = document.getElementById('cosmeticScanProgressBar');
      document.getElementById('cosmeticScanBoxLayer').innerHTML = '';
      progressBar.style.transition = 'none';
      progressBar.style.width = '0%';
      statusText.textContent = '준비 중...';
      img.src = photoDataUrl;
      modal.classList.remove('hidden');

      await new Promise((resolve) => {
        if (img.complete && img.naturalWidth > 0) { resolve(); return; }
        img.onload = () => resolve();
        img.onerror = () => resolve();
      });
      if (cosmeticScanCancelled) return;

      let model = cocoSsdModel;
      if (!model) { model = await preloadCocoSsd(); }
      if (cosmeticScanCancelled) return;

      statusText.textContent = '화장품 정보를 인식하고 있어요...';
      let predictions = [];
      if (model) {
        try { predictions = await model.detect(img); }
        catch (e) { console.error('coco-ssd detect 오류:', e); predictions = []; }
      }
      if (cosmeticScanCancelled) return;

      // 감지 0개(또는 모델 로드 실패)여도 박스가 하나도 없는 상황은 무조건 방지
      const boxes = predictions.length > 0
        ? predictions.map((p) => ({
            left: (p.bbox[0] / img.width) * 100,
            top: (p.bbox[1] / img.height) * 100,
            width: (p.bbox[2] / img.width) * 100,
            height: (p.bbox[3] / img.height) * 100,
          }))
        : [{ left: 20, top: 20, width: 60, height: 60 }];
      renderCosmeticScanBoxes(boxes);

      const scanDurationMs = 2400;
      requestAnimationFrame(() => {
        progressBar.style.transition = `width ${scanDurationMs}ms ease-out`;
        progressBar.style.width = '100%';
      });
      await new Promise((resolve) => {
        const t = setTimeout(resolve, scanDurationMs);
        cosmeticScanTimers.push(t);
      });
      if (cosmeticScanCancelled) return;
      completeCosmeticScan();
    }

    function completeCosmeticScan() {
      document.getElementById('cosmeticScanModal').classList.add('hidden');

      // 인식된 화장품들로 리스트를 새로 채우는 동안 자동 접힘을 잠깐 막아서
      // "등록하기" 버튼까지 함께 눈에 보이게 함
      suppressPouchAutoCollapse = true;
      pouchCaptureForceOpen = true;
      // 이미 등록된 제품은 그대로 두고, 아직 없는 제품만 추가함(재촬영 시 기존 파우치가 통째로
      // 지워지지 않도록). 최초 1회(파우치가 비어있을 때)는 데모용으로 9개를 한번에 채우고,
      // 이후("+ 추가"로 재촬영)에는 사진 한 장 = 제품 한 개 인식처럼 1개만 추가함
      const existingNames = new Set(getMyProducts().map((product) => product.name));
      const newProducts = pouchScanProducts.filter((product) => !existingNames.has(product.name));
      const productsToAdd = existingNames.size === 0 ? newProducts : newProducts.slice(0, 1);
      productsToAdd.forEach((product) => {
        cosmeticRows.appendChild(buildCosmeticRow(product.name, product.category));
      });
      updatePouchSectionView();
      setTimeout(() => {
        suppressPouchAutoCollapse = false;
      }, 0);
    }

    function cancelCosmeticScan() {
      cosmeticScanCancelled = true;
      clearCosmeticScanTimers();
      document.getElementById('cosmeticScanModal').classList.add('hidden');
    }
    document.getElementById('cosmeticScanCloseBtn').addEventListener('click', cancelCosmeticScan);

    cosmeticPhotoInput.addEventListener('change', () => {
      const file = cosmeticPhotoInput.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = () => {
        runCosmeticScan(reader.result);
        cosmeticPhotoInput.value = '';
      };
      reader.readAsDataURL(file);
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

    // ===== "등록하기" → 파우치 바구니 애니메이션 페이지 =====
    // 파우치 사진으로 인식되는 9개 제품을 실제 패키지 형태에 가깝게 표현하기 위한 매핑
    // (제품명이 정확히 일치하면 그 모양을, 아니면 카테고리 기본 모양을 사용)
    const POUCH_VISUALS = {
      '넘버즈인 1번 진정 맑게 담은 청초토너 토너': { shape: 'bottle', label: 'numbuzin', img: '__POUCH_VISUAL_TONER__' },
      '넘버즈인 1번 판토텐산 액티브업 수딩세럼': { shape: 'bottle', label: 'numbuzin', img: '__POUCH_VISUAL_SERUM__' },
      '넘버즈인 1번 청초 진정맑은 물막선크림': { shape: 'tube', label: 'numbuzin', img: '__POUCH_VISUAL_SUNCREAM__' },
      '비디비치 블랙 퍼펙션 커버 핏 쿠션': { shape: 'cushion', label: 'VIDIVICI', img: '__POUCH_VISUAL_CUSHION__' },
      '웨이크메이크 소프트 블러링 아이팔레트 10호 레이지 핑크 블러링': { shape: 'palette-pink', label: 'wakemake', img: '__POUCH_VISUAL_EYEPALETTE__' },
      '롬앤 베러 댄 컨투어 02 그레이 쿨': { shape: 'palette-brown', label: 'romand', img: '__POUCH_VISUAL_CONTOUR__' },
      '롬앤 더 쥬시 래스팅 틴트 03 베어그레이프': { shape: 'lip', label: 'romand', img: '__POUCH_VISUAL_TINT__' },
      '에스쁘아 더브로우': { shape: 'pencil', label: 'espoir', img: '__POUCH_VISUAL_BROW__' },
      '글린트 하이라이터 듀이 문': { shape: 'highlighter', label: 'Glint', img: '__POUCH_VISUAL_HIGHLIGHTER__' },
    };
    // 위 9개는 리터럴에 직접 사진을 넣어뒀지만, 닥터지 크림은 나중에 추가된 10번째 제품이라
    // 거대한 리터럴을 직접 건드리지 않고 별도로 등록 (동작은 완전히 동일)
    POUCH_VISUALS['닥터지 레드 블레미쉬 클리어 수딩 크림'] = {
      shape: 'cream',
      label: 'Dr.G',
      img: '__POUCH_VISUAL_DRG_CREAM__',
    };
    const POUCH_CATEGORY_SHAPE_FALLBACK = {
      cleanser: 'tube', toner: 'bottle', serum: 'bottle', essence: 'bottle', lotion: 'bottle',
      cream: 'bottle', emulsion: 'bottle', sunscreen: 'tube', cushion: 'cushion',
      eye: 'palette-pink', shading: 'palette-brown', lip: 'lip', highlighter: 'highlighter',
    };
    // 바구니 안에서 각 제품이 자리잡는 위치/크기 - 사용자가 첨부한 "파우치 담긴 버전" 참고
    // 이미지의 실제 배치를 좌표로 옮겨서 최대한 동일하게 재현 (위치/크기/간격 모두 참고 사진 기준).
    // pouchScanProducts와 같은 순서: 토너/세럼/선크림/쿠션/아이팔레트/컨투어/틴트/브로우/하이라이터
    // 파우치 안쪽에 제품이 놓일 고정 위치 (top/left는 .pouch-basket-items 기준 퍼센트).
    // 파우치 사진의 실제 격자무늬 안쪽 영역(위쪽 퍼프 테두리·오른쪽 지퍼 트랙 바깥으로 나가지 않는 범위)에만
    // 3행 x 3열로 분산 배치, 회전은 -5~+5도로 최소화하고 크기도 비슷한 범위로 통일
    // 유리 선반 사진의 선반 라인(세로 약 55%, 87%) 바로 위에 제품이 서 있도록,
    // 각 제품의 세로 중심을 위 선반 48% / 아래 선반 80% 지점에 맞춤 (제품 높이 h=62px 기준)
    // 선반 3단(3개/3개/4개)에 맞춰 배치. top은 각 제품의 "윗변" 기준 %로, 아래쪽 유리
    // 선반 라인(35.2% / 64.3% / 93.5%)에 제품 밑면이 닿도록 계산해둠. 화면을 꽉 채우도록
    // 이전보다 훨씬 큰 크기(w/h)를 사용
    const POUCH_SLOTS = [
      { top: 13.5, left: 8.9, rot: 0, w: 74, h: 100 },
      { top: 13.5, left: 39.3, rot: 0, w: 74, h: 100 },
      { top: 13.5, left: 69.6, rot: 0, w: 74, h: 100 },
      { top: 42.6, left: 8.9, rot: 0, w: 74, h: 100 },
      { top: 42.6, left: 39.3, rot: 0, w: 74, h: 100 },
      { top: 42.6, left: 69.6, rot: 0, w: 74, h: 100 },
      { top: 71.7, left: 3.8, rot: 0, w: 70, h: 100 },
      { top: 71.7, left: 27.8, rot: 0, w: 70, h: 100 },
      { top: 71.7, left: 51.9, rot: 0, w: 70, h: 100 },
      { top: 71.7, left: 75.9, rot: 0, w: 70, h: 100 },
    ];
    // 각 제품이 바구니 밖 어느 방향에서 날아들어오는지(연출용 시작 위치/각도)
    const POUCH_FROM = [
      { x: 0, y: -260, r: -30 },
      { x: 220, y: -160, r: 40 },
      { x: -220, y: -160, r: -50 },
      { x: 240, y: 40, r: 30 },
      { x: -240, y: 60, r: -35 },
      { x: 0, y: 260, r: 25 },
      { x: 230, y: 200, r: -40 },
      { x: -230, y: 220, r: 45 },
      { x: 0, y: -260, r: 20 },
      { x: 240, y: -80, r: -25 },
    ];

    function buildPouchItemEl(product, index) {
      const visual = POUCH_VISUALS[product.name] || {
        shape: POUCH_CATEGORY_SHAPE_FALLBACK[product.category] || 'bottle',
        label: product.name.split(' ')[0],
      };
      const slot = POUCH_SLOTS[index % POUCH_SLOTS.length];
      const from = POUCH_FROM[index % POUCH_FROM.length];
      const el = document.createElement('div');
      // 실제 제품 사진이 매핑되어 있으면 일러스트 모양 대신 사진을 그대로, 이름 라벨 없이 크게 보여줌
      el.className = visual.img ? 'pouch-item pouch-item-photo' : `pouch-item pouch-shape-${visual.shape}`;
      el.style.top = `${slot.top}%`;
      el.style.left = `${slot.left}%`;
      if (visual.img) {
        el.style.width = `${slot.w}px`;
        el.style.height = `${slot.h}px`;
      }
      el.style.setProperty('--rot', `${slot.rot}deg`);
      el.style.setProperty('--from-x', `${from.x}px`);
      el.style.setProperty('--from-y', `${from.y}px`);
      el.style.setProperty('--from-rot', `${from.r}deg`);
      el.style.setProperty('--delay', `${index * 0.18}s`);
      el.innerHTML = (visual.img
        ? `<img src="${visual.img}" alt="${product.name}" />`
        : `<span class="pouch-item-label">${visual.label}</span>`)
        + `<span class="pouch-item-badge">${index + 1}</span>`;
      el.addEventListener('click', (e) => {
        e.stopPropagation();
        showPouchItemTooltip(el, product.name);
      });
      return el;
    }

    // 제품을 탭하면 그 제품 근처에 이름을 말풍선으로 잠깐 보여줌 (긴 목록 대신 필요할 때만 확인)
    let pouchTooltipHideTimer = null;
    function showPouchItemTooltip(itemEl, name) {
      const tooltip = document.getElementById('pouchItemTooltip');
      const stage = itemEl.closest('.pouch-basket-stage');
      const itemRect = itemEl.getBoundingClientRect();
      const stageRect = stage.getBoundingClientRect();

      tooltip.textContent = name;
      tooltip.classList.remove('visible');

      const itemCenterX = itemRect.left + itemRect.width / 2 - stageRect.left;
      const itemTopY = itemRect.top - stageRect.top;
      const itemBottomY = itemRect.bottom - stageRect.top;

      const showAbove = itemTopY > 44;
      const tooltipHeight = 30;
      const top = showAbove ? itemTopY - tooltipHeight - 6 : itemBottomY + 6;

      // 말풍선이 파우치 사진 좌우 밖으로 넘치지 않도록 위치를 clamp
      const halfW = 80;
      const clampedX = Math.min(Math.max(itemCenterX, halfW + 4), stageRect.width - halfW - 4);

      tooltip.style.left = `${clampedX}px`;
      tooltip.style.top = `${top}px`;
      requestAnimationFrame(() => tooltip.classList.add('visible'));

      clearTimeout(pouchTooltipHideTimer);
      pouchTooltipHideTimer = setTimeout(() => tooltip.classList.remove('visible'), 2200);
    }
    document.querySelector('.pouch-basket-stage').addEventListener('click', () => {
      document.getElementById('pouchItemTooltip').classList.remove('visible');
    });

    // 등록된 제품 1개를 "번호 배지 + 이름" 칩으로 표시 (선반 위 번호와 정확히 대응, 하나씩 순차 페이드인)
    function buildPouchChipEl(product, index) {
      const chip = document.createElement('div');
      chip.className = 'pouch-chip';
      chip.style.setProperty('--chip-delay', `${0.15 + Math.min(index * 0.03, 0.25)}s`);
      chip.innerHTML = `
        <span class="pouch-chip-badge">${index + 1}</span>
        <span class="flex-1 leading-snug">${product.name}</span>
      `;
      return chip;
    }

    let pouchBasketAutoCloseTimer = null; // 확인 탭 없이도 담기 연출이 끝나면 자동으로 선반으로 넘어가기 위한 타이머
    function openPouchBasketModal() {
      const myProducts = getMyProducts();
      const products = myProducts.length > 0 ? myProducts : pouchScanProducts;
      const itemsEl = document.getElementById('pouchBasketItems');
      itemsEl.innerHTML = '';
      const shown = products.slice(0, POUCH_SLOTS.length);
      shown.forEach((product, index) => {
        itemsEl.appendChild(buildPouchItemEl(product, index));
      });

      document.getElementById('pouchCompleteCount').textContent = products.length;

      const chipsRow = document.getElementById('pouchChipsRow');
      chipsRow.innerHTML = '';
      products.forEach((product, index) => {
        chipsRow.appendChild(buildPouchChipEl(product, index));
      });

      document.getElementById('pouchBasketModal').classList.remove('hidden');

      // 아이템이 다 날아들어와 자리잡는 연출(최대 9개 * 0.18s 지연 + 0.65s 비행)이 끝나고
      // 잠깐 볼 시간을 준 뒤, 확인 탭을 하지 않아도 자동으로 선반(카드 그리드)으로 넘어감
      clearTimeout(pouchBasketAutoCloseTimer);
      pouchBasketAutoCloseTimer = setTimeout(closePouchBasketModal, 3200);
    }

    function closePouchBasketModal() {
      clearTimeout(pouchBasketAutoCloseTimer);
      document.getElementById('pouchBasketModal').classList.add('hidden');
      document.getElementById('pouchItemTooltip').classList.remove('visible');
      // 등록이 끝나면 파우치 섹션을 접어 등록된 화장품 카드 그리드(선반)를 그 자리에서 그대로 보여줌
      // (이미 홈 화면 안에서 일어나는 흐름이라 switchTab('inuse')로 화면을 다시 튕길 필요가 없음)
      pouchCaptureForceOpen = false;
      updatePouchSectionView();
      document.getElementById('pouchSection').scrollIntoView({ behavior: 'smooth', block: 'start' });
    }

    document.getElementById('pouchRegisterBtn').addEventListener('click', () => {
      openPouchBasketModal();
    });

    document.getElementById('pouchBasketCloseBtn').addEventListener('click', closePouchBasketModal);
    document.getElementById('pouchBasketConfirmBtn').addEventListener('click', closePouchBasketModal);

    // 전략미션A: 여행지별 반입 금지 성분 정보 (우선 이탈리아/EU만 반영, 이후 일본·미국 등으로 확장 가능)
    // EU 회원국 + 미국 + 캐나다 여행지 등록 시 공통으로 안내하는 CBD(칸나비디올) 반입 경고.
    // (해당 지역은 CBD 함유 화장품·오일 등이 합법적으로 유통돼 여행자가 모르고 구매하기 쉬운데,
    // 한국으로 반입 시에는 대마 성분으로 분류돼 형사처벌 대상이 될 수 있어 국가별 성분 규제보다
    // 이 경고를 우선 안내함)
    const CBD_IMPORT_WARNING = {
      title: 'CBD 함유 제품은 한국 반입이 불법이에요',
      message:
        "한국에서 CBD(칸나비디올)는 「마약류 관리에 관한 법률」상 '대마'로 분류되는 성분입니다. CBD가 함유된 화장품·오일·기호품 등은 EU를 포함한 해외에서 합법적으로 구매하셨더라도, 한국으로 반입하는 것은 불법이며 형사처벌 대상이 됩니다. 대마의 줄기 등에서 추출한 CBD도 동일하게 규제되며, 해외에서 사용한 경우에도 처벌될 수 있으니 각별히 유의해 주시기 바랍니다. 구매 전 제품에 HEMP, Cannabis, CBD, CBN, THC 등의 표시가 있는지 반드시 확인하세요.",
      authority: '마약류 관리에 관한 법률',
      ingredient: 'CBD(칸나비디올)',
      ingredientKeywords: [], // 실제 보유 제품에 CBD가 들어있는 경우는 없어 파우치 성분 대조 배너는 사용하지 않음
      productHint: '',
      alternative: '구매 전 제품 라벨에 HEMP·Cannabis·CBD·CBN·THC 표시가 있는지 꼭 확인하세요',
      source: '관세청 여행자 휴대품 통관 안내',
      lastUpdated: '',
    };
    const CBD_WARNING_COUNTRIES = [
      // EU 27개 회원국
      '오스트리아', '벨기에', '불가리아', '크로아티아', '키프로스', '체코', '덴마크', '에스토니아', '핀란드', '프랑스',
      '독일', '그리스', '헝가리', '아일랜드', '이탈리아', '라트비아', '리투아니아', '룩셈부르크', '몰타', '네덜란드',
      '폴란드', '포르투갈', '루마니아', '슬로바키아', '슬로베니아', '스페인', '스웨덴',
      // + 미국, 캐나다
      '미국', '캐나다',
    ];
    const importBanData = {};
    CBD_WARNING_COUNTRIES.forEach((country) => {
      importBanData[country] = { ...CBD_IMPORT_WARNING, displayCountry: country };
    });

    // 등록된 파우치 제품 중, 현재 등록된 여행 구간 국가에서 반입 금지된 성분을 포함한 제품을 찾음
    function findPouchIngredientBanMatches() {
      const destinations = new Set(tripSegments.map((seg) => seg.country));
      const matches = [];
      getMyProducts().forEach((product) => {
        const detail = PRODUCT_DETAILS[product.name];
        if (!detail) return;
        destinations.forEach((country) => {
          const info = importBanData[country];
          if (!info) return;
          const hasBannedIngredient = detail.ingredients.some((ing) => info.ingredientKeywords.includes(ing));
          if (hasBannedIngredient) {
            matches.push({ product, country, info });
          }
        });
      });
      return matches;
    }

    // 파우치 화면 안에서 보여줄 인라인 경고 배너 (여행지 등록 시 뜨는 전체화면 팝업과 별개)
    function renderPouchIngredientWarning() {
      if (!pouchIngredientCheckReady) return;
      const banner = document.getElementById('pouchIngredientWarning');
      const matches = findPouchIngredientBanMatches();
      if (matches.length === 0) {
        banner.classList.add('hidden');
        banner.textContent = '';
        return;
      }
      const { product, info } = matches[0];
      banner.innerHTML = `⚠️ <b>${product.name}</b>에 ${info.displayCountry} 반입 금지 성분(${info.ingredient})이 포함되어 있어요. ${info.alternative}`;
      banner.classList.remove('hidden');
    }

    // 반입 금지 성분에 해당하면 경고 팝업을 띄우고 true를 반환
    function checkImportBan(destinationKey) {
      const info = importBanData[destinationKey];
      if (!info) return false;

      document.getElementById('importBanTitle').textContent = info.title;
      document.getElementById('importBanMessage').textContent = info.message;
      document.getElementById('importBanAuthority').textContent = info.authority;
      document.getElementById('importBanIngredient').textContent = info.ingredient;
      document.getElementById('importBanAlternative').textContent = info.alternative;
      document.getElementById('importBanSource').textContent = `출처 · ${info.source}${info.lastUpdated ? ' · ' + info.lastUpdated : ''}`;
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

    let tripSegments = []; // 확정 값 - "저장하기"를 눌렀을 때만 갱신되고, 홈 화면 전체가 이 값만 참조함
    let draftSegments = []; // 폼에서 편집 중인 임시 값 - 저장 전까지는 홈 화면에 아무 영향도 주지 않음
    let tripSegmentsExpanded = false;
    let prevValidSegmentCount = 0;
    pouchIngredientCheckReady = true; // 이제부터는 tripSegments 참조가 안전함
    renderPouchIngredientWarning();

    // container: 이 행이 들어갈 컨테이너 (구간 번호를 그 안의 기존 행 수로 계산)
    // onChange: 필드가 바뀔 때마다 호출할 콜백 (메인 화면/온보딩 화면이 각자 다른 콜백을 전달)
    // initial: 값을 미리 채워야 할 때 사용 (온보딩에서 완료한 구간을 메인 화면으로 옮길 때)
    // 여행 구간별 포인트 컬러 (핑크/파랑/초록/보라 파스텔톤, 구간이 4개를 넘으면 순환)
    // 1번 색은 기존 주황 대신 핑크로 - 4번(보라)이 새 브랜드 accent와 겹치지 않도록 구분
    const SEGMENT_COLORS = [
      { bg: '#FDF0F8', border: '#F5A8D0', solid: '#EC7FB8', text: '#BE185D' },
      { bg: '#EFF6FF', border: '#93C5FD', solid: '#60A5FA', text: '#1D4ED8' },
      { bg: '#ECFDF5', border: '#6EE7B7', solid: '#34D399', text: '#047857' },
      { bg: '#F5F3FF', border: '#C4B5FD', solid: '#A78BFA', text: '#6D28D9' },
    ];
    function getSegmentColor(index) {
      return SEGMENT_COLORS[index % SEGMENT_COLORS.length];
    }

    // 구간 행이 추가/삭제될 때마다 순서가 바뀌므로, 매번 인덱스 기준으로 카드 테두리/배경/라벨 색을 다시 입힘
    function refreshSegmentRowColors() {
      Array.from(tripSegmentRowsEl.querySelectorAll('.trip-segment-row')).forEach((row, i) => {
        const color = getSegmentColor(i);
        row.style.borderColor = color.border;
        row.style.background = color.bg;
        const label = row.querySelector('.segment-number-label');
        if (label) {
          label.textContent = `구간 ${i + 1}`;
          label.style.color = color.text;
        }
      });
    }

    function formatDateRangeLabel(start, end) {
      if (!start || !end) return '여행 날짜를 선택해주세요';
      const shorten = (d) => d.slice(5).replace('-', '/');
      return `${shorten(start)} ~ ${shorten(end)}`;
    }

    function buildTripSegmentRow(container, onChange, initial) {
      initial = initial || {};
      const row = document.createElement('div');
      row.className = 'trip-segment-row rounded-xl p-3 space-y-2 border-2';
      const countryOptions = ALL_COUNTRIES
        .map((c) => `<option value="${c}" ${c === initial.country ? 'selected' : ''}>${c}</option>`)
        .join('');
      row.innerHTML = `
        <div class="flex items-center justify-between">
          <p class="segment-number-label text-xs font-bold">구간</p>
          <button type="button" class="remove-segment-btn text-gray-300 hover:text-gray-500 text-sm px-1">✕</button>
        </div>
        <button type="button" class="segment-date-range-btn w-full bg-white border border-gray-200 rounded-xl px-3 py-2.5 text-sm text-left flex items-center justify-between">
          <span class="segment-date-range-label ${initial.start && initial.end ? 'text-gray-700' : 'text-gray-400'}">${formatDateRangeLabel(initial.start, initial.end)}</span>
          <span class="text-gray-300">📅</span>
        </button>
        <input type="hidden" class="segment-start-input" value="${initial.start || ''}" />
        <input type="hidden" class="segment-end-input" value="${initial.end || ''}" />
        <select class="segment-country-select w-full border border-gray-200 rounded-xl px-3 py-2 text-sm bg-white focus:outline-none focus:border-brand-500">
          <option value="">국가를 선택해주세요</option>
          ${countryOptions}
        </select>
      `;
      row.querySelector('.remove-segment-btn').addEventListener('click', () => {
        row.remove();
        manualSummarySegmentIndex = null;
        refreshSegmentRowColors();
        onChange();
      });
      row.querySelector('.segment-date-range-btn').addEventListener('click', () => {
        openTripDateRangePicker(row);
      });
      row.querySelector('.segment-country-select').addEventListener('change', () => {
        onChange();
        const country = row.querySelector('.segment-country-select').value;
        if (country) {
          checkImportBan(country);
        }
      });
      return row;
    }

    const tripSegmentRowsEl = document.getElementById('tripSegmentRows');

    document.getElementById('addTripSegmentBtn').addEventListener('click', () => {
      tripSegmentRowsEl.appendChild(buildTripSegmentRow(tripSegmentRowsEl, syncDraftSegmentsFromDOM));
      refreshSegmentRowColors();
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

    // 날짜만 한글 형식으로 ("6월 30일 - 7월 7일")
    function formatSegmentRangeKorean(seg) {
      const s = new Date(`${seg.start}T00:00:00`);
      const e = new Date(`${seg.end}T00:00:00`);
      return `${s.getMonth() + 1}월 ${s.getDate()}일 - ${e.getMonth() + 1}월 ${e.getDate()}일`;
    }

    // 오늘 날짜 기준 출발 임박도/여행 중 여부에 따라 타이틀 문구를 4단계로 분기
    function getTripHeadlineText(seg) {
      const today = new Date();
      const todayDate = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const startDate = new Date(`${seg.start}T00:00:00`);
      const endDate = new Date(`${seg.end}T00:00:00`);
      if (todayDate >= startDate && todayDate <= endDate) {
        return `${seg.country} 여행 중이군요 ☀️`;
      }
      if (todayDate > endDate) {
        return `${seg.country} 여행 잘 다녀오셨어요?`;
      }
      const diffDays = Math.round((startDate - todayDate) / 86400000);
      if (diffDays >= 1 && diffDays <= 3) {
        return `${seg.country} 여행이 코앞이에요!`;
      }
      return `${seg.country} 여행이 다가와요 ✈️`;
    }

    // 화면 최상단 타이틀 + 그 아래 링크 텍스트 갱신 - 확정값(tripSegments)이 바뀔 때(저장 시)만
    // 호출됨. 폼 자체의 위치/열림상태는 건드리지 않음
    function updateTripSegmentsUI() {
      const hasSegments = tripSegments.length > 0;
      const headline = document.getElementById('mainTripHeadline');
      const registerBtn = document.getElementById('mainRegisterTripBtn');
      registerBtn.classList.toggle('hidden', !hasSegments);
      if (hasSegments) {
        const seg = getActiveSegment() || tripSegments[0];
        const moreNote = tripSegments.length > 1 ? ` 외 ${tripSegments.length - 1}건` : '';
        headline.textContent = getTripHeadlineText(seg);
        registerBtn.innerHTML = `${formatSegmentRangeKorean(seg)}${moreNote} <span style="color:#999;">· 수정하기</span>`;
      } else {
        headline.innerHTML = '어디로<br />여행가시나요?';
      }
      renderTripCountryChips();
    }

    // 등록된 나라 칩: 탭하면 그 구간 기준으로 요약 카드/날씨가 바뀌고, 맨 끝 [+]로 여행 계획 수정 화면을 염
    function renderTripCountryChips() {
      const row = document.getElementById('tripCountryChipsRow');
      row.classList.toggle('hidden', tripSegments.length === 0);
      row.innerHTML = '';
      if (tripSegments.length === 0) return;
      const activeIndex = resolveActiveSegmentIndex();
      tripSegments.forEach((seg, i) => {
        const color = getSegmentColor(i);
        const chip = document.createElement('button');
        chip.type = 'button';
        chip.className = `trip-country-chip shrink-0 rounded-full px-3 py-1.5 text-xs font-bold border ${i === activeIndex ? 'active' : ''}`;
        chip.style.background = color.bg;
        chip.style.borderColor = color.border;
        chip.style.color = color.text;
        chip.textContent = seg.country;
        chip.addEventListener('click', () => {
          manualSummarySegmentIndex = i;
          renderTripOverview();
          renderTripCountryChips();
        });
        row.appendChild(chip);
      });
      const plusBtn = document.createElement('button');
      plusBtn.type = 'button';
      plusBtn.setAttribute('aria-label', '여행지 추가');
      plusBtn.className = 'shrink-0 w-7 h-7 rounded-full bg-gray-100 text-gray-500 flex items-center justify-center text-sm font-bold';
      plusBtn.textContent = '+';
      plusBtn.addEventListener('click', expandTripSegmentsForm);
      row.appendChild(plusBtn);
    }

    // 여행 계획 폼을 인라인 카드로 둘지 팝업(바텀시트)으로 둘지, 그리고 열지 닫을지 결정.
    // "수정하기"/저장/닫기 같은 명시적인 열기·닫기 액션에서만 호출해서, 입력 중에 폼이
    // 인라인 <-> 팝업 사이로 갑자기 옮겨지지 않게 함 (등록 완료 순간에는 폼이 이미 닫히는 중이라 티가 안 남)
    function applyTripSegmentsFormMode() {
      const hasSegments = tripSegments.length > 0;
      const section = document.getElementById('tripSegmentsSection');
      const inlineSlot = document.getElementById('tripSegmentsInlineSlot');
      const modal = document.getElementById('tripSegmentsModal');
      const backdrop = document.getElementById('tripSegmentsBackdrop');

      if (!hasSegments) {
        inlineSlot.appendChild(section);
        inlineSlot.classList.remove('hidden');
        modal.classList.add('hidden');
        backdrop.classList.add('hidden');
        return;
      }

      modal.appendChild(section);
      inlineSlot.classList.add('hidden');
      modal.classList.toggle('hidden', !tripSegmentsExpanded);
      backdrop.classList.toggle('hidden', !tripSegmentsExpanded);
    }

    // 여행지 수정하기 클릭 시 팝업(바텀시트)을 염
    function expandTripSegmentsForm() {
      tripSegmentsExpanded = true;
      applyTripSegmentsFormMode();
      updateTripSegmentsUI();
      refreshSegmentRowColors();
      playScreenTransition(document.getElementById('tripSegmentsModal'));
    }

    // 파우치 섹션으로 스크롤 + 촬영/입력 UI를 펼침 (메인 화면 상단으로 이동한 파우치 진입점들이 공유)
    function expandPouchSection() {
      pouchCaptureForceOpen = true;
      updatePouchSectionView();
      document.getElementById('pouchSection').scrollIntoView({ behavior: 'smooth' });
    }

    // 폼 입력이 바뀔 때마다(국가 선택, 날짜 확정 등) 호출됨 - 임시값(draftSegments)만 갱신하고
    // "저장하기"의 활성/비활성만 반영함. 홈 화면(인사말/제목/처방 카드/경고 배너/지도)은 절대 건드리지 않음
    function syncDraftSegmentsFromDOM() {
      draftSegments = readTripSegmentsFromDOM();
      const saveBtn = document.getElementById('tripSegmentsSaveBtn');
      if (saveBtn) saveBtn.disabled = draftSegments.length === 0;
    }

    // "저장하기"를 눌렀을 때만 호출됨 - 임시값을 확정값으로 반영하고, 그 결과로 홈 화면 전체를 갱신함
    function commitTripSegments() {
      tripSegments = draftSegments;
      updateTripSegmentsUI();
      if (tripSegments.length > 0 && prevValidSegmentCount === 0 && getMyProducts().length === 0) {
        document.getElementById('pouchPromptModal').classList.remove('hidden');
      }
      prevValidSegmentCount = tripSegments.length;
      refreshAdjustedRoutine();
      renderHistoryRecords();
      renderPouchIngredientWarning();
    }

    // "저장하기" 없이 닫을 때(✕/배경 클릭) 호출됨 - 편집 중이던 폼 내용을 버리고,
    // 마지막으로 저장된 확정값(tripSegments) 기준으로 폼을 다시 그림
    function resetDraftFormToConfirmed() {
      tripSegmentRowsEl.innerHTML = '';
      if (tripSegments.length > 0) {
        tripSegments.forEach((seg) => {
          tripSegmentRowsEl.appendChild(buildTripSegmentRow(tripSegmentRowsEl, syncDraftSegmentsFromDOM, seg));
        });
      } else {
        tripSegmentRowsEl.appendChild(buildTripSegmentRow(tripSegmentRowsEl, syncDraftSegmentsFromDOM));
      }
      refreshSegmentRowColors();
      syncDraftSegmentsFromDOM();
    }

    // 요약 카드에 표시할 구간을 사용자가 나라 칩으로 직접 골랐을 때의 인덱스 (null이면 자동 판정)
    let manualSummarySegmentIndex = null;

    // 오늘 날짜가 속한 구간 → 없으면 가장 가까운 미래 구간 → 없으면 가장 최근 지난 구간
    // (단, 나라 칩으로 직접 고른 구간이 있으면 그걸 최우선으로)
    function resolveActiveSegmentIndex() {
      if (tripSegments.length === 0) return -1;
      if (manualSummarySegmentIndex != null && tripSegments[manualSummarySegmentIndex]) {
        return manualSummarySegmentIndex;
      }
      const today = new Date();
      const todayDate = new Date(today.getFullYear(), today.getMonth(), today.getDate());
      const withDates = tripSegments.map((seg, i) => ({
        i,
        startDate: new Date(`${seg.start}T00:00:00`),
        endDate: new Date(`${seg.end}T00:00:00`),
      }));
      const current = withDates.find((x) => todayDate >= x.startDate && todayDate <= x.endDate);
      if (current) return current.i;
      const future = withDates.filter((x) => x.startDate > todayDate).sort((a, b) => a.startDate - b.startDate);
      if (future.length > 0) return future[0].i;
      const past = withDates.filter((x) => x.endDate < todayDate).sort((a, b) => b.endDate - a.endDate);
      if (past.length > 0) return past[0].i;
      return -1;
    }

    function getActiveSegment() {
      const idx = resolveActiveSegmentIndex();
      return idx === -1 ? null : tripSegments[idx];
    }

    function getCurrentTripDestination() {
      const seg = getActiveSegment();
      return seg ? seg.country : null;
    }

    // ===== 여행 날짜 선택(월간 달력, 범위 선택) =====
    let tripDateRangeActiveRow = null;
    let tripDateRangeViewYear = 0;
    let tripDateRangeViewMonth = 0; // 0-indexed
    let tripDateRangePickStart = null;
    let tripDateRangePickEnd = null;

    function pad2(n) {
      return String(n).padStart(2, '0');
    }
    function toDateStr(y, m, d) {
      return `${y}-${pad2(m + 1)}-${pad2(d)}`;
    }

    // 지금 편집 중인 행을 제외한 다른 구간들의 시작/종료(및 색 인덱스) - 같은 달력에 함께 표시
    function getOtherSegmentDraftsForCalendar(excludeRow) {
      return Array.from(tripSegmentRowsEl.querySelectorAll('.trip-segment-row'))
        .map((row, i) => ({
          row,
          index: i,
          start: row.querySelector('.segment-start-input').value,
          end: row.querySelector('.segment-end-input').value,
        }))
        .filter((s) => s.row !== excludeRow && s.start && s.end);
    }

    function openTripDateRangePicker(row) {
      tripDateRangeActiveRow = row;
      const start = row.querySelector('.segment-start-input').value;
      const end = row.querySelector('.segment-end-input').value;
      tripDateRangePickStart = start || null;
      tripDateRangePickEnd = end || null;
      const base = start ? new Date(`${start}T00:00:00`) : new Date();
      tripDateRangeViewYear = base.getFullYear();
      tripDateRangeViewMonth = base.getMonth();
      renderTripDateRangeGrid();
      document.getElementById('tripDateRangeModal').classList.remove('hidden');
      document.getElementById('tripDateRangeBackdrop').classList.remove('hidden');
    }

    function closeTripDateRangePicker() {
      document.getElementById('tripDateRangeModal').classList.add('hidden');
      document.getElementById('tripDateRangeBackdrop').classList.add('hidden');
      tripDateRangeActiveRow = null;
    }

    function changeTripDateRangeMonth(delta) {
      tripDateRangeViewMonth += delta;
      if (tripDateRangeViewMonth < 0) {
        tripDateRangeViewMonth = 11;
        tripDateRangeViewYear -= 1;
      } else if (tripDateRangeViewMonth > 11) {
        tripDateRangeViewMonth = 0;
        tripDateRangeViewYear += 1;
      }
      renderTripDateRangeGrid();
    }

    // 시작일 탭 → 종료일 탭 → 범위 선택. 시작일보다 이른 날을 탭하면 그 날짜를 새 시작일로 다시 잡음
    function handleTripDateTap(dateStr) {
      if (!tripDateRangePickStart || tripDateRangePickEnd) {
        tripDateRangePickStart = dateStr;
        tripDateRangePickEnd = null;
      } else if (dateStr < tripDateRangePickStart) {
        tripDateRangePickStart = dateStr;
      } else {
        tripDateRangePickEnd = dateStr;
      }
      renderTripDateRangeGrid();
    }

    function renderTripDateRangeGrid() {
      const y = tripDateRangeViewYear;
      const m = tripDateRangeViewMonth;
      document.getElementById('tripDateRangeMonthLabel').textContent = `${y}년 ${m + 1}월`;

      const activeIndex = Array.from(tripSegmentRowsEl.querySelectorAll('.trip-segment-row')).indexOf(tripDateRangeActiveRow);
      const activeColor = getSegmentColor(activeIndex >= 0 ? activeIndex : 0);
      const others = getOtherSegmentDraftsForCalendar(tripDateRangeActiveRow);

      const firstWeekday = new Date(y, m, 1).getDay(); // 0=일요일
      const daysInMonth = new Date(y, m + 1, 0).getDate();
      const prevDaysInMonth = new Date(y, m, 0).getDate();

      const cells = [];
      for (let i = firstWeekday - 1; i >= 0; i--) {
        cells.push({ day: prevDaysInMonth - i, muted: true });
      }
      for (let d = 1; d <= daysInMonth; d++) {
        cells.push({ day: d, muted: false, dateStr: toDateStr(y, m, d) });
      }
      const trailing = (7 - (cells.length % 7)) % 7;
      for (let d = 1; d <= trailing; d++) {
        cells.push({ day: d, muted: true });
      }

      const grid = document.getElementById('tripDateRangeGrid');
      grid.innerHTML = cells.map((cell) => {
        if (cell.muted) {
          return `<div class="trip-date-cell muted"><span class="trip-date-cell-inner">${cell.day}</span></div>`;
        }
        const dateStr = cell.dateStr;
        const isStart = dateStr === tripDateRangePickStart;
        const isEnd = dateStr === tripDateRangePickEnd;
        const inRange = !!(tripDateRangePickStart && tripDateRangePickEnd && dateStr >= tripDateRangePickStart && dateStr <= tripDateRangePickEnd);

        let classes = 'trip-date-cell';
        let innerStyle = '';
        let dot = '';
        let cellStyle = '';
        if (inRange) {
          classes += ' in-range';
          if (isStart) classes += ' range-start';
          if (isEnd) classes += ' range-end';
          cellStyle = `--range-bg:${activeColor.bg};`;
        }
        if (isStart || isEnd) {
          innerStyle = `background:${activeColor.solid};color:#fff;`;
        } else {
          const other = others.find((o) => dateStr >= o.start && dateStr <= o.end);
          if (other) {
            const oc = getSegmentColor(other.index);
            dot = `<span style="position:absolute;bottom:2px;left:50%;transform:translateX(-50%);width:4px;height:4px;border-radius:9999px;background:${oc.solid};"></span>`;
          }
        }
        return `<div class="${classes}" style="${cellStyle}" data-date="${dateStr}"><span class="trip-date-cell-inner" style="${innerStyle}">${cell.day}</span>${dot}</div>`;
      }).join('');

      grid.querySelectorAll('.trip-date-cell:not(.muted)').forEach((el) => {
        el.style.cursor = 'pointer';
        el.addEventListener('click', () => handleTripDateTap(el.dataset.date));
      });

      const confirmBtn = document.getElementById('tripDateRangeConfirmBtn');
      confirmBtn.disabled = !(tripDateRangePickStart && tripDateRangePickEnd);
      const hint = document.getElementById('tripDateRangeHint');
      if (!tripDateRangePickStart) {
        hint.textContent = '시작일을 선택해주세요';
      } else if (!tripDateRangePickEnd) {
        hint.textContent = '종료일을 선택해주세요';
      } else {
        hint.textContent = `${tripDateRangePickStart} ~ ${tripDateRangePickEnd}`;
      }
    }

    document.getElementById('tripDateRangePrevBtn').addEventListener('click', () => changeTripDateRangeMonth(-1));
    document.getElementById('tripDateRangeNextBtn').addEventListener('click', () => changeTripDateRangeMonth(1));
    document.getElementById('tripDateRangeCloseBtn').addEventListener('click', closeTripDateRangePicker);
    document.getElementById('tripDateRangeBackdrop').addEventListener('click', closeTripDateRangePicker);
    document.getElementById('tripDateRangeConfirmBtn').addEventListener('click', () => {
      if (!tripDateRangeActiveRow || !tripDateRangePickStart || !tripDateRangePickEnd) return;
      tripDateRangeActiveRow.querySelector('.segment-start-input').value = tripDateRangePickStart;
      tripDateRangeActiveRow.querySelector('.segment-end-input').value = tripDateRangePickEnd;
      const label = tripDateRangeActiveRow.querySelector('.segment-date-range-label');
      label.textContent = formatDateRangeLabel(tripDateRangePickStart, tripDateRangePickEnd);
      label.classList.remove('text-gray-400');
      label.classList.add('text-gray-700');
      closeTripDateRangePicker();
      syncDraftSegmentsFromDOM();
    });

    tripSegmentRowsEl.appendChild(buildTripSegmentRow(tripSegmentRowsEl, syncDraftSegmentsFromDOM));
    refreshSegmentRowColors();
    applyTripSegmentsFormMode();
    updateTripSegmentsUI();
    syncDraftSegmentsFromDOM();

    document.getElementById('wizardFinishBtn').addEventListener('click', () => {
      onboardingComplete = true;
      updateTabLockUI();
      switchTab('inuse');
    });

    // ===== 내 파우치 (메인 화면 상단, 촬영 UI ↔ 등록된 화장품 카드 그리드 토글) =====
    // 화장품 카드 1장을 만드는 공통 로직 (내 파우치의 등록된 화장품 그리드에서 사용)
    function buildProductCard(product) {
      const category = cosmeticCategories.find((c) => c.value === product.category);
      const img = POUCH_CARD_IMG[product.name];
      const card = document.createElement('div');
      card.className = 'pouch-card bg-white border border-gray-100 rounded-2xl p-3 cursor-pointer active:opacity-70';
      card.innerHTML = `
        <div class="w-10 h-10 rounded-xl bg-brand-50 flex items-center justify-center text-lg mb-2 overflow-hidden">
          ${img ? `<img src="${img}" alt="${product.name}" class="w-full h-full object-contain" />` : (category ? category.icon : '🧴')}
        </div>
        <p class="text-sm font-semibold truncate">${product.name}</p>
        <p class="text-xs text-gray-400">${category ? category.label : ''}</p>
      `;
      card.addEventListener('click', () => openProductDetailModal(product));
      return card;
    }

    // 파우치 카드를 탭하면 목업 가격/전성분 정보를 담은 상세 팝업을 띄움
    let productDetailCurrentName = null; // 삭제 버튼이 어떤 제품을 지울지 기억해두는 용도
    function openProductDetailModal(product) {
      productDetailCurrentName = product.name;
      const category = cosmeticCategories.find((c) => c.value === product.category);
      const detail = PRODUCT_DETAILS[product.name];
      const img = POUCH_CARD_IMG[product.name];
      document.getElementById('productDetailIcon').innerHTML = img
        ? `<img src="${img}" alt="${product.name}" class="w-full h-full object-contain" />`
        : (category ? category.icon : '🧴');
      document.getElementById('productDetailName').textContent = product.name;
      document.getElementById('productDetailMeta').textContent = [category ? category.label : '', detail && detail.volume].filter(Boolean).join(' · ');
      document.getElementById('productDetailPrice').textContent = detail ? `${detail.price.toLocaleString()}원` : '가격 정보 준비 중';
      document.getElementById('productDetailIngredients').textContent = detail ? detail.ingredients.join(', ') : '성분 정보 준비 중';
      document.getElementById('productDetailModal').classList.remove('hidden');
    }
    document.getElementById('productDetailCloseBtn').addEventListener('click', () => {
      document.getElementById('productDetailModal').classList.add('hidden');
    });
    // 등록된 제품 삭제: "+ 추가 → 사진으로 추가"를 거쳐야만 지울 수 있던 것을
    // 카드 상세 팝업에서 바로 지울 수 있게 함
    document.getElementById('productDetailDeleteBtn').addEventListener('click', () => {
      const row = Array.from(cosmeticRows.querySelectorAll('.cosmetic-row'))
        .find((r) => r.querySelector('input').value.trim() === productDetailCurrentName);
      if (row) row.remove();
      document.getElementById('productDetailModal').classList.add('hidden');
    });

    // "+ 추가" 1단계(선택) → 2단계(사진/직접입력) 전환 - 온보딩 마법사의 showWizardStep()과 동일한 패턴
    function showPouchAddStep(step) {
      pouchAddStep = step;
      document.querySelectorAll('.pouch-add-step').forEach((el) => {
        const stepId = { choice: 'pouchAddChoiceView', photo: 'pouchAddPhotoView', text: 'pouchAddTextView' }[step];
        el.classList.toggle('hidden', el.id !== stepId);
      });
      // 선택 화면의 뒤로가기는 이미 등록된 화장품이 있을 때만(돌아갈 그리드가 있을 때만) 노출
      document.getElementById('pouchAddChoiceBackBtn').classList.toggle('hidden', getMyProducts().length === 0);
    }

    document.getElementById('pouchChoosePhotoBtn').addEventListener('click', () => showPouchAddStep('photo'));
    document.getElementById('pouchChooseTextBtn').addEventListener('click', () => showPouchAddStep('text'));
    document.querySelectorAll('.pouch-add-back-btn').forEach((btn) => {
      btn.addEventListener('click', () => showPouchAddStep('choice'));
    });
    document.getElementById('pouchAddChoiceBackBtn').addEventListener('click', () => {
      pouchCaptureForceOpen = false;
      updatePouchSectionView();
    });

    // 직접 입력 폼: 제품명/카테고리 select 옵션 채우기 (buildCosmeticRow와 동일한 목록 사용)
    document.getElementById('pouchAddTextCategory').innerHTML = cosmeticCategories
      .map((c) => `<option value="${c.value}">${c.label}</option>`)
      .join('');
    document.getElementById('pouchAddTextSaveBtn').addEventListener('click', () => {
      const nameInput = document.getElementById('pouchAddTextName');
      const name = nameInput.value.trim();
      if (!name) return;
      const category = document.getElementById('pouchAddTextCategory').value;
      cosmeticRows.appendChild(buildCosmeticRow(name, category));
      nameInput.value = '';
    });

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
      showPouchAddStep('choice'); // "+ 추가"를 누르면 항상 선택 화면부터 새로 시작
      updatePouchSectionView();
    });

    showPouchAddStep('choice'); // 최초 로드 시(파우치가 비어있을 때)도 선택 화면부터 시작
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
      이탈리아: { temp: 26, humidity: 47, uvi: 6, climate: `온대기후`, waterQuality: `경수`, en: `Italy`, lat: 41.9028, lng: 12.4964, cityKey: `rome`, cityLabel: `로마` },
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
      // 구글 맵 기준 실제 좌표 (Via del Tritone 74 / Via del Corso 486-487 / Piazza dei Cinquecento)
      rome: [
        { name: 'Sephora 트레비 (Via del Tritone)', category: '뷰티 편집샵', distance: '0.3km', products: ['수분 크림', '립틴트'], lat: 41.9036, lng: 12.4857 },
        { name: 'Sephora 델 코르소 (Via del Corso)', category: '뷰티 편집샵', distance: '1.2km', products: ['향수', '립밤'], lat: 41.9095, lng: 12.4768 },
        { name: 'Sephora 테르미니 (Piazza dei Cinquecento)', category: '뷰티 편집샵', distance: '1.5km', products: ['선크림', '핸드크림'], lat: 41.9009, lng: 12.5016 },
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

    // 피부타입별 아바타 배경 파스텔 컬러 (지성=블루, 건성=핑크, 복합성=퍼플, 민감성=그린)
    // 건성을 기존 오렌지 대신 핑크로 바꿔서, 브랜드 accent(퍼플)와 복합성 색이 겹치지 않게 함
    function getSkinTypeAvatarBg(skinType) {
      const bgMap = { 지성: 'bg-blue-100', 건성: 'bg-rose-100', 복합성: 'bg-purple-100', 민감성: 'bg-green-100' };
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
      document.getElementById('communitySharedCountrySelect').value = '이탈리아';
      communitySelectedCountry = '이탈리아';
    }

    ['communityCountryFilter', 'communityGenderFilter', 'communityAgeFilter', 'communitySkinFilter'].forEach((id) => {
      document.getElementById(id).addEventListener('change', renderCommunityFeed);
    });
    renderCommunityFeed();

    // ===== 커뮤니티: [리뷰] / [나라별 인기템] 서브탭 + 공유 국가 선택 =====
    let communitySelectedCountry = '이탈리아';

    function isCommunityPopularTabActive() {
      return !document.getElementById('communityPopularTab').classList.contains('hidden');
    }

    // 상단 공유 국가 선택이 바뀌면: 리뷰 탭 필터도 같은 나라로 맞추고, 인기템 탭이 보이는 중이면 바로 다시 그림
    function setCommunitySharedCountry(country) {
      communitySelectedCountry = country;
      document.getElementById('communityCountryFilter').value = country;
      renderCommunityFeed();
      document.getElementById('popularStoreCountryLabel').textContent = country;
      document.getElementById('popularItemsCountryLabel').textContent = country;
      if (isCommunityPopularTabActive()) {
        renderCommunityPopularTab(country);
      }
    }

    document.getElementById('communitySharedCountrySelect').addEventListener('change', (e) => {
      setCommunitySharedCountry(e.target.value);
    });

    document.querySelectorAll('.community-subtab-btn').forEach((btn) => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.community-subtab-btn').forEach((b) => b.classList.remove('active'));
        btn.classList.add('active');
        const subtab = btn.dataset.subtab;
        document.getElementById('communityReviewTab').classList.toggle('hidden', subtab !== 'review');
        document.getElementById('communityPopularTab').classList.toggle('hidden', subtab !== 'popular');
        if (subtab === 'popular') {
          renderCommunityPopularTab(communitySelectedCountry);
        }
      });
    });

    // 국가 → 지도/매장 데이터가 있는 도시 별칭 (storeData/weatherData의 city 키와 연결)
    const COMMUNITY_COUNTRY_CITY_ALIAS = { 이탈리아: `밀라노`, 일본: `도쿄`, 프랑스: `파리`, 태국: `방콕`, 한국: `판교` };
    function getCommunityCityAlias(country) {
      return COMMUNITY_COUNTRY_CITY_ALIAS[country] || null;
    }

    // '99 data/skintrip_나라별_인기템.csv' 원본 그대로 반영 (국가별 순위 1~3위)
    const countryPopularItems = {
      독일: [
        { rank: 1, name: `도펠헤르츠 콜라겐`, category: `이너뷰티(건강기능식품)`, recommendRate: 58, priceRange: `15,000~25,000원`, desc: `독일 국민 건강기능식품 브랜드. 피부 탄력을 위한 콜라겐 보충제로 여행 기념 구매 1순위` },
        { rank: 2, name: `이지치오 핸드크림`, category: `핸드크림`, recommendRate: 41, priceRange: `8,000~12,000원`, desc: `독일 약국(Apotheke) 스테디셀러 핸드크림, 저자극이라 여행 중 건조함 케어에 인기` },
        { rank: 3, name: `니베아 크림(캔형, 독일판)`, category: `올인원 크림`, recommendRate: 37, priceRange: `5,000~8,000원`, desc: `독일 현지 한정 큰 사이즈 캔형이 가성비로 인기, 얼굴/바디 겸용` },
      ],
      일본: [
        { rank: 1, name: `비오레 UV 아쿠아리치 워터리 에센스`, category: `선크림`, recommendRate: 72, priceRange: `8,000~10,000원`, desc: `끈적임·백탁 없이 수분크림처럼 가볍게 스며드는 선크림, 현지가가 한국보다 저렴` },
        { rank: 2, name: `하다라보 고쿠쥰 로션`, category: `스킨/토너`, recommendRate: 55, priceRange: `6,000~9,000원`, desc: `히알루론산 고보습 라인으로 건조한 비행 후 피부에 즉각적인 수분감 채워줌` },
        { rank: 3, name: `멘소래담 워터크림`, category: `수분크림`, recommendRate: 44, priceRange: `7,000~10,000원`, desc: `저자극 산뜻한 텍스처로 여름철 끈적임 없는 마무리감 인기` },
      ],
      미국: [
        { rank: 1, name: `Farmacy 클렌징밤`, category: `클렌저`, recommendRate: 63, priceRange: `25,000~32,000원`, desc: `순한 성분에 클렌징력이 좋아 이중세안 첫 단계로 유명한 제품` },
        { rank: 2, name: `CeraVe 모이스처라이징 크림`, category: `수분크림`, recommendRate: 68, priceRange: `18,000~24,000원`, desc: `피부과 추천 세라마이드 크림, 미국 드럭스토어 부동의 스테디셀러` },
        { rank: 3, name: `The Ordinary 나이아신아마이드 세럼`, category: `세럼/앰플`, recommendRate: 51, priceRange: `10,000~14,000원`, desc: `가성비 좋은 미백/피지 컨트롤 세럼으로 SNS에서 꾸준히 언급됨` },
      ],
      이탈리아: [
        { rank: 1, name: `산타마리아 노벨라 아쿠아 디 로즈(장미수)`, category: `미스트/토너`, recommendRate: 66, priceRange: `45,000~60,000원`, desc: `피렌체 수도원에서 유래한 전통 장미수, 진정 및 수분 공급용 미스트로 인기` },
        { rank: 2, name: `콜리스타 크림`, category: `핸드/바디크림`, recommendRate: 39, priceRange: `12,000~18,000원`, desc: `이탈리아 약국(Farmacia) 스테디셀러, 저자극 보습 크림으로 여행객 사이 입소문` },
        { rank: 3, name: `라 로슈포제 안텔리오스 선크림(EU판)`, category: `선크림`, recommendRate: 58, priceRange: `20,000~26,000원`, desc: `유럽 자외선 기준에 맞춘 고자차단 선크림, 현지 가격이 한국 대비 저렴` },
      ],
      프랑스: [
        { rank: 1, name: `루센트 루미에르 쿠션`, category: `쿠션/베이스메이크업`, recommendRate: 47, priceRange: `35,000~42,000원`, desc: `은은한 광채 마무리로 유명한 프랑스 쿠션, 건조한 기후에도 밀착력 좋다는 평` },
        { rank: 2, name: `니베아 프랑스판 마이크로셀라 세럼`, category: `세럼/앰플`, recommendRate: 42, priceRange: `20,000~28,000원`, desc: `프랑스 약국 화장품 라인 중 저자극 보습 세럼으로 여행객에게 인기` },
        { rank: 3, name: `라보라토와르 A-더마 시카밤`, category: `진정크림`, recommendRate: 49, priceRange: `15,000~20,000원`, desc: `민감성 피부 진정 크림으로 유럽 약국 화장품 중 스테디셀러` },
      ],
      태국: [
        { rank: 1, name: `Oxecure Dark Spot Clearing Potion`, category: `미백/잡티케어`, recommendRate: 45, priceRange: `15,000~20,000원`, desc: `태국 피부과 브랜드의 잡티 케어 앰플, 강한 자외선 노출 후 케어용으로 인기` },
        { rank: 2, name: `스네일 화이트 크림`, category: `수분/미백크림`, recommendRate: 53, priceRange: `10,000~15,000원`, desc: `달팽이점액 성분의 진정+미백 크림, 태국 드럭스토어 대표 인기템` },
        { rank: 3, name: `미스틴 선크림`, category: `선크림`, recommendRate: 61, priceRange: `8,000~12,000원`, desc: `가볍고 산뜻한 텍스처로 고온다습한 현지 기후에 최적화된 선크림` },
      ],
      호주: [
        { rank: 1, name: `고트(Goat) 오리지널 핸드크림/비누`, category: `핸드크림/비누`, recommendRate: 56, priceRange: `10,000~15,000원`, desc: `염소유 성분의 저자극 핸드크림·비누로 건조한 호주 기후에 맞춘 인기템` },
        { rank: 2, name: `라놀린 크림`, category: `보습크림`, recommendRate: 48, priceRange: `12,000~18,000원`, desc: `양모 유래 라놀린 성분의 고보습 크림, 호주 약국 스테디셀러` },
        { rank: 3, name: `블리스텍스 립밤`, category: `립케어`, recommendRate: 39, priceRange: `5,000~8,000원`, desc: `건조하고 강한 자외선 환경에서 입술 보호용으로 여행객들이 많이 구매` },
      ],
      한국: [
        { rank: 1, name: `넘버즈인(numbuzin) 판토텐산 스킨케어 라인`, category: `세럼/앰플`, recommendRate: 62, priceRange: `18,000~25,000원`, desc: `피부 장벽 강화에 특화된 국내 인기 스킨케어 라인, 여행 후 리커버리용으로도 언급됨` },
        { rank: 2, name: `라운드랩 자작나무 수분크림`, category: `수분크림`, recommendRate: 57, priceRange: `18,000~22,000원`, desc: `약산성 포뮬러의 고보습 크림, 국내외 여행자 모두에게 꾸준히 인기` },
        { rank: 3, name: `아누아 어성초 77 토너`, category: `스킨/토너`, recommendRate: 54, priceRange: `15,000~20,000원`, desc: `진정 성분 위주의 토너로 트러블 케어용으로 자주 언급되는 제품` },
      ],
      그리스: [
        { rank: 1, name: `KORRES Greek Yoghurt Foaming Cream Cleanser`, category: `클렌저`, recommendRate: 50, priceRange: `18,000~24,000원`, desc: `그릭 요거트 성분의 순한 폼 클렌저, 그리스 대표 브랜드 코레스의 스테디셀러` },
        { rank: 2, name: `KORRES 와일드로즈 비타민C 세럼`, category: `세럼/앰플`, recommendRate: 46, priceRange: `30,000~38,000원`, desc: `톤업 및 잡티케어 세럼으로 강한 지중해 자외선 케어용으로 인기` },
        { rank: 3, name: `아포이보디 올리브오일 비누`, category: `바디케어`, recommendRate: 38, priceRange: `6,000~10,000원`, desc: `그리스산 올리브오일 성분의 천연 비누, 여행 기념품으로도 인기` },
      ],
    };

    // 인기템 카테고리(느슨한 매칭)로 매장의 취급 제품과 비교해 "어디서 살 수 있어요" 매장을 찾음.
    // 정확히 맞는 매장이 없으면 그 나라(도시) 매장 중 가장 가까운 곳을 대신 표시
    function normalizeMatchTokens(str) {
      return str
        .replace(/\([^)]*\)/g, '')
        .split('/')
        .map((t) => t.replace(/\s+/g, ''))
        .filter(Boolean);
    }
    function matchStoreForItem(item, stores) {
      if (!stores || stores.length === 0) return null;
      const tokens = normalizeMatchTokens(item.category);
      const matched = stores.find((store) =>
        store.products.some((p) => {
          const pNorm = p.replace(/\s+/g, '');
          return tokens.some((t) => pNorm.includes(t) || t.includes(pNorm));
        })
      );
      if (matched) return matched;
      return stores.slice().sort((a, b) => parseFloat(a.distance) - parseFloat(b.distance))[0];
    }

    // 나라별 인기템 탭 전용 지도 인스턴스 (홈 화면 지도와 분리)
    let communityMapInstance = null;
    let communityCityMarkers = [];
    let communityCurrentStores = [];

    function initCommunityMapIfNeeded() {
      if (communityMapInstance) return;
      const el = document.getElementById('communityPopularMapViz');
      if (!el || typeof maplibregl === 'undefined') return;
      communityMapInstance = new maplibregl.Map({
        container: el,
        style: 'https://tiles.openfreemap.org/styles/liberty',
        center: [20, 15],
        zoom: 1.3,
        attributionControl: false,
      });
      communityMapInstance.on('load', () => {
        try {
          communityMapInstance.setProjection({ type: 'globe' });
        } catch (e) {
          console.error('커뮤니티 지도 setProjection 오류:', e);
        }
      });
    }

    function clearCommunityMarkers() {
      communityCityMarkers.forEach((m) => m.remove());
      communityCityMarkers = [];
    }

    function renderCommunityPopularStoreList(cityKey, stores) {
      const list = document.getElementById('communityPopularStoreList');
      const empty = document.getElementById('communityPopularStoreEmpty');
      if (!stores || stores.length === 0) {
        list.innerHTML = '';
        empty.classList.remove('hidden');
        return;
      }
      empty.classList.add('hidden');
      list.innerHTML = stores.map((store, i) => `
        <button type="button" class="community-popular-store-item w-full flex items-center gap-3 bg-white border border-gray-100 rounded-xl p-3 text-left" data-index="${i}">
          <div class="w-10 h-10 rounded-xl ${getCategoryStyle(store.category)} flex items-center justify-center text-lg shrink-0">🏬</div>
          <div class="flex-1 min-w-0">
            <p class="text-sm font-semibold truncate">${store.name}</p>
            <p class="text-xs text-gray-400 truncate">${store.category} · ${store.products.join(', ')}</p>
          </div>
          <p class="text-xs text-gray-500 shrink-0">${store.distance}</p>
        </button>
      `).join('');
      list.querySelectorAll('.community-popular-store-item').forEach((btn) => {
        btn.addEventListener('click', () => {
          const store = communityCurrentStores[Number(btn.dataset.index)];
          if (!store) return;
          if (communityMapInstance) {
            communityMapInstance.flyTo({ center: [store.lng, store.lat], zoom: 15, duration: 1000, essential: true });
            if (store.marker) store.marker.togglePopup();
          }
          highlightPopularItemsForStore(store.name);
        });
      });
    }

    // 지도 마커/리스트 클릭 시 그 매장에서 살 수 있는 인기템으로 스크롤 + 잠깐 강조
    function highlightPopularItemsForStore(storeName) {
      const cards = document.querySelectorAll(`#communityPopularItemsList .popular-item-card[data-store-name="${CSS.escape(storeName)}"]`);
      if (cards.length === 0) return;
      cards[0].scrollIntoView({ behavior: 'smooth', block: 'center' });
      cards.forEach((card) => {
        card.classList.remove('popular-item-flash');
        void card.offsetWidth;
        card.classList.add('popular-item-flash');
      });
    }

    function renderCommunityStoreMarkers(cityKey, weather) {
      clearCommunityMarkers();
      const storeKey = weather.cityKey || (weather.en ? weather.en.toLowerCase() : '');
      const baseStores = storeData[storeKey] || [];
      const offsets = [
        [0.008, 0.006], [-0.009, 0.004], [0.004, -0.009], [-0.006, -0.007], [0.011, -0.002],
      ];
      communityCurrentStores = baseStores.map((store, i) => {
        if (store.lat != null && store.lng != null) return { ...store };
        const off = offsets[i % offsets.length];
        return { ...store, lng: weather.lng + off[0], lat: weather.lat + off[1] };
      });
      communityCurrentStores.forEach((store) => {
        const popup = new maplibregl.Popup({ offset: 18, closeButton: false, className: 'store-popup' }).setHTML(`
          <div style="min-width:140px;">
            <div style="display:flex;align-items:center;justify-content:space-between;gap:8px;margin-bottom:5px;">
              <p style="font-weight:700;font-size:12px;color:#111827;">${store.name}</p>
              <span style="font-size:10px;color:#9ca3af;white-space:nowrap;">${store.distance}</span>
            </div>
            <span style="display:inline-block;font-size:10px;padding:2px 8px;border-radius:9999px;background:#fac7ce;color:#b4001f;font-weight:600;">${store.category}</span>
          </div>
        `);
        const el = document.createElement('div');
        el.className = 'store-marker';
        el.addEventListener('click', () => highlightPopularItemsForStore(store.name));
        const marker = new maplibregl.Marker({ element: el })
          .setLngLat([store.lng, store.lat])
          .setPopup(popup)
          .addTo(communityMapInstance);
        store.marker = marker;
        communityCityMarkers.push(marker);
      });
      renderCommunityPopularStoreList(cityKey, communityCurrentStores);
    }

    function renderCommunityPopularItems(country) {
      const container = document.getElementById('communityPopularItemsList');
      const empty = document.getElementById('communityPopularItemsEmpty');
      const items = countryPopularItems[country];
      container.innerHTML = '';
      if (!items || items.length === 0) {
        empty.classList.remove('hidden');
        return;
      }
      empty.classList.add('hidden');
      items.forEach((item) => {
        const store = matchStoreForItem(item, communityCurrentStores);
        const card = document.createElement('div');
        card.className = `popular-item-card bg-white border rounded-2xl p-4 ${item.rank === 1 ? 'rank-1 border-brand-500' : 'border-gray-100'}`;
        if (store) card.dataset.storeName = store.name;
        card.innerHTML = `
          <div class="flex items-center gap-2 mb-2">
            <span class="text-xs font-bold ${item.rank === 1 ? 'bg-brand-500 text-white' : 'bg-gray-100 text-gray-500'} rounded-full w-5 h-5 flex items-center justify-center shrink-0">${item.rank}</span>
            <p class="text-sm font-bold flex-1 min-w-0 truncate">${item.name}</p>
            <span class="text-xs font-semibold text-brand-600 shrink-0">${item.recommendRate}% 추천</span>
          </div>
          <p class="text-xs text-gray-400 mb-1">${item.category} · ${item.priceRange}</p>
          <p class="text-xs text-gray-600 leading-relaxed mb-2">${item.desc}</p>
          ${store ? `<span class="inline-block text-[11px] font-semibold text-brand-600 bg-brand-50 rounded-full px-2.5 py-1">🛍️ ${store.name}에서 판매</span>` : ''}
        `;
        container.appendChild(card);
      });
    }

    // 지도→매장 렌더링이 끝난 뒤에 인기템을 그려야 매장 매칭 칩이 정확해짐 (moveend 콜백에서 이어서 호출)
    function renderCommunityPopularTab(country) {
      document.getElementById('popularStoreCountryLabel').textContent = country;
      document.getElementById('popularItemsCountryLabel').textContent = country;

      const cityKey = getCommunityCityAlias(country);
      const weather = cityKey ? weatherData[cityKey] : null;

      if (!weather || weather.lat == null) {
        clearCommunityMarkers();
        communityCurrentStores = [];
        document.getElementById('communityPopularStoreList').innerHTML = '';
        document.getElementById('communityPopularStoreEmpty').classList.remove('hidden');
        if (communityMapInstance) {
          communityMapInstance.flyTo({ center: [20, 15], zoom: 1.3, duration: 800 });
        }
        renderCommunityPopularItems(country);
        return;
      }

      initCommunityMapIfNeeded();
      if (!communityMapInstance) {
        renderCommunityPopularItems(country);
        return;
      }
      requestAnimationFrame(() => communityMapInstance.resize());
      communityMapInstance.flyTo({ center: [weather.lng, weather.lat], zoom: 12, duration: 1200, essential: true });
      communityMapInstance.once('moveend', () => {
        renderCommunityStoreMarkers(cityKey, weather);
        renderCommunityPopularItems(country);
      });
    }

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

    // 한글 명사 뒤에 붙는 조사(은/는, 을/를 등)를 받침 유무로 자동 선택
    function hasBatchim(char) {
      const code = char.charCodeAt(0);
      if (code < 0xac00 || code > 0xd7a3) return false;
      return (code - 0xac00) % 28 !== 0;
    }
    function withParticle(word, withBatchim, withoutBatchim) {
      return word + (hasBatchim(word[word.length - 1]) ? withBatchim : withoutBatchim);
    }

    // 날씨 원인(습도/자외선)에 맞는 "오늘의 처방" 한 문장 (핵심 제품 단어만 주황 강조)
    function getTodayInsight(weather, label) {
      const place = withParticle(label, '은', '는');
      if (weather.humidity <= 30) {
        return {
          emoji: '🌬️',
          weatherLine: `${place} 지금 많이 건조해요`,
          mainBefore: '오늘은 ',
          mainHighlight: '고보습 크림',
          mainAfter: '을 두 겹 발라주세요',
          sub: '가벼운 로션보다 크림 타입을 추천해요',
        };
      }
      if (weather.humidity >= 70) {
        return {
          emoji: '🌧️',
          weatherLine: `${place} 지금 습도가 높아요`,
          mainBefore: '오늘은 가벼운 ',
          mainHighlight: '토너',
          mainAfter: ' 위주로 산뜻하게 마무리하세요',
          sub: '무거운 크림은 잠시 쉬어가도 좋아요',
        };
      }
      if (weather.uvi >= 8) {
        return {
          emoji: '☀️',
          weatherLine: `${place} 지금 자외선이 강해요`,
          mainBefore: '오늘은 ',
          mainHighlight: '선크림',
          mainAfter: '을 한 번 더 덧발라 주세요',
          sub: '평소 쓰던 토너는 그대로 두셔도 좋아요',
        };
      }
      return {
        emoji: '🌤️',
        weatherLine: `${place} 지금 날씨가 맑고 쾌적해요`,
        mainBefore: '오늘은 가벼운 데일리 ',
        mainHighlight: '선크림',
        mainAfter: '이면 충분해요',
        sub: '특별한 변화 없이 평소 루틴을 유지하시면 돼요',
      };
    }

    function formatTodayDate() {
      const now = new Date();
      return `${now.getMonth() + 1}월 ${now.getDate()}일`;
    }

    // 이미 다녀온(과거) 여행이면 "오늘의 처방" 대신 그때 날씨를 돌아보는 회고 톤 문구로 대체
    // (인사말 헤드라인이 "~여행 잘 다녀오셨어요?"로 바뀌는 것과 시제를 맞춤)
    function getTripRecapInsight(weather, label) {
      if (weather.humidity <= 30) {
        return { weatherLine: `${label} 여행은 어떠셨어요?`, mainHighlight: '건조한', mainAfter: ' 날씨였어요', sub: '다음엔 고보습 크림이 도움이 될 거예요' };
      }
      if (weather.humidity >= 70) {
        return { weatherLine: `${label} 여행은 어떠셨어요?`, mainHighlight: '습도 높은', mainAfter: ' 날씨였어요', sub: '가벼운 토너 위주 루틴이 잘 맞았을 거예요' };
      }
      if (weather.uvi >= 8) {
        return { weatherLine: `${label} 여행은 어떠셨어요?`, mainHighlight: '자외선이 강한', mainAfter: ' 날씨였어요', sub: '선크림을 자주 덧발랐어야 했어요' };
      }
      return { weatherLine: `${label} 여행은 어떠셨어요?`, mainHighlight: '맑고 쾌적한', mainAfter: ' 날씨였어요', sub: '가벼운 데일리 루틴으로 충분했을 거예요' };
    }

    // 오늘의 처방(또는 과거 여행이면 회고) 히어로 카드 렌더링:
    // 날씨 요약 한 줄 → 처방/회고 문장(강조) → 보조 안내 → 수치는 하단에 작게
    function renderTodayInsightCard(label, weather, start, end, isPast) {
      const insight = isPast
        ? { emoji: '📷', ...getTripRecapInsight(weather, label), mainBefore: '' }
        : getTodayInsight(weather, label);

      document.getElementById('todayInsightWeatherLine').textContent = `${insight.emoji} ${insight.weatherLine}`;
      document.getElementById('todayInsightMain').innerHTML =
        `${insight.mainBefore}<span class="text-brand-500">${insight.mainHighlight}</span>${insight.mainAfter}`;
      document.getElementById('todayInsightSub').textContent = insight.sub;
      document.getElementById('todayInsightMetrics').innerHTML = `
        <span>🌡️ ${weather.temp}°C</span>
        <span>💧 습도 ${weather.humidity}%</span>
        <span>☀️ 자외선 ${weather.uvi}</span>
      `;
    }

    // 예측 경고 배너: 처방 카드와 함께 여행 등록 시에만 노출 (mock)
    document.getElementById('predictiveWarningBanner').addEventListener('click', () => {
      const card = document.getElementById('todayInsightCard');
      card.scrollIntoView({ behavior: 'smooth', block: 'center' });
      card.classList.add('ring-2', 'ring-brand-400');
      setTimeout(() => card.classList.remove('ring-2', 'ring-brand-400'), 900);
    });

    function renderTripOverview() {
      const activeSegment = getActiveSegment();
      const destinationKey = activeSegment ? activeSegment.country : null;

      if (!destinationKey) {
        document.getElementById('mainDashboard').classList.add('hidden');
        document.getElementById('todayInsightCard').classList.add('hidden');
        document.getElementById('predictiveWarningBanner').classList.add('hidden');
        renderCareRecommendations(null);
        return;
      }

      document.getElementById('mainDashboard').classList.remove('hidden');
      document.getElementById('todayInsightCard').classList.remove('hidden');
      renderCareRecommendations(destinationKey);

      const label = destinationKey;
      const start = activeSegment.start;
      const end = activeSegment.end;

      // 이미 끝난(과거) 여행이면 예측 경고는 더 이상 의미가 없으므로 숨기고,
      // 처방 카드도 회고 톤으로 대체 (인사말 헤드라인의 "~잘 다녀오셨어요?"와 시제를 맞춤)
      const todayDate = new Date();
      const todayDateOnly = new Date(todayDate.getFullYear(), todayDate.getMonth(), todayDate.getDate());
      const isPastTrip = todayDateOnly > new Date(`${end}T00:00:00`);
      document.getElementById('predictiveWarningBanner').classList.toggle('hidden', isPastTrip);

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

      renderTodayInsightCard(label, weather, start, end, isPastTrip);

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

    // "들고 가면 좋을 제품": 여행지의 기후(weatherData[destination].climate)에 맞춰
    // 국가별 추천화장품 DB(260713_추천화장품.csv)를 기후 단위로 묶어서 추천
    // "들고 가면 좋을 제품": 여행지(국가)별 추천화장품 DB(나라별_준비물_추천_최종_중복제거_ment.csv) 기준
const CARE_IMG_URIS = {"TORRIDEN_BALANCEFUL":"__CARE_IMG_TORRIDEN_BALANCEFUL__","BANILA_PRIMER":"__CARE_IMG_BANILA_PRIMER__","KISSME_EYELINER":"__CARE_IMG_KISSME_EYELINER__","ISNTREE_SUNCREAM":"__CARE_IMG_ISNTREE_SUNCREAM__","SONATURAL_FIXER":"__CARE_IMG_SONATURAL_FIXER__","ABIB_AQUAFIT":"__CARE_IMG_ABIB_AQUAFIT__","TORRIDEN_DIVEIN":"__CARE_IMG_TORRIDEN_DIVEIN__","ABIB_SERUM":"__CARE_IMG_ABIB_SERUM__","TORRIDEN_LIP":"__CARE_IMG_TORRIDEN_LIP__","HAIRPLUS_ESSENCE":"__CARE_IMG_HAIRPLUS_ESSENCE__","ROUNDLAB_TONIC":"__CARE_IMG_ROUNDLAB_TONIC__","BRINGGREEN_ALOE":"__CARE_IMG_BRINGGREEN_ALOE__"};
const CARE_RECOMMEND_DATA = {"싱가포르":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"일본":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"이탈리아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"대만":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"몽골":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"태국":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"베트남":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"인도네시아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"필리핀":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"아랍에미리트":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"이집트":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"호주":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"미국":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"프랑스":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"영국":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"스페인":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"튀르키예":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"캐나다":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"러시아":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"아이슬란드":{"ment":"혹독하게 춥고 건조한 곳이에요. 강력한 수분 진정과 바디 보습으로 피부 장벽을 지키는 게 가장 중요해요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"독일":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"인도":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"브라질":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"멕시코":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"아르헨티나":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"남아프리카공화국":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"스위스":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"네덜란드":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"그리스":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"포르투갈":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"오스트리아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"스웨덴":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"노르웨이":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"핀란드":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"뉴질랜드":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"말레이시아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"카타르":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"사우디아라비아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"모로코":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"케냐":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"페루":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"칠레":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"쿠바":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"자메이카":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"크로아티아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"체코":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"헝가리":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"폴란드":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"대한민국":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"중국":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"캄보디아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"스리랑카":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"나이지리아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"에티오피아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"콜롬비아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"베네수엘라":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"파나마":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"니카라과":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"과테말라":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"온두라스":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"아이티":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"도미니카공화국":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"파푸아뉴기니":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"피지":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"몰디브":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"미얀마":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"방글라데시":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"라오스":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"가나":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"탄자니아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"아프가니스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"알제리":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"리비아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"요르단":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"쿠웨이트":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"이라크":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"이란":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"파키스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"카자흐스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"튀니지":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"오만":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"벨기에":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"덴마크":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"아일랜드":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"몰타":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"슬로바키아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"슬로베니아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"세르비아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"루마니아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"불가리아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"우크라이나":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"우루과이":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"파라과이":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"몰도바":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"조지아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"레바논":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"벨라루스":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"에스토니아":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"라트비아":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"리투아니아":{"ment":"춥고 건조한 곳이에요. 얼굴은 수분 진정으로, 당기는 몸은 수분-바디로 촉촉하게 채워주세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"브링그린 알로에 97% 수딩젤","img":"BRINGGREEN_ALOE"}]},"알바니아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"안도라":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"앙골라":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"앤티가바부다":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"아르메니아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"아제르바이잔":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"바하마":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"바레인":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"바베이도스":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"벨리즈":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"베냉":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"부탄":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"볼리비아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"보스니아헤르체고비나":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"보츠와나":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"브루나이":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"부르키나파소":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"부룬디":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"카보베르데":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"카메룬":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"중앙아프리카공화국":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"차드":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"코모로":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"콩고공화국":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"콩고민주공화국":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"코스타리카":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"코트디부아르":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"키프로스":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"지부티":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"도미니카":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"에콰도르":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"엘살바도르":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"적도기니":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"에리트레아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"에스와티니":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"가봉":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"감비아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"그레나다":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"기니":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"기니비사우":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"가이아나":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"이스라엘":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"키리바시":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"키르기스스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"레소토":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"라이베리아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"리히텐슈타인":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"룩셈부르크":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"마다가스카르":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"말라위":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"말리":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"마셜제도":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"모리타니":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"모리셔스":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"미크로네시아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"모나코":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"몬테네그로":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"모잠비크":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"나미비아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"나우루":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"네팔":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"니제르":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"북한":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"북마케도니아":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"팔라우":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"르완다":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"세인트키츠네비스":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"세인트루시아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"세인트빈센트그레나딘":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"사모아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"산마리노":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"상투메프린시페":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"세네갈":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"세이셸":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"시에라리온":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"솔로몬제도":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"소말리아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"남수단":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"수단":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"수리남":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"시리아":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"타지키스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"동티모르":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"토고":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"통가":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"트리니다드토바고":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"투르크메니스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"투발루":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"우간다":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"우즈베키스탄":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"바누아투":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"예멘":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]},"잠비아":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"짐바브웨":{"ment":"덥고 습해 피지와 땀이 많은 곳이에요. 번들거림을 잡아주는 유분 관리와 강한 햇빛을 막을 선케어, 무너짐을 잡는 픽서를 챙기세요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"쏘내추럴 올 데이 타이트 메이크업 세팅 픽서","img":"SONATURAL_FIXER"}]},"바티칸":{"ment":"온화한 사계절 기후예요. 피지 균형을 위한 유분 관리와 수분 진정, 가벼운 선케어면 데일리로 충분해요.","products":[{"name":"토리든 패드 밸런스풀","img":"TORRIDEN_BALANCEFUL"},{"name":"바닐라코 프라임 프라이머 피니쉬 파우더","img":"BANILA_PRIMER"},{"name":"키스미 스무스 리퀴드 아이라이너","img":"KISSME_EYELINER"},{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"}]},"팔레스타인":{"ment":"건조하고 자외선이 강한 곳이에요. 속당김을 막을 수분 진정과 선케어는 필수, 푸석해지기 쉬운 모발을 위한 헤어 케어도 잊지 마세요.","products":[{"name":"아비브 약산성 pH 시트 마스크 핏 -아쿠아 핏","img":"ABIB_AQUAFIT"},{"name":"토리든 패드 다이브인","img":"TORRIDEN_DIVEIN"},{"name":"아비브 히알루로닉 붐 세럼 워터드롭","img":"ABIB_SERUM"},{"name":"토리든 솔리드인 세라마이드 립 에센스","img":"TORRIDEN_LIP"},{"name":"이즈앤트리 히알루론산 에어리 바디 선크림","img":"ISNTREE_SUNCREAM"},{"name":"헤어플러스 단백질본드 워터에센스","img":"HAIRPLUS_ESSENCE"},{"name":"라운드랩 소나무 진정 시카 두피 토닉","img":"ROUNDLAB_TONIC"}]}};

    function renderCareRecommendations(destination) {
      const section = document.getElementById('careRecommendSection');
      const data = destination ? CARE_RECOMMEND_DATA[destination] : null;
      if (!data) {
        section.classList.add('hidden');
        return;
      }
      section.classList.remove('hidden');
      document.getElementById('careRecommendMent').textContent = data.ment;
      const grid = document.getElementById('careRecommendGrid');
      grid.innerHTML = data.products
        .map(
          (p) => `
            <div class="care-card bg-white border border-gray-100 rounded-2xl p-2">
              <div class="w-full h-[84px] rounded-xl bg-gray-50 overflow-hidden mb-1.5 flex items-center justify-center">
                <img src="${CARE_IMG_URIS[p.img]}" alt="${p.name}" />
              </div>
              <p class="text-[11px] font-semibold leading-snug">${p.name}</p>
            </div>
          `
        )
        .join('');
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

const ALL_STACKS = {"jan":{"base":"__ARCHIVE_JAN_BASE__","aspect":1.2549,"elems":{"sun":{"img":"__ARCHIVE_JAN_SUN__","cut":true,"left":13,"top":31,"width":24,"height":24},"street":{"img":"__ARCHIVE_JAN_STREET__","cut":false,"left":45,"top":18,"width":27,"height":17},"map":{"img":"__ARCHIVE_JAN_MAP__","cut":false,"left":60,"top":33,"width":25,"height":15},"selfie":{"img":"__ARCHIVE_JAN_SELFIE__","cut":false,"left":25,"top":40,"width":19,"height":22},"izakaya":{"img":"__ARCHIVE_JAN_IZAKAYA__","cut":false,"left":52,"top":49,"width":35,"height":15},"plate":{"img":"__ARCHIVE_JAN_PLATE__","cut":true,"left":25,"top":61,"width":25,"height":13},"flag":{"img":"__ARCHIVE_JAN_FLAG__","cut":true,"left":50,"top":70,"width":12,"height":15},"player":{"img":"__ARCHIVE_JAN_PLAYER__","cut":false,"left":5,"top":64,"width":39,"height":14}},"order":["sun","street","map","selfie","izakaya","plate","flag","player"]},"feb":{"base":"__ARCHIVE_FEB_BASE__","aspect":1.2549,"elems":{"cushion":{"img":"__ARCHIVE_FEB_CUSHION__","cut":true,"left":8,"top":32,"width":25,"height":20},"cafe":{"img":"__ARCHIVE_FEB_CAFE__","cut":false,"left":44,"top":22,"width":24,"height":18},"map":{"img":"__ARCHIVE_FEB_MAP__","cut":false,"left":60,"top":33,"width":25,"height":17},"selfie":{"img":"__ARCHIVE_FEB_SELFIE__","cut":false,"left":25,"top":40,"width":19,"height":22},"eiffel":{"img":"__ARCHIVE_FEB_EIFFEL__","cut":false,"left":52,"top":48,"width":33,"height":18},"plate":{"img":"__ARCHIVE_FEB_PLATE__","cut":true,"left":26,"top":63,"width":20,"height":9},"flag":{"img":"__ARCHIVE_FEB_FLAG__","cut":true,"left":42,"top":64,"width":13,"height":16},"player":{"img":"__ARCHIVE_FEB_PLAYER__","cut":false,"left":5,"top":66,"width":35,"height":12}},"order":["cushion","cafe","map","selfie","eiffel","plate","flag","player"]},"mar":{"base":"__ARCHIVE_MAR_BASE__","aspect":1.2549,"elems":{"cream":{"img":"__ARCHIVE_MAR_CREAM__","cut":true,"left":15,"top":30,"width":20,"height":16},"sign":{"img":"__ARCHIVE_MAR_SIGN__","cut":true,"left":47,"top":17,"width":16,"height":20},"map":{"img":"__ARCHIVE_MAR_MAP__","cut":false,"left":60,"top":30,"width":20,"height":18},"selfie":{"img":"__ARCHIVE_MAR_SELFIE__","cut":false,"left":27,"top":37,"width":21,"height":23},"group":{"img":"__ARCHIVE_MAR_GROUP__","cut":false,"left":52,"top":46,"width":30,"height":18},"plate":{"img":"__ARCHIVE_MAR_PLATE__","cut":true,"left":27,"top":58,"width":21,"height":10},"flag":{"img":"__ARCHIVE_MAR_FLAG__","cut":true,"left":46,"top":61,"width":10,"height":11},"player":{"img":"__ARCHIVE_MAR_PLAYER__","cut":false,"left":17,"top":62,"width":36,"height":12}},"order":["cream","sign","map","selfie","group","plate","flag","player"]},"apr":{"base":"__ARCHIVE_APR_BASE__","aspect":2.1591,"elems":{"collagen":{"img":"__ARCHIVE_APR_COLLAGEN__","cut":true,"left":3,"top":27,"width":25,"height":17},"meeting":{"img":"__ARCHIVE_APR_MEETING__","cut":false,"left":45,"top":21,"width":33,"height":12},"map":{"img":"__ARCHIVE_APR_MAP__","cut":false,"left":66,"top":30,"width":26,"height":16},"selfie":{"img":"__ARCHIVE_APR_SELFIE__","cut":false,"left":22,"top":50,"width":24,"height":14},"beer":{"img":"__ARCHIVE_APR_BEER__","cut":false,"left":52,"top":54,"width":40,"height":12},"plate":{"img":"__ARCHIVE_APR_PLATE__","cut":true,"left":18,"top":62,"width":37,"height":8},"flag":{"img":"__ARCHIVE_APR_FLAG__","cut":true,"left":45,"top":65,"width":12,"height":8},"player":{"img":"__ARCHIVE_APR_PLAYER__","cut":false,"left":5,"top":70,"width":53,"height":10}},"order":["collagen","meeting","map","selfie","beer","plate","flag","player"]},"jun":{"base":"__ARCHIVE_JUN_BASE__","aspect":2.1591,"elems":{"cleanser":{"img":"__ARCHIVE_JUN_CLEANSER__","cut":true,"left":62,"top":16,"width":23,"height":19},"selfie":{"img":"__ARCHIVE_JUN_SELFIE__","cut":false,"left":18,"top":37,"width":28,"height":20},"meeting":{"img":"__ARCHIVE_JUN_MEETING__","cut":false,"left":52,"top":49,"width":40,"height":14},"map":{"img":"__ARCHIVE_JUN_MAP__","cut":false,"left":68,"top":59,"width":24,"height":16},"plate":{"img":"__ARCHIVE_JUN_PLATE__","cut":true,"left":5,"top":58,"width":30,"height":9},"flag":{"img":"__ARCHIVE_JUN_FLAG__","cut":true,"left":37,"top":60,"width":15,"height":10},"sunset":{"img":"__ARCHIVE_JUN_SUNSET__","cut":false,"left":42,"top":72,"width":30,"height":14},"player":{"img":"__ARCHIVE_JUN_PLAYER__","cut":false,"left":5,"top":70,"width":41,"height":10}},"order":["cleanser","selfie","meeting","map","plate","flag","sunset","player"]},"may":{"base":"__ARCHIVE_MAY_BASE__","aspect":2.1605,"elems":{"meeting1":{"img":"__ARCHIVE_MAY_MEETING1__","cut":false,"left":58,"top":5,"width":34,"height":13},"serum":{"img":"__ARCHIVE_MAY_SERUM__","cut":true,"left":62,"top":13,"width":18,"height":15},"map1":{"img":"__ARCHIVE_MAY_MAP1__","cut":false,"left":78,"top":16,"width":17,"height":12},"plate1":{"img":"__ARCHIVE_MAY_PLATE1__","cut":true,"left":5,"top":28,"width":23,"height":8},"thmap":{"img":"__ARCHIVE_MAY_THMAP__","cut":true,"left":28,"top":28,"width":14,"height":10},"selfie":{"img":"__ARCHIVE_MAY_SELFIE__","cut":false,"left":18,"top":37,"width":30,"height":20},"goat":{"img":"__ARCHIVE_MAY_GOAT__","cut":true,"left":55,"top":53,"width":17,"height":19},"meeting2":{"img":"__ARCHIVE_MAY_MEETING2__","cut":false,"left":55,"top":50,"width":37,"height":13},"plate2":{"img":"__ARCHIVE_MAY_PLATE2__","cut":true,"left":5,"top":58,"width":30,"height":9},"aumap":{"img":"__ARCHIVE_MAY_AUMAP__","cut":true,"left":37,"top":60,"width":18,"height":10},"map2":{"img":"__ARCHIVE_MAY_MAP2__","cut":false,"left":68,"top":60,"width":24,"height":16},"player":{"img":"__ARCHIVE_MAY_PLAYER__","cut":false,"left":5,"top":66,"width":41,"height":10}},"order":["meeting1","serum","map1","plate1","thmap","selfie","goat","meeting2","plate2","aumap","map2","player"]}};
const MAY_STACK = {"base":"__ARCHIVE_MAYSTACK_BASE__","aspect":1.2556,"elems":{"perfume":{"img":"__ARCHIVE_MAYSTACK_PERFUME__","left":17.86,"top":29.29,"width":17.86,"height":18.31},"meeting":{"img":"__ARCHIVE_MAYSTACK_MEETING__","left":47.96,"top":16.27,"width":22.45,"height":20.75},"map":{"img":"__ARCHIVE_MAYSTACK_MAP__","left":62.24,"top":30.92,"width":17.35,"height":17.09},"selfie":{"img":"__ARCHIVE_MAYSTACK_SELFIE__","left":27.35,"top":45.57,"width":19.59,"height":14.24},"dinner":{"img":"__ARCHIVE_MAYSTACK_DINNER__","left":53.57,"top":52.89,"width":35.71,"height":15.46},"plate":{"img":"__ARCHIVE_MAYSTACK_PLATE__","left":26.33,"top":62,"width":19.08,"height":8.95},"coliseum":{"img":"__ARCHIVE_MAYSTACK_COLISEUM__","left":45.71,"top":65.91,"width":7.35,"height":5.04},"player":{"img":"__ARCHIVE_MAYSTACK_PLAYER__","left":17.86,"top":70.79,"width":37.24,"height":11.8}},"order":["perfume","meeting","map","selfie","dinner","plate","coliseum","player"]};

    // ===== 기록 화면 (03 calendar_archive_pkg 통합) =====
    // 이 화면은 실제 등록된 tripSegments 대신, 통합 패키지가 제공하는 데모 여행 아카이브
    // (1~7월, 콜라주+도장 애니메이션 상세보기)로 대체됨.
    const travelArchive = [
      {
        id: 'jan-japan', month: 1, monthEn: 'January', country: '일본', city: '도쿄',
        start: '2026-01-06', end: '2026-01-15', flag: '🇯🇵', accent: '#E4002B',
        stack: 'jan', weather: { icon: '❄️', label: '흐림', temp: 8 }, steps: 9200, cosmetic: 'Bioré UV 아쿠아리치',
        diary: '도쿄 드럭스토어에서 <b>Bioré UV 아쿠아리치</b>를 쟁여왔어요. 겨울 햇살에도 자외선이 은근 강해서 매일 아침 꼼꼼히 발랐는데, 산뜻하게 발려서 파운데이션이 밀리지 않았어요. 시부야를 종일 걸어도 피부가 편했던 건 다 이 선크림 덕분이었어요.',
        moments: [
          { c: '#EF4444', t: '시부야 스크램블 · 도심 산책', tag: '설렘' },
          { c: '#3B82F6', t: '거래처 미팅 · 나리타 이동', tag: '집중' },
          { c: '#22C55E', t: '이자카야 회식 · 건배', tag: '즐거움' },
          { c: '#A855F7', t: '대나무숲 · Plastic Love 감상', tag: '여유' },
        ],
      },
      {
        id: 'feb-france', month: 2, monthEn: 'February', country: '프랑스', city: '파리',
        start: '2026-02-10', end: '2026-02-19', flag: '🇫🇷', accent: '#0055A4',
        stack: 'feb', weather: { icon: '🌧️', label: '비', temp: 6 }, steps: 11800, cosmetic: '로레알 루센트 쿠션',
        diary: '파리 백화점에서 <b>로레알 루센트 쿠션</b>을 만났어요. 흐린 겨울 날씨에도 화사한 광이 살아나서 사진마다 얼굴이 밝게 나왔어요. 에펠탑 앞에서 셀카 찍을 때마다 톤이 무너지지 않아서 정말 만족스러운 쇼핑이었어요.',
        moments: [
          { c: '#EF4444', t: '에펠탑 · 몽마르트 계단', tag: '설렘' },
          { c: '#3B82F6', t: '카페 미팅 · Le Marais', tag: '집중' },
          { c: '#22C55E', t: 'CDG 공항 · 파리 이동', tag: '분주' },
          { c: '#A855F7', t: 'La Vie en Rose 감상', tag: '낭만' },
        ],
      },
      {
        id: 'mar-usa', month: 3, monthEn: 'March', country: '미국', city: '캘리포니아',
        start: '2026-03-09', end: '2026-03-23', flag: '🇺🇸', accent: '#3C3B6E',
        stack: 'mar', weather: { icon: '⛅', label: '구름조금', temp: 19 }, steps: 14500, cosmetic: 'Farmacy 그린클린',
        diary: 'LA 세포라에서 <b>Farmacy 그린클린</b> 클렌징밤을 집어왔어요. 캘리포니아 햇볕과 먼지에 하루 종일 노출됐는데, 저녁마다 이걸로 싹 녹여내니 피부가 개운했어요. 레드우드 트레킹으로 지친 날에도 세안 한 번이면 리셋되는 기분이었어요.',
        moments: [
          { c: '#EF4444', t: '레드우드 · PCH 드라이브', tag: '설렘' },
          { c: '#3B82F6', t: '현지 미팅 · 루트 이동', tag: '집중' },
          { c: '#22C55E', t: 'Chick-fil-A · 로컬 맛집', tag: '즐거움' },
          { c: '#A855F7', t: 'Pure Thing (Live) 감상', tag: '자유' },
        ],
      },
      {
        id: 'apr-germany', month: 4, monthEn: 'April', country: '독일', city: '베를린',
        start: '2026-04-08', end: '2026-04-16', flag: '🇩🇪', accent: '#000000',
        stack: 'apr', weather: { icon: '☁️', label: '흐림', temp: 14 }, steps: 10300, cosmetic: 'Doppelherz 콜라겐',
        diary: '베를린 약국에서 <b>Doppelherz 콜라겐</b>을 챙겼어요. 출장 일정이 빡빡해 피부가 푸석했는데, 매일 챙겨 먹으니 컨디션이 확실히 올라왔어요. 슈프레 강가를 걷고 비어가든에서 건배할 때도 피부 걱정 없이 즐길 수 있었어요.',
        moments: [
          { c: '#EF4444', t: '브란덴부르크 · 슈프레 강가', tag: '설렘' },
          { c: '#3B82F6', t: '미테 미팅 · BER 이동', tag: '집중' },
          { c: '#22C55E', t: '비어가든 · 프로스트!', tag: '즐거움' },
          { c: '#A855F7', t: 'Strobe (Deadmau5) 감상', tag: '몰입' },
        ],
      },
      {
        id: 'may-thai-au', month: 5, monthEn: 'May', country: '태국·호주', city: '방콕·시드니',
        start: '2026-05-02', end: '2026-05-22', flag: '🇹🇭🇦🇺', accent: '#3182F6',
        stack: 'may', weather: { icon: '☀️', label: '맑음', temp: 33 }, steps: 16200, cosmetic: 'goat 오리지널 마스크폼',
        diary: '방콕 편의점에서 산 세럼과 시드니에서 만난 <b>goat 오리지널 마스크폼</b>이 이번 여행의 득템이에요. 습하고 더운 방콕에선 산뜻하게, 건조한 시드니에선 촉촉하게 — 두 도시의 다른 기후를 한 번에 케어할 수 있었어요.',
        moments: [
          { c: '#EF4444', t: '수상시장 · 오페라하우스', tag: '설렘' },
          { c: '#3B82F6', t: '방콕·시드니 미팅', tag: '집중' },
          { c: '#22C55E', t: '로컬 푸드 · 하버 투어', tag: '즐거움' },
          { c: '#A855F7', t: 'Down Under 감상', tag: '자유' },
        ],
      },
      {
        id: 'jun-greece', month: 6, monthEn: 'June', country: '그리스', city: '아테네·산토리니',
        start: '2026-06-05', end: '2026-06-12', flag: '🇬🇷', accent: '#0D5EAF',
        stack: 'jun', weather: { icon: '🌤️', label: '맑음', temp: 28 }, steps: 13100, cosmetic: 'KORRES 그릭요거트 클렌저',
        diary: '산토리니 편집숍에서 <b>KORRES 그릭요거트 클렌저</b>를 만났어요. 강한 지중해 햇살에 달아오른 피부를 부드럽게 진정시켜줬어요. 아크로폴리스를 걷고 산토리니 일몰을 보는 내내 피부가 촉촉하게 유지돼서 여행이 더 완벽했어요.',
        moments: [
          { c: '#EF4444', t: '아크로폴리스 · 산토리니 일몰', tag: '설렘' },
          { c: '#3B82F6', t: '항구뷰 미팅 · 페리 이동', tag: '집중' },
          { c: '#22C55E', t: '그릭 다이닝 · 골목 산책', tag: '즐거움' },
          { c: '#A855F7', t: "Zorba's Dance 감상", tag: '낭만' },
        ],
      },
      {
        id: 'jul-italy', month: 7, monthEn: 'July', country: '이탈리아', city: '로마',
        start: '2026-07-09', end: '2026-07-23', flag: '🇮🇹', accent: '#008C45',
        stack: 'italy', weather: { icon: '☀️', label: '맑음', temp: 26 }, steps: 12400,
        keyDays: [12, 13, 14, 15],
        cosmetic: 'Acqua di Rore',
        song: { title: 'Volare', artist: 'Domenico Modugno' },
        plate: 'ROMA · IT',
        diary: '로마 골목의 작은 편집숍에서 <b>Acqua di Rore</b>를 만났어요. 향을 맡는 순간 바로 반해서 결국 지갑을 열었네요. 여행 내내 아침마다 한 번씩 뿌렸는데, 은은한 시트러스 향이 햇살 좋은 로마랑 정말 잘 어울렸어요. 두고두고 이 향을 맡으면 이번 여행이 떠오를 것 같아 <b style="color:#3182F6">가장 잘한 쇼핑</b>이었어요.',
        moments: [
          { c: '#EF4444', t: '트레비 분수 · 콜로세움 투어', tag: '설렘' },
          { c: '#3B82F6', t: '쇼룸 미팅 · 바이어 상담', tag: '집중' },
          { c: '#22C55E', t: '단체 디너 · 파스타 & 와인', tag: '행복' },
          { c: '#A855F7', t: '해안 드라이브 · Volare 감상', tag: '여유' },
        ],
      },
    ];

    // 오늘 날짜 기준 상태 계산 (데모 시나리오: "현재 7월, 이탈리아 여행 중")
    const ARCHIVE_TODAY = new Date('2026-07-13T00:00:00');
    function getArchiveStatus(item) {
      const todayDate = new Date(ARCHIVE_TODAY.getFullYear(), ARCHIVE_TODAY.getMonth(), ARCHIVE_TODAY.getDate());
      const startDate = new Date(`${item.start}T00:00:00`);
      const endDate = new Date(`${item.end}T00:00:00`);
      if (todayDate < startDate) return { key: 'upcoming', label: '예정', className: 'text-brand-500', bg: 'bg-brand-50' };
      if (todayDate > endDate) return { key: 'past', label: '다녀옴', className: 'text-gray-500', bg: 'bg-gray-100' };
      return { key: 'current', label: '여행 중', className: 'text-brand-600', bg: 'bg-brand-100' };
    }

    // 국기 이모지 문자열을 개별 국기 단위로 분리 (국기 하나 = 지역 표시자 코드포인트 2개)
    // "태국·호주"처럼 국기 2개가 이어붙은 항목(🇹🇭🇦🇺)을 ['🇹🇭','🇦🇺']로 나눔
    function splitFlagEmojis(flagStr) {
      const codePoints = Array.from(flagStr);
      const flags = [];
      for (let i = 0; i < codePoints.length; i += 2) {
        flags.push(codePoints[i] + (codePoints[i + 1] || ''));
      }
      return flags;
    }

    // 여행 기록 카드 (달력별 기록). "여행 중"인 카드만 살짝 크고 진한 주황 강조,
    // "다녀옴"은 화이트 배경 + 회색 뱃지로 차분하게 톤다운
    function buildArchiveCard(item) {
      const status = getArchiveStatus(item);
      const isCurrent = status.key === 'current';
      const flags = splitFlagEmojis(item.flag);
      const card = document.createElement('button');
      card.type = 'button';
      card.className = `archive-history-card w-full flex items-center text-left border ${
        isCurrent
          ? 'gap-3.5 rounded-2xl p-4 bg-brand-50 border-2 border-brand-400 shadow-sm'
          : 'gap-3 rounded-2xl p-3.5 bg-white border-gray-100'
      }`;
      card.innerHTML = `
        <div class="h-11 rounded-full ${status.bg} flex items-center justify-center gap-0.5 shrink-0 px-2" style="font-size: 30px; line-height: 1;">
          ${flags.map((f) => `<span>${f}</span>`).join('')}
        </div>
        <div class="flex-1 min-w-0">
          <div class="flex items-center gap-1.5">
            <p class="text-sm font-bold text-gray-900 truncate">${item.country}</p>
            <span class="text-[11px] font-semibold text-gray-400">· ${item.monthEn}</span>
          </div>
          <p class="text-xs text-gray-400 mt-0.5">${item.city} · ${item.start} ~ ${item.end}</p>
        </div>
        <span class="text-xs font-bold shrink-0 ${status.className}">${status.label}</span>
      `;
      card.addEventListener('click', () => openArchiveDetail(item));
      return card;
    }

    // 여행 요약 히어로: 방문 국가/도시/연도를 데이터에서 자동 집계 + 방문 국기 나열
    function renderHistorySummaryHero() {
      const hero = document.getElementById('historySummaryHero');
      if (travelArchive.length === 0) {
        hero.classList.add('hidden');
        return;
      }
      hero.classList.remove('hidden');

      const countrySet = new Set();
      const citySet = new Set();
      const yearSet = new Set();
      const flagList = [];
      const seenFlags = new Set();

      travelArchive.forEach((item) => {
        item.country.split('·').forEach((c) => countrySet.add(c.trim()));
        item.city.split('·').forEach((c) => citySet.add(c.trim()));
        yearSet.add(new Date(`${item.start}T00:00:00`).getFullYear());
        splitFlagEmojis(item.flag).forEach((f) => {
          if (!seenFlags.has(f)) {
            seenFlags.add(f);
            flagList.push(f);
          }
        });
      });

      document.getElementById('summaryMainSentence').innerHTML = `올해, <span class="text-brand-500">${countrySet.size}개 나라</span>를 여행했어요 ✈️`;
      document.getElementById('summarySubSentence').textContent = `${citySet.size}개 도시 · ${[...yearSet].sort().join(', ')}년`;
      document.getElementById('summaryFlagsRow').innerHTML = flagList.map((f) => `<span>${f}</span>`).join('');
    }

    function renderHistoryRecords() {
      renderHistorySummaryHero();
      // 정렬: 현재 여행 중 → 과거(최근달→1월) → 예정된 출장/여행(맨 아래, 가까운 순)
      const withStatus = travelArchive.map((it) => ({ it, st: getArchiveStatus(it) }));
      const current = withStatus.filter((x) => x.st.key === 'current').map((x) => x.it);
      const past = withStatus
        .filter((x) => x.st.key === 'past')
        .sort((a, b) => b.it.month - a.it.month)
        .map((x) => x.it);
      const upcoming = withStatus
        .filter((x) => x.st.key === 'upcoming')
        .sort((a, b) => a.it.month - b.it.month)
        .map((x) => x.it);

      const calendarList = document.getElementById('historyCalendarList');
      calendarList.innerHTML = '';

      [...current, ...past].forEach((item) => calendarList.appendChild(buildArchiveCard(item)));

      // 예정된 출장/여행은 구분선 + 라벨과 함께 맨 아래
      if (upcoming.length > 0) {
        const divider = document.createElement('div');
        divider.className = 'flex items-center gap-2 pt-3 pb-1';
        divider.innerHTML = `
          <span class="text-xs font-bold text-gray-400">✈️ 예정된 출장 · 여행</span>
          <span class="flex-1 h-px bg-gray-100"></span>
        `;
        calendarList.appendChild(divider);
        upcoming.forEach((item) => calendarList.appendChild(buildArchiveCard(item)));
      }

      document.getElementById('historyCalendarEmpty').classList.toggle('hidden', travelArchive.length > 0);

      if (typeof twemoji !== 'undefined') {
        twemoji.parse(document.getElementById('screen-history'), { folder: 'svg', ext: '.svg' });
      }
    }

    // ===== 아카이빙 상세: 월별 달력 오마주 + 도장 애니메이션 =====
    let archiveStampTimers = [];

    function clearArchiveStampTimers() {
      archiveStampTimers.forEach((t) => clearTimeout(t));
      archiveStampTimers = [];
    }

    function openArchiveDetail(item) {
      const modal = document.getElementById('archiveModal');
      const canvas = document.getElementById('archiveCanvas');
      const status = getArchiveStatus(item);

      clearArchiveStampTimers();

      // stack(콜라주 에셋)이 있는 모든 달은 풀 콜라주 화면, 없으면 준비중 안내
      if (item.stack) {
        // 콜라주 화면은 자체 제목/날짜를 그리므로 상단 헤더 텍스트는 비움
        document.getElementById('archiveHeaderTitle').textContent = '';
        document.getElementById('archiveHeaderSub').textContent = '';
        canvas.innerHTML = buildItalyArchiveMarkup(item);
        modal.classList.remove('hidden');
        requestAnimationFrame(() => runStampSequence());
        wireArchiveTapTargets();
      } else {
        document.getElementById('archiveHeaderTitle').textContent = `${item.flag} ${item.country} · ${item.city}`;
        document.getElementById('archiveHeaderSub').textContent = `${item.start} ~ ${item.end} · ${status.label}`;
        canvas.innerHTML = buildComingSoonMarkup(item);
        modal.classList.remove('hidden');
      }
    }

    function closeArchiveDetail() {
      clearArchiveStampTimers();
      document.getElementById('archiveModal').classList.add('hidden');
      document.getElementById('archiveCanvas').innerHTML = '';
      document.getElementById('archivePhotoLightbox').classList.add('hidden');
    }

    document.getElementById('archiveCloseBtn').addEventListener('click', closeArchiveDetail);
    document.getElementById('archiveBackdrop').addEventListener('click', closeArchiveDetail);

    // 콜라주 사진(스탬프)을 탭하면 확대해서 보여주고, 음악 플레이어는 재생 중 느낌을 토글
    // (실제 오디오 재생은 없는 데모 데이터라, 다른 mock 인터랙션들과 동일하게 시각 피드백만 제공)
    function wireArchiveTapTargets() {
      document.querySelectorAll('#archiveCanvas .archive-tappable').forEach((el) => {
        el.addEventListener('click', (e) => {
          e.stopPropagation();
          el.classList.add('tap-flash');
          setTimeout(() => el.classList.remove('tap-flash'), 120);
          if (el.dataset.stampName === 'player') {
            el.classList.toggle('is-playing');
            return;
          }
          openArchivePhotoLightbox(el.src, el.alt);
        });
      });
    }

    function openArchivePhotoLightbox(src, alt) {
      document.getElementById('archivePhotoLightboxImg').src = src;
      document.getElementById('archivePhotoLightboxImg').alt = alt || '';
      document.getElementById('archivePhotoLightbox').classList.remove('hidden');
    }
    document.getElementById('archivePhotoLightbox').addEventListener('click', () => {
      document.getElementById('archivePhotoLightbox').classList.add('hidden');
    });

    // 아직 오마주 화면이 없는 월: 안내
    function buildComingSoonMarkup(item) {
      return `
        <div class="absolute inset-0" style="background:linear-gradient(180deg,#1e3a5f 0%,#3182F6 100%);"></div>
        <div class="absolute inset-0 flex flex-col items-center justify-center text-white px-8 text-center">
          <div class="text-5xl mb-3">${item.flag}</div>
          <p class="text-lg font-bold mb-1">${item.country} · ${item.monthEn}</p>
          <p class="text-sm opacity-80">이 달의 여행 기록 콜라주는<br/>곧 만나보실 수 있어요</p>
        </div>
      `;
    }

    // 순차적으로 .stamp-el 에 stamped 클래스를 붙여 도장 애니메이션 실행
    function runStampSequence() {
      const els = Array.from(document.querySelectorAll('#archiveCanvas .stamp-el'));
      els.forEach((el, i) => {
        const delay = 250 + i * 320; // 첫 요소 후 약 0.32초 간격으로 하나씩
        const t = setTimeout(() => {
          el.classList.add('stamped');
        }, delay);
        archiveStampTimers.push(t);
      });
    }

    // ===== 여행 상세(범용): 상단 검은 영역(월 제목 + 확대 콜라주 + 뱃지) =====
    // + 하단 흰 영역(위치 → 일기 → 이번 여행의 순간들). 콜라주 안 요소 순차 도장.
    // 이탈리아는 MAY_STACK, 나머지 달은 ALL_STACKS[item.stack] 에셋 사용.
    function buildItalyArchiveMarkup(item) {
      let S = null;
      if (item.stack === 'italy') {
        S = (typeof MAY_STACK !== 'undefined') ? MAY_STACK : null;
      } else if (typeof ALL_STACKS !== 'undefined' && item.stack && ALL_STACKS[item.stack]) {
        S = ALL_STACKS[item.stack];
      }
      if (!S) return buildComingSoonMarkup(item);

      const status = (typeof getArchiveStatus === 'function') ? getArchiveStatus(item) : { label: '' };

      // --- 콜라주: 검은 영역을 꽉 채우도록 확대. 화면 폭 기준, 원본 비율 유지 ---
      const appW = 393;
      const sidePad = 24; // 좌우 여백 (하단 흰 영역과 동일)

      // 요소 회전: 요소명이 달마다 달라 index 기반으로 살짝씩 다른 각도 부여
      const rotSeq = [-8, 2, 4, 1, -2, -5, 7, 0, 3, -4, 6, -3];
      const stamps = S.order.map((name, i) => {
        const e = S.elems[name];
        if (!e) return '';
        const r = rotSeq[i % rotSeq.length];
        return `
          <img class="stamp-el archive-tappable" data-stamp-order="${i}" data-stamp-name="${name}" src="${e.img}"
            style="--stamp-rot:${r}deg;--stamp-tilt:${(r * 0.35).toFixed(1)}deg;
                   position:absolute;
                   left:${e.left}%;top:${e.top}%;width:${e.width}%;height:${e.height}%;
                   filter:drop-shadow(0 4px 10px rgba(0,0,0,0.45));" />
        `;
      }).join('');

      // 월 제목(대문자) + 날짜. 국가/월에 따라 자동 반영.
      const monthTitle = item.monthEn;
      const dEnd = new Date(item.end + 'T00:00:00');
      const dateLabel = `${dEnd.getFullYear()}. ${String(dEnd.getMonth() + 1).padStart(2, '0')}. ${String(dEnd.getDate()).padStart(2, '0')}`;

      // 여행 일기 = 이번 여행에서 산 화장품 구매 후기 (데이터에서 읽음)
      const diary = item.diary || `${item.city}에서의 소중한 기록들.`;

      // 이번 여행의 순간들 (데이터에서 읽음)
      const moments = (item.moments || []);
      const recordCount = S.order.length;
      // 월별 날씨/걸음수 (데이터에서 읽음, 없으면 기본값)
      const w = item.weather || { icon: '☀️', label: '맑음', temp: 26 };
      const wIcon = w.icon, wLabel = w.label, wTemp = w.temp;
      const stepsStr = (item.steps || 12400).toLocaleString('en-US');
      const scheduleItems = moments.map((s) => `
        <div style="display:flex;align-items:center;gap:12px;padding:13px 0;border-bottom:1px solid #f1f1f3;">
          <span style="width:9px;height:9px;border-radius:50%;background:${s.c};flex:0 0 auto;"></span>
          <span style="flex:1;font-size:14px;color:#1f2937;font-weight:600;">${s.t}</span>
          <span style="font-size:11px;font-weight:700;color:#6b7280;background:#f3f4f6;padding:4px 9px;border-radius:999px;">${s.tag}</span>
        </div>
      `).join('');

      return `
        <div class="absolute inset-0 overflow-y-auto" style="-webkit-overflow-scrolling:touch;background:#0d0d0f;">
          <!-- ===== 상단 검은 영역 ===== -->
          <div style="position:relative;background:#0d0d0f;padding:104px ${sidePad}px 22px;">
            <!-- 월 제목 + 흔들리는 국기 / 날짜 -->
            <div style="display:flex;align-items:flex-end;justify-content:space-between;margin-bottom:18px;">
              <h1 style="font-size:40px;font-weight:800;color:#fff;margin:0;letter-spacing:-1px;line-height:1;">
                ${monthTitle}<span style="color:#3182F6;">.</span>
              </h1>
              <span style="font-size:12px;color:#9ca3af;padding-bottom:4px;">${dateLabel}</span>
            </div>

            <!-- 확대 콜라주 (검은 영역 꽉 채움, 화면 폭 full-bleed, 테두리 없음) + 뱃지 오버레이 -->
            <div style="position:relative;width:${appW}px;margin:0 -${sidePad}px;">
              <div style="position:relative;width:${appW}px;height:${Math.round(appW * S.aspect)}px;overflow:hidden;background:#0d0d0f;">
                <img src="${S.base}" alt="${item.country} ${item.city} ${monthTitle} 콜라주"
                     style="position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;" />
                ${stamps}
                <!-- 위/아래 검은 그라데이션: 검은 영역과 부드럽게 이어지도록 -->
                <div style="position:absolute;left:0;right:0;top:0;height:110px;z-index:15;pointer-events:none;
                            background:linear-gradient(180deg,#0d0d0f 0%,rgba(13,13,15,0.6) 42%,rgba(13,13,15,0) 100%);"></div>
                <div style="position:absolute;left:0;right:0;bottom:0;height:130px;z-index:15;pointer-events:none;
                            background:linear-gradient(0deg,#0d0d0f 0%,rgba(13,13,15,0.6) 45%,rgba(13,13,15,0) 100%);"></div>
                <!-- 사진 위 하이라이트 뱃지 3개 (상단 오버레이) - 앱 다른 화면의 흰색 플랫 칩과 톤을 맞춤 -->
                <div style="position:absolute;left:${sidePad}px;right:${sidePad}px;top:14px;display:flex;gap:6px;flex-wrap:wrap;z-index:20;">
                  <span style="font-size:11px;font-weight:700;color:#374151;background:rgba(255,255,255,0.95);padding:5px 10px;border-radius:999px;box-shadow:0 1px 4px rgba(0,0,0,0.15);border:1px solid rgba(255,255,255,0.6);">${wIcon} ${wLabel} ${wTemp}°</span>
                  <span style="font-size:11px;font-weight:700;color:#374151;background:rgba(255,255,255,0.95);padding:5px 10px;border-radius:999px;box-shadow:0 1px 4px rgba(0,0,0,0.15);border:1px solid rgba(255,255,255,0.6);">🚶 ${stepsStr}보</span>
                  <span style="font-size:11px;font-weight:700;color:#374151;background:rgba(255,255,255,0.95);padding:5px 10px;border-radius:999px;box-shadow:0 1px 4px rgba(0,0,0,0.15);border:1px solid rgba(255,255,255,0.6);">📸 ${recordCount}개의 기록</span>
                </div>
              </div>
            </div>
          </div>

          <!-- ===== 하단 흰 영역: 위치(국가/일정) → 일기 → 이번 여행의 순간들 ===== -->
          <div style="background:#fff;border-radius:26px 26px 0 0;margin-top:-18px;position:relative;
                      padding:24px 24px 40px;min-height:200px;">
            <!-- 1) 위치 정보 (국가/일정) -->
            <div style="display:flex;align-items:center;gap:8px;">
              <span style="font-size:16px;">📍</span>
              <div>
                <p style="font-size:16px;font-weight:800;color:#111827;margin:0;letter-spacing:-0.3px;">${item.city}, ${item.country}</p>
                <p style="font-size:12px;color:#9ca3af;margin:2px 0 0;">${item.start} ~ ${item.end} · ${status.label || '여행'}</p>
              </div>
            </div>

            <!-- 2) 여행 일기 (화장품 구매 후기) -->
            <div style="margin-top:18px;background:#f9fafb;border-radius:16px;padding:16px 18px;">
              <p style="font-size:12px;font-weight:700;color:#9ca3af;margin:0 0 8px;">🛍️ 여행 일기 · 이번 여행의 득템</p>
              <p style="font-size:14px;line-height:1.7;color:#374151;margin:0;">${diary}</p>
            </div>

            <!-- 3) 이번 여행의 순간들 -->
            <p style="font-size:12px;font-weight:700;color:#9ca3af;margin:24px 0 4px;">이번 여행의 순간들</p>
            ${scheduleItems}
          </div>
        </div>
      `;
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
    .replace("__AVATAR_URI_5__", AVATAR_URIS[4])
    .replace("__CARE_IMG_TORRIDEN_BALANCEFUL__", CARE_IMG_TORRIDEN_BALANCEFUL)
    .replace("__CARE_IMG_BANILA_PRIMER__", CARE_IMG_BANILA_PRIMER)
    .replace("__CARE_IMG_KISSME_EYELINER__", CARE_IMG_KISSME_EYELINER)
    .replace("__CARE_IMG_ISNTREE_SUNCREAM__", CARE_IMG_ISNTREE_SUNCREAM)
    .replace("__CARE_IMG_SONATURAL_FIXER__", CARE_IMG_SONATURAL_FIXER)
    .replace("__CARE_IMG_GOODAL_VITAC__", CARE_IMG_GOODAL_VITAC)
    .replace("__CARE_IMG_DERMATORY_AMPOULE__", CARE_IMG_DERMATORY_AMPOULE)
    .replace("__CARE_IMG_BIODANCE_MASK__", CARE_IMG_BIODANCE_MASK)
    .replace("__CARE_IMG_ABIB_AQUAFIT__", CARE_IMG_ABIB_AQUAFIT)
    .replace("__CARE_IMG_TORRIDEN_DIVEIN__", CARE_IMG_TORRIDEN_DIVEIN)
    .replace("__CARE_IMG_ABIB_SERUM__", CARE_IMG_ABIB_SERUM)
    .replace("__CARE_IMG_TORRIDEN_LIP__", CARE_IMG_TORRIDEN_LIP)
    .replace("__CARE_IMG_HAIRPLUS_ESSENCE__", CARE_IMG_HAIRPLUS_ESSENCE)
    .replace("__CARE_IMG_ROUNDLAB_TONIC__", CARE_IMG_ROUNDLAB_TONIC)
    .replace("__CARE_IMG_BRINGGREEN_ALOE__", CARE_IMG_BRINGGREEN_ALOE)
    .replace("__CARD_IMG_TONER__", CARD_IMG_TONER)
    .replace("__CARD_IMG_SERUM__", CARD_IMG_SERUM)
    .replace("__CARD_IMG_SUNCREAM__", CARD_IMG_SUNCREAM)
    .replace("__CARD_IMG_DRG_CREAM__", CARD_IMG_DRG_CREAM)
    .replace("__CARD_IMG_CUSHION__", CARD_IMG_CUSHION)
    .replace("__CARD_IMG_EYEPALETTE__", CARD_IMG_EYEPALETTE)
    .replace("__CARD_IMG_CONTOUR__", CARD_IMG_CONTOUR)
    .replace("__CARD_IMG_TINT__", CARD_IMG_TINT)
    .replace("__CARD_IMG_BROW__", CARD_IMG_BROW)
    .replace("__CARD_IMG_HIGHLIGHTER__", CARD_IMG_HIGHLIGHTER)
    .replace("__POUCH_VISUAL_DRG_CREAM__", CARD_IMG_DRG_CREAM)
    .replace("__POUCH_VISUAL_TONER__", CARD_IMG_TONER)
    .replace("__POUCH_VISUAL_SERUM__", CARD_IMG_SERUM)
    .replace("__POUCH_VISUAL_SUNCREAM__", CARD_IMG_SUNCREAM)
    .replace("__POUCH_VISUAL_CUSHION__", CARD_IMG_CUSHION)
    .replace("__POUCH_VISUAL_EYEPALETTE__", CARD_IMG_EYEPALETTE)
    .replace("__POUCH_VISUAL_CONTOUR__", CARD_IMG_CONTOUR)
    .replace("__POUCH_VISUAL_TINT__", CARD_IMG_TINT)
    .replace("__POUCH_VISUAL_BROW__", CARD_IMG_BROW)
    .replace("__POUCH_VISUAL_HIGHLIGHTER__", CARD_IMG_HIGHLIGHTER)
)


for _archive_key, _archive_uri in ARCHIVE_URIS.items():
    HTML_PAGE = HTML_PAGE.replace(f"__{_archive_key}__", _archive_uri)

components.html(HTML_PAGE, height=852, scrolling=True)