from flask import Flask 
app = Flask(__name__)
@app.route('/')
def head():
     return 'Hello World:>'
@app.route('/secondpage')
def second():
     return 'this is the second page and im already tired:>'
@app.route('/third')
def third():
     return 'this is the third page i wanna quiet:>'
@app.route('/fourth/<string:id>')
def fourth(id):
     return f'this is the fourt page why the hell am i still hear? id of this page is {id}'

if __name__ == '__main__':

     #app.run(debug=True, port=3000)
     app.run(host= '0.0.0.0', port=80)