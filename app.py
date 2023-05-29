from flask import Flask
import os
app = Flask(__name__)

@app.route('/',methods=['GET'])
def home():
    return 'Hello world'

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)
    # host=0.0.0.0,port=5000 with the help of this we can host application with our local ip and locahost
    # http://172.31.96.1:5000/
    # http://localhost:5000/