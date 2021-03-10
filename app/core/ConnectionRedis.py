import redis
from app.config.redis import db

class ConnectionRedis:
    def __init__(self):
        self.pool = redis.ConnectionPool(host = db["hostname"], port = db["port"], password = db["password"], db = db["database"])

    @property
    def conn(self):
        if not hasattr(self, '_conn'):
            self.__getConnection()
        return self._conn

    def __getConnection(self):
        try:
            self._conn = redis.StrictRedis(connection_pool = self.pool, charset="utf8")
            print("Connection to redis has beend established...")
        except redis.ConnectionError:
            print("Cannot connect to redis...")