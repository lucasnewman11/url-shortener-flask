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
    url = request.form['url']
    filename = hashlib.sha1(url.encode('ascii')).hexdigest()[:10]
    f = open(path + filename, 'w')
    f.write(url)
    f.close()
    return Markup('To link to %s, use %s/redirect/%s') % (url, name, filename)

@app.route('/redirect/<key>')
def redirect(key):
    f = open(path + key, 'r')
    if f:
        url = f.read()
        return Markup('%s redirects to %s') % (key, url)
        f.close()
    else:
        return Markup('%s not found') % key

if __name__ == '__main__':
    app.run(host='0.0.0.0')
