from app import db
from app.models import User, Post


def createNewDb():
    db.create_all()


def inserts():
    user1 = User(userName='user1',
                 email='user1@gmail.com', password='12345')
    user2 = User(userName='user2',
                 email='user2@gmail.com', password='abcdef')
    user3 = User(userName='user3',
                 email='user3@gmail.com', password='a1b2c3d4')

    db.session.add(user1)
    db.session.add(user2)
    db.session.add(user3)

    post1 = Post(title='PostTitle1',
                 url='pskjlf.com/hjiwef', postedBy=user1)
    post11 = Post(title='post2user1',
                  url='gogo.com', postedBy=user1)
    post12 = Post(title='post 3 do user 1',
                  url='ijo.com', postedBy=user1)

    post2 = Post(title='apredneda',
                 url='df.com/gogogo', postedBy=user2)
    post21 = Post(title='Msafdi guinu',
                  url='hjio92.com', postedBy=user2, ranking=12)

    post3 = Post(title='ew324 jkh 40023 jfdds',
                 url='hi3208.com', postedBy=user3)

    db.session.add(post1)
    db.session.add(post11)
    db.session.add(post12)
    db.session.add(post2)
    db.session.add(post21)
    db.session.add(post3)

    db.session.commit()
