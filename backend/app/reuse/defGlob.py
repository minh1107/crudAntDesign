from app.db.session import session_scope
from app.models import AuthUser
from helper.alchemy_helper import get_stmt_upsert, select_by_query
from helper.error_helper import log_error

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

def assignValueToAuthUser(user, user_model, user_id):
    if user_id != None:
        user_model.id = int(user_id)
    if user.name != None and user.username != None and user.email != None and user.phone != None:
        user_model.name = user.name
        user_model.username = user.username
        user_model.email = user.email
        user_model.phone = user.phone
    else:
        return False
    user_model.website = user.website
    user_model.addressstreet = user.addressstreet
    user_model.addresssuite = user.addresssuite
    user_model.addresscity = user.addresscity
    user_model.addresszipcode = user.addresszipcode
    user_model.companyname = user.companyname
    user_model.companycatchphrase = user.companycatchphrase
    user_model.companybs = user.companybs
    return upsert_lst_user([user_model.dict()])
