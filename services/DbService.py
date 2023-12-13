from flask import jsonify
import json
from bson import json_util # To JSONIFY _id

def update_chat_history(collection, email, query, gptResponse):
    entry = collection.find_one({'email': email})

    if entry:
        # Updatethe chatHistory
        updatedChatHistory = entry.get('chatHistory')
        updatedChatHistory.append({
            'query': json.dumps(query),
            'gptResponse': json.dumps(gptResponse)
        })
        collection.update_one({'email': email}, {'$set' : {'chatHistory': updatedChatHistory}})
        return jsonify({'message': 'Data Updated successfully'})
    else:
        print("entry not present")
        result = collection.insert_one({
            'email': str(email),
            'chatHistory': [{
                'query': json.dumps(query),
                'gptResponse': json.dumps(gptResponse)
            }]
        })
        print('inserted_id '+ str(result.inserted_id))
        return jsonify({'message': 'Data saved successfully'})

def get_chat_history(collection, email):
    data = collection.find_one({'email': email})

    if data : 
        # Extract only the 'chatHistory' field from each document
        chat_history_list = data['chatHistory']

        # Serialize the extracted 'chatHistory' data to JSON
        serialized_chat_history = json_util.dumps(chat_history_list)
        
        return serialized_chat_history
    else:
        return jsonify([])