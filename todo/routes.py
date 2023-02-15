from todo.app import app, templates
from fastapi import Request, Depends
from todo.database.base import get_db
from sqlalchemy.orm import Session
from todo.models import ToDo
from config import settings


@app.get('/')
def index(request: Request, db_session: Session = Depends(get_db)):
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request, 'app_name': settings.app_name,
                                       'todo_list': todos}
                                      )
