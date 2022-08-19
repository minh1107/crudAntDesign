from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, Session
from sqlalchemy.pool import QueuePool

from app.core.config import settings

engine = create_engine(settings.SQLALCHEMY_DATABASE_URI,
                       pool_size=24,
                       pool_pre_ping=True,
                       pool_use_lifo=True,
                       # use_batch_mode=True,
                       # statement_cache_size=0
                       echo=False,
                       echo_pool=False,
                       poolclass=QueuePool
                       )

connection_session = engine.connect()

SessionScope = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


@contextmanager
def session_scope() -> Session:
    """Provide a transactional scope around a series of operations."""
    session = SessionScope()
    session.expire_on_commit = False
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
