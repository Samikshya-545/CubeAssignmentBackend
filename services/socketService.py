from flask_socketio import emit
from openai import OpenAI
from flask import jsonify
import time
import os

def test_connect():
    """event listener when client connects to the server"""
    print("client has connected")
    emit('isConnected',True)

def handle_message(msg):
    print('Received message:', msg)

    client = OpenAI(
        api_key=os.environ.get("OPENAI_API_KEY"),
    )

    if msg:
        stream = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": msg}],
            stream=True,
        )
        
        for chunk in stream:
            time.sleep(0.05)
            if chunk.choices[0].delta.content is not None:
                emit('gptResponse',chunk.choices[0].delta.content, end="")
            elif(chunk.choices[0].finish_reason == 'stop'):
                emit('ongoingGptResponseEnded', True)

    else:
        emit('gptResponse', 'No Data received')

def handle_disconnect():
    print('WebSocket disconnected')

