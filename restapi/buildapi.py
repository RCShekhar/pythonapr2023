from flask import Flask, jsonify, request
import sqlite3 as sql
from sqlite3 import Error

def connect_db(path):
    try:
        return sql.connect(path, check_same_thread=False)
    except Error:
        print("Unable to connect")


connection = connect_db('db.sqlite')
cur = connection.cursor()
cur.execute("create table if not exists student (id int primary key, name varchar(50), score float)")

app = Flask('Studentapp')

@app.get('/')
def home():
    return '<h1> Welcome</h1>'

@app.get('/student')
def getstudents():
    header = ('std_id', 'std_name', 'score')
    response = []
    try:
        records = cur.execute("select id,name,score from student")
        for record in records:
            res_data = dict(zip(header,record))
            response.append(res_data)
    except Error as e:
        return jsonify({'status':str(e)})
    
    return jsonify(response)
    


@app.get('/student/<int:std_id>')
def get_a_student(std_id):
    header = ('std_id', 'std_name', 'score')
    response = []
    query = f"select id, name, score from student where id = {std_id}"

    try:
        rs = cur.execute(query)
        for rec in rs:
            res_data = dict(zip(header,rec))
            response.append(res_data)
        return jsonify(response)
    except Error as e:
        return jsonify({'status': str(e)})
    

@app.post('/student')
def insert_student():
    query = "insert into student(id, name, score) values({std_id}, '{std_name}', {score})"

    try:
        cur.execute(query.format(**request.get_json()))
        connection.commit()
    except Error as e:
        return jsonify({'status': str(e)})
    
    return jsonify({'status':'Record loaded successfully'})

@app.put('/student/<int:std_id>')
def update_student(std_id):
    req = request.get_json()
    updates = []

    for key, value in req.items():
        if key == 'std_id':
            new_key = "id="
        elif key == 'std_name':
            new_key ="name ="
        else:
            new_key =key+'='

        updates.append(new_key + str(value) if str(value).isnumeric() else "'"+str(value)+"'")

    query = f"update student set {','.join(updates)} where id={std_id}"
    print(query)
    try:
        cur.execute(query)
        connection.commit()
        return jsonify({'status':'Record updated successfully'})
    except Error as e:
        return jsonify({'staus': str(e)})

    # update set id = 1, name='name', score=99.3
    # where id=2

app.run(port=8080, debug=True)
