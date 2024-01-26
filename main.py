from flask import Flask, render_template

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///Book.sqlite3'


class Book(db.Model):
    id = db.column("id", db.integer, primarykey=True)
    title = db.column(db.String())
    author = db.column(db.String())
    def __int__(self, title, author):
        self.title = title
        self.author = author


@app.route('/book')
def book():
    render_template("index.html", Book=Book.query.all())


if __name__ == "__main__":
    app.run(debug=True)