import mysql.connector
from flask import Flask, make_response, jsonify, request

# configurações de conexão com o banco de dados:
mydb = mysql.connector.connect(
    host='localhost',
    user='MainUser',
    password='MainPassword',
    database='Tasks-API',
)

# instanciando o Flask:
app = Flask(__name__)

# por default, os dados são organizados em ordem alfabética
# para que isso não ocorra, define-se o status como False
app.config['JSON_SORT_KEYS'] = False


# Para retornar uma lista com todas as tarefas:
@app.route('/tasks', methods=['GET'])
def get_tasks():
    try:
        # instanciando um cursor:
        my_cursor = mydb.cursor()
        my_cursor.execute('SELECT * FROM tasks')

        # retornando a lista de dados capturada pelo cursor:
        my_tasks = my_cursor.fetchall()

        tasks = list()
        for task in my_tasks:
            tasks.append(
                {
                    'id': task[0],
                    'title': task[1],
                    'description_task': task[2],
                    'date_conclusion': task[3],
                    'created_at': task[4]
                }
            )

        return make_response(
            jsonify(
                message='Lista de Tarefas',
                tasks_list=tasks
                )
        )
    except Exception as e:
        return make_response(jsonify(message=str(e)), 500)


# Para retornar a tarefa com o id especificado:
@app.route('/tasks/<int:id>', methods=['GET'])
def get_task(id):
    my_cursor = mydb.cursor()
    my_cursor.execute(f"SELECT * FROM tasks WHERE id={id}")
   
   # retorna apenas a tarefa especificada pelo id:
    task = my_cursor.fetchone()
    if task:
        task_dict = {
            'id': task[0],
            'title': task[1],
            'description_task': task[2],
            'date_conclusion': task[3],
            'created_at': task[4]
        }
        return make_response(
            jsonify(
                message='Tarefa encontrada',
                task=task_dict
            )
        )
    else:
        return make_response(jsonify(message='Tarefa não encontrada'), 404)


# Para criar uma nova tarefa:
@app.route('/tasks', methods=['POST'])
def create_task():
    task = request.json
    
    # verificando se o atributo 'title' foi preenchido:
    if not task or not 'title' in task:
        return make_response(jsonify(message='Dados incompletos: Título é obrigatório'), 400)
    try:
        my_cursor = mydb.cursor()
        
        #preenchimento "automático" dos campos 'description_task' e 'date_conclusion', caso não sejam informados pelo usuário
        sql = f"INSERT INTO tasks (title, description_task, date_conclusion) VALUES ('{task['title']}', '{task.get('description_task', '')}', '{task.get('date_conclusion', None)}')"
        my_cursor.execute(sql)
       
        #registrando a tarefa no banco de dados:
        mydb.commit()

        return make_response(
            jsonify(
                message='Tarefa criada!',
                task=task
            )
        )
    except Exception as e:
        return make_response(jsonify(message=str(e)), 500)


# Para atualizar uma tarefa com o id especificado:
@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = request.json
    try:
        my_cursor = mydb.cursor()
        my_cursor.execute(f"SELECT * FROM tasks WHERE id={id}")
        existing_task = my_cursor.fetchone()
       
        # verificando se a tarefa existe no banco de dados, antes de atualizá-la:
        # caso exista, conclui-se a atualização
        if existing_task:
            title = task.get('title', existing_task[1])
            description_task = task.get('description_task', existing_task[2])
            date_conclusion = task.get('date_conclusion', existing_task[3])
            sql = f"UPDATE tasks SET title='{title}', description_task='{description_task}', date_conclusion='{date_conclusion}' WHERE id={id}"
            my_cursor.execute(sql)
            mydb.commit()
            return make_response(jsonify(message='Tarefa atualizada!'), 200)
        else:
            return make_response(jsonify(message='Tarefa não encontrada'), 404)
    except Exception as e:
        return make_response(jsonify(message=str(e)), 500)


# Para excluir a tarefa com o id especificado:
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    try:
        my_cursor = mydb.cursor()
        my_cursor.execute(f"SELECT * FROM tasks WHERE id={id}")
        existing_task = my_cursor.fetchone()
        
        #verificando se a tarefa existe no banco de dados:
        if existing_task:
            my_cursor.execute(f"DELETE FROM tasks WHERE id={id}")
            mydb.commit()
            return make_response(jsonify(message='Tarefa deletada!'), 200)
        else:
            return make_response(jsonify(message='Tarefa não encontrada'), 404)
    except Exception as e:
        return make_response(jsonify(message=str(e)), 500)

app.run()