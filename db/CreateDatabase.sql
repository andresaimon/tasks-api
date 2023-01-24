USE Tasks-API;

CREATE TABLE tasks (
    id integer not null auto_increment,
    title varchar(150) not null,
    description_task text,
    date_conclusion date,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO tasks (title, description_task, date_conclusion) VALUES ('Tarefa 1', 'Descrição da Tarefa 1', '2023-01-24');
INSERT INTO tasks (title, description_task, date_conclusion) VALUES ('Tarefa 2', 'Descrição da Tarefa 2', '2023-01-25');
INSERT INTO tasks (title, description_task, date_conclusion) VALUES ('Tarefa 3', 'Descrição da Tarefa 3', '2023-01-26');
INSERT INTO tasks (title, description_task, date_conclusion) VALUES ('Tarefa 4', 'Descrição da Tarefa 4', '2023-01-27');
INSERT INTO tasks (title, description_task, date_conclusion) VALUES ('Tarefa 5', 'Descrição da Tarefa 5', '2023-01-28');
