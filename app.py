import os
from flask import Flask
from flask_cors import CORS
from config.DbConfig import getMongoDBCollection
from config.socketConfig import getSocket

collection = getMongoDBCollection()

app = Flask(__name__)

# CORS config
# CORS(app, resources={r"*": {
#     "origins": "*",
#     "cors_allowed_origins": ["http://localhost:3000", "http://localhost:3000/chat"]
#     }})
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})

# Socket config
socketio = getSocket(app)

# Import routes and sockets
from services.socketService import test_connect, handle_disconnect, handle_message
from routes.chatRoute import post_example, hello, save_data, retrieve_data

# Register routes
app.add_url_rule('/post_example', 'post_example', post_example, methods=['POST'])
app.add_url_rule('/', 'hello', hello, methods=['GET'])
app.add_url_rule('/api/saveChatHistory', 'save_data', save_data, methods=['POST'])
app.add_url_rule('/api/gatAllChatHistory', 'retrieve_data', retrieve_data, methods=['POST'])

# Register socket Connections
socketio.on_event('connect', test_connect)
socketio.on_event('requestToFlask', handle_message)
socketio.on_event('disconnect', handle_disconnect)


if __name__ == '__main__':
    socketio.run(app, debug=True)