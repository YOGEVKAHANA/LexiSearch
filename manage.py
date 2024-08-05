#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import cx_Oracle
cx_Oracle.init_oracle_client(r'C:\Users\sapirg\Oracle\instantclient-basic-windows.x64-23.4.0.24.05\instantclient_23_4')

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LexiSearch.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


os.environ['PATH'] = r'C:\Users\sapirg\Oracle\instantclient-basic-windows.x64-23.4.0.24.05\instantclient_23_4;' + \
                     os.environ['PATH']
os.environ['ORACLE_HOME'] = r'C:\Users\sapirg\Oracle\instantclient-basic-windows.x64-23.4.0.24.05\instantclient_23_4'

# Initialize Oracle Client (uncomment if needed)
# cx_Oracle.init_oracle_client(lib_dir=r"C:\Users\sapirg\Oracle\instantclient-basic-windows.x64-23.4.0.24.05\instantclient_23_4")

# Oracle database connection details
host = '192.168.1.162'  # IP address of the VM
port = '1521'  # Default Oracle listener port
service_name = 'freepdb1'  # Service name from lsnrctl status
username = 'hr'  # Replace with your actual username
password = 'oracle'  # Replace with your actual password
#
# # Construct the connection string
# dsn = cx_Oracle.makedsn(host, port, service_name=service_name)
#
# try:
#     # Establish the connection
#     connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
#     print("Connection successful!")
#
#     # Create a cursor
#     cursor = connection.cursor()
#
#     # Execute a sample query
#     cursor.execute("SELECT * FROM employees")
#     for row in cursor:
#         print(row)
#
#     # Close the cursor and connection
#     cursor.close()
#     connection.close()
#
# except cx_Oracle.DatabaseError as e:
#     error, = e.args
#     print(f"Error connecting to the database: {error.message}")

if __name__ == '__main__':
    main()
