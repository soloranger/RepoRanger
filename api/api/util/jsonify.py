from flask import current_app

APP_CODES = {
    100: "OK.",
    101: "Feature is not implemented.",
}


def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
    resource = state.copy()
    resource.update(metadata)
    resource["code"] = code
    if current_app.debug is True:
        resource["message"] = APP_CODES[code]
    return resource, status, headers
