from todo.database.base import Base
from sqlalchemy import Column, Integer, String, Boolean


class ToDo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    completed = Column(Boolean, default=False)

    def __repr__(self):
        return f'ToDo(id={self.id}, title={self.title}, description={self.description}, completed={self.completed})'
