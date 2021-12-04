from app.api.user import bp
from app.errors import bad_request
from flask import jsonify, request, make_response
from app.models import User, Post


@bp.route('/<string:userName>', methods=['GET'])
def getUserInfo(userName):
    queryResult = User.query.first()
    postqueryResult = Post.query.first()
    # Return user profile
    return jsonify({'user':
                    {
                        'userName': queryResult.userName,
                        'kharma': queryResult.kharma,
                        'email': queryResult.email,
                        'createdAt': queryResult.createdAt,
                        'urlPost': postqueryResult.url,
                        'postTitle': postqueryResult.title,
                        'postedBy': postqueryResult.postedBy.userName
                    },
                    }
                   )


@bp.route('/<string:userName>/submissions', methods=['GET'])
def getPostsFrom(userName):
    # Returns all sumissions from specified user
    return jsonify({'post_list': [userName]})


@bp.route('/create', methods=['POST'])
def createUser():
    # Create a new user
    data = request.get_json() or {}
    if 'userName' not in data or 'password' not in data:
        return bad_request('bad')

    res = make_response(data)
    res.status_code = 201

    return res


@bp.route('/edit', methods=['PUT'])
def editUser():
    pass


@bp.route('/delete', methods=['DELETE'])
def deleteUser():
    pass


@bp.route('/favorite', methods=['PATCH'])
def favoritePost():
    pass


@bp.route('/unfavorite', methods=['PATCH'])
def unfavoritePost():
    pass


@bp.route('/favorites', methods=['GET'])
def listFavoritePosts():
    # Lists all favorited posts - Only accessible by user
    pass


@bp.route('/hide', methods=['PATCH'])
def hidePost():
    pass


@bp.route('/unhide', methods=['PATCH'])
def unhidePost():
    pass


@bp.route('/hiden', methods=['GET'])
def listHidenPosts():
    # Lists all hiden posts - Only accessible by user
    pass
