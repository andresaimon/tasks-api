
<h1 align="center">
API de Gerenciamento de Tarefas
</h1>

<p> API RESTful usando o framework Flask que permite o gerenciamento de tarefas. A API conecta-se a um banco de dados MySQL e permite as operações CRUD (Create, Read, Update e Delete) para as tarefas. </p>

## Ferramentas e configurações
- A solução foi desenvolvida através do Sistema Operacional Ubuntu 20.04.5 LTS; 
-  A IDE utilizada foi o VS Code, versão 1.74.2, sendo adicionadas extensões para o Docker e a linguagem de Programação Python; 
-  Foi utilizado o Docker versão 20.10.22 e o Python versão 3.9.16.

- A aplicação foi desenvolvida em um ambiente virtual Python. Para ativar o ambiente virtual:
- ```source venv/bin/activate```
- Para realizar a instalação das dependências utilizadas no projeto no ambiente virtual Python:
- ```pip install -r requirements.txt```
- Para construir uma imagem do MySQL no Docker:
- ```sudo docker build -t tasks-api .```
- Para ativar o container:
- ```sudo docker run -h 127.0.0.1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=RootPassword -e MYSQL_DATABASE=Tasks-API -e MYSQL_USER=MainUser -e MYSQL_PASSWORD=MainPassword tasks-api```


## Requisitos
- As tarefas possuem os seguintes campos: 
- id (inteiro, gerado automaticamente pelo banco de dados) 
- título (string, obrigatório) 
- descrição (string, opcional) 
- data de conclusão (data, opcional)
- data de criação (data, gerada automaticamente pelo banco de dados)

## Endpoints
- Os seguintes endpoints foram implementados:
- GET: Retorna uma lista de todas as tarefas.
- POST: Cria uma nova tarefa.
- GET_ID: Retorna a tarefa com o id especificado.
- PUT: Atualiza a tarefa com o id especificado.
- DELETE: Exclui a tarefa com o id especificado.
- Os endpoints podem ser testados a partir do arquivo Tasks_API.postman.collection.json
