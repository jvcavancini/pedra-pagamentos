# pedra-pagamentos
 desafio stone

para rodar a api você deve ter o docker instalado e seguir os seguintes comandos após estar no diretorio pedra-pagamentos:
cd pedra-api
.\venv\Scripts\activate
docker compose up -d db
docker compose up --build pythonapp

Assim, vai ser criado a base de dados no Postgres e carregado o arquivo desafio_joao_virgilio.csv para a base de dados
Devido ao grande volume dos dados, este processo pode demorar cerca de 5 minutos

após isso, terá acesso a REST API desenvolvida na porta 80

Para uso da api, os seguintes endpoints foram criados:

/atendimentos (GET,POST)
- GET: Caso use o método GET, retornará todos os atendimentos existentes no banco de dados
- POST: O método POST, você enviará um JSON que será inserido no banco de dados

/atendimentos/:id_atendimento (GET, DEL, PUT)
- GET: este método retornará o atendimento especificado pela variavel id_atendimento
- DEL: este método deletará o atendimento especificado pela variavel id_atendimento
- PUT: este método atualizará o atendimento especificado pela variavel id_atendimento com o json inserido no corpo

/atendimentos/cliente/:id_cliente (GET)
- GET: este método retornará todos os atendimentos realizados para o cliente especificado na variável id_cliente

/atendimentos/cliente/:angel (GET)
- GET: este método retornará todos os atendimentos realizados pelo angel cujo nome possua a substring referente à variável

/atendimentos/cliente/:uf (GET)
- GET: este método retornará todos os atendimentos realizados em uma determinada uf
