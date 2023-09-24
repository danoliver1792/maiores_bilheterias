<h1>Maiores bilheterias do cinema</h1>
<p>Coletando os dados dos 50 filmes com maiores bilheterias da história do cinema que estão no site do <a href="https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria">Wikipedia</a>
. O trabalho foi dividido nas etapas abaixo: </p>

<h3>Primeira Etapa - Extração dos dados no Wikipedia</h3>
<p>Usando o Python para extrair a lista com os filmes de maior bilheteria mundial. Os dados são retirados do site https://pt.wikipedia.org/wiki/Lista_de_filmes_de_maior_bilheteria e seus valores são representados em dólares. Um filme pode gerar renda por meio de várias fontes, como nas exibições públicas nos cinemas, nas vendas de mídia para o público ou dos direitos de exibição na televisão, assim como por meio de publicidade. 
Para extrair os dados, usamos a biblioteca requests e BeautifulSoup, passando a URL, verificando se há resposta com o servidor e percorrendo a tabela coletando as informações</p>

<img src="https://github.com/danoliver1792/maiores_bilheterias/assets/99451711/3fa90675-f1a5-4cf3-a5e7-83168611c2c9">

<h3>Segunda Etapa - Criação e inserção no MySQL</h3>
<p>Usamos a biblioteca mysql-connector-python, assim estabelecemos uma conexão com o banco de dados MySQL usando o host,
  usuário, senha e nome do banco. Após a conexão com o banco, inserimos os dados na tabela 'filmes' que contém as colunas 'título' e 'bilheteria'</p>

<img src="https://github.com/danoliver1792/maiores_bilheterias/assets/99451711/bc87c00e-c314-4da3-96e6-2511425fd57e">

<p>Eu tive o erro "Error: 1265 (01000): Data truncated for column 'bilheteria' at row 1" no terminal, então alterei o tipo de dato na coluna 'bilheteria' da tabela 'filmes' para receber um decimal maior. 
  Também mudei o código para trocar o espaço em branco que separa os números por nada, isso para agregar todos os algarimos. Dessa forma, os dados foram inseridos com sucesso</p>

<img src="https://github.com/danoliver1792/maiores_bilheterias/assets/99451711/a79fa9fa-612d-45bf-b27b-da0448af4297">
