from sqlalchemy.sql.expression import desc
from app.api import bp
from flask import jsonify
from app.models import Post
from app.config import QUERY_LIM

from flask_sqlalchemy import sqlalchemy
from sqlalchemy import desc


@bp.route('/', methods=['GET'])
def getTopPosts():
    # Returns the XX top posts
    queryResult = Post.query.order_by(desc('ranking')).limit(QUERY_LIM).all()

    queryResultList = {}
    for post in queryResult:
        queryResultList[post.id] = {
            'title': post.title,
            'url': post.url,
            'userId': post.userId,
            'createdAt': post.createdAt,
            'ranking': post.ranking,
            'likes': post.likes
        }

    return jsonify(queryResultList)


@ bp.route('/latest', methods=['GET'])
def getLatestPosts():
    # Returns the XX latest posts
    return jsonify({'post_list': ['latest 1', 'ihull2']})

# @bp.route('/submissions/<int:userUUID>', methods=['GET'])
# def getPostsFrom(userUUID):
#     # Returns all sumissions from specified user
#     return jsonify({'post_list': [userUUID]})
