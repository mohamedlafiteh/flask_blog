from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {'author': 'Ali lafiteh',
     'title': 'blog post 1',
     'content': 'first post content',
     'date_posted': 'April 20, 2018'
     },
    {'author': 'lauren curr',
     'title': 'blog post 2',
     'content': 'first post content',
     'date_posted': 'April 21, 2018'
     }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
