import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# [필수] 페이지 설정 (최상단 선언)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="춘향전 줄거리 빈칸 채우기",
    layout="wide"
)

# 기본 스타일 설정
st.markdown("""
    <style>
    .main-title {
        text-align: center;
        font-size: 2rem;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 8px;
    }
    .sub-title {
        text-align: center;
        font-size: 1rem;
        color: #7f8c8d;
        margin-bottom: 25px;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">📜 춘향전 줄거리 어휘 빈칸 채우기</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">중학교 2학년 국어 | 줄거리를 읽고 빈칸에 들어갈 알맞은 단어를 작성하세요.</div>', unsafe_allow_html=True)

# 줄거리 빈칸 문제 데이터셋
quiz_data = [
    {
        "번호": 1,
        "지문": "조선 시대 남원 부사의 아들 이몽룡은 단옷날 광한루에 놀러 갔다가 기생 월매의 딸 ( ① )을/를 보고 첫눈에 반하게 된다.",
        "정답": "성춘향",
        "힌트": "여주인공 이름"
    },
    {
        "번호": 2,
        "지문": "두 사람은 백년가약을 맺고 사랑을 나누지만, 이몽룡의 아버지가 한양으로 관직을 옮기게 되면서 두 사람은 ( ② )을/를 맞이하게 된다.",
        "정답": "이별",
        "힌트": "헤어짐"
    },
    {
        "번호": 3,
        "지문": "새로 부임한 신관 사또 ( ③ )은/는 춘향이에게 수청을 들라고 강요하지만, 춘향은 정절을 지키기 위해 이를 거절한다.",
        "정답": "변학도",
        "힌트": "탐관오리 사또"
    },
    {
        "번호": 4,
        "지문": "수청을 거절하여 옥에 갇힌 춘향을 뒤로하고, 한양으로 간 이몽룡은 과거 시험에 합격하여 ( ④ )(으)로 내려오게 된다.",
        "정답": "암행어사",
        "힌트": "임금의 특명을 받은 벼슬"
    },
    {
        "번호": 5,
        "지문": "변학도의 생일 잔칫날, 이몽룡은 \"( ⑤ ) 출두야!\"를 외치며 탐관오리를 처단하고 춘향을 구출하여 한양으로 함께 올라간다.",
        "정답": "어사",
        "힌트": "출두 구호"
    }
]

# 세션 상태 초기화
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

st.subheader("✍️ 문제 풀기")

with st.form(key="story_quiz_form"):
    for item in quiz_data:
        idx = item["번호"]
        text = item["지문"]
        
        st.markdown(f"**문제 {idx}.** {text}")
        st.session_state.user_answers[idx] = st.text_input(
            f"정답 입력 #{idx}",
            key=f"input_{idx}",
            label_visibility="collapsed",
            placeholder=f"답안 작성 (힌트: {item['힌트']})"
        )
        st.divider()
        
    submit_btn = st.form_submit_button(label="💯 정답 제출 및 채점하기")

# 채점 결과 및 상세 확인
if submit_btn:
    score = 0
    total = len(quiz_data)
    
    for item in quiz_data:
        idx = item["번호"]
        correct = item["정답"].strip()
        user_input = st.session_state.user_answers.get(idx, "").strip()
        if user_input == correct:
            score += 1
            
    st.success(f"🎉 채점 완료! 내 점수: {score} / {total} 점")
    
    results = []
    for item in quiz_data:
        idx = item["번호"]
        correct = item["정답"]
        user_input = st.session_state.user_answers.get(idx, "").strip()
        status = "✅ 정답" if user_input == correct else f"❌ 오답 (정답: {correct})"
        results.append({
            "번호": idx,
            "내가 작성한 답": user_input if user_input else "(미입력)",
            "정답": correct,
            "채점 결과": status
        })
        
    st.subheader("📋 상세 채점 결과표")
    st.table(pd.DataFrame(results))