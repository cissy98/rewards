from flask import Blueprint, render_template
import glob

bp = Blueprint('bp', __name__, template_folder='templates')


def fetch_points():
    final_points=[]
    points = glob.glob('./points/*.point')

    for point in points:
        with open(point) as _file:
            final_points.append(_file.read())
        _file.close()

    return final_points



@bp.route('/')
def show():
    return render_template('index.html', points=fetch_points())
