import sqlite3
from bottle import route, run, debug, template

@route('/todo')
@route('/todo-new-page')
def todo_list():
    conn = sqlite3.connect('todo.db')
    c = conn.cursor()
    c.execute("SELECT id, task FROM todo WHERE status LIKE '1'")
    result = c.fetchall()
    c.close()
    return template('make_table', rows=result)
debug(True)
run(reloader=True)