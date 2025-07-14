import streamlit as st

# 레고 시리즈별 제품 데이터 (예시)
lego_data = {
    "City": [
        "60200 Capital City",
        "60204 Hospital",
        "60206 Jet Patrol",
        "60372 Police Academy"
    ],
    "Star Wars": [
        "75301 Luke Skywalker's X-Wing",
        "75308 R2-D2",
        "75288 AT-AT",
        "75341 Luke Skywalker's Landspeeder"
    ],
    "Technic": [
        "42100 Liebherr R 9800 Excavator",
        "42115 Lamborghini Sián",
        "42131 Cat D11 Bulldozer",
        "42154 2022 Ford GT"
    ],
    "Ninjago": [
        "71741 Ninjago City Gardens",
        "71738 Zane's Titan Mech",
        "71765 Ninja Ultra Combo Mech"
    ],
    "Harry Potter": [
        "76391 Hogwarts Icons",
        "75955 Hogwarts Express",
        "76389 Hogwarts Chamber of Secrets"
    ]
}

st.title("레고 시리즈별 제품 안내")
st.write("Streamlit으로 만든 간단한 레고 제품 정보 앱입니다.")

# 시리즈 선택
selected_series = st.selectbox("레고 시리즈를 선택하세요:", list(lego_data.keys()))

# 선택된 시리즈의 제품 출력
st.subheader(f"🧱 {selected_series} 시리즈의 제품 목록:")
for product in lego_data[selected_series]:
    st.markdown(f"- {product}")
