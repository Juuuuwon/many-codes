from fastapi import FastAPI
import pymysql


app = FastAPI()

@app.get("/app")
def index():
    conn = pymysql.connect(
        host='db',   
        user='testuser', 
        password='testpassword', 
        database='testdb'
    )

    try:
        with conn.cursor() as cursor:
            sql = "SELECT * from test;"
            cursor.execute(sql)
    finally:
        conn.close()

    return {"message": "ok"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)