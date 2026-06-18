import streamlit as st
from packaging import tags

st.title("choose a color")
st.subheader("color game")
st.write("game to play")

if "login_in" not in st.session_state:
    st.session_state.login_in = False

if 'attempt_in' not in st.session_state:
    st.session_state.attempt_in =0

if not st.session_state.login_in:
    name = st.text_input("Please enter your name")
    password = st.text_input("Please enter your password", type='password')
    email = st.text_input("input your email")

    if st.button("login"):
        if password == '0000':
            st.write('Login successful')
            st.session_state.login_in = True
            st.session_state.login_in = True
            st.session_state.name = name
            st.session_state.email = email
        else:
            st.session_state.Attempt_in+=1
            st.write('wrong password')

            st.error(f'wrong password. Attempts : {st.session_state.attempts}')
    st.stop()

game = st.selectbox (
    label="choose a color",
    options= ("colors", "blue", "red","yellow")
)

mood = st.radio("feelings",
                ["calm","sad","happy"]
                )
minute = st.slider(
    label='how long?',
    min_value=0,
    max_value=60,
)

if st.button("out comes of each color"):
    if game == "blue":
        task = [
            "blue is correct!"

        ]
    elif game == "red":
        task = "not red you lose"
    elif game == "yellow":
        task = "not yellow you lose"
    else:
        task = "didn't even choose a color"

    if mood == "sad":
        tip ="have a rest and have fun playing this game :)"
    elif mood == "happy":
        tip ="have great fun playing this game :)"
    elif mood == "calm":
        tip ="great your calm have a chill time playing this game"


    st.info(task)
    st.write(tip)
    st.write("thanks for playing")
    st.write("tell other people about this game!")






