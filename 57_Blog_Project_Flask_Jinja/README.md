# 📝 Flask Blog Project

<p align="center">
  <img src="https://redeem-innovations.com/wp-content/uploads/2025/06/blog.jpg" alt="Artwork Grid Example" />
</p>

A dynamic blog website built with Flask. It pulls blog post data from an external API and displays individual blog posts using routing and templates.

## 🎯 Project Goal

- Learn how to render dynamic content using Flask and Jinja2.
- Work with JSON APIs and integrate them into a web frontend.
- Build a multi-page blog-style layout using HTML and CSS.

## 🧠 Python Concepts Practiced

- Flask routing and app structure
- HTTP requests using `requests`
- Dynamic routing with URL parameters (`/post/<int:index>`)
- Jinja2 templating for HTML generation
- Working with APIs (`npoint.io` JSON endpoint)
- Passing data to templates

## 📋 Features

- Home page displaying all blog posts
- Clickable links to individual posts
- External blog content loaded from a remote JSON endpoint
- Clean layout using custom CSS and Google Fonts

## 🛠 How to Run

1. Clone the project and ensure Flask is installed:

```bash
pip install flask requests
```

2. Run the app:

```bash
python server.py
```

3. Open your browser at `http://127.0.0.1:5000` to view the blog.

---

This project simulates how content platforms work by dynamically generating pages from API data. Great for mastering backend–frontend communication!
