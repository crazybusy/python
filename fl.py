from flask import Flask
from bit import getpercentfin

app = Flask(__name__)
 
@app.route("/")
def hello():
    return str(getpercentfin())
 
if __name__ == "__main__":
    app.run()
