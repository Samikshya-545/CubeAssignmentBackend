from services.DbService import get_chat_history, update_chat_history
from flask import jsonify, request
from openai import OpenAI
import os
from config.DbConfig import getMongoDBCollection

collection = getMongoDBCollection()

def post_example():
    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    reqJson = request.json  # Assuming the data is in JSON format
    if reqJson:
        query = reqJson.get('query', '')

        completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": query}
        ])
        
        resMessage = completion.choices[0].message.content
        print(resMessage)
        return jsonify({'message': f'Hello, {resMessage}!'})
    else:
        return jsonify({'error': 'No JSON data received'})

def hello():
    return 'Hello, World!'

def save_data():
    try :
        email, query, gptResponse = request.json.values()
        return update_chat_history(collection, email, query, gptResponse)
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error occured while saving the data to DB'}), 400


def retrieve_data():
    try:
        email = str(request.json.get('email'))
        
        return get_chat_history(collection, email)
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error occured while retrieving from DB'}), 400
