from flask import Flask, render_template, request, redirect, url_for
import pymysql.cursors

app = Flask(__name__)

db = pymysql.connect(host="localhost", user="root", password="root", db="users")

@app.route("/main")
def main():
	return render_template("template.html")

@app.route("/popular_items")
def popular_items():
	return render_template("popular_items.html")

@app.route("/popular_keys")
def popular_keys():
	return render_template("popular_keys.html")

@app.route("/shop")
def shop():
	return render_template("shop.html")

@app.route("/all_keys")
def all_keys():
	return render_template("all_keys.html")

@app.route("/misc_items")
def misc_items():
	return render_template("misc_items.html")

@app.route("/try_your_luck")
def try_your_luck():
	return render_template("try_your_luck.html")

@app.route("/contact")
def contact():
	return render_template("contact.html")

@app.route("/login")
def login():
	return render_template("login.html")

@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/register", methods=['POST', 'GET'])
def register():
	error = None
	if request.method == 'POST':
		usrname = request.form["username"]
		pwd = request.form['password']
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		#maxid = cursor.fetchone()
		# Execute the SQL command
		cursor.execute("""INSERT INTO login (username, password) VALUES (%s, %s)""", (usrname, pwd))
		# Commit your changes in the database
		db.commit()
	return render_template("template.html", error = error)
	db.close()

@app.route("/login2", methods=['POST', 'GET'])
def login2():
	error = None
	if request.method == 'POST':
		usrname = request.form["username"]
		pwd = request.form['password']
		# prepare a cursor object using cursor() method
		cursor = db.cursor()
		#maxid = cursor.fetchone()
		# Execute the SQL command
		sql = ("SELECT username, password FROM login WHERE username = '"+usrname+"'")
		cursor.execute(sql)
		# Commit your changes in the database
		db.commit()
		result = cursor.fetchall()
		for i in result:
			if usrname == str(i[0]):
				if pwd == str(i[1]):
					return render_template("template.html", error = error, username = usrname)
	db.close()

@app.route("/logout")
def logout():
	return render_template("template.html")

if __name__ == '__main__':
	app.debug = True
	app.run(host="0.0.0.0", port=8000)
