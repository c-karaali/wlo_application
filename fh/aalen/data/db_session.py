import sqlalchemy as sa
import sqlalchemy.orm as orm
from fh.aalen.data.modelbase import ModelBase


class DBSession:
    __session=None

    @classmethod
    def get_session(cls):
        # If a session exists, we can return it
        if cls.__session!=None:
            return cls.__session

        # Otherwise we must create a session
        connection_string = "postgresql+psycopg2://postgres:postgres@localhost/videoarchive"
        print(f"Connecting to database: {connection_string}")

        engine = sa.create_engine(connection_string, echo=True)
        Session = orm.sessionmaker(bind=engine)
        cls.__session=Session()

        ModelBase.metadata.create_all(engine)
        return cls.__session