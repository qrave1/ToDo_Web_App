from fastapi_users import fastapi_users, FastAPIUsers

from todo.app import app, templates
from fastapi import Request, Depends, Form

from todo.auth.auth import auth_backend
from todo.auth.database import User
from todo.auth.manager import get_user_manager
from todo.auth.schemas import UserRead, UserCreate
from todo.database.base import get_db
from sqlalchemy.orm import Session
from todo.models import ToDo
from todo.config import settings
from starlette.responses import RedirectResponse
from starlette.status import HTTP_303_SEE_OTHER, HTTP_302_FOUND


@app.get('/')
def home(request: Request, db_session: Session = Depends(get_db)):
    """Маршрут на index"""
    todos = db_session.query(ToDo).all()
    return templates.TemplateResponse('todo/index.html',
                                      {'request': request,
                                       'app_name': settings.app_name,
                                       'todo_list': todos}
                                      )


@app.post('/add')
def add(title: str = Form(...), db_session: Session = Depends(get_db)):
    """Добавление новой задачи"""
    new_todo = ToDo(title=title)
    db_session.add(new_todo)
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_303_SEE_OTHER)


@app.get('/update/{todo_id}')
def update(todo_id: int, db_session: Session = Depends(get_db)):
    """Обновление статуса задачи"""
    todo = db_session.query(ToDo).filter_by(id=todo_id).first()
    todo.completed = not todo.completed
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


@app.get('/delete/{todo_id}')
def delete(todo_id: int, db_session: Session = Depends(get_db)):
    """Удаление задачи"""
    todo = db_session.query(ToDo).filter_by(id=todo_id).first()
    db_session.delete(todo)
    db_session.commit()

    url = app.url_path_for('home')
    return RedirectResponse(url=url, status_code=HTTP_302_FOUND)


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

current_user = fastapi_users.current_user()


@app.get("/protected-route")
def protected_route(user: User = Depends(current_user)):
    return f"Hello, {user.username}"
