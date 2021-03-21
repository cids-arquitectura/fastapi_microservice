import sys

import cx_Oracle


class Database:

    def __init__(self):
        self.pool = None

    def create_pool(self, settings):
        if not self.pool:
            try:
                connection_str = cx_Oracle.makedsn(settings.DB_HOST, settings.DB_PORT, sid=settings.DB_SID)
                self.pool = cx_Oracle.SessionPool(settings.DB_USER,
                                                  settings.DB_PASS,
                                                  connection_str,
                                                  min=int(settings.DB_CONN_MIN),
                                                  max=int(settings.DB_CONN_MAX),
                                                  increment=1,
                                                  encoding="UTF-8")
                print("CONNECTED TO DB POOL")
            except Exception as e:
                print("ERROR CONECTANDOSE A LA DB")
                print(e)
                sys.exit(1)

    def close_pool(self):
        if not self.pool:
            try:
                self.pool.close()
            except Exception as e:
                print(e)
