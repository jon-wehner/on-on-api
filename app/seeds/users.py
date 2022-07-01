from app.models import db, User


def seed_users():

    demo_user = User(username='demo', email='demo@demo.com',
                     password='password')
    db.session.add(demo_user)
    db.session.commit()


def undo_users():
    db.session.execute('TRUNCATE users RESTART IDENTITY CASCADE')
    db.session.commit()
