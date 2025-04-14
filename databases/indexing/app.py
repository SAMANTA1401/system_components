from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Connect to MySQL database
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="mYsql@2022",  # replace with your actual password
        database="index_demo"
    )

@app.route("/add")
def add_users():
    db = get_connection()
    cursor = db.cursor()
    
    # Insert 10,000 users
    for i in range(100):
        name = f"User {i}"
        email = f"user{i}@example.com"
        age = 20 + (i % 30)
        cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name, email, age))
    
    db.commit()
    cursor.close()
    db.close()
    return "✅ Inserted 100 users."

@app.route("/search/<email>")
def search_by_email(email):
    db = get_connection()
    cursor = db.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM users WHERE email = %s", (email,))
    user = cursor.fetchone()
    
    cursor.close()
    db.close()
    
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found."})

if __name__ == "__main__":
    app.run(debug=True)
