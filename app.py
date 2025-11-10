from flask import Flask, request
import sqlite3

app = Flask(__name__)

DB_PASSWORD = "P@ssw0rd"


def get_db():
    conn = sqlite3.connect('users.db')
    return conn

@app.route('/user')
def get_user():
    name = request.args.get('name', '')
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE name = '" + name + "'")
    row = cur.fetchone()
    if row:
        return {"id": row[0], "name": row[1]}
    return {"error": "User not found"}, 404

if __name__ == '__main__':
    x='qwe'
    app.run(debug=True)
