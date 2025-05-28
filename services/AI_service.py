from DB.AIconnection import ai_core_client
import os
from dotenv import load_dotenv
import json
from DB.Hanaconnection import connection
from sqlalchemy import text
import requests

load_dotenv()

def ask_ai_question_for_SQL_query(question,metadata_json):
    TOKEN = ai_core_client.rest_client.get_token()
    api = os.getenv("AI_API")
    
    headers = {
        'Content-type': 'application/json', 
        'AI-Resource-Group': 'default', 
        'Authorization': TOKEN
    }
    payload = json.dumps({
        "messages": [
            {'role': 'system', 'content': f""" 
             Here is the metadata of the database: {metadata_json}. Always answer with only the SQL query of how to fetch the data from the database.
             Any queries always need to be in the format from "DBE_00_INNOVATION"."name_of_the_view" 
             It needs to be in a format that allows me to immediately execute. Do not add any additional text or comments.
             Any custom part of the query should be in double quotes, e.g. "column_name". Also the value of the column should be in single quotes, e.g. 'value'. 
             Nationalities are stored by their 3 most prominent letters, e.g. 'USA' for United States of America, BEL for Belgium, etc.
             """},
            {'role': 'user', "content": question} 
        ], 
        "max_tokens": 500 #default value is 100
    })

    predict = requests.post(api, data=payload, headers=headers)
    response = predict.json()['choices'][0]['message']['content']
    return response

def execute_query(query):
    try:
        query_to_execute = text(query)
        result = connection.execute(query_to_execute)
        columns = result.keys()
        return [dict(zip(columns, row)) for row in result.fetchall()]
    except Exception as e:
        return str(e)


def clean_sql_response(ai_response):
    """Remove Markdown code blocks and whitespace"""
    # Remove starting ```sql or ```
    if ai_response.startswith('```sql'):
        cleaned = ai_response[6:]  # Remove ```sql
    elif ai_response.startswith('```'):
        cleaned = ai_response[3:]  # Remove ```
    else:
        cleaned = ai_response
    
    # Remove trailing ``` if exists
    cleaned = cleaned.replace('```', '')
    return cleaned.strip()  # Remove any remaining whitespace

def handle_sql_response(response,question):
    TOKEN = ai_core_client.rest_client.get_token()
    api = os.getenv("AI_API")
    headers = {
        'Content-type': 'application/json', 
        'AI-Resource-Group': 'default', 
        'Authorization': TOKEN
    }
    payload = json.dumps({
        "messages": [
            {'role': 'system', 'content': f""" 
             You are a Hana Database expert. The user has just asked a question and another AI has provided a SQL query to fetch the data from the database.
             The SQL query has been executed and the result is as follows: {response}.
             Your task is to format the response in a user-friendly way, providing a clear and concise answer based on the data retrieved.
             """},
            {'role': 'user', "content": question} 
        ], 
        "max_tokens": 500 #default value is 100
    })

    ask_ai = requests.post(api, data=payload, headers=headers)
    response = ask_ai.json()['choices'][0]['message']['content']
    return response

    
def ask_question_to_ai(question, allMetadata_json):
    sql_query = ask_ai_question_for_SQL_query(question, allMetadata_json)
    clean_sql_query = clean_sql_response(sql_query)
    result = execute_query(clean_sql_query)
    print(result)
    ai_formatted_response = handle_sql_response(result, question)
    return ai_formatted_response


