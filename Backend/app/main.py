from fastapi import FastAPI
import psycopg2, os

app = FastAPI()

@app.get("/tasks")
def get_tasks():
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tasks (id SERIAL PRIMARY KEY, title TEXT)")
    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return {"tasks": tasks}

@app.post("/tasks")
def create_task(title: str):
    conn = psycopg2.connect(
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        host=os.getenv("POSTGRES_HOST"),
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("INSERT INTO tasks (title) VALUES (%s)", (title,))
    conn.commit()
    cur.close()
    conn.close()
    return {"message": "Task added"}


