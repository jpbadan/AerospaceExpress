from app.api.post import bp
from flask import jsonify, request
from app.models import Post
from app import db
from app.errors import id_notFound


@bp.route('/<int:uuid>', methods=['GET'])
def getPost(uuid):
    return jsonify({'post':
                    {'id': uuid,
                     'title': 'Embraer anuncia NADA',
                     'posted_by': 'userX',
                     'post_date': 122478998234,
                     'link': 'google.com',
                     'kharma': 12,
                     'ranking': 123,
                     }
                    })


@bp.route('/create', methods=['POST'])
def createPost():
    # Create a new post
    # data = request.get_json() or {}
    # Title + Link
    pass


@bp.route('/like/<int:postId>', methods=['PATCH'])
def likePost(postId):
    # Like a post. Accessible only to post creator
    # When a user likes a post the post kharma increases,
    # post id is listed under user profile
    if Post.query.filter_by(id=postId).update(
            {Post.likes: Post.likes + 1}):

        db.session.commit()
        return jsonify({'res': 'sucess'})
    else:
        return id_notFound(postId)


@bp.route('/unlike', methods=['PATCH'])
def unlikePost():
    # unLike a liked post. Accessible only to post creator
    # When a user likes a post the post kharma increases,
    # post id is listed under user profile
    pass


@bp.route('/delete', methods=['DELETE'])
def deletePost():
    # Delete a post. Accessible only to post creator
    pass
