from flask import Flask,render_template,request
import os
from flaskext.mysql import MySQL
import pymysql
from flask import jsonify

app = Flask(__name__)

mysql = MySQL()

mysql_database_host = 'MYSQL_DATABASE_HOST' in os.environ and os.environ['MYSQL_DATABASE_HOST'] or  'localhost'

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'admin'
app.config['MYSQL_DATABASE_DB'] = 'first'
app.config['MYSQL_DATABASE_HOST'] = 'db'
app.config['MYSQL_DATABASE_PORT']=int('3306')
mysql.init_app(app)


@app.route("/")
def main():
    return render_template("index.html")

@app.route('/checkStatus')
def hello():
    return render_template("checkStatus.html")

@app.route('/save',methods=['GET','POST'])
def save():
    if request.method == "POST":

        id = request.form['id']
        fname = request.form['Fname']
        lname = request.form['Lname']
        status = request.form['status']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)

        cursor.execute("insert into covid values(%s,%s,%s,%s)",(id,fname,lname,status))
        conn.commit()
        cursor.close()
        conn.close()
        return "Data Save Successfully!!!"
    else:
        return render_template("index.html")

@app.route('/check',methods=['GET','POST'])
def check():
    if request.method == 'POST':
        id = request.form['id']
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("select Fname,VacStatus from covid where RegNo = %s",id)

        rows = cursor.fetchall()
        if rows is not None:
            resp = jsonify(rows)
            resp.status_code = 200
            cursor.close()
            conn.close()

            return resp
        else:
            return "Enter Valid Input!!!"
        # res = cursor.fetchone()
        # if res is not None:
        #     name = res[0]
        #     status = res[1]
        #     if status == "Yes" or status == "yes":
        #         return f"{name} Vaccinated"
        #     else:
        #         return f"{name} Not Vaccinated"
        # else:
        #     return "Enter valid id"
    # return render_template("checkStatus.html")

@app.route('/read from database')
def read():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM covid")
    row = cursor.fetchone()
    result = []
    while row is not None:
      row = cursor.fetchone()
      result.append(row)

      return ','.join(str(result)[1:-1])
    #   for column in row:
    #       result.append(column)
     
      
    cursor.close()
    conn.close()
    
    # return ','.join(','.join(map(str, l)) for l in result)
    return ",".join(result)

@app.route('/all users')
def users():
    conn = mysql.connect()

    cursor = conn.cursor(pymysql.cursors.DictCursor)

    cursor.execute("SELECT * FROM covid")

    rows = cursor.fetchall()

    resp = jsonify(rows)
    resp.status_code = 200
    cursor.close()
    conn.close()

    return resp

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')