from flask import Flask, render_template, request ,jsonify
import pymysql

app = Flask(__name__)

## DB 연결설정
cos_db = pymysql.connect(
        host='localhost', 
        port=3306, 
        user='****', 
        passwd='r*******', 
        db='cosmetics', 
        charset='utf8')
cursor = cos_db.cursor()

# @app.route('/', methods=["GET","POST"])
# def main():
    
#     return render_template("main.html")

@app.route('/search', methods=["GET","POST"])
def search():
   
    return render_template('main.html') 
    # cos_name    = request.json
    # print(cos_name)
    # return jsonify(cos_name)


@app.route('/result', methods=["GET","POST"])
def result():
    # URI 파라미터 변수를 넣어주면 해당 파라미터의 값을 가져옴
    search_name = request.args.get('cos_name') 
    
    # DB에서 검색어 조회
    sql = "select name,ingredients from cos where name = '%s' " % (search_name) 
    cursor.execute(sql)
    # 가져온 데이터 저장
    result = cursor.fetchall() # fetchall 모든 데이터를 가져옴 
    result_name = result[0][0] # 검색 결과 이름 저장
    result_igd = result[0][1]  # 검색 결과 성분 저장
    
    return render_template("result.html",cos_name = search_name, 
                                        name=result_name, 
                                        ingredients= result_igd)   # html 파일 templates 폴더안에 꼭 넣어주기

if __name__ == "__main__" :
    app.run(debug=True)
