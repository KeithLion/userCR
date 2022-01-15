from flask import flask, render_template, redirect, request
from users import User
app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
