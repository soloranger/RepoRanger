from flask import Flask,request,Blueprint
from os import environ

# app = Flask(__name__)

app_v1= Blueprint("app_V1",__name__,url_prefix="/app/v1")
app_v2= Blueprint("app_V2",__name__,url_prefix="/app/v2")

@app_v1.route("/test")
def app_v1_test():
    return "Hello from App1 !"

@app_v2.route("/test")
def app_v2_test():
    return "Hello from App2 !"



def create_app():
    app = Flask(__name__)
    if bool(int(environ.get("ENABLE_APP_V1", "0"))):
        app.register_blueprint(app_v1)
    if bool(int(environ.get("ENABLE_APP_V2", "0"))):
        app.register_blueprint(app_v2)
    return app




# @app.route("/<name>")
# def index(name):
#     print(request.get_data)
#     return f"Hello {name}! from {request.remote_addr}"





# if __name__ == "__main__":
#     app.run()