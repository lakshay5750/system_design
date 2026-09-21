from after_user import User
from after_user_repository import UserRepository

user=User('lakshay varshney','25','lakshyavarshney62@gmail.com')
user_repo=UserRepository('db','root','root')

print(user_repo.save_to_database(user))
print(user_repo.delete_from_database(user))