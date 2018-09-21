from flask import Blueprint, render_template, request, redirect
import random


bp2 = Blueprint('bp2', __name__, template_folder='templates')

def random_string(length=16):
    final_string=''
    chars = 'adkfasdgsdgete20123456789'

    for i in range(0,length):
        final_string += chars[random.randint(0, len(chars)-1)]
    return final_string

@bp2.route('/getpoint', methods=['POST', 'GET'])
def show():
    if request.method == 'POST':
        if request.form.get('getpoints'):
            text = request.form.get('pointtext')
            #return random_string(16)   #text

            with open('./points/{}.point'.format(random_string()), 'w+') as _file:
                _file.write(text)
            _file.close()

            return redirect('/')

            #return _file.name.replace("./points/","") + ".point file saved"

    return render_template('getpoint.html')