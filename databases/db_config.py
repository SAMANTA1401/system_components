import mysql.connector
import redis

# DB connection to Shard 1
shard_1 = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    database="user_db_shard_1",
    password="mYsql@2022",
)

# DB connection to Shard 2
shard_2 = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mYsql@2022",
    database="user_db_shard_2"
)

# Redis connection
redis_cache = redis.StrictRedis(host='localhost', port=6379, db=0, decode_responses=True)


def get_shard(user_id: int):
    # Simple modulo-based sharding
    if user_id % 2 == 0:
        return shard_1
    else:
        return shard_2



if __name__ == "__main__":
    print(get_shard(1))
    print(get_shard(2))
