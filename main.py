from flask import Flask, render_template, request, Markup
from pdb import set_trace
import hashlib

app = Flask(__name__)
path = "db/"
name = "localhost:5000"

@app.route('/url/')
def url_shortener():
    return render_template('index.html')

@app.route('/form_handler/', methods = ['GET', 'POST'])
def form_handler():
    #set_trace()
    url = request.form['url']
    filename = hashlib.sha1(url.encode('ascii')).hexdigest()
    f = open(path + filename, 'w')
    f.write(url)
    return Markup('To link to %s, use %s/redirect/%s') % (url, name, filename)

@app.route('/redirect/<key>')
def redirect():
    pass
    # look for file named key & redirect to the url in it

if __name__ == '__main__':
    app.run(host='0.0.0.0')
