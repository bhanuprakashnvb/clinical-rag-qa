import redis
import hashlib
import json
r=redis.Redis(host='localhost',port=6379,db=0)

def cache_get(key):
    hashed = hashlib.sha256(key.encode()).hexdigest() # encode= bytes, hexdigest= hexaadecimal , both needed by sha256 for encrytion
    result =r.get(hashed)  #Attempts to retrieve a value 
    return json.loads(result) if result else None  #if value found-- decodes into json format
    return None

def cache_set(key,value):
    hashed = hashlib.sha256(key.encode()).hexdigest()
    r.set(hashed, json.dumps(value), ex=3600)
    pass

    