from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskprofesores'
mysql = MySQL(app)



app.secret_key = 'mysecretkey'

@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM profesores')
    data = cur.fetchall()
    return render_template('Index.html', profesor=data)

@app.route('/add_profesor', methods=['GET', 'POST'])
def add_profesor():
    if request.method == 'POST':
       fullname = request.form['fullname'] 
       classroom = request.form['classroom'] 
       materia = request.form['materia']
       cur = mysql.connection.cursor() 
       cur.execute('INSERT INTO profesores (fullname, classroom, materia) VALUES (%s, %s, %s)', 
       (fullname, classroom, materia))
       
       mysql.connection.commit()
       flash('Profesor Added successfully')
       return redirect(url_for('Index'))
    
    @app.route('/edit/<id>')
    def get_profesor(id):
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM profesores WHERE id = %s', (id,))
        data = cur.fetchall()
        return 'recevied'

    return render_template('edit.html, profesor=data')

@app.route('/delete/ <int:id>')
def delete_profesor(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM profesores WHERE id = {0}', format(id,))
    mysql.connection.commit()
    flash('Profesor eliminado correctamente')
    return redirect(url_for('Index'))
    
if __name__ == '__main__':
    app.run(port = 80, debug = True)




