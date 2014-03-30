from flask import Flask, render_template, request, Markup
import hashlib

app = Flask(__name__)

@app.route('/url/')
def url_shortener():
    return render_template('index.html')

@app.route('/form_handler/', methods = ['GET', 'POST'])
def form_handler():
    return Markup('%s') % hashlib.sha1(request.form['url'].encode('ascii')).hexdigest()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
