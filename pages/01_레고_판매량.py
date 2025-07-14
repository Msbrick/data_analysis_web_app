import streamlit as st
import plotly.express as px
import pandas as pd

st.title("가장 많이 팔린 레고 TOP 10")
st.write("Plotly로 시각화된 인기 레고 제품")

# 예시 데이터
data = {
    "제품명": [
        "10179 Millennium Falcon",
        "10276 Colosseum",
        "10294 Titanic",
        "75192 UCS Millennium Falcon",
        "10256 Taj Mahal",
        "10307 Eiffel Tower",
        "71043 Hogwarts Castle",
        "21318 Tree House",
        "10265 Ford Mustang",
        "75252 UCS Imperial Star"
    ],
    "판매량(만개)": [120, 110, 105, 100, 95, 90, 88, 85, 82, 80]
}

df = pd.DataFrame(data)

# Plotly 시각화
fig = px.bar(
    df,
    x="제품명",
    y="판매량(만개)",
    title="가장 많이 팔린 레고 제품 TOP 10",
    labels={"판매량(만개)": "판매량 (만개)", "제품명": "레고 제품"},
    color="판매량(만개)",
    color_continuous_scale="Blues"
)

fig.update_layout(xaxis_tickangle=-45)

st.plotly_chart(fig)
