import json

from flask import Blueprint, Response

from lineup.auth.repositories import users
from lineup.core.exceptions import NotFoundError

blueprint = Blueprint(
    name='users',
    import_name=__name__
)


@blueprint.route('/')
def list_users():
    repository = users.Repository()
    items, total, page = repository.all(
        limit=123,
        page=0
    )
    return {
        'items': [x.to_dict(as_camel_case=True) for x in items],
        'page': page,
        'total': total
    }


@blueprint.route('/<int:user_id>')
def retrieve_user(user_id: int):
    repository = users.Repository()

    try:
        item = repository.find_by_id(user_id)
    except NotFoundError:
        return Response(
            status=404,
            content_type='application/json',
            response=json.dumps({
                'error': f'Instance of id `{user_id}` not found.'
            })
        )

    return item.to_dict(as_camel_case=True)
