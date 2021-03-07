from flask import Blueprint

blueprint = Blueprint(
    name='users',
    import_name=__name__
)


@blueprint.route('/')
def list_users():
    return {
        'items': [
            {
                'id': 1
            }
        ],
        'page': 1,
        'total': 100
    }


@blueprint.route('/<int:user_id>')
def retrieve_user(user_id: int):
    return {
        'id': user_id
    }
