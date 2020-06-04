 
from flask import Flask,render_template, request, session, Response, redirect

app = Flask(__name__)

@app.route('/static/<content>')
def static_content(content):
    return render_template(content)

@app.route('/multiplo/<numero>/<numero2>')
def multiplo(numero,numero2):
    contador = int(numero)%int(numero2)
    if( contador == 0):
        return ("esmultiplo")
    else:
        return ("noesmultiplo")



@app.route('/palindromo/<palabra>')
def palindromo(palabra):
    if(str(palabra)==str(palabra[::-1])):
        return "es palindrome"
    else:
        return "noespalidnrome"


if __name__ == '__main__':
    app.secret_key = ".."
    app.run(port=8080, threaded=True, host=('127.0.0.1'))