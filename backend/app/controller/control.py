# from pyexpat import models


from app.db.session import session_scope
from app.models import AuthUser
from helper.alchemy_helper import get_stmt_upsert, select_by_query
from helper.error_helper import log_error
from app.core.config import settings
import psycopg2

def get_query_output(query, params):
    query_output = None
    with session_scope() as session:
        try:
            query_output = select_by_query(query=query, params=params, connection=session)
        except Exception as e:
            log_error(e)
    return query_output

def upsert_lst_user(_lst_user):
    with session_scope() as session:
        try:
            on_conflict_stmt = get_stmt_upsert(model=AuthUser,
                                               rows=_lst_user,
                                               index_elements=['id'],
                                               no_update_cols=[],
                                               not_update_null=True,
                                               debug=False)

            session.execute(on_conflict_stmt)
            session.commit()
            session.close()
        except Exception as e:
            log_error(e)
            return False
    return True
