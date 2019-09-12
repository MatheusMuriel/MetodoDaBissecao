<h1 align="center">
  <br>
  <img src="https://image.flaticon.com/icons/png/512/51/51661.png" alt="Logo" width="200">
  <br>
  Djanguladora
  <br>
</h1>

<h4 align="center">Calculadora de zero de função feita com <a href="https://www.djangoproject.com/" target="_blank">Django</a> e <a href="https://vuejs.org/" target="_blank">Vue.js</a>.</h4>


<h5 align="center">Acesse: <a href="http://matheusmuriel.pythonanywhere.com">MatheusMuriel.pythonanywhere.com</a></h5>

## Índice
- [Contexto](#contexto)
- [Estrutura do sistema](#estrutura-do-sistema)
- [Como testar](#como-testar)
- [Utilização](#utilização)
- [Créditos](#créditos)
- [Bibliotecas](#bibliotecas)
- [Licença](#licença)

## Screenshot
![screenshot](https://imgur.com/mdLTVgH.jpg)

## Contexto

Trabalho da matéria de Calculo Numérico do curso de Ciência da Computação - UniFil
Professora: Tania Camila Kochmanscky Goulart

Calculo feito utilizando o método da [Bisseção](https://pt.wikipedia.org/wiki/M%C3%A9todo_da_bisse%C3%A7%C3%A3o).

## Como testar

Para executar localmente a aplicação você vai precisar ter [Git](https://git-scm.com), [Python](https://www.python.org/) e [npm](http://npmjs.com) instalados em seu computador.

No seu terminal digite:
```bash
# Clone o repositorio
$ git clone https://github.com/MatheusMuriel/Djanguladora.git

# Va para o diretorio da aplicação
$ cd Djanguladora

# Va para o diretorio dos arquivos de frontend
$ cd frontend

# Instale as dependencias do frontend
$ npm install

# Construa o frontend
$ npm run build

# Instale as dependencias do backend
$ cd ..
$ pip install -r requeriments.txt

# Inicie o servidor do Django
$ python manage.py collectstatic
$ python manage.py runserver

# Acesse http://localhost:8000
```

## Estrutura do sistema

Backend:  [Django Framework](https://www.djangoproject.com/)
Frontend: [Vue.js](https://vuejs.org/) + [webpack](https://webpack.js.org/)

Requisição [REST](https://pt.wikipedia.org/wiki/REST)

![flow](https://imgur.com/1l1BDjB.jpg)

## Utilização

Basta inserir os valores em seus determinados campos (Caso o valor não se aplique deixar como zero). E adicionar no campo "Epsilon" uma precisão para o calculo.

## Bibliotecas

- [Vue](https://vuejs.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [MathJax](https://www.mathjax.org/)
- [Bootstrap](https://getbootstrap.com/)
- [Function Plot](https://mauriciopoppe.github.io/function-plot/)
- [Axios](https://github.com/axios/axios)
- [Vue Input Autowidth](https://github.com/syropian/vue-input-autowidth)


## Licença
[GNU General Public License v3.0](LICENSE)

 [Matheus Muriel](https://github.com/MatheusMuriel/) e [Guilherme Manhani](https://github.com/guilhermemanhani)
