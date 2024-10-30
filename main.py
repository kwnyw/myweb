
import streamlit as st
menu=st.sidebar.selectbox("Menu",["로그인","회원가입"])

db_id="test"
db_pw="123"
if menu=="로그인":    
    st.title("🍭 로그인")
    id=st.text_input("아이디", placeholder="아이디를 입력하세요")
    pw=st.text_input("비밀번호", type="password")
    login=st.button("로그인")
    if login:
        if db_id==id and db_pw==pw:
            st.success("로그인 성공")
            #st.balloons()
            
        else:
            st.error("로그인 실패")
            st.snow()
elif menu=="회원가입":
    st.title("🍩회원가입")            
        
st.video("https://youtu.be/OA4xWoZ6Ygo?si=SR8rRJh5D-u20Dwc")



# check1=st.checkbox("짜장면(5000원)")
# check2=st.checkbox("짬뽕(7000원)")
# check3=st.checkbox("탕수육(15000원)")
# sum=0
# if check1:
#     sum+=5000
# if check2:
#     sum+=7000
# if check3:
#     sum+=15000
# st.write(str(sum))
# 과목 = st.selectbox("과목을 선택하세요",
#                     ["확률과 통계",
#                      "미분과 적분",
#                      "기하와 벡터"])
# st.subheader(f"당신이 선택한 과목은 {과목}입니다.")




# 버튼=st.button("버튼")
# check=st.checkbox("동의")
# if check:
#     st.write("동의를 선택했습니다")
#     st.write(check)  
# if 버튼:
#     st.write("버튼을 눌렀습니다")

# st.title("🍭 :blue[ Title ] 🍬")
# st.header("header")
# st.subheader("subheader")
# st.write(":red[작은] 글씨")

