import pymysql


cos_db = pymysql.connect(
        host='localhost', 
        port=3306, 
        user='root', 
        passwd='root4321', 
        db='cosmetics', 
        charset='utf8')

# cursor = cos_db.cursor()

    
# sql = "select name,ingredients from cos where name = '%s' " % (name) 
# cursor.execute(sql)
# result = cos_db.fetchall()
# name = result[0][0]
# igd = result[0][1]



# def conn_cosdb() :
#     if not cos_db.open():
#         cos_db.ping(reconnect=True)
#     return cos_db











# db = {
#     'user' : 'root',
#     'password' : 'root4321',
#     'host' : 'localhost',
#     'port' : 3306,
#     'database' : 'cosmetics'
# }

# DB_URL = f"mysql+mysqlconnector://{db:['user']}:{db:['password']}@{db:['host']}:{db['port']}/{db['database']}?charser=utf8"


