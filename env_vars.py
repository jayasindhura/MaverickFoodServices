import os

db_user = os.environ.get('DB_USER')
db_password = os.environ.get('DB_PASS')
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG_VALUE = os.environ.get('DEBUG')

print(db_user)
print(db_password)
print(SECRET_KEY)
print(DEBUG_VALUE)