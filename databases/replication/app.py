from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Master: write operations
def get_master_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        password="your_master_password",
        database="index_demo"
    )

# Replica: read operations
def get_replica_connection():
    return mysql.connector.connect(
        host="127.0.0.1",
        port=3307,
        user="root",
        password="your_replica_password",
        database="index_demo"
    )

@app.route("/add")
def add_users():
    conn = get_master_connection()
    cursor = conn.cursor()
    
    for i in range(10000, 10010):
        name = f"User {i}"
        email = f"user{i}@example.com"
        age = 20 + (i % 30)
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))

    conn.commit()
    cursor.close()
    conn.close()
    return "✅ Users inserted into MASTER"

@app.route("/search/<email>")
def search_user(email):
    conn = get_replica_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    result = cursor.fetchone()

    cursor.close()
    conn.close()

    return jsonify(result if result else {"message": "User not found"})

if __name__ == "__main__":
    app.run(debug=True)
