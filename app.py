from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def principal():

 return render_template("index.html")

if __name__ == '__main__':

 app.run(debug=False,port=8080,host="0.0.0.0")
