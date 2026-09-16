import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")
```python
import streamlit as st

# -----------------------------
# 페이지 설정
# -----------------------------
st.set_page_config(
    page_title="MBTI 여행 처방전 💗",
    page_icon="🌷",
    layout="centered"
)

# -----------------------------
# 귀여운 CSS
# -----------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(
            135deg,
            #fff8fc 0%,
            #fff1f7 45%,
            #f4efff 100%
        );
    }

    .main-title {
        text-align: center;
        font-size: 46px;
        font-weight: 900;
        color: #ff79a5;
        margin-top: 15px;
        margin-bottom: 5px;
    }

    .sub-title {
        text-align: center;
        color: #9b8a99;
        font-size: 17px;
        margin-bottom: 25px;
    }

    .heart {
        text-align: center;
        font-size: 25px;
        letter-spacing: 8px;
    }

    .result-card {
        background: rgba(255, 255, 255, 0.92);
        border: 2px solid #ffd9e7;
        border-radius: 30px;
        padding: 30px;
        margin-top: 25px;
        box-shadow: 0 10px 30px rgba(255, 150, 190, 0.16);
    }

    .mbti-label {
        text-align: center;
        color: #ff79a5;
        font-size: 18px;
        font-weight: 800;
    }

    .place {
        text-align: center;
        color: #9b75d1;
        font-size: 38px;
        font-weight: 900;
        margin: 12px 0;
    }

    .travel-style {
        text-align: center;
        color: #777;
        font-size: 17px;
        font-weight: 700;
    }

    .section-title {
        color: #ff79a5;
        font-size: 18px;
        font-weight: 800;
        margin-top: 20px;
    }

    .text {
        color: #666;
        font-size: 16px;
        line-height: 1.8;
    }

    .cute-box {
        background: #fff5fa;
        border-radius: 20px;
        padding: 15px;
        text-align: center;
        color: #777;
        margin-top: 15px;
    }

    .footer {
        text-align: center;
        color: #b8aeb5;
        font-size: 13px;
        margin-top: 35px;
        padding-bottom: 20px;
    }

    div.stButton > button {
        width: 100%;
        border-radius: 25px;
        border: none;
        background: linear-gradient(
            90deg,
            #ff91b4,
            #c99bea
        );
        color: white;
        font-size: 17px;
        font-weight: 800;
        padding: 12px;
    }

    div.stButton > button:hover {
        transform: scale(1.02);
    }
</style>
""", unsafe_allow_html=True)


# -----------------------------
# 여행 데이터
# -----------------------------
travel_data = {

    "INTJ": {
        "place": "🇨🇭 스위스",
        "style": "조용하고 완벽한 계획형 여행 🏔️",
        "reason": "웅장한 자연을 차분하게 감상하면서 내가 세운 여행 계획을 하나씩 실현하기 좋아요.",
        "activity": "🚞 알프스 산악열차 · 🏔️ 자연 감상 · ☕ 조용한 카페"
    },

    "INTP": {
        "place": "🇯🇵 교토",
        "style": "호기심을 채우는 탐구 여행 🔎",
        "reason": "오랜 역사와 독특한 문화가 가득해서 새로운 것을 발견하는 재미가 있어요.",
        "activity": "⛩️ 사찰 탐방 · 🍵 다도 체험 · 📚 전통문화 구경"
    },

    "ENTJ": {
        "place": "🇬🇧 런던",
        "style": "알차고 야무진 도시 여행 👑",
        "reason": "볼거리와 즐길 거리가 많아서 효율적인 여행 계획을 세우는 재미가 있어요.",
        "activity": "🏛️ 박물관 · 🎡 런던 아이 · ☕ 감성 카페"
    },

    "ENTP": {
        "place": "🇪🇸 바르셀로나",
        "style": "즉흥과 모험이 가득한 여행 🎨",
        "reason": "새로운 사람과 장소를 만나고 예상하지 못했던 재미를 발견하기 좋아요.",
        "activity": "🏖️ 해변 · 🎨 가우디 건축 · 🍴 타파스"
    },

    "INFJ": {
        "place": "🇳🇿 뉴질랜드",
        "style": "마음까지 편안해지는 힐링 여행 🌿",
        "reason": "웅장한 자연 속에서 조용히 산책하며 나만의 시간을 보내기 좋아요.",
        "activity": "🥾 트레킹 · 🌌 별 보기 · 🏞️ 자연 산책"
    },

    "INFP": {
        "place": "🇫🇷 프랑스",
        "style": "감성을 가득 채우는 낭만 여행 💕",
        "reason": "예술과 음악, 예쁜 골목과 카페가 어우러져 감성적인 시간을 보내기 좋아요.",
        "activity": "🥐 카페 투어 · 🎨 미술관 · 📸 감성 사진"
    },

    "ENFJ": {
        "place": "🇮🇹 이탈리아",
        "style": "사랑하는 사람과 함께하는 따뜻한 여행 🍝",
        "reason": "맛있는 음식과 아름다운 풍경을 소중한 사람들과 함께 즐기기 좋아요.",
        "activity": "🍕 맛집 탐방 · 🍦 젤라또 · 🏛️ 역사 여행"
    },

    "ENFP": {
        "place": "🇵🇹 포르투갈",
        "style": "설렘이 가득한 자유 여행 🌈",
        "reason": "예쁜 풍경과 맛있는 음식, 새로운 경험이 가득해서 자유롭게 돌아다니기 좋아요.",
        "activity": "🚋 트램 타기 · 🌊 해안 산책 · 🍮 디저트 먹기"
    },

    "ISTJ": {
        "place": "🇩🇪 독일",
        "style": "깔끔하고 알찬 계획형 여행 🧳",
        "reason": "정돈된 도시와 역사적인 장소를 계획적으로 둘러보는 여행과 잘 어울려요.",
        "activity": "🏰 성 탐방 · 🚆 기차 여행 · 🥨 현지 음식"
    },

    "ISFJ": {
        "place": "🇯🇵 일본",
        "style": "포근하고 아기자기한 소확행 여행 🍡",
        "reason": "예쁜 골목과 맛있는 음식, 따뜻한 분위기 속에서 편안하게 여행할 수 있어요.",
        "activity": "🍡 디저트 · 🛍️ 소품샵 · ♨️ 온천"
    },

    "ESTJ": {
        "place": "🇺🇸 뉴욕",
        "style": "하루도 놓치지 않는 알찬 여행 🗽",
        "reason": "도시 곳곳에 볼거리가 많아서 하루 일정을 꽉 채워 즐기기 좋아요.",
        "activity": "🗽 랜드마크 · 🛍️ 쇼핑 · 🎭 공연"
    },

    "ESFJ": {
        "place": "🇰🇷 제주도",
        "style": "친구와 가족과 함께하는 행복 여행 🌸",
        "reason": "맛있는 음식과 아름다운 자연을 사랑하는 사람들과 함께 즐기기 좋아요.",
        "activity": "🌊 바다 · 🍊 카페 · 🚗 드라이브"
    },

    "ISTP": {
        "place": "🇨🇦 캐나다",
        "style": "자유롭게 떠나는 액티비티 여행 🏕️",
        "reason": "자연 속에서 직접 움직이며 새로운 경험을 즐기는 여행과 잘 어울려요.",
        "activity": "🏕️ 캠핑 · 🛶 카약 · 🥾 하이킹"
    },

    "ISFP": {
        "place": "🇬🇷 그리스",
        "style": "예쁜 풍경 속 감성 충전 여행 🩵",
        "reason": "푸른 바다와 아름다운 건축물을 천천히 감상하며 여유를 즐기기 좋아요.",
        "activity": "🌊 바다 구경 · 📸 사진 · 🌅 노을 감상"
    },

    "ESTP": {
        "place": "🇹🇭 태국",
        "style": "신나게 즐기는 액티비티 여행 🔥",
        "reason": "맛있는 음식부터 다양한 액티비티까지 재미있는 경험을 한 번에 즐길 수 있어요.",
        "activity": "🏝️ 섬 투어 · 🛵 도시 탐험 · 🍜 길거리 음식"
    },

    "ESFP": {
        "place": "🇦🇺 호주",
        "style": "즐거움이 끊이지 않는 여행 🎉",
        "reason": "활기찬 도시와 아름다운 자연을 모두 즐길 수 있어 여행의 재미가 가득해요.",
        "activity": "🏄 서핑 · 🐨 동물 체험 · 🌴 해변"
    }
}


# -----------------------------
# 제목
# -----------------------------
st.markdown(
    '<div class="heart">♡ ♡ ♡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">🌷 MBTI 여행 처방전 💗</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">너의 MBTI에게 딱 맞는 여행지를 찾아줄게! ✈️</div>',
    unsafe_allow_html=True
)


# -----------------------------
# MBTI 선택
# -----------------------------
st.markdown("### 💌 먼저 MBTI를 골라줘!")

mbti = st.selectbox(
    "나의 MBTI",
    list(travel_data.keys()),
    label_visibility="collapsed"
)

st.write("")


# -----------------------------
# 추천 버튼
# -----------------------------
if st.button("💖 나의 여행 처방전 확인하기"):

    data = travel_data[mbti]

    st.balloons()

    st.markdown(
        f"""
        <div class="result-card">

            <div class="mbti-label">
                ✨ {mbti}에게 내려진 여행 처방전 ✨
            </div>

            <div class="place">
                {data["place"]}
            </div>

            <div class="travel-style">
                {data["style"]}
            </div>

            <hr>

            <div class="section-title">
                💭 왜 여기가 어울릴까?
            </div>

            <div class="text">
                {data["reason"]}
            </div>

            <div class="section-title">
                🎀 여기서 꼭 해보기!
            </div>

            <div class="text">
                {data["activity"]}
            </div>

            <div class="cute-box">
                🧸 여행 가방 챙기고 설레는 마음만 가져가세요! 💕
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# -----------------------------
# 하단
# -----------------------------
st.markdown(
    '<div class="footer">Made with ♡ for your next adventure ✈️🌷</div>',
    unsafe_allow_html=True
)
```
