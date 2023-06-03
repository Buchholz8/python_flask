from flask import Flask
app = Flask(__name__)

@app.get('/hello')
def get_hello():
    return 'hello world'

app.run(debug=True)