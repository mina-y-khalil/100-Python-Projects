import requests
from flask import Flask, render_template


app = Flask(__name__)
blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
blog_requests = requests.get(blog_url)
all_blog = blog_requests.json()

@app.route('/')
def home():

    return render_template("index.html",all_blog = all_blog)

@app.route('/post/<int:index>')
def show_post (index):
    for post in all_blog:
        if post['id'] == index:
            return render_template("post.html", post=post)

    return "Bad Data"

if __name__ == "__main__":
    app.run(debug=True)
