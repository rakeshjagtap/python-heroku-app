from flask import Flask

app = Flask(__name__)


@app.route("/")
def show_landing_page() -> str:
    print("On landing page")
    print("Will write more logic later on.")
    return "Hello from Rakesh on the landing page v.0.0.2!"

@app.route("/uk")
def home() -> str:
    print("Inside uk.")
    print("Will write more logic later on.")
    return "Hello from Rakesh inside home Function v.0.0.1!"

@app.route("/uk-store")
def shop() -> str:
    print("Inside uk-store")
    print("Will write more logic later on.")
    return "Hello from Rakesh inside shop Function v.0.0.1!"