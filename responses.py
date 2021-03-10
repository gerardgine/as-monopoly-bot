from flask import jsonify


def success(text: str = None):
    response = {"success": True, "code": 200}
    if text:
        response["body"] = text
    return jsonify(response)


def error(code: int, text: str = None):
    """
    It looks like Telegram keeps retrying requests if we return an error status code,
    even if the code is 4xx, so we'll always return 200 and specify the error in the
    JSON body of the response on error.
    """
    response = {"success": False, "code": code}
    if text:
        response["body"] = text
    return jsonify(response)
