# API de Cadastro de Cadastro de Pacientes para Predição de Parada Cardíaca 

Este pequeno projeto faz parte da Disciplina **Engenharia de Sistemas de Software Inteligentes** da Pós-Graduação Engenharia de Software PUC-Rio

A idéia desse projeto é apresentar a Predição de Parada Cardíaca. 

Esta API foi desenvolvida em Swagger e seu back-end em Python e Flask. Para o banco de dados, foi utilizado o SQLite.

O front-end foi desenvolvido em uma SPA (Single Page Application) utilizando [Bootstrap](https://getbootstrap.com/) para tornar responsivo e a biblioteca [jQuery](https://jquery.com/) para interação JavaScript. Foi utilizado também o plug-in de jQuery [DataTables](https://datatables.net/), para exibição dos dados em uma grid.  


---
# Como executar 
Após clonar o repositório, é necessário ir ao diretório raiz, pelo terminal, para poder executar os comandos descritos abaixo.

É fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html).

Para criar o ambiente:
```
py -m venv env
```
Para ativar o ambiente:
```
.\env\Scripts\activate
```
Será necessário ter todas as libs python listadas no arquivo `requirements.txt` instaladas.
Para instalar as libs:
```
(env)pip install -r requirements.txt
```
Pode acontecer no momento de executar a API, a falta de alguma lib no projeto. Basta executar o comando abaixo para instalar alguma lib que esteja faltando:
```
(env)pip install <nome_da_lib>
```
Para executar a API  basta executar:

```
(env)flask run --host 0.0.0.0 --port 5000
```
Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)flask run --host 0.0.0.0 --port 5000 --reload
```

Abra o [http://localhost:5000/#/](http://localhost:5000/#/) no navegador para verificar o status da API em execução.

> Todos os comandos acima foram executados no sistema operacional Windows. Em Linux, alguns desses comandos tem sintaxe diferente.

---
## Como executar o Front-end

Basta fazer o download do projeto e abrir o arquivo index.html no seu browser.



