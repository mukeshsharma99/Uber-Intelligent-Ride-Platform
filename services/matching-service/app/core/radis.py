import redis

redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)

def test_redis():
    return redis_client.ping()