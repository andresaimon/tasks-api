# Utilizando a imagem do MySQL versão 5.7
FROM mysql:5.7

# Adicionando os scripts SQL para serem executados na criação do banco
COPY ./db/ /docker-entrypoint-initdb.d/