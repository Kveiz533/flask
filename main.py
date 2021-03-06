from flask import Flask
from data import db_session
from data.users import User


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/mars_explorers.db")
    user = User()
    user.surname = input()
    user.name = input()
    user.age = int(input())
    user.position = input()
    user.speciality = input()
    user.address = input()
    user.email = input()
    user.hashed_password = ""
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
    # app.run()


if __name__ == '__main__':
    main()
