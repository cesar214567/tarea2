 
from flask import Flask,render_template, request, session, Response, redirect

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)




if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))