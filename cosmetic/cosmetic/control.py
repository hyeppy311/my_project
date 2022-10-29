from db_model.mysql import conn_cosdb

def find(name_id) : 
    mysql_db = conn_cosdb()
    db_cursor = mysql_db.cursor()

    sql = "SELECT name FROM cosmetic WHERE name_id = %d" % (name_id)
    db_cursor.execute(sql)
    result = db_cursor.fetchall()
    print(result)