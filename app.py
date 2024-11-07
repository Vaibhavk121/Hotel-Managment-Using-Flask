from flask import Flask, render_template, request, redirect
from flask_mysqldb import MySQL
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

mysql = MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/reserve', methods=['POST'])
def reserve():
    guest_name = request.form['guest_name']
    room_number = request.form['room_number']
    check_in = request.form['check_in']
    check_out = request.form['check_out']

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO reservations (guest_name, room_number, check_in, check_out) VALUES (%s, %s, %s, %s)",
                (guest_name, room_number, check_in, check_out))
    mysql.connection.commit()
    cur.close()

    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
