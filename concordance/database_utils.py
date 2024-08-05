from django.conf import settings
import cx_Oracle


def get_oracle_connection():
    # Use the DSN directly from the settings
    dsn = settings.DATABASES['default']['NAME']

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
