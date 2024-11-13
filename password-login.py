import streamlit as st

# 페이지 제목 설정
st.title("비밀번호 입력 예제")

# session_state에 login_status가 없으면 초기화
if 'login_status' not in st.session_state:
    st.session_state.login_status = False

# 미리 설정된 비밀번호 (실제 앱에서는 더 안전한 방법으로 관리해야 합니다)
CORRECT_PASSWORD = "1234"

def check_password():
    """비밀번호를 확인하고 로그인 상태를 업데이트하는 함수"""
    if st.session_state.password == CORRECT_PASSWORD:
        st.session_state.login_status = True
        st.success("로그인 성공!")
    else:
        st.error("비밀번호가 올바르지 않습니다.")

# 로그인하지 않은 상태일 때 비밀번호 입력 폼 표시
if not st.session_state.login_status:
    st.text_input(
        label="비밀번호를 입력하세요",
        type="password",
        key="password",
        on_change=check_password
    )

# 로그인 된 상태일 때 콘텐츠 표시
if st.session_state.login_status:
    st.write("안녕하세요! 로그인된 페이지입니다.")
    
    if st.button("로그아웃"):
        st.session_state.login_status = False
        st.experimental_rerun()
