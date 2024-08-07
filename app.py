from flask import Flask, make_response

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def principal():
 html_content = "<h1>It Works</h1>"
 return make_response(html_content)

if __name__ == '__main__':

 app.run(debug=False,port=8080,host="0.0.0.0")
