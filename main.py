import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")
python
import streamlit as st

# --------------------------------------------------
# 기본 설정
# --------------------------------------------------
st.set_page_config(
    page_title="MBTI Travel 💗",
    page_icon="🌷",
    layout="centered"
)

# --------------------------------------------------
# CSS
# --------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(135deg, #fff7fb 0%, #f5f1ff 100%);
    }

    .title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: #ff6f91;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #777;
        margin-bottom: 30px;
    }

    .card {
        background: rgba(255, 255, 255, 0.9);
        border-radius: 25px;
        padding: 28px;
        margin-top: 25px;
        box-shadow: 0 8px 25px rgba(180, 130, 170, 0.15);
        border: 1px solid #f5dce8;
    }

    .destination {
        text-align: center;
        font-size: 38px;
        font-weight: 800;
        color: #9b72cf;
        margin: 10px 0;
    }

    .tag {
        text-align: center;
        color: #ff6f91;
        font-size: 17px;
        font-weight: 600;
    }

    .reason {
        font-size: 17px;
        line-height: 1.8;
        color: #555;
    }

    .footer {
        text-align: center;
        color: #aaa;
        margin-top: 40px;
        font-size: 14px;
    }

    div.stButton > button {
        border-radius: 20px;
        border: none;
        background: #ff8fab;
        color: white;
        font-weight: bold;
        padding: 10px 25px;
    }
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# MBTI 데이터
# --------------------------------------------------
travel_data = {
    "INTJ": {
        "place": "🇨🇭 스위스",
        "style": "차분하게 계획하는 전략가 여행 ✨",
        "reason": "아름다운 자연을 여유롭게 감상하면서 자신만의 여행 계획을 실현하기 좋은 곳이에요.",
        "activity": "🏔️ 알프스 감상 · 🚞 산악열차 · ☕ 조용한 카페"
    },
    "INTP": {
        "place": "🇯🇵 교토",
        "style": "호기심 가득한 탐구 여행 🔎",
        "reason": "역사와 전통, 독특한 문화가 가득해서 새로운 것을 알아가는 재미가 있어요.",
        "activity": "⛩️ 사찰 탐방 · 📚 전통문화 체험 · 🍵 다도"
    },
    "ENTJ": {
        "place": "🇬🇧 런던",
        "style": "알차고 야무진 리더 여행 👑",
        "reason": "볼거리와 즐길 거리가 많아서 효율적으로 여행 일정을 구성하는 재미가 있어요.",
        "activity": "🏛️ 박물관 · ☕ 런던 카페 · 🎡 런던 아이"
    },
    "ENTP": {
        "place": "🇪🇸 바르셀로나",
        "style": "즉흥과 모험이 가득한 여행 🎨",
        "reason": "새로운 장소와 사람을 만나고 예상하지 못한 경험을 즐기기에 딱 좋은 여행지예요.",
        "activity": "🏖️ 해변 · 🎨 가우디 건축 · 🍴 타파스"
    },
    "INFJ": {
        "place": "🇳🇿 뉴질랜드",
        "style": "마음이 편안해지는 힐링 여행 🌿",
        "reason": "웅장한 자연 속에서 조용히 생각하고 자신만의 시간을 보내기 좋아요.",
        "activity": "🏞️ 자연 산책 · 🌌 별 보기 · 🥾 트레킹"
    },
    "INFP": {
        "place": "🇫🇷 프랑스",
        "style": "감성을 충전하는 낭만 여행 💕",
        "reason": "예술과 음악, 예쁜 골목과 카페가 어우러져 감성적인 여행을 즐기기 좋아요.",
        "activity": "🥐 카페 투어 · 🎨 미술관 · 📸 감성 사진"
    },
    "ENFJ": {
        "place": "🇮🇹 이탈리아",
        "style": "사람과 함께 즐기는 따뜻한 여행 🍝",
        "reason": "맛있는 음식과 아름다운 도시를 사랑하는 사람들과 함께 즐기기 좋은 곳이에요.",
        "activity": "🍕 맛집 투어 · 🏛️ 역사 탐방 · 🍦 젤라또"
    },
    "ENFP": {
        "place": "🇵🇹 포르투갈",
        "style": "설렘 가득한 자유 여행 🌈",
        "reason": "예쁜 풍경과 맛있는 음식, 새로운 경험이 가득해서 자유로운 여행을 즐기기 좋아요.",
        "activity": "🚋 트램 · 🌊 해안 산책 · 🍮 에그타르트"
    },
    "ISTJ": {
        "place": "🇩🇪 독일",
        "style": "깔끔하고 알찬 계획형 여행 🧳",
        "reason": "정돈된 도시와 다양한 역사적 장소를 계획적으로 둘러보기 좋아요.",
        "activity": "🏰 성 탐방 · 🚆 기차 여행 · 🍺 전통 음식"
    },
    "ISFJ": {
        "place": "🇯🇵 일본",
        "style": "편안하고 따뜻한 소확행 여행 🍡",
        "reason": "아기자기한 거리와 맛있는 음식, 편안한 분위기 속에서 여유를 즐길 수 있어요.",
        "activity": "🍡 디저트 · 🛍️ 소품샵 · ♨️ 온천"
    },
    "ESTJ": {
        "place": "🇺🇸 뉴욕",
        "style": "바쁘지만 알찬 도시 여행 🗽",
        "reason": "짧은 시간에도 다양한 명소를 효율적으로 돌아다니며 성취감을 느낄 수 있어요.",
        "activity": "🗽 랜드마크 · 🛍️ 쇼핑 · 🎭 브로드웨이"
    },
    "ESFJ": {
        "place": "🇰🇷 제주도",
        "style": "사랑하는 사람과 함께하는 여행 🌸",
        "reason": "맛있는 음식과 아름다운 자연을 가족이나 친구와 함께 즐기기에 좋아요.",
        "activity": "🌊 바다 · 🍊 카페 · 🚗 드라이브"
    },
    "ISTP": {
        "place": "🇨🇦 캐나다",
        "style": "자유롭게 떠나는 액티비티 여행 🏕️",
        "reason": "자연 속에서 직접 움직이고 새로운 경험을 즐기는 여행과 잘 어울려요.",
        "activity": "🏕️ 캠핑 · 🛶 카약 · 🏔️ 하이킹"
    },
    "ISFP": {
        "place": "🇬🇷 그리스",
        "style": "예쁜 풍경 속 감성 여행 🩵",
        "reason": "아름다운 바다와 건축물을 천천히 즐기면서 감성을 충전하기 좋아요.",
        "activity": "🌊 바다 · 📸 사진 · 🌅 노을 감상"
    },
    "ESTP": {
        "place": "🇹🇭 태국",
        "style": "신나게 즐기는 액티비티 여행 🔥",
        "reason": "맛있는 음식부터 액티비티까지 다양한 경험을 한 번에 즐길 수 있어요.",
        "activity": "🏝️ 섬 투어 · 🛵 시내 탐험 · 🍜 길거리 음식"
    },
    "ESFP": {
        "place": "🇦🇺 호주",
        "style": "즐거움이 끊이지 않는 여행 🎉",
        "reason": "활기찬 도시와 아름다운 자연을 모두 즐길 수 있어 에너지 넘치는 여행에 잘 어울려요.",
        "activity": "🏄 서핑 · 🐨 동물 체험 · 🌴 해변"
    }
}

