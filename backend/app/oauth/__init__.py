from app.core.config import settings
from app.oauth.oauth_base import OAuthBase

oauth_base_object = OAuthBase(secret_key=settings.OAUTH_SECRET_KEY)
