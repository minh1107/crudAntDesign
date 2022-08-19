from app.main import app as fast_api_app


def get_all_url_list():
    url_list = [{"path": route.path, "name": route.name} for route in fast_api_app.router.routes]
    return url_list
