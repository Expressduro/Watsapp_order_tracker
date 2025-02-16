from flask import Flask
from routes import bp

app = Flask(__name__)

# Register Blueprint
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
