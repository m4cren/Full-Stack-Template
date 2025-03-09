from backend import socketio, create_website, db
from backend.db_config import host, port



app = create_website()




if __name__ == "__main__":
    socketio.run(app, debug=True, host=host, port=port)
