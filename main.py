import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="MBTI 직업 추천기", layout="centered")

# MBTI별 직업 추천 데이터 (예시)
mbti_jobs = {
    "ISTJ": ["회계사", "공무원", "데이터 분석가"],
    "ISFJ": ["간호사", "초등교사", "상담사"],
    "INFJ": ["심리학자", "작가", "NGO 활동가"],
    "INTJ": ["전략기획자", "데이터 사이언티스트", "엔지니어"],
    "ISTP": ["기계공", "응급 구조사", "파일럿"],
    "ISFP": ["디자이너", "플로리스트", "요리사"],
    "INFP": ["시인", "소설가", "예술가"],
    "INTP": ["연구원", "프로그래머", "이론물리학자"],
    "ESTP": ["기업가", "세일즈 전문가", "스턴트맨"],
    "ESFP": ["배우", "이벤트 플래너", "방송인"],
    "ENFP": ["마케터", "콘텐츠 크리에이터", "기획자"],
    "ENTP": ["스타트업 창업자", "변호사", "정치 전략가"],
    "ESTJ": ["경영자", "군인", "프로젝트 매니저"],
    "ESFJ": ["인사담당자", "고객지원 매니저", "간호 관리자"],
    "ENFJ": ["교육자", "코치", "사회운동가"],
    "ENTJ": ["CEO", "변호사", "비즈니스 컨설턴트"]
}

# 타이틀
st.title("🧠 MBTI 기반 직업 추천기")

# 사용자 입력
selected_mbti = st.selectbox("당신의 MBTI 유형을 선택하세요:", sorted(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"🔎 {selected_mbti} 유형에게 어울리는 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
