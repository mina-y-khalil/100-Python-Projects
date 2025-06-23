import requests
from flask import Flask, render_template
import templates


app = Flask(__name__)

@app.route('/')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_requests = requests.get(blog_url)
    all_blog = blog_requests.json()

    return render_template("index.html",all_blog = all_blog)

if __name__ == "__main__":
    app.run(debug=True)
