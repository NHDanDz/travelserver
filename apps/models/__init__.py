from apps.models.models import Users, LoginHistory, AccessRecord, ChatHistory, Relation, Prompt, Base
from apps.base.db import engine

def initdb():
    """
    Initialize database tables
    """
    Base.metadata.create_all(engine)