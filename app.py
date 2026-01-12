import streamlit as st
import random

st.title("じゃんけんゲーム")

# 横並びレイアウト
left, right = st.columns(2)

# 左側に画像
with right:
    st.image("janken.png", caption="じゃんけん画像")
    

# 右側にじゃんけんゲーム
with left:
    hands = ["グー", "チョキ", "パー"]
    user = st.radio("手を選んでね", hands)
    ai = random.choice(hands)

    if st.button("勝負！"):
        st.write("あなた:", user)
        st.write("AI:", ai)

        if user == ai:
            st.info("あいこ")
        elif (user == "グー" and ai == "チョキ") or \
             (user == "チョキ" and ai == "パー") or \
             (user == "パー" and ai == "グー"):
            st.success("あなたの勝ち！")
        else:
            st.error("AIの勝ち…")

