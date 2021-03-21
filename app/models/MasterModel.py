import cx_Oracle
from pydantic import BaseModel
from app.sessions import database_instance


class MasterModel(BaseModel):

    @staticmethod
    def call_sp(name, parameters, with_return_cursor=True):
        cursor = database_instance.pool.acquire().cursor()
        l_cur = cursor.var(cx_Oracle.CURSOR)
        if parameters is not None:
            sp_params = ((l_cur, ) + parameters) if with_return_cursor else parameters
        else:
            sp_params = (l_cur, ) if with_return_cursor else None
        l_test = cursor.callproc(name, sp_params)
        ret_cursor = l_test[0]
        return ret_cursor

    @staticmethod
    def load(from_where, data):
        raise Exception('Error loading object from ' + from_where + ' NOT IMPLEMENTED')
