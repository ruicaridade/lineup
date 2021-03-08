import os

from flask import Flask
from flask_cors import CORS

from lineup import settings
from lineup.auth.views import users

app = Flask(__name__)

# We're allowing all origins because this isn't very important for this particular case, but might be a bad idea.
CORS(app)

app.register_blueprint(
    blueprint=users.blueprint,
    url_prefix='/users'
)


@app.route('/')
def welcome():
    return {
        'description': 'Wubba Lubba Dub Dub',
        'version': settings.VERSION
    }


if __name__ == '__main__':
    app.run(
        port=os.environ.get('PORT', 8000),
        debug=True
    )
