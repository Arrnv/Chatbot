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
 

chatbotquestiontype = [
    {
        "Question": "Inquiry about internships?"
    },
    {
        "Question": "Want to connect."
    },
    {
        "Question": "Services provided"
    },
    {
        "Question": "facing Issues"
    },{
        "Question": "types of product"
    }
]

st.title("AI- Query Chatbot")
st.text("Test model ChatBots")

Query = st.selectbox("Select your query",[items["Question"] for items in chatbotquestiontype])

submit = st.button("Analyze")




if submit:
    prompt= f"""You are a Chatbot, Give sutable ansers for : {Query} . answer only to the query and dont give any other information There are no internship avaliable , If want to connect mail lahanearna9@gmail.com , services provided : machine learning software and models , website creation. it facing any issue: mail on lahanearnav9@gmail.com your issue"""
    result = llm.invoke(prompt)
    print(result.content)

    st.subheader(result.content)

st.write("_________")
