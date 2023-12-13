from flask_socketio import SocketIO

def getSocket(app):
    socketio = SocketIO(app, debug=True, cors_allowed_origins="*")
    return socketio