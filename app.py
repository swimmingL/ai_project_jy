import streamlit as st


st.set_page_config(
    page_title="AI Collaboration Practice",
    page_icon="🤝",
    layout="centered",
)

st.title("AI 협업 개발 실습")
st.write("첫 번째 Streamlit 앱입니다.")

name = st.text_input("이름을 입력하세요", placeholder="예: 홍길동")

if name:
    st.success(f"{name}님, Streamlit 앱 실행에 성공했습니다.")
else:
    st.info("이름을 입력하면 결과가 표시됩니다.")
