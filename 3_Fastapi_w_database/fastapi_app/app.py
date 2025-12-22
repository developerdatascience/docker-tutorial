from fastapi import FastAPI
import pymysql


app = FastAPI()


def dbConnect():
    connection = pymysql.connect(
        host="mysql_container",
        user="root",
        password="rootpassword",
        database="mydatabase"
        )

    return connection

@app.get("/")
async def read_root():
    return "Welcome to FastAPI with Database"

@app.get("/insert-data/{name}/{email}")
async def insert_data(name: str, email: str):
    cursor = None
    connection = None
    try:
        connection = dbConnect()
        cursor = connection.cursor()
        sql = "INSERT INTO users (name, email) VALUES (%s, %s)"
        val = (name, email)
        cursor.execute(sql, val)
        connection.commit()
        return {"message": "Data inserted successfully"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()


@app.get("/fetch-data/search")
async def fetch_data(name: str):
    cursor = None
    connection = None
    try:
        connection = dbConnect()
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        search_term = f"%{name}%"
        sql = "SELECT * FROM users WHERE name LIKE %s"
        cursor.execute(sql, (search_term,))
        result = cursor.fetchall()
        return {"data": result}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()
