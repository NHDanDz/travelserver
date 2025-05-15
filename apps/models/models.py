from sqlalchemy import Column, Integer, String, Text, DateTime, BigInteger, SmallInteger
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(32), nullable=False, comment='User ID')
    username = Column(String(32), nullable=False, comment='Username')
    passwd = Column(String(32), nullable=False, comment='Password')
    nickname = Column(String(32), nullable=True, comment='Nickname')
    phone = Column(String(32), nullable=True, comment='Phone')
    email = Column(String(64), nullable=True, comment='Email')
    status = Column(SmallInteger, nullable=True, default=0, comment='Status')
    last_login = Column(DateTime, nullable=True, comment='Last login time')
    gmt_create = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Create time')
    gmt_modified = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Update time')

class LoginHistory(Base):
    __tablename__ = 'login_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(32), nullable=False, comment='Username')
    nickname = Column(String(32), nullable=True, comment='Nickname')
    phone = Column(String(32), nullable=True, comment='Phone')
    email = Column(String(64), nullable=True, comment='Email')
    login_ip = Column(String(32), nullable=True, comment='Login IP')
    gmt_create = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Create time')
    gmt_modified = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Update time')

class AccessRecord(Base):
    __tablename__ = 'access_record'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String(32), nullable=False, comment='User ID')
    username = Column(String(32), nullable=False, comment='Username')
    nickname = Column(String(32), nullable=True, comment='Nickname')
    url = Column(String(255), nullable=True, comment='Access URL')
    method = Column(String(32), nullable=True, comment='Request method')
    gmt_create = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Create time')
    gmt_modified = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Update time')

class ChatHistory(Base):
    __tablename__ = 'chat_history'

    id = Column(Integer, primary_key=True, autoincrement=True)
    session_id = Column(String(32), nullable=False, comment='Session ID')
    user_id = Column(String(32), nullable=False, comment='User ID')
    type = Column(SmallInteger, nullable=True, default=0, comment='Message type')
    content = Column(Text, nullable=True, comment='Message content')
    is_deleted = Column(SmallInteger, nullable=True, default=0, comment='Is deleted')
    gmt_create = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Create time')
    gmt_modified = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Update time')

class Relation(Base):
    __tablename__ = 'relation'

    id = Column(Integer, primary_key=True, autoincrement=True)
    from_key = Column(String(32), nullable=False, comment='From key')
    to_key = Column(String(32), nullable=False, comment='To key')
    category = Column(String(32), nullable=True, comment='Category')
    direction = Column(SmallInteger, nullable=True, default=0, comment='Direction')
    is_deleted = Column(SmallInteger, nullable=True, default=0, comment='Is deleted')
    gmt_create = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Create time')
    gmt_modified = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Update time')

class Prompt(Base):
    __tablename__ = 'prompt'

    id = Column(Integer, primary_key=True, autoincrement=True)
    prompt_id = Column(String(32), nullable=False, comment='Prompt ID')
    category = Column(String(32), nullable=True, comment='Category')
    act = Column(String(255), nullable=True, comment='Action')
    prompt = Column(Text, nullable=True, comment='Prompt content')
    creator = Column(String(32), nullable=True, comment='Creator')
    modifier = Column(String(32), nullable=True, comment='Modifier')
    is_deleted = Column(SmallInteger, nullable=True, default=0, comment='Is deleted')
    gmt_create = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Create time')
    gmt_modified = Column(DateTime, nullable=True, default=datetime.datetime.now, comment='Update time')