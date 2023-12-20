import streamlit as st
from llama_index import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms import Gemini
from llama_index import ServiceContext
from llama_index.embeddings import HuggingFaceEmbedding
from IPython.display import Markdown, display
import os

os.environ["GOOGLE_API_KEY"]="AIzaSyAqGPICr190pACB8wijn7FMlSK5s5NXOCs"

# Streamlit title and description
st.title("Gemini-File with Llama-Index")
st.write("This app allows you to upload your own Pdf and query your document, Powered By Gemini")

#function to save a file
def save_uploadedfile(uploadedfile):
     with open(os.path.join("data",uploadedfile.name),"wb") as f:
         f.write(uploadedfile.getbuffer())
     return st.success("Saved File:{} to directory".format(uploadedfile.name))

# Streamlit input for user file upload
uploaded_pdf = st.file_uploader("Upload your PDF", type=['pdf'])

# Load data and configure the index
if uploaded_pdf is not None:
    input_file = save_uploadedfile(uploaded_pdf)
    st.write("File uploaded successfully!")
    documents = SimpleDirectoryReader("data").load_data()
    llm = Gemini()
    embed_model_uae = HuggingFaceEmbedding(model_name="WhereIsAI/UAE-Large-V1")

    # Configure Service Context
    service_context = ServiceContext.from_defaults(
        llm=llm, chunk_size=800, chunk_overlap=20, embed_model=embed_model_uae
    )
    index = VectorStoreIndex.from_documents(documents, service_context=service_context, show_progress=True)
    index.storage_context.persist()
    query_engine = index.as_query_engine()

    # Streamlit input for user query
    user_query = st.text_input("Enter your query:")

    # Query engine with user input
    if user_query:
        response = query_engine.query(user_query)
        st.markdown(f"**Response:** {response}")
else:
    st.write("Please upload a file first.")
