from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def render_home():
    header = '<h1>inicio</h1>'
    
    return header

@app.route('/counter')
def count_btn():
    btn = '<btn>clique</btn>'
    return btn

@app.route('/txt')
def txt_area():
    txtbox = '<textarea></textarea>'
    return txtbox

@app.route('/gif')
def send_gif():
    gif = '<div class="tenor-gif-embed" data-postid="5716621" data-share-method="host" data-aspect-ratio="1.58" data-width="100%"><a href="https://tenor.com/view/nyan-cat-rainbow-cat-kitten-kitty-gif-5716621">Nyan Cat Rainbow GIF</a>from <a href="https://tenor.com/search/nyan+cat-gifs">Nyan Cat GIFs</a></div> <script type="text/javascript" async src="https://tenor.com/embed.js"></script>'
    return gif

@app.route('/link')
def redirect():
    lnk = 'http://localhost:7070/'
    return f'<a href="{lnk}">Voltar ao inicio</a>'

@app.route('/ola/<name>')
def grts(name):
    return render_template('index.html', person=name)



if __name__ == '__main__':
    app.run(debug=True, port=7070, host='0.0.0.0')