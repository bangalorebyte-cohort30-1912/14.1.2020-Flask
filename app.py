from flask import Flask, render_template, request
# import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine('sqlite:///temp.db', echo=True,
                       connect_args={'check_same_thread': False})
Base = declarative_base()
Session = sessionmaker(bind=engine)

app = Flask(__name__)
 
class Comments(Base):
    __tablename__ = 'Comments'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    comment_text =Column(String(1000))

    def __repr__(self):
        return f"{self.name} has commented {self.comment_text}"


COMMENTS = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/comment',  methods=['GET', 'POST'])
def comment():
    comment_list = session.query(Comments).all()[::-1]
    if request.method == "POST":        
        name = request.form['name']
        comment = request.form['comment']
        obj = Comments(id=len(comment_list)+1, name=name, comment_text=comment)
        session.add(obj)
        session.commit()
        COMMENTS.append((name, comment))        
        return render_template('comment.html', COMMENTS=comment_list)
    elif request.method == "GET":
        return render_template('comment.html', COMMENTS=comment_list)

@app.route('/api/comments')
def commentlist():
    comment_list = session.query(Comments).all()[::-1]
    comments_list = []
    comment_dict = {}
    for comment in comment_list:
        comment_dict['id'] = comment.id
        comment_dict['name'] = comment.name
        comment_dict['comment'] = comment.comment_text
        comments_list.append(comment_dict)
    return json.dumps(comments_list)



if __name__ == "__main__":
    session = Session()
    app.run(debug=True)


    






