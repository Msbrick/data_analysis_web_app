import streamlit as st
import pandas as pd

# 임의의 가상 레고 제품 데이터 생성
data = {
    '제품명': ['레고 스타워즈 X윙', '레고 해리포터 호그와트', '레고 시티 소방서', '레고 테크닉 스포츠카', '레고 프렌즈 카페'],
    '판매량': [15000, 12000, 9000, 7000, 5000],
    '시리즈': ['스타워즈', '해리포터', '시티', '테크닉', '프렌즈'],
    '이미지URL': [
        'https://example.com/xwing.jpg',
        'https://example.com/hogwarts.jpg',
        'https://example.com/firestation.jpg',
        'https://example.com/sportscar.jpg',
        'https://example.com/cafe.jpg',
    ]
}

df = pd.DataFrame(data)

# 판매량 기준 내림차순 정렬
df_sorted = df.sort_values(by='판매량', ascending=False)

# 가장 인기 많은 레고 제품 1개 추출
most_popular_lego = df_sorted.iloc[0]

# 출력
st.write("### 가장 인기 많은 레고 제품")
st.write(f"**제품명:** {most_popular_lego['제품명']}")
st.write(f"**판매량:** {most_popular_lego['판매량']}")
st.write(f"**시리즈:** {most_popular_lego['시리즈']}")

# 이미지 출력 (예시 URL이므로 실제 URL로 교체 필요)
st.image(most_popular_lego['이미지URL'], width=300)
