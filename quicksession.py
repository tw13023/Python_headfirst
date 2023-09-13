from flask import Flask, session
app = Flask('__name__')
app.secret_key = 'YouWillNeverGuess'

@app.route('/setuser/<user>')
def setuser(user:str) -> str:
    session['user'] = user
    return 'User Value set to:' + session['user']

@app.route('/getuser')
def getuser() -> str :
    return 'User Value is currently set to:' + session['user']

if __name__ == '__main__':
    app.run(debug=True)