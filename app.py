from flask import Flask
from views.index import bp as index_bp
from views.getpoint import bp2 as getpoint_bp

app = Flask(__name__, template_folder='templates')

app.register_blueprint(index_bp)
app.register_blueprint(getpoint_bp)
