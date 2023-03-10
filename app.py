from flask import Flask, render_template, request

app = Flask(__name__)

# Define a route for the home page
@app.route('/')
def home():
    return render_template('home.html')

# Define a route for the form submission
@app.route('/post_cves', methods=['POST'])
def post_cves():
    cves = request.json.get('cves', [])
    # Code to process the CVE information and display it on the website
    return "CVE information posted successfully"

if __name__ == '__main__':
    app.run()
