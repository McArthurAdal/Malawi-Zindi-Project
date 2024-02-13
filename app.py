import streamlit as st
from dotenv import load_dotenv

def main():
    st.set_page_config(page_title="IDSR Chat", page_icon=":books:")
    st.header("IntelSurv Chat")
    st.text_input("Ask a question")

    with st.sidebar:
        st.subheader("TG for IDSR Booklet")
        st.file_uploader("Upload booklet here")
        st.button("Process")






if __name__ == '__main__':
    main()