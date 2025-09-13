

from dotenv import load_dotenv
load_dotenv()

import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os

# 専門家ごとのシステムメッセージ
expert_roles = {
    "医療専門家": "あなたは優秀な医療専門家であり、ユーザーの健康や病気に関する質問に対して正確で丁寧な医学的助言を提供してください。",
    "法律専門家": "あなたは信頼できる法律専門家です。ユーザーの法律に関する質問に分かりやすく、正確な助言を提供してください。",
    "ITエンジニア": "あなたは熟練したITエンジニアです。プログラミング、システム開発、AIなどの技術的な質問に的確に答えてください。",
    "歴史学者": "あなたは優秀な歴史学者であり、過去の出来事や人物、文化などについて深い知識を持っています。歴史に関する質問に丁寧に答えてください。"
}

# -----------------------------------------
# LLM応答を取得する関数
# -----------------------------------------
def get_expert_response(user_input: str, expert_type: str) -> str:
    system_prompt = expert_roles.get(expert_type, "あなたは親切なアシスタントです。")
    
    # LangChainのChatモデル（OpenAIのchatモデルを使用）
    llm = ChatOpenAI(temperature=0)

    # 会話形式でメッセージを構築
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]

    # 応答を取得
    response = llm(messages)

    return response.content

# -----------------------------------------
# Streamlit UI
# -----------------------------------------

st.title("🧠 専門家に聞いてみよう")

# ラジオボタンで専門家を選択
expert_type = st.radio(
    "質問を答える専門家の種類を選んでください：",
    list(expert_roles.keys())
)

# ユーザーの入力
user_input = st.text_area("質問を入力してください：")

# 送信ボタン
if st.button("送信"):
    if user_input.strip() == "":
        st.warning("質問を入力してください。")
    else:
        with st.spinner("回答を生成中..."):
            answer = get_expert_response(user_input, expert_type)
            st.markdown("### 回答:")
            st.write(answer)

