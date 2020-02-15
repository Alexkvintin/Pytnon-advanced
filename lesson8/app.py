from flask import Flask, render_template, request, redirect, url_for
import sqlite3


class DBContextManager:

    def __init__(self, db):
        self._db = db

    def __enter__(self):
        self._conn = sqlite3.connect(self._db)
        self._cursor = self._conn.cursor()
        return self._cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._conn.commit()
        self._conn.close()


app = Flask(__name__)
db = "shop.db"


@app.route("/")
def home():
    with DBContextManager(db) as db_obj:
        request = db_obj.execute("select category_name, id from categories")
        result = request.fetchall()
    categories_dict = {key: value for (key, value) in result}
    return render_template("index.html", categories_dict=categories_dict)


@app.route("/products/<category>/<id>/")
def products_by_id(id, category):
    with DBContextManager(db) as db_obj:
        sql = "select name, id from products where category = ? and  (quantity_on_sale or quantity_in_stock) > 0"
        request = db_obj.execute(sql, [id])
        result = request.fetchall()
    products = {key: value for (key, value) in result}
    return render_template("products.html", category=category, products=products)


@app.route("/item/<id>")
def item_detail(id):
    with DBContextManager(db) as db_obj:
        sql = "select * from products where id = ?"
        request = db_obj.execute(sql, [id])
        item = request.fetchall()[0]
    specification = item[6].replace('\n', '<br>')
    return render_template("item.html", item=item, specification=specification)


@app.route("/admin")
def admin_home():
    with DBContextManager(db) as db_obj:
        request = db_obj.execute("select category_name, id from categories")
        result = request.fetchall()
    categories_dict = {key: value for (key, value) in result}
    return render_template("admin.html", categories_dict=categories_dict)


@app.route("/add_category", methods = ['POST'])
def add_category():
    category_name = request.form.get('category_name')
    with DBContextManager(db) as db_obj:
        sql = "insert into categories ('category_name') values (?)"
        db_obj.execute(sql, [category_name])
    return redirect(url_for('admin_home'))


@app.route("/add_item", methods = ['POST'])
def add_item():
    item_name, category, price, quantity_on_sale, quantity_in_stock, characteristics = (
        request.form[s] for s in ("item_name", "category", "price", "quantity_on_sale", "quantity_in_stock", "characteristics")
    )

    with DBContextManager(db) as db_obj:
        sql = "insert into products ('name', 'category', 'price', 'quantity_on_sale', 'quantity_in_stock', specifications) values (?, ?, ?, ?, ?, ?)"
        db_obj.execute(sql, [item_name, category, price, quantity_on_sale, quantity_in_stock, characteristics])
    return redirect(url_for('admin_home'))


if __name__ == "__main__":
    app.run(debug=True)
