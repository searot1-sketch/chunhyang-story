import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# [필수] 페이지 설정 (최상단 선언)
# -----------------------------------------------------------------------------
st.set_page_config(
    page_title="춘향전 줄거리 쓰기 (20문제)",
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

st.markdown('<div class="main-title">📜 「춘향전」 줄거리 쓰기</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">중학교 2학년 국어 | 줄거리를 읽고 빈칸(1~20)에 들어갈 알맞은 단어를 써봅시다.</div>', unsafe_allow_html=True)

# 20개 빈칸 문제 데이터셋
quiz_data = [
    {"번호": 1, "정답": "성춘향", "힌트": "기생 월매의 딸 / 여주인공"},
    {"번호": 2, "정답": "이별", "힌트": "몽룡의 이사로 인한 헤어짐"},
    {"번호": 3, "정답": "변학도", "힌트": "남원 부사로 새로 부임해 온 인물"},
    {"번호": 4, "정답": "탐관오리", "힌트": "자신의 욕심만 채우는 부패한 관리"},
    {"번호": 5, "정답": "수청", "힌트": "사또를 모시는 일"},
    {"번호": 6, "정답": "정절", "힌트": "지조와 함께 지키고자 한 마음 (또는 절개)"},
    {"번호": 7, "정답": "옥", "힌트": "감옥"},
    {"번호": 8, "정답": "장원급제", "힌트": "과거 시험에 1등으로 합격함"},
    {"번호": 9, "정답": "암행어사", "힌트": "지방 관리를 감찰하는 임금의 특사"},
    {"번호": 10, "정답": "걸인", "뜻풀이": "초라한 차림의 거지/거지 꼴"},
    {"번호": 11, "정답": "생일", "힌트": "변 사또의 잔치가 열린 계기"},
    {"번호": 12, "정답": "개다리소반", "힌트": "귀퉁이가 깨진 질 낮은 밥상"},
    {"번호": 13, "정답": "한시", "힌트": "관리들의 탐욕을 비판하는 시"},
    {"번호": 14, "정답": "육모 방망이", "힌트": "역졸들이 들고 들이닥친 무기"},
    {"번호": 15, "정답": "어사", "힌트": "'OO 출두야!'"},
    {"번호": 16, "정답": "용수", "힌트": "갓 대신 머리에 쓴 것"},
    {"번호": 17, "정답": "우스꽝스러운", "힌트": "도망치는 모양새 (또는 우스운)"},
    {"번호": 18, "정답": "정렬부인", "힌트": "임금이 춘향에게 내린 칭호"},
    {"번호": 19, "정답": "풍자", "힌트": "부패한 사회를 돌려 비판함"},
    {"번호": 20, "정답": "해학", "힌트": "웃음을 자아내는 표현 기법"}
]

# 사용자 입력 저장용 세션 상태
if 'user_answers' not in st.session_state:
    st.session_state.user_answers = {}

# 본문 지문 제시
st.subheader("📖 본문 읽기 및 빈칸 입력")

story_html = """
<div style="background-color: #f9f9f9; padding: 25px; border-radius: 10px; border: 1px solid #e0e0e0; line-height: 2.0; font-size: 1.05rem;">
전라도 남원 부사의 아들인 이몽룡은 단오날 광한루에 구경을 나갔다가, 기생 월매의 딸 <b>( 1 )</b>을/를 보고 첫눈에 반해 서로 인연을 맺게 된다. 두 사람은 행복한 시간을 보내지만, 몽룡의 아버지가 한양으로 관직을 옮기게 되면서 어쩔 수 없이 <b>( 2 )</b>을/를 하게 된다.<br><br>

몽룡이 떠난 후 남원 부사로 새롭게 부임해 온 <b>( 3 )</b>은/는 백성들을 돌보기는커녕 자신의 욕심만 채우는 <b>( 4 )</b>의 모습을 보인다. 그는 부임하자마자 춘향에게 자신을 모시는 <b>( 5 )</b>을/를 들라고 강요한다. 하지만 춘향은 몽룡을 향한 지조와 <b>( 6 )</b>을/를 지키기 위해 이를 단호히 거절하고, 화가 난 변 사또는 춘향을 포악하다는 핑계로 <b>( 7 )</b>에 가두어 버린다.<br><br>

한편 한양으로 올라간 몽룡은 학업에 매진하여 과거 시험에서 <b>( 8 )</b>을/를 하게 되고, 임금으로부터 지방 관리를 감찰하는 <b>( 9 )</b>의 직책을 받는다. 몽룡은 신분을 숨긴 채 초라한 <b>( 10 )</b>의 차림을 하고 남원으로 내려와, 변 사또의 <b>( 11 )</b> 잔치가 열리고 있는 관아로 찾아간다.<br><br>

잔칫상에서 다른 수령들은 화려한 다담상을 받는 반면, 몽룡 앞에는 귀퉁이가 깨진 <b>( 12 )</b>에 콩나물과 깍두기, 막걸리 한 사발만 차려진다. 몽룡은 굴하지 않고 백성들의 피와 기름을 쥐어짜는 관리들의 탐욕을 비판하는 <b>( 13 )</b> 한 수를 지어 남긴다. 시의 내용을 본 수령들은 몽룡이 암행어사임을 직감하고 놀라 서둘러 관아를 빠져나간다.<br><br>

술에 취해 사정을 알지 못하던 변 사또가 춘향을 끌어내라고 명령하는 순간, 정파역 역졸들이 <b>( 14 )</b>을/를 들고 "<b>( 15 )</b> 출두야!"를 외치며 관아로 들이닥친다. 놀란 관직들과 사또는 갓 대신 <b>( 16 )</b>을/를 쓰거나 송편과 유밀과를 쥐는 등 <b>( 17 )</b> 방식으로 도망치며 횡설수설한다.<br><br>

마침내 관아를 정돈하고 마루에 앉은 어사또는 변 사또의 벼슬을 박탈하고, 감옥에 갇힌 춘향을 불러내어 모르는 척 다시 한번 수청을 들라고 시험한다. 춘향은 "높은 바위가 바람에 무너지며, 푸른 나무가 눈 온다고 빛이 변하겠느냐"며 끝까지 절개를 지키는 말을 한다. 이에 몽룡은 자신의 정체를 드러내고 두 사람은 기쁨의 재회를 한다.<br><br>

이후 몽룡은 춘향과 모녀를 한양으로 데려가고, 임금은 몽룡에게 높은 벼슬을 내리는 한편 춘향에게는 <b>( 18 )</b>이라는 칭호를 내린다. 춘향과 몽룡은 세 아들과 세 딸을 두고 오래도록 행복하게 살았으며, 이 소설은 불합리한 신분 사회와 관리의 부패를 <b>( 19 )</b>과/와 <b>( 20 )</b>의 표현 기법을 통해 효과적으로 보여준다.
</div>
"""
st.markdown(story_html, unsafe_allow_html=True)
st.write("---")

# 답안 입력 폼 (2열 배치)
st.subheader("✍️ 답안 작성하기")

with st.form(key="quiz_form_20"):
    cols = st.columns(2)  # 화면을 2열로 나눠 깔끔하게 표시
    
    for i, item in enumerate(quiz_data):
        idx = item["번호"]
        col = cols[i % 2]
        
        with col:
            st.session_state.user_answers[idx] = st.text_input(
                f"빈칸 ({idx})번 답안",
                key=f"input_{idx}",
                placeholder=f"({idx})번 정답 입력"
            )
            
    submit_btn = st.form_submit_button(label="💯 20문제 전체 정답 제출 및 자동 채점")

# 채점 결과 출력
if submit_btn:
    score = 0
    total = len(quiz_data)
    
    for item in quiz_data:
        idx = item["번호"]
        correct = item["정답"].strip()
        user_input = st.session_state.user_answers.get(idx, "").strip()
        
        # 유연한 채점 (공백 제거 및 부분 인정)
        if user_input == correct:
            score += 1
        elif idx == 6 and user_input in ["절개", "정절"]: # 6번 정절/절개 유연 채점
            score += 1
        elif idx == 17 and user_input in ["우스꽝스러운", "우스운", "해학적인"]:
            score += 1

    st.success(f"🎉 채점 완료! 학생 점수: {score} / {total} 점")
    
    results = []
    for item in quiz_data:
        idx = item["번호"]
        correct = item["정답"]
        user_input = st.session_state.user_answers.get(idx, "").strip()
        
        status = "✅ 정답" if (user_input == correct or (idx == 6 and user_input == "절개")) else f"❌ 오답 (정답: {correct})"
        
        results.append({
            "번호": f"({idx})번",
            "내가 적은 답": user_input if user_input else "(미입력)",
            "정답": correct,
            "채점 결과": status
        })
        
    st.subheader("📋 상세 채점 결과표")
    st.table(pd.DataFrame(results))
