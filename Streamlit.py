import streamlit as st

# 미리 설정한 암호
correct_password = "mysecretpassword"


# Streamlit 애플리케이션 구성
def main():
    st.title("암호 보안 페이지")

    # 비밀번호 입력 상자
    password_input = st.text_input("암호를 입력하세요", type="password")

    # 암호 확인 버튼
    if st.button("접근 허용"):
        if password_input == correct_password:
            st.success("암호가 일치합니다! 접근이 허용됩니다.")
            # 여기에 접근을 허용한 후의 동작을 추가할 수 있습니다.
        else:
            st.error("잘못된 암호입니다. 접근이 거부되었습니다.")


if __name__ == "__main__":
    main()
