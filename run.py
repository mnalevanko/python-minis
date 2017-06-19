from flask import Flask

app = Flask(__name__)

@app.route('/michal')
def pozdrav():
    return 'Ahoj Misko, moj tvorca!'

if __name__ == '__main__':
    app.run(debug=True)
