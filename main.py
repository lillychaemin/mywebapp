import streamlit as st

st.title("첫 배포 확인 👋")
st.write("여기까지 보이면 배포 성공입니다.")
```python
import streamlit as st

# ----------------------------------------
# 페이지 설정
# ----------------------------------------
st.set_page_config(
    page_title="MBTI 고전소설 처방전 💕",
    page_icon="📖",
    layout="centered"
)

# ----------------------------------------
# 귀여운 디자인
# ----------------------------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(
        135deg,
        #fff8fc 0%,
        #fff2f7 50%,
        #f5f0ff 100%
    );
}

.main-title {
    text-align: center;
    color: #e889a8;
    font-size: 45px;
    font-weight: 900;
    margin-top: 10px;
    margin-bottom: 5px;
}

.sub-title {
    text-align: center;
    color: #9a8c96;
    font-size: 17px;
    margin-bottom: 25px;
}

.deco {
    text-align: center;
    font-size: 25px;
    letter-spacing: 8px;
}

.book-card {
    background: rgba(255, 255, 255, 0.94);
    border: 2px solid #f6d6e2;
    border-radius: 30px;
    padding: 30px;
    margin-top: 25px;
    box-shadow: 0 10px 30px rgba(200, 140, 170, 0.16);
}

.mbti {
    text-align: center;
    color: #e889a8;
    font-size: 18px;
    font-weight: 800;
}

.book-title {
    text-align: center;
    color: #9a78c7;
    font-size: 32px;
    font-weight: 900;
    margin-top: 12px;
}

.author {
    text-align: center;
    color: #888;
    font-size: 16px;
    margin-bottom: 20px;
}

.description {
    color: #666;
    font-size: 16px;
    line-height: 1.8;
}

.section {
    color: #e889a8;
    font-size: 18px;
    font-weight: 800;
    margin-top: 20px;
    margin-bottom: 5px;
}

.cute-box {
    background: #fff4f8;
    border-radius: 20px;
    padding: 16px;
    margin-top: 20px;
    text-align: center;
    color: #888;
}

.footer {
    text-align: center;
    color: #b9aeb5;
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
        #ff9fbc,
        #c9a3ed
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


# ----------------------------------------
# MBTI별 고전소설 추천 데이터
# ----------------------------------------
books = {

    "INTJ": {
        "title": "1984",
        "author": "조지 오웰",
        "emoji": "👁️",
        "reason": "사회 구조와 인간의 자유에 대해 깊이 생각하는 것을 좋아한다면 잘 어울리는 작품이에요.",
        "point": "🧠 사회 · 권력 · 자유 · 인간의 사고",
        "message": "조용히 읽으면서 작품 속 세계를 분석해보는 시간을 가져보세요."
    },

    "INTP": {
        "title": "프랑켄슈타인",
        "author": "메리 셸리",
        "emoji": "⚡",
        "reason": "과학과 인간의 본질, 창조와 책임이라는 흥미로운 질문을 던지는 작품이에요.",
        "point": "🔬 과학 · 철학 · 인간 본성",
        "message": "책을 읽으며 '창조한 사람의 책임은 어디까지일까?' 생각해보세요."
    },

    "ENTJ": {
        "title": "레 미제라블",
        "author": "빅토르 위고",
        "emoji": "⚖️",
        "reason": "거대한 사회와 인간의 선택을 다루는 장대한 이야기를 좋아한다면 잘 맞아요.",
        "point": "⚔️ 사회 · 정의 · 변화 · 인간",
        "message": "등장인물들의 선택과 그 결과를 따라가며 읽어보세요."
    },

    "ENTP": {
        "title": "돈키호테",
        "author": "미겔 데 세르반테스",
        "emoji": "🐴",
        "reason": "엉뚱하고 자유로운 상상력과 풍자를 좋아한다면 재미있게 읽을 수 있어요.",
        "point": "🎭 모험 · 유머 · 풍자 · 상상",
        "message": "현실과 상상의 경계가 어떻게 뒤섞이는지 찾아보세요!"
    },

    "INFJ": {
        "title": "데미안",
        "author": "헤르만 헤세",
        "emoji": "🦋",
        "reason": "자아와 성장, 자신의 내면을 탐색하는 이야기를 좋아한다면 잘 어울려요.",
        "point": "🌙 성장 · 자아 · 내면 · 삶",
        "message": "주인공의 성장 과정에서 나와 비슷한 순간을 찾아보세요."
    },

    "INFP": {
        "title": "어린 왕자",
        "author": "앙투안 드 생텍쥐페리",
        "emoji": "🌹",
        "reason": "따뜻하면서도 깊은 의미가 담긴 이야기를 좋아하는 사람에게 잘 어울려요.",
        "point": "🌟 사랑 · 우정 · 관계 · 순수함",
        "message": "책을 읽고 '나에게 정말 소중한 것은 무엇일까?' 생각해보세요."
    },

    "ENFJ": {
        "title": "작은 아씨들",
        "author": "루이자 메이 올컷",
        "emoji": "🏡",
        "reason": "사람 사이의 관계와 성장, 가족의 따뜻함을 좋아한다면 잘 맞는 작품이에요.",
        "point": "💕 가족 · 성장 · 우정 · 꿈",
        "message": "네 자매의 서로 다른 꿈과 성장을 비교하며 읽어보세요."
    },

    "ENFP": {
        "title": "이상한 나라의 앨리스",
        "author": "루이스 캐럴",
        "emoji": "🐇",
        "reason": "상상력이 풍부하고 엉뚱하고 신비로운 세계를 좋아한다면 딱이에요!",
        "point": "🎀 모험 · 상상 · 판타지 · 호기심",
        "message": "현실에서는 절대 볼 수 없는 이상한 세계를 마음껏 즐겨보세요."
    },

    "ISTJ": {
        "title": "오만과 편견",
        "author": "제인 오스틴",
        "emoji": "💌",
        "reason": "인물들의 관계와 사회적 배경을 차분하게 관찰하며 읽는 재미가 있어요.",
        "point": "🎩 사랑 · 사회 · 관계 · 편견",
        "message": "등장인물들이 처음 서로를 어떻게 판단하는지 주목해보세요."
    },

    "ISFJ": {
        "title": "비밀의 화원",
        "author": "프랜시스 호지슨 버넷",
        "emoji": "🌷",
        "reason": "따뜻한 분위기와 치유, 우정이 담긴 이야기를 좋아한다면 잘 맞아요.",
        "point": "🌱 우정 · 자연 · 치유 · 성장",
        "message": "비밀의 정원이 등장인물들에게 어떤 변화를 주는지 살펴보세요."
    },

    "ESTJ": {
        "title": "삼총사",
        "author": "알렉상드르 뒤마",
        "emoji": "⚔️",
        "reason": "빠른 전개와 목표를 향해 나아가는 모험 이야기를 좋아한다면 추천해요.",
        "point": "🗡️ 모험 · 우정 · 용기 · 액션",
        "message": "네 친구의 우정과 모험을 따라가며 신나게 읽어보세요."
    },

    "ESFJ": {
        "title": "빨간 머리 앤",
        "author": "루시 모드 몽고메리",
        "emoji": "🌸",
        "reason": "밝고 따뜻한 인간관계와 사랑스러운 캐릭터를 좋아한다면 잘 맞아요.",
        "point": "🌼 우정 · 가족 · 성장 · 긍정",
        "message": "앤의 상상력과 주변 사람들과의 관계 변화를 즐겨보세요."
    },

    "ISTP": {
        "title": "보물섬",
        "author": "로버트 루이스 스티븐슨",
        "emoji": "🏴‍☠️",
        "reason": "모험과 긴장감 넘치는 사건을 직접 따라가는 듯한 재미를 느낄 수 있어요.",
        "point": "🗺️ 모험 · 보물 · 바다 · 탐험",
        "message": "보물 지도를 들고 모험을 떠난다는 느낌으로 읽어보세요!"
    },

    "ISFP": {
        "title": "제인 에어",
        "author": "샬럿 브론테",
        "emoji": "🌿",
        "reason": "섬세한 감정과 아름다운 분위기, 자신의 삶을 개척하는 이야기가 담겨 있어요.",
        "point": "🌹 사랑 · 독립 · 감정 · 성장",
        "message": "주인공이 자신의 가치와 선택을 지켜가는 모습을 느껴보세요."
    },

    "ESTP": {
        "title": "모비 딕",
        "author": "허먼 멜빌",
        "emoji": "🐋",
        "reason": "거대한 목표를 향해 돌진하는 모험과 긴장감 넘치는 이야기를 좋아한다면 추천해요.",
        "point": "🌊 바다 · 모험 · 도전 · 집념",
        "message": "끝없이 펼쳐지는 바다에서 펼쳐지는 거대한 모험을 즐겨보세요."
    },

    "ESFP": {
        "title": "위대한 개츠비",
        "author": "F. 스콧 피츠제럴드",
        "emoji": "🥂",
        "reason": "화려한 분위기와 사람들의 관계, 사랑과 꿈에 관한 이야기를 좋아한다면 잘 맞아요.",
        "point": "✨ 사랑 · 꿈 · 파티 · 인간관계",
        "message": "화려함 뒤에 숨겨진 등장인물들의 진짜 마음을 찾아보세요."
    }
}


# ----------------------------------------
# 제목
# ----------------------------------------
st.markdown(
    '<div class="deco">♡ 📖 ♡ 📚 ♡</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-title">📖 MBTI 고전소설 처방전 💗</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="sub-title">너의 성격에 어울리는 한 권의 이야기를 찾아줄게 🌷</div>',
    unsafe_allow_html=True
)


# ----------------------------------------
# MBTI 선택
# ----------------------------------------
st.markdown("### 💌 너의 MBTI는 무엇인가요?")

mbti = st.selectbox(
    "MBTI 선택",
    list(books.keys()),
    label_visibility="collapsed"
)

st.write("")


# ----------------------------------------
# 추천 버튼
# ----------------------------------------
if st.button("💗 나에게 맞는 고전소설 찾기"):

    book = books[mbti]

    st.balloons()

    st.markdown(
        f"""
        <div class="book-card">

            <div class="mbti">
                ✨ {mbti} 독자를 위한 오늘의 책 ✨
            </div>

            <div class="book-title">
                {book["emoji"]} {book["title"]}
            </div>

            <div class="author">
                ✍️ {book["author"]}
            </div>

            <hr>

            <div class="section">
                💭 이 책을 추천하는 이유
            </div>

            <div class="description">
                {book["reason"]}
            </div>

            <div class="section">
                🌷 이런 이야기가 담겨 있어요
            </div>

            <div class="description">
                {book["point"]}
            </div>

            <div class="section">
                🧸 읽을 때 이런 생각을 해보세요
            </div>

            <div class="description">
                {book["message"]}
            </div>

            <div class="cute-box">
                📚 오늘 하루, 책 한 권과 조금 특별한 시간을 보내보세요 💕
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )

else:

    st.markdown(
        """
        <div class="book-card">

            <div style="text-align:center; font-size:24px;">
                🧸 책장을 열어볼까요?
            </div>

            <div style="
                text-align:center;
                color:#999;
                margin-top:12px;
                line-height:1.8;
            ">
                MBTI를 선택하고<br>
                💗 버튼을 눌러 나만의 고전소설을 찾아보세요!
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ----------------------------------------
# 푸터
# ----------------------------------------
st.markdown(
    '<div class="footer">Made with ♡ and 📚 for curious readers</div>',
    unsafe_allow_html=True
)
```
