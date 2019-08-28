from flask import Flask, Response, escape,request,render_template
from requests_html import HTMLSession

app = Flask(__name__)

@app.route('/')
def helloa():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'
    
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id
    
@app.route('/get/<path>')
def getPath(path):
    session = HTMLSession()
    print(path)
    try:
        get = session.get('http://www.baidu.com')
    except:
        return "Nothing has been got."
    return get.html.text

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    list = {
        1: name,
        2: 2333
            }
    return render_template('index.html' , list = list)

if __name__ == '__main__':
    app.run()