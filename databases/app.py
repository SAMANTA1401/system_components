from flask import Flask, request, jsonify
from db_config import get_shard, redis_cache 
import json

app = Flask(__name__)

@app.route("/user", methods=["POST"])
def create_user():
    data = request.get_json()
    user_id = data["id"]
    name = data["name"]

    conn = get_shard(user_id)
    cursor = conn.cursor()

    try:
        cursor.execute("INSERT INTO users (id, name) VALUES (%s, %s)", (user_id, name))
        conn.commit()

        # Cache this new user
        redis_cache.set(f"user:{user_id}", json.dumps({"id": user_id, "name": name}))

        return jsonify({"message": f"User inserted into shard {user_id % 2 + 1}"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/user/<int:user_id>", methods=["GET"])
def get_user(user_id):

    # Check Redis cache first
    cached_user = redis_cache.get(f"user:{user_id}")
    if cached_user:
        return jsonify(json.loads(cached_user))
    
    # If not cached, fetch from DB
    conn = get_shard(user_id)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    result = cursor.fetchone()

    if result:
        # Cache result in Redis
        redis_cache.set(f"user:{user_id}", json.dumps(result))
        
        return jsonify(result)
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)
