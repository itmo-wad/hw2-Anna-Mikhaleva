from flask import Flask, send_from_directory, render_template
app = Flask(__name__)

#Render HTML document on http://localhost:5000/
@app.route('/')
def index():
    return render_template('index.html')

# Show static images on http://localhost:5000/images/<image_name>
@app.route('/images/')
def show_img(path):
    return send_from_directory('images', path)

# External CSS and JS files are returned on http://localhost:5000/static/<js/css filename>
@app.route('/static/<path:filename>')
def show_css_files(filename):
    return send_from_directory('static', filename)

if __name__ == "__main__":
    app.run(host='localhost', port=5000, debug=True)