import streamlit as st
import os
import time
import tempfile
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PyPDFLoader

st.set_page_config(page_title="Vectorless RAG", page_icon="📚", layout="wide")

def init_session_state():
    defaults = {
        "full_text": "",
        "docs_loaded": False,
        "groq_api_key": "",
        "messages": [],
    }
    for k, v in defaults.items():
        st.session_state.setdefault(k, v)

@st.cache_resource
def initialize_llm(groq_api_key: str):
    return ChatGroq(
        groq_api_key=groq_api_key,
        model_name="llama-3.1-8b-instant",
        temperature=0,
    )

def process_documents(uploaded_files):
    try:
        all_text = ""
        with st.status("📄 Processing...", expanded=True) as status:
            for uploaded_file in uploaded_files:
                with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                    tmp.write(uploaded_file.read())
                    tmp_path = tmp.name
                loader = PyPDFLoader(tmp_path)
                docs = loader.load()
                os.unlink(tmp_path)
                for doc in docs:
                    all_text += doc.page_content + "\n\n"
            
            st.session_state.full_text = all_text
            st.session_state.docs_loaded = True
            status.update(label="✅ Ready!", state="complete")
        return True
    except Exception as e:
        st.error(f"Error: {e}")
        return False

def main():
    init_session_state()
    st.title("📚 Vectorless RAG Q&A")
    st.markdown("##### No embeddings, No FAISS — Pure LLM Power!")

    with st.sidebar:
        st.title("⚙️ Setup")
        groq_api_key = st.text_input("Groq API Key", type="password")
        if groq_api_key:
            st.session_state.groq_api_key = groq_api_key
            st.success("API Key Saved ✅")

        st.divider()
        uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], 
                                           accept_multiple_files=True)
        if uploaded_files:
            if st.button("📄 Process Documents", use_container_width=True):
                process_documents(uploaded_files)

        if st.session_state.docs_loaded:
            # Token count കാണിക്കുന്നു
            word_count = len(st.session_state.full_text.split())
            st.info(f"✅ Loaded — ~{word_count} words")
            if st.button("🗑️ Clear Chat", use_container_width=True):
                st.session_state.messages = []
                st.rerun()

    if not st.session_state.groq_api_key:
        st.info("👈 Enter Groq API Key")
        return
    if not st.session_state.docs_loaded:
        st.info("👈 Upload PDFs to start")
        return

    # Chat History കാണിക്കുന്നു
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat Input
    if prompt := st.chat_input("Ask about your documents..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            try:
                llm = initialize_llm(st.session_state.groq_api_key)
                
                prompt_template = ChatPromptTemplate.from_template("""
You are a helpful assistant. Answer based only on the document below.
If not found, say "This information is not in the document."

Document:
{context}

Question: {input}

Answer:""")

                with st.spinner("Thinking..."):
                    t0 = time.perf_counter()
                    
                    # No vector search — full text directly!
                    formatted = prompt_template.format(
                        context=st.session_state.full_text,
                        input=prompt
                    )
                    response = llm.invoke(formatted)
                    elapsed = time.perf_counter() - t0

                st.markdown(response.content)
                st.caption(f"⏱️ Response time: {elapsed:.2f}s")
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response.content
                })

            except Exception as e:
                st.error(f"❌ Error: {e}")

if __name__ == "__main__":
    main()