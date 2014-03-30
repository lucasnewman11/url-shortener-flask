from flask import Flask, render_template, request, Markup

app = Flask(__name__)

@app.route('/url/')
def url_shortener():
    return render_template('index.html')

@app.route('/form_handler/', methods = ['GET', 'POST'])
def form_handler():

    return Markup('%s') % request.form['url'] # request.args.get('url')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
