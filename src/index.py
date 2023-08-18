from flask import Flask, jsonify, request, Response
import pymysql

app = Flask(__name__)

def db_conn():
    conn = None
    try:
        conn = pymysql.connect(
            host="database-1.culm8jzv5xie.ap-south-1.rds.amazonaws.com",
            port=3306,
            database="mydb",
            user="admin",
            password="MySqlAws2023",
            charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.Error as e:
        print(str(e))
    return conn

@app.route('/players',methods=['GET','POST'])
def players():
    conn = db_conn()
    if request.method == 'GET':
        cursor = conn.cursor()
        sql_query = "select * from WPL_PLAYERS_2023"
        cursor.execute(sql_query)
        return jsonify(cursor.fetchall())

    if request.method == 'POST':
        try:
            cursor = conn.cursor()
            payload = request.json
            sql_query = """INSERT INTO WPL_PLAYERS_2023 (EmployeeID, EmployeeName, MailID, PhoneNum, Role, RoleLevel, BattingHand, BowlingHand, TeamName, InsertDate, ModifiedDate) VALUES (%s, %s, %s, %s, %s, %s, '', '', '', '2023-08-18', '2023-08-18')"""
            cursor.execute(sql_query,(int(payload['EmployeeID']),payload['EmployeeName'],payload['MailID'],int(payload['PhoneNum']),payload['Role'],payload['RoleLevel']))
            conn.commit()
            return jsonify({"msg":"data inserted successfully"}), 500
        except Exception as e:
            return jsonify({'error':str(e)}), 201

@app.route('/',methods=['GET'])
def home():
    return "Hello World"


if __name__=="__main__":
    app.run(debug=True)