import os
import streamlit as st
import base64
from langchain_community.embeddings.huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.messages import ChatMessage
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.faiss import FAISS
from langserve import RemoteRunnable
from langchain.schema import Document
import fitz  # PyMuPDF


RAG_PROMPT_TEMPLATE = """
다음 정보를 바탕으로 질문에 답하세요:
{context}

질문:
{question}

질문의 핵심만 파악하여 간결하게 1-2문장으로 답변하고, 불필요한 설명은 피하며 동서울대학교와 관련된 정보만 제공하세요.

답변:
"""

st.set_page_config(page_title="Chatbot PY", page_icon="💬")
st.title("DU Chatbot 파이")

if "messages" not in st.session_state:
    st.session_state["messages"] = [
        ChatMessage(role="assistant", content="DU Chatbot 파이입니다.")
    ]

# 이미지를 base64로 인코딩하는 함수
def get_base64_of_bin_file(bin_file):
    with open(bin_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

# 백그라운드 이미지 설정하는 함수
def set_bg_hack(main_bg):
    bin_str = get_base64_of_bin_file(main_bg)
    page_bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"]::before {{
        content: "";
        background-image: url("data:image/png;base64,{bin_str}");
        background-size: 30%;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        opacity: 0.1;
        position: absolute;
        top: 0;
        left: 0;
        bottom: 0;
        right: 0;
    }}
    [data-testid="stHeader"] {{
        background-color: rgba(0,0,0,0);
    }}
    [data-testid="stToolbar"] {{
        right: 2rem;
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def print_history():
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)
        
def add_history(role, content):
    st.session_state.messages.append(ChatMessage(role=role, content=content))

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

set_bg_hack("./DU_logo.png")

# RAG 구현
doc = fitz.open("./QADataset.pdf")
text = ""
for page in doc:
    text += page.get_text()

splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=50)
chunk_temp = splitter.split_text(text)
chunks = [Document(page_content=t) for t in chunk_temp]

# device 설정을 CPU 또는 CUDA로 변경
model_kwargs = {"device": "cuda"} 
encode_kwargs = {"normalize_embeddings": True}
embeddings = HuggingFaceEmbeddings(
    model_name="intfloat/multilingual-e5-large",
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs,
)

db = FAISS.from_documents(chunks, embedding=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 2})

st.sidebar.title("채팅 목록")
option = st.sidebar.selectbox(
    "채팅목록을 선택하세요.:", ("동서울대학교 휴학 신청", "논문 요청", "장학생 준비")
)

st.write(f"{option}")

if st.sidebar.button("BJ.Park"):
    st.sidebar.text("캡스톤 디자인 재밌었습니다.")
if st.sidebar.button("J.Jeong"):
    st.sidebar.text("모든 개발은 저를 통합니다.")
if st.sidebar.button("JH.Lee"):
    st.sidebar.text("주희 is free.")
if st.sidebar.button("SH.Kim"):
    st.sidebar.text("김승현을 국회로!!!!!!. ")

print_history()

if user_input := st.chat_input():
    add_history("user", user_input)
    st.chat_message("user").write(user_input)
    with st.chat_message("assistant"):
        ollama = RemoteRunnable("ngrok server url/llm/")
        chat_container = st.empty()
        prompt = ChatPromptTemplate.from_template(RAG_PROMPT_TEMPLATE)

        rag_chain = (
            {
                "context": retriever | format_docs,
                "question": RunnablePassthrough(),
            }
            | prompt
            | ollama
            | StrOutputParser()
        )
        answer = rag_chain.stream(user_input)
        chunks = []
        for chunk in answer:
            chunks.append(chunk)
            chat_container.markdown("".join(chunks))
        add_history("ai", "".join(chunks))
