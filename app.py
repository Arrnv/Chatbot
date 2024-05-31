import streamlit as st
import os
import dotenv
dotenv.load_dotenv()

key = os.getenv('apikey')

from langchain_google_genai import ChatGoogleGenerativeAI
try:
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key = key)
except:
    llm = ChatGoogleGenerativeAI(model="gemini-pro", google_api_key = key)
 


st.title("AI- Query Chatbot")
st.text("Ask me ChatBots")
text = st.text_input(
    label="Query"
)

submit = st.button("Analyze")




if submit:
    prompt = f"""You are a support chatbot for an e-commerce website. Provide suitable answers for: {text}. Answer only the query without giving any additional information. For product inquiries, order status, and returns, please provide the necessary details or steps to follow. 
    For any issues, contact us at support@ecommerce.com. 
    For business inquiries or collaboration, email us at business@ecommerce.com. 
    Services provided include: product sales, order tracking, and customer support."""
    result = llm.invoke(prompt)
    print(result.content)

    st.subheader(result.content)

st.write("_________")
