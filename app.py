import streamlit as st

st.title("サンプルアプリ②：少し複雑なwebアプリ")

st.write("#### 動作モード１：文字数カウント")
st.write("入力フォームにテキストを入力して、「実行」ボタンを押すと文字数をカウントします")
st.write("#### 動作モード２：身長と体重を入力してBMIを計算")

selected_item = st.radio(
    "動作モードを選択してください",
    ("文字数カウント", "BMI計算"),
)

st.divider()

if selected_item == "文字数カウント":
    input_message = st.text_input("文字数のカウント対象となるテキストを入力してください")
    text_count = len(input_message)
else:
    height = st.text_input("身長(cm)を入力してください")
    weight = st.text_input("体重(kg)を入力してください")

if st.button("実行"):
    st.divider()

    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数： **{text_count}** ")
        else:
            st.write("テキストが入力されていません")

    else:
        if height and weight:
            try:
                bmi = round(int(weight) / ( (int(height)/100) ** 2), 1)
                st.write(f"BMI： **{bmi}** ")
            except ValueError as e: 
                st.error("数値を入力してください")
        else:
            st.error("身長と体重の両方を入力してください")