# --------------------------------------------------
# 화면
# --------------------------------------------------
st.markdown('<div class="title">🌷 MBTI TRAVEL 💗</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">너의 MBTI에 딱 맞는 여행지를 찾아볼까? ✈️</div>',
    unsafe_allow_html=True
)

st.write("")

mbti = st.selectbox(
    "💌 나의 MBTI를 선택해줘!",
    list(travel_data.keys())
)

st.write("")

if st.button("💖 나에게 맞는 여행지 찾기", use_container_width=True):

    data = travel_data[mbti]

    st.markdown(
        f"""
        <div class="card">
            <div class="tag">✨ {mbti}에게 추천하는 여행 ✨</div>
            <div class="destination">{data["place"]}</div>
            <div class="tag">{data["style"]}</div>
            <hr>
            <p class="reason">
                💭 <b>추천 이유</b><br>
                {data["reason"]}
            </p>
            <p class="reason">
                🎀 <b>이곳에서 해보면 좋은 것</b><br>
                {data["activity"]}
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.balloons()

else:
    st.markdown(
        """
        <div class="card">
            <div style="text-align:center; font-size:22px;">
                🧸 아직 여행지가 비어 있어요!
            </div>
            <div style="text-align:center; color:#888; margin-top:10px;">
                MBTI를 선택하고 버튼을 눌러보세요 💕
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown(
    '<div class="footer">Made with 💗 for your next adventure ✈️</div>',
    unsafe_allow_html=True
)
