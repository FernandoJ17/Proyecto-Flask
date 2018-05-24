from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('user.html')

@app.route('/hash/<string:parametro>/<string:nombre>/')
def main(parametro=None,nombre=None):
    if parametro is not None and nombre is not None:
        return render_template('templat.html', param=parametro, param2 = nombre)

@app.route('/hash/<string:parametro>/<string:nombre>/json')
def main_json(parametro=None, nombre = None):
    if parametro is not None:
        return jsonify(parametro , nombre)

if __name__=='__main__':
    app.run(debug=True)