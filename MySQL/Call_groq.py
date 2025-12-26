from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv
load_dotenv()
llm = init_chat_model(
    model="llama-3.1-8b-instant",
    model_provider="openai",
    base_url = "https://api.groq.com/openai/v1",
    api_key = os.getenv("groq_api_key")
)
def explain_query_result(user_input, query, result_data, rows_affected=0):
    prompt = f"""
    You are a Data Analyst assistant. Your goal is to explain the outcome of a database operation in natural, conversational English.

    CONTEXT:
    - User's Intent: "{user_input}"
    - SQL Executed: "{query}"
    - Data Found: {result_data}
    - Records Changed: {rows_affected}

    GUIDELINES:
    1. If data was retrieved (SELECT): Summarize the specific findings. Use names and values. (e.g., "I found that Neha Verma is in HR and earns 50,000.")
    2. If data was changed (UPDATE/INSERT/DELETE): Confirm the action based on the user's intent. (e.g., "I've updated Suresh's salary to 800,000 as you requested.")
    3. If no data was found: Explain why. (e.g., "I couldn't find any employees in the Marketing department.")
    4. Speak like a human, not a computer. Avoid "rows," "tables," or "null."
    5. Keep it to 1 or 2 clear sentences.

    EXPLANATION:
    """
    response = llm.invoke(prompt)
    return response.content

def generate_mysql_query(table, user_input):
    if not user_input:
        return None
    
    llm_input = f"""
    ROLE: You are a strict MySQL Expert. 
    TABLE SCHEMA:
    Table Name: employees
    Columns: [id, name, department, salary, hire_date]

    DATA SAMPLE (FOR CONTEXT ONLY):
    {table[:2]}  # Just show the first 2 rows so it knows the format

    USER QUESTION: "{user_input}"

    STRICT RULES:
    1. Output ONLY the raw MySQL query code. 
    2. No markdown, no backticks (```), no explanations.
    3. Use ONLY the columns listed in the schema.
    4. Do NOT add filters (like dates or IDs) unless the user specifically asked for them.
    5. If the user asks for "Navanath", the query should be: SELECT * FROM employees WHERE name LIKE '%Navanath%';
    6. If you cannot create a valid query, output 'Error'.
    7. Use standard MySQL syntax.

    SQL QUERY:
"""

    result = llm.invoke(llm_input)
    return result.content