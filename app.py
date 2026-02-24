from flask import *
import pymysql
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER']= 'static/images'

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

@app.route("/api/add_product", methods=["POST"])
def addProduct():
    product_name= request.form["product_name"]
    product_description=request.form["product_description"]
    product_category=request.form["product_category"]
    product_cost= request.form["product_cost"]
    product_image= request.files["product_image"]
    print(product_name,product_description,product_category,product_cost,product_image)
    
    image_name=product_image.filename
    print(image_name)


    file_path= os.path.join(app.config['UPLOAD_FOLDER'],image_name)
    print(file_path)
    product_image.save(file_path)


    connection =pymysql.connect(host="localhost",user="root",password="",database="fadhili_sokogarden")
    cursor=connection.cursor(pymysql.cursors.DictCursor)
    sql="insert into product_details(product_name,product_description,product_category,product_cost,product_image) values (%s,%s,%s,%s,%s)"
    print(sql)

    data=(product_name,product_description,product_category,product_cost,image_name)
    print(data)

    cursor.execute(sql,data)

    connection.commit()

    return jsonify({"message":"product added successfully"})

@app.route("/api/get_product", methods=["POST"])
def addProduct():
    connection =pymysql.connect(host="localhost",user="root",password="",database="fadhili_sokogarden")
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    sql= "select * from product_details"
    cursor.execute(sql)

    if cursor.rowcount == 0:
        return jsonify({"message": "No products found"})
    else:
        products= cursor.fetchall()
        return jsonify(products)
 
if (__name__)=="__main__":
    app.run(debug=True)