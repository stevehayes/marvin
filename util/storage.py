import redis

try:
    server = redis.StrictRedis(host='pub-redis-14854.us-east-1-2.2.ec2.garantiadata.com', port=14854, db=0, password="marvin")
except:
    server = None



def has_key(key):
    if server:
        return server.exists(key)
    return False


def get_value(key):
    if server:
        return server.get(key)
    return None


def set_value(key, value):
    if server:
        server.set(key, value)


def add_to_list(key, value):
    if server:
        server.sadd(key,value)


def get_list(key):
    if server:
        return server.smembers(key)
    return None

def delete_from_list(key, value):
    if server:
        server.srem(key, value)


def get_server():
    return server

def get_random_value(key):
    if server:
        return server.srandmember(key)
    return None

def get_hash_value(hash_list_name, hash_key):
    if server:
        return server.hget(hash_list_name, hash_key)
    return None

def set_hash_value(hash_list_name, key, value):
    if server:
        server.hset(hash_list_name, key, value)


def delete_hash_value(hash_list_name, key):
    if server:
        server.hdel(hash_list_name, key)

def get_hash_keys(hash_list_name):
    if server:
        return server.smembers(hash_list_name)