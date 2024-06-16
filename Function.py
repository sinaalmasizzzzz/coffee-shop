def edith(Object,order):
    import sqlite3
    c=sqlite3.Connection("Product.db")
    db=c.cursor()
    SQL=f"UPDATE product SET Number = {Object} WHERE code = '{order}';"
    db.execute(SQL)
    c.commit()
    c.close()
def read(iF,feld,name):
    import sqlite3
    c=sqlite3.Connection("Product.db")
    db=c.cursor()
    SQL=f"SELECT {feld} FROM product WHERE {iF}='{name}';"
    x=db.execute(SQL)
    x=list(x)
    x=x[0][0]
    c.close
    return x
def List():
    import sqlite3
    c=sqlite3.Connection("Product.db")
    db=c.cursor()
    SQL="SELECT * FROM product"
    x=db.execute(SQL)
    x=list(x)
    c.close
    z="Menu:"
    for i in range(len(x)):
        z=f"{z}\nproduct_name = {x[i][0]} ∣ Price = {x[i][1]} ∣ Number = {x[i][2]} ∣ Code = {x[i][3]}\n\n"
    return z