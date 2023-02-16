from sqlalchemy import Column, Integer, String, Boolean
from todo.database.base import Base, engine


class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    completed = Column(Boolean, default=False)


Base.metadata.create_all(bind=engine)
