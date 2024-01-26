from flask import Flask, render_template

app = Flask(__name__)
app.config['SQL_ALCHEMY_DATABASE_URI'] = 'sqlite:///Book.sqlite3'

class Book(db.Model):
    id = db.column("id", db.integer, primarykey=True)
    title = db.column(db.String())
    author = db.column(db.String())


@app.route('/books')
def book():
    render_template("book.html",)


if __name__ == "__main__":
    app.run(debug=True)
