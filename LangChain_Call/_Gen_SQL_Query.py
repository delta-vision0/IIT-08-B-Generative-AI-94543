from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
import pandas as pd
load_dotenv()
llm = init_chat_model(
    model="llama-3.3-70b-versatile",
    model_provider="openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api_key")
)

csv_file = input("Enter Path For a CSV File : ")
df = pd.read_csv(csv_file)
print("CSV Schema")
print(df.dtypes)

conversation = list()
while True:
    user_input = input("Ask Anything about this CSV : ")
    if user_input == "exit":
        break
    llm_input = f"""
        Table Name : data
        Table Schema : {df.dtypes}
        Question : {user_input}
        instruction : Write a SQL query for the above question. 
            Generate SQL query only in plain text format and nothing else.
            If you cannot generate the query, then output 'Error'.    """

    result = llm.invoke(llm_input)
    print(result.content)
    # user_msg = {"role" : "user" , "content" : user_input}
    # conversation.append(user_msg)
    # llm_output = llm.invoke(conversation)
    # print("AI : ",llm_output.content)
    # llm_msg = {"role" : "assistant" , "content" : llm_output.content}
    # conversation.append(llm_msg)
