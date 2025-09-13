import streamlit as st
import os

# ✅ Streamlit Cloud 用：Secretsから API キーを環境変数に設定
os.environ["OPENAI_API_KEY"] = st.secrets["OPENAI_API_KEY"]

from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

# 必要に応じてmodel_nameを明示的に指定（これ重要）
llm = ChatOpenAI(
    temperature=0,
    model_name="gpt-3.5-turbo"  # ← GPT-4だと認証エラーになる場合あり
)


from langchain_community.chat_models import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
import os

# ✅ ここが重要：APIキーをos.environにセット
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# 専門家ごとのシステムメッセージ
expert_roles = {
    "医療の専門家": "あなたは優秀な医療専門家であり、健康や病気に関する質問に対して正確で丁寧な医学的助言を一般の人でもわかるように簡単に提供してください。",
    "ITエンジニア": "あなたは熟練したITエンジニアです。プログラミング、システム開発、AIなどの技術的な質問に的確に答えてください。",
}

def get_expert_response(user_input: str, expert_type: str) -> str:
    system_prompt = expert_roles.get(expert_type, "あなたは親切なアシスタントです。")
    
    llm = ChatOpenAI(temperature=0)
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_input)
    ]
    response = llm(messages)
    return response.content

st.title("専門家を選択して質問する")

expert_type = st.radio(
    "専門家を選んでください：",
    list(expert_roles.keys())
)

user_input = st.text_area("質問を入力してください：")

if st.button("送信"):
    if user_input.strip() == "":
        st.warning("質問を入力してください。")
    else:
        with st.spinner("回答を生成中..."):
            answer = get_expert_response(user_input, expert_type)
            st.markdown("### 回答:")
            st.write(answer)
