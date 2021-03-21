from datetime import timedelta

import redis
import sys


class Redis:

    def __init__(self):
        self.conn = None

    def connect(self, settings):
        if not self.conn:
            try:
                client = redis.Redis(
                    host=settings.REDIS_HOST,
                    port=settings.REDIS_PORT,
                    password=settings.REDIS_PASSWORD,
                    db=0,
                    socket_timeout=5,
                )
                ping = client.ping()
                if ping is True:
                    print('conectado a redis')

                self.conn = client
            except redis.AuthenticationError:
                print("AuthenticationError")
                sys.exit(1)

    def startup(self):
        if not self.conn:
            return None


    def get(self, key):
        if self.conn:
            return self.conn.get(key)
        return None

    def set(self, key, val, delta=timedelta(minutes=10)):
        """
        El default delta son 10 minutos
        """
        if self.conn and key is not None:
            result = self.conn.setex(key, delta, value=val)
            return result

        return False

    def close(self):
        if self.conn:
            self.conn.dissconect()

