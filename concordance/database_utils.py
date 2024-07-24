import cx_Oracle
from django.conf import settings
import os

os.environ['PATH'] = r'C:\Users\sapirg\Oracle\instantclient-basic-windows.x64-23.4.0.24.05\instantclient_23_4;' + \
                     os.environ['PATH']
os.environ['ORACLE_HOME'] = r'C:\Users\sapirg\Oracle\instantclient-basic-windows.x64-23.4.0.24.05\instantclient_23_4'


def get_oracle_connection():
    # Construct the connection string
    dsn = cx_Oracle.makedsn(
        settings.DATABASES['default']['HOST'],
        settings.DATABASES['default']['PORT'],
        service_name=settings.DATABASES['default']['NAME']
    )
    # Establish the connection
    connection = cx_Oracle.connect(
        user=settings.DATABASES['default']['USER'],
        password=settings.DATABASES['default']['PASSWORD'],
        dsn=dsn
    )
    return connection


def execute_sql(sql, params=None):
    with get_oracle_connection() as connection:
        with connection.cursor() as cursor:
            if params:
                cursor.execute(sql, params)
            else:
                cursor.execute(sql)
            if sql.strip().upper().startswith('SELECT'):
                return cursor.fetchall()
            else:
                connection.commit()
