from app.database import Base
from app.database import engine

from app.models import *


def init_database():

    Base.metadata.create_all(
        bind=engine
    )


if __name__ == "__main__":

    init_database()

    print("Database Created Successfully")
