from fastapi import FastAPI, HTTPException
import psycopg2
import requests

app = FastAPI()


@app.post("/blogs/")
async def create_blog(user_id: int, title: str, content: str):
    """_summary_
    """

    response = requests.get(f"http://usersvc:5000/users/{user_id}")
    if response.status_code != 200:
        raise HTTPException(status_code=400, detail="User not found")
    conn = psycopg2.connect(
        database="blogs", user="postgres", password="postgres", host="db")
    cur = conn.cursor()
    cur.execute("INSERT INTO blogs (user_id, title, content) VALUES (%s, %s, %s) RETURNING id",
                (user_id, title, content))
    blog_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return {"id": blog_id}


@app.get("/blogs/")
async def get_blogs():
    """_summary_
    """
    conn = psycopg2.connect(
        database="blogs", user="postgres", password="postgres", host="db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM blogs")
    blogs = cur.fetchall()
    cur.close()
    conn.close()
    return [{"id": blog[0], "user_id": blog[1], "title": blog[2], "content": blog[3]} for blog in blogs]
