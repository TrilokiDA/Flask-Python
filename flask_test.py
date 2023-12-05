from flask import Flask, redirect, url_for, request, render_template, Response,jsonify, abort
from werkzeug.exceptions import HTTPException
import pandas
import json


app = Flask(__name__)

# @app.route('/')
# def index():
#     res = "Hello, World!"
#     return Response(res)

@app.errorhandler(Exception)
def handle_error(e):
    if isinstance(e, HTTPException):
        code = e.code
    else:
        code = 500
    ret = json.dumps({"error": str(e)})
    return Response(ret, status=code, mimetype="application/json")

##### 1. Installation and Setup:
@app.route('/')
def hello_world():
    return "Hello, World! This is my Flask API."


##### 2. Routing and Endpoints:
# @app.route('/user/<username>')
# def get_user(username):
#     return f'User: {username}'

# @app.route('/success/<name>')
# def success(name):
#    return 'Welcome %s' % name
#
# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


##### 3. HTTP Methods and Request Handling
# @app.route('/submit', methods=['POST'])
# def submit_data():
#     data = request.form['data']
#     return f'Submitted data: {data}'


##### 4. JSON Responses
# @app.route('/api/data', methods=['POST'])
# def get_json_data():
#     key = request.get_json()['key']
#     value = request.get_json()['value']
#     data = {key: value}
#     return jsonify(data)


##### 5. Error Handling
# @app.route('/user/<user_id>')
# def get_user_by_id(user_id):
#     def get_user_from_database(id):
#         return id
#     user = get_user_from_database(user_id)
#     if user.isdigit():
#         abort(403, description='User not foundsfdsf')
#     return jsonify(user)

# @app.get('/upload-excel')
# def upload():
#     return render_template('upload-excel.html')
#
# @app.post('/view')
# def view():
#     file = request.files['file']
#     data = pandas.read_excel(file)
#     return data.to_html()

# @app.post('/file-upload')
# def upload_file():
#     file = request.files['file']
#     # file.save(file.filename)
#     data = pandas.read_excel(file)
#     return data.to_html()

# @app.route('/thanks')
# def thanks():
#     return render_template('thanks.html')

if __name__ == '__main__':
    app.run(debug=True)
