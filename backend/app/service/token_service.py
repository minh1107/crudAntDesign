import traceback

from app.oauth import oauth_base_object


def create_token(user_id):
    return oauth_base_object.create_access_token({
        "user_id": user_id
    })


if __name__ == '__main__':
    print(create_token(1))
    try:
        print(oauth_base_object.get_current_token(
            "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxLCJleHAiOjE2NDYzMjg5Nzh9.rSjqkQzlIsNpftgTeeNnSnSmfPGRj_1lCZ5C6ByNfDw"))
    except Exception as e:
        traceback.print_exc()
