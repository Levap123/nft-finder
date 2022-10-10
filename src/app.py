from src import create_app
from src.config import Config

if __name__ == '__main__':
    app = create_app('flask.cfg')
    app.run(debug=True, port=Config.port)
