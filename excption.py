from ___init__ import app


class APIException(Exception):

    def __init__(self, error_id, message, code=500):
        self.raw_message = message
        self.error_id = error_id
        self.code = code
        self.message = message

    def to_dict(self):
        result = {
            "id": self.error_id,
            "message": self.message,
        }
        return result


@app.errorhandler(APIException)
def handle_api_exception(error):
    from flask import jsonify
    response = jsonify(error.to_dict())
    response.status_code = error.code
    return response
