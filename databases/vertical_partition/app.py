import mysql.connector

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="userdb"
)
cursor = conn.cursor()

# Fetch user basic and profile
def get_user(user_id):
    cursor.execute("SELECT * FROM user_basic WHERE id = %s", (user_id,))
    basic = cursor.fetchone()

    cursor.execute("SELECT * FROM user_profile WHERE user_id = %s", (user_id,))
    profile = cursor.fetchone()

    return {
        "id": basic[0],
        "username": basic[1],
        "email": basic[2],
        "bio": profile[1],
        "last_login": profile[3]
    }

# Example usage
user = get_user(1)
print(user)
