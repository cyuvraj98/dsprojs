from fastapi import FastAPI
import sqlite3

def run_sql_code(query):
    con = sqlite3.connect("local.db") # con is the shortform for connection
    cur = con.cursor()
    cur.execute(query)
    res = cur.fetchall()
    col = [e[0] for e in cur.description]
    res = [{k: v for k, v in zip(col, e)} for e in res]
    cur.close()
    con.close()
    return res

app = FastAPI() # creates the FastAPI instance

# how you define a new route (we use .get bc we wanna issue a GET request)
@app.get("/hello") # placed on the root of the server, "/"
async def root(): # async stands for asynchronous
    return {"message": "Hello World"} # complies w JSON stds, therefore is JSON formatted

# Type the following cmd into the terminal (make sure you are in the same file directory)
# uvicorn fastAPI:app --reload (Note that fastAPI is the Python name of this file and app is app as declared in line 3)

# to find your computer ip address, type "ipconfig" (w/o the inverted commas) into the terminal and then see the IPv4 Address

# get a user w a specified ID
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    response = run_sql_code(f"SELECT * FROM users WHERE id='{user_id}' ")
    return response

@app.put("/birthday/{user_id}") # route is used for editing
async def user_has_birthday(user_id: int):
    response = run_sql_code(f"SELECT age FROM users WHERE id='{user_id}' ")
    return response

