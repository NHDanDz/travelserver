from sqlalchemy import or_

from apps.base.db import new_session
from apps.models.models import Users

def find_user(username: str = None, email: str = None):
    """
    Find user by username or email
    This is a stub function that always returns None
    """
    return None