from flask import *
import pymysql
app = Flask(__name__)

@app.route("/api/signup", methods= ["POST"])
def signUp():
    username = request.form['username']
    email = request.form['email']
    phone = request.form['phone']
    password = request.form['password']

    print(username, email, phone, password)
    # create connection to db

    connection =pymysql.connect(host="localhost", user="root", password="",database="fadhili_sokogarden",)
    
    # create cursor 
    cursor=connection.cursor()
    #
    sql= "insert into users(username,email,phone,password) values(%s,%s,%s,%s)"
    print(sql)

    #
    data=(username,email,phone,password)
    print (data)
    # execute sql query
    cursor.execute(sql,data)
    #save data
    connection.commit()

    return jsonify({"message":"Sign up successful"})




if (__name__)=="__main__":
    app.run(debug=True)