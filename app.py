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
    cursor = connection.cursor()
    #connect sql
    sql= "insert into users(username,email,phone,password) values(%s,%s,%s,%s)"
    print(sql)

    
    data=(username,email,phone,password)
    print (data)
    # execute sql query
    cursor.execute(sql,data)
    #save data
    connection.commit()

    return jsonify({"message":"Sign up successful"})


@app.route("/api/signin", methods=["POST"])
def signIn():
    email= request.form["email"]
    password= request.form["password"]
    print(email,password)

    connection =pymysql.connect(host="localhost",user="root",password="",database="fadhili_sokogarden")
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    sql="select user_id, username, email, phone from users where email= %sand password =%s"
    #data to execute the query
    data=(email,password)

    # execute 
    cursor.execute(sql,data)
    # check resulting rows
    if cursor.rowcount == 0:
        return jsonify({"message":"Invalid credentials"})
    else:
        # get user data
        user= cursor.fetchone()
        return jsonify({"message":"log in successful", "user": user })
    return jsonify({"message": "signin api"})

if (__name__)=="__main__":
    app.run(debug=True)