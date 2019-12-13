"""
entry of the app_server
"""
from todo_list import app_server

APP = app_server.create_app()

if __name__ == '__main__':
    APP.run(debug=True, host='0.0.0.0')
