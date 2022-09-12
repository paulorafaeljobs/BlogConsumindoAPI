import requests, json
from flask import Flask , request
from flask import render_template
app = Flask(__name__)

token = "aaeabc5f3599593eb4587ab7953a01fb"
@app.route('/')
def exibir():
    dataAPI = requests.get("http://localhost:8000/api/blog/"+token)
    data = json.loads(dataAPI.content)
    return render_template('home.html',blog=data,title='Blog')

@app.route('/post')
def query_example():
    url = request.args.get('url')
    dataAPI = requests.get("http://localhost:8000/api/blog/"+ token+ "/"+url)
    data = json.loads(dataAPI.content)
    title = data[0]['title']    
    return render_template('post.html',post=data,title=title)

app.run(debug=True)