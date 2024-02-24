from flask import Flask

app = Flask(__name__)

# Configure Flask to serve static files from the 'assets' directory
app.static_folder = 'assets'

@app.route('/')
def index():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True)
