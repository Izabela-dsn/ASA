### O que é para fazer: 
Desenvolva um sistema backend com uma camada de mensageria entre os microserviços e o banco de dados. A ideia é que, quando uma requisição HTTP chegue para o backend, o mesmo envie as informações para o broker AMQP. Dessa forma, o backend fará o papel de publisher. Da outra ponta, existe um client do tipo subscriber, que é responsável por pegar a informação e armazenar no banco de dados. 

### Documentação

Seguindo o que está sendo documentado no https://anyzizabela.notion.site/ASA-58abf6b0b9bb4714822b0063be6017a6 de acordo com o que está sendo ensinado na disciplina será feito o desenvolvimento do trabalho.

### O que eu fiz até agora
* Crud com logs
    * PUT, DELETE, POST, GET feitos
    * tenho que padronizar responses e logs
* mensageria
    * iniciado o RabbitMQ pelo Docker (no meu caso o Docker Desktop)
    * foi criado um arquivo para cada POST (foi feito somente o Aluno no momento)
    * o send_aluno.py recebe da chamada HTTP com os dados (payload) e manda para a fila (queue)
    * o receiver_aluno.py consome essa mensagem e transforma os dados para a Classe correta do ORM para aí sim poder ir para o banco de dados

### To-do
* funções para as outras tabelas: Professor, Curso, Aluno em relação ao Curso
* docker (dockerfile, docker-compose)

### Fazendo build com o dockerfile
<code>docker build --tag trab02 -f ./src/Dockerfile .</code>

