"""
Simple settings file. There's no global dynamic `settings` import like in Django, so we can't create a, say,
`prod.settings.py` and override settings.

In a real project we'd ideally allow defining a file, similarly to `DJANGO_SETTINGS_MODULE`.
"""

VERSION = '0.1.0'

REPOSITORIES = {
    'users': 'lineup.auth.repositories.users.UserApiRepository'
}
