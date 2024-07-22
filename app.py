from flask import Flask, render_template, url_for
import json

# Create some random data for this projects
table_data = [
    {"name": "John", "age": 30, "country": "USA"},
    {"name": "Jane", "age": 25, "country": "Canada"},
    {"name": "Bob", "age": 40, "country": "Mexico"}
]


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', data=table_data)

if __name__ == "__main__":
    app.run(debug=True)

    