from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import streamlit as st
import pandas as pd
from pandasql import sqldf
load_dotenv()
llm = init_chat_model(
    model="llama-3.1-8b-instant",
    model_provider="openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api_key")
)

csv_file = st.file_uploader(label="upload a file",type=["csv"])
if csv_file is not None:
    df = pd.read_csv(csv_file)
    data = df
    st.dataframe(df)
    conversation = list()
    user_input = st.chat_input("Ask Anything about this CSV : ")
    if user_input:
        llm_input = f"""
            Table Name : df
            Table Schema : {df.dtypes}
            Table content : {df.head().to_string()}
            Question : {user_input}
            instruction : Write a SQL query for the above question. 
                        Generate SQL query only in plain text format and nothing else.
                        If you cannot generate the query, then output 'Error'. 
                        Write ONLY a valid SQL query.
                        No explanation.
            I           if not possible, output Error.
                        ⚠️ IMPORTANT:
                        Use ONLY years present in the data.
                        If year not found, return Error.
              """

        result = llm.invoke(llm_input)
        st.write("Given Query : " , result.content)
        if result.content == "Error":
            st.write("Cannot generate SQL query for the given question.")
        else:
            query = str(result.content)
            result2 = sqldf(query, globals())
            st.write("Result : ")
            st.write(result2)
        prompt = f"""
        You have to Explain the Given Question and its result in simple english
        dont use sql language in explaination 
        keep it understandable even for those who dont know SQL at All 
        don't give long explaination , keep it short and understanding , short but should explain well
        given info for above task :
        question : {user_input}
        generated query: {query}
        result : {result2}

        if user tries to delete or truncate , it should say only select queries allowed
"""
        explain = llm.invoke(prompt)
        st.write(explain.content)

