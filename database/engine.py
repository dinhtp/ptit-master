import os
import sqlalchemy


def open_engine():
    db_host = os.environ['MYSQL_HOST']
    db_user = os.environ['MYSQL_USER']
    db_password = os.environ['MYSQL_PASSWORD']
    db_name = os.environ['MYSQL_DATABASE']

    connection_string = "mysql+pymysql://%s:%s@%s/%s" % (
        db_user, db_password, db_host, db_name
    )

    return sqlalchemy.create_engine(connection_string)


def close_engine(mysql_engine):
    mysql_engine.dispose()
