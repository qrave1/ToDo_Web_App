FROM python
WORKDIR /app
COPY todo/ /app/todo/
COPY main.py/ /app/
COPY .env/ /app/
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
CMD uvicorn main:app --reload --port 5000