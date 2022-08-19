# poetry install python-jose -E cryptography
# poetry install passlib -E bcrypt
import random
import string
import traceback
from datetime import datetime, timedelta
from typing import Optional

import jose
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from passlib.context import CryptContext

from app.db.session import session_scope
from app import models
from app import schemas

credentials_exception = HTTPException(
    status_code=status.HTTP_401_UNAUTHORIZED,
    detail="Could not validate credentials",
    headers={"WWW-Authenticate": "Bearer"},
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
token_alive_time_in_milis = float(60)
token_algorithm = "HS256"


class OAuthBase:
    def __init__(self, secret_key):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
        self.secret_key = secret_key

    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)

    def get_password_hash(self, password):
        return self.pwd_context.hash(password)

    def authenticate_user_by_basicauth(self, email: str, password: str):
        with session_scope() as session:
            try:
                auth_user = session.query(models.AuthUser).filter_by(email=email, is_active=True).first()
                if auth_user is None:
                    return None
                if self.verify_password(plain_password=password, hashed_password=auth_user.password):
                    return auth_user.id
            except Exception as e:
                traceback.print_exc()
                return None
        return None

    def create_access_token(self, data: dict, expires_delta: Optional[timedelta] = timedelta(minutes=15)):
        to_encode = data.copy()
        if expires_delta is not None:
            expire = datetime.now() + expires_delta
            to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=token_algorithm)
        return encoded_jwt

    def login_for_access_token(self, email: str, password: str):
        user_id = self.authenticate_user_by_basicauth(email=email, password=password)
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(minutes=token_alive_time_in_milis)
        access_token = self.create_access_token(
            data={"user_id": user_id}, expires_delta=access_token_expires
        )
        return {"access_token": access_token, "token_type": "bearer"}

    @staticmethod
    def _get_user(user_id: int) -> Optional[schemas.AuthUser]:
        auth_user = None
        with session_scope() as session:
            try:
                auth_user = session.query(models.AuthUser).filter_by(id=user_id, is_active=True).first()
            except Exception as e:
                traceback.print_exc()
        return auth_user

    @staticmethod
    def _get_token(jwt_token: str) -> Optional[schemas.Token]:
        with session_scope() as session:
            try:
                token: models.Token = session.query(models.Token).filter_by(jwt_token=jwt_token).first()
            except Exception as e:
                traceback.print_exc()
        if token is not None:
            return schemas.Token.from_orm(token)
        return token

    @staticmethod
    def _get_user_by_email(email: str):
        with session_scope() as session:
            try:
                auth_user = session.query(models.AuthUser).filter_by(email=email, is_active=True).first()
                if auth_user is None:
                    raise credentials_exception
                user_info = {
                    "email": auth_user.email,
                    "user_id": auth_user.id,
                    "username": auth_user.username,
                    "fullname": auth_user.fullname
                }
            except Exception as e:
                traceback.print_exc()
                user_info = None
        return user_info

    def get_current_user(self, token: str = Depends(oauth2_scheme)) -> schemas.AuthUser:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[token_algorithm])
            user_id: int = payload.get("user_id")
            if user_id is None:
                raise credentials_exception
            user = self._get_user(user_id=user_id)
            if user is None:
                raise credentials_exception
            return user
        except JWTError:
            traceback.print_exc()
            raise credentials_exception

    def get_current_token(self, token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[token_algorithm])
            # payload data: user_id
            user_id: int = payload.get("user_id")
            if user_id is None:
                raise credentials_exception
            token = self._get_token(jwt_token=token)
            if token is None:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token can't not validate: #00001",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            if not token.is_active:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token can't not validate: #00001",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            if token.user_id != user_id:
                # todo: remove this token
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Token can't not validate: #00001",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            user = self._get_user(user_id=user_id)
            if user is None:
                raise credentials_exception
            if not user.is_active:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="This token doesn't belong to active user",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            return token
        except jose.ExpiredSignatureError:
            # todo remove this token
            traceback.print_exc()
            raise credentials_exception
        except JWTError:
            traceback.print_exc()
            raise credentials_exception

    # return token, user_id
    def generate_access_token_from_email(self, email):

        user_info = self._get_user_by_email(email=email)
        if user_info is None:
            raise credentials_exception
        access_token = self.create_access_token(
            data={"user_id": user_info['user_id']}, expires_delta=timedelta(minutes=token_alive_time_in_milis)
        )
        return {
            "token": access_token,
            "email": user_info['email'],
            "user_id": user_info['user_id'],
            "username": user_info['username'],
            "fullname": user_info['fullname']
        }

    def create_auth_user_if_non_exist(self, email, fullname, username, password=None, is_active=True):
        with session_scope() as session:
            try:

                auth_user = session.query(models.AuthUser).filter_by(email=email).first()

                if auth_user is None:
                    _hash_password = None
                    if password is None:
                        _hash_password = self.get_password_hash(password=''.join(random.choice(
                            string.ascii_uppercase + string.digits + string.ascii_lowercase + string.printable) for _ in
                                                                                 range(20))
                                                                )
                    else:
                        _hash_password = self.get_password_hash(password=password)
                    auth_user = models.AuthUser(email=email, fullname=fullname, username=username, is_active=is_active,
                                                password=self.get_password_hash(password=_hash_password))
                    session.add(auth_user)
                    session.commit()
                    session.close()
            except Exception as e:
                traceback.print_exc()
                return None
        user_info = self.generate_access_token_from_email(email=email)
        return user_info
