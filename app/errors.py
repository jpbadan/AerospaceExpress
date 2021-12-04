from flask import make_response


def bad_request(errorMessage):
    res = make_response(f'ERROR: {errorMessage}')
    res.status_code = 400
    return res


def id_notFound(id):
    res = make_response(f'The id:{id} cannot be found')
    res.status_code = 400
    return res
