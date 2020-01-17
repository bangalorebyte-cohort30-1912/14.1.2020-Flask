from flask import Flask, render_template, request

app = Flask(__name__)

COMMENTS = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/comment',  methods=['GET', 'POST'])
def comment():
    if request.method == "POST":
        name = request.form['name']
        comment = request.form['comment']
        COMMENTS.append((name, comment))        
        return render_template('comment.html', COMMENTS=COMMENTS)
    elif request.method == "GET":
        return render_template('comment.html')



if __name__ == "__main__":
    app.run(debug=True)


    






