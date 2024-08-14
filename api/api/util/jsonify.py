from flask import current_app

APP_CODES = {
    100: "OK.",
    101: "Feature is not implemented.",
    102: "Database error",
    103: "Schema instance error",
    104: "Input Validation error",
    105: "Resource Not Found",
}


def jsonify(state={}, metadata={}, status=200, code=100, headers={}):
    resource = {}
    resource["output"] = state
    resource["metadata"] = metadata
    resource["status"] = {"code": code}
    if current_app.debug is True:
        resource["status"]["message"] = APP_CODES[code]
    return resource, status, headers
