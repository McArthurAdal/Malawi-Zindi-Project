import streamlit as st
from dotenv import load_dotenv
from pypdf import PdfReader
from langchain.text_splitter import CharacterTextSplitter as CSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS

def get_pdf_text(docs):
    text = ""
    for pdf in docs:
        reader = PdfReader(pdf)
        for page in reader.pages:
            text += page.extract_text()

def get_text_chunks(text):
    splitter = CSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = splitter.split_text(text)
    return chunks

def get_embeddings():
    model_name = "sentence-transformers/all-mpnet-base-v2"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}
    
    return HuggingFaceEmbeddings( 
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )

def get_vectorstore(chunks):
    hf = get_embeddings()
    vectorstore = FAISS.from_texts(text=chunks, embedding=hf)


def main():
    load_dotenv()
    st.set_page_config(page_title="IDSR Chat", page_icon=":books:")
    st.header("IntelSurv Chat")
    st.text_input("Ask a question")

    with st.sidebar:
        st.subheader("TG for IDSR Booklet")
        docs= st.file_uploader("Upload booklet here", accept_multiple_files=True)
        
        if st.button("Process"):
            with st.spinner("Processing"):
                raw_text = get_pdf_text(docs)

                chunks = get_text_chunks()
        st.write(chunks)






if __name__ == '__main__':
    main()