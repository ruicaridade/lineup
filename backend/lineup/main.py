import os

from flask import Flask

from lineup import settings
from lineup.auth.views import users

app = Flask(__name__)

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
