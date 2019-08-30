<template>
<div class="app">
  <div id="app">
    <!--- --->
    <img src="https://cdn1.iconfinder.com/data/icons/dotted-charts/512/hyperbole_plot-2-512.png">
  </div>

  <header class="Funcao">
    <a>
      <vue-mathjax :formula="fdex"></vue-mathjax>
    </a>
    <div id="div-x5" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x5" value="0"/>
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^5+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x4" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x4" value="0"/>  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^4+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x3" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x3" value="1"/>  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^3+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x2" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x2" value="0"/>  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^2+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x1" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x1" value="-9"/>  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-xf" class="Funcao">
      <div>
          <input class="inputX" type="text" id="xf" value="3"/>  
      </div>
    </div>

  </header>

  <div class="secaoDeElementos">
    <div class="dadosAdicionais">
      <div class="epsilon">
        <div class="labelEpsilon">
          <vue-mathjax class="labelEpsilon" :formula="epsilon"></vue-mathjax>:
        </div>
        <div>
          <!-- Adicionar Limitações de valores -->
            <input class="inputEpsilon" type="number" id="epsilon" value="-3"/>  
        </div>
      </div>

    </div>

    <aside class="botaoCalcular">
      <button class="botaoCalcular" v-on:click="calcular()" >
        Calcular
      </button>
    </aside>
  </div>

  <component v-bind:is="currentTabComponent"></component>

   <table id="tabelaIteracoes" ref="tabelaIteracoes" class="tabelaResultado" align="center">
        <thead>
            <tr>
                <th>Iteração</th>
                <th><vue-mathjax :formula="'$$x$$'"></vue-mathjax></th>
                <th><vue-mathjax :formula="'$$f(x)$$'"></vue-mathjax></th>
                <th><vue-mathjax :formula="'$$b-a$$'"></vue-mathjax></th>
            </tr>
        </thead>
    </table>

  <footer>
    <div>
      {{ info }}
    </div>
  </footer>
  

</div>
</template>

<script>
import Vue from 'vue'
import axios from 'axios'
import VueAxios from 'vue-axios'
import { VueMathjax } from 'vue-mathjax'
import BootstrapVue from 'bootstrap-vue'
 
Vue.use(VueAxios, axios)
export default {
  components: {
    'vue-mathjax': VueMathjax
  },
  name: 'App',
  data () {
    return {
      fdex: '$$f(x)=$$',
      epsilon: '$$\\varepsilon$$',
      info: 'Em desenvolvimento',
      x1: 0,
    }
  },methods: {
    calcular: function(){
      var arrValores = [x5.value, x4.value, x3.value, x2.value, x1.value, xf.value, epsilon.value]

      console.log(this)

      axios.post('http://localhost:8000/calculo/', arrValores)
          .then((response) => {
            var dados = response.data

            var intervalos = dados.split("$$$")
            console.log("Intervalos: ", intervalos)

            var tabela = (this.$refs.tabelaIteracoes);
            var colunas = 4

            // Começando em 1 por causa dos caracteres especiais de inicio da respostas
            for (let i = 1; i < intervalos.length; i++){

              let interacoes = intervalos[i].split("#")
              console.log("Interações: ", interacoes)

              let valores_intervalo = interacoes[0].split("::")
              console.log("Valores do intervalo: " + valores_intervalo)

              // Começa em 1 porq o primeiro indice contem os valores do intervalo
              for (let j = 1; j < interacoes.length; j++){
                
                let str_da_vez = interacoes[j]
                console.log("Iteracao da vez: " + str_da_vez)
                
                let num_iteracao = str_da_vez.substring(0,str_da_vez.indexOf("["))
                console.log("Numero da iteração: " + num_iteracao)
                
                let valores_lista = str_da_vez.substring(str_da_vez.indexOf("[")+1,str_da_vez.indexOf("]")).split(";")
                console.log("Lista de valores: " + valores_lista)
                
                let valor_x = valores_lista[0]
                let valor_fdex = valores_lista[1]
                let valor_b_a = valores_lista[2]
                
                let arrDados = [num_iteracao, valor_x, valor_fdex, valor_b_a]

                let novaLinha = tabela.insertRow();
                for(let k = 0; k < colunas; k++){
                  let novaCelula = novaLinha.insertCell();
                  novaCelula.innerHTML = "<tr><td>" + arrDados[k] + "</td></tr>";
                }

              }
            }
          })
          .catch(function (error) {
            console.log(error);
          });
      // FIM DO METODO CALCULA
    },
    processaTabela: function(arrDados){
      console.log(this.$refs.tabelaIteracoes)

      var tabela = (this.$refs.tabelaIteracoes);
      var novaLinha = tabela.insertRow();

      var colunas = 4

      for(let i = 0; i < colunas; i++){
        var novaCelula = novaLinha.insertCell();
        novaCelula.innerHTML = "<tr><td>" + arrDados[i] + "</td></tr>";
      }
    }
  }
}
</script>

<style scoped>
.app{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  line-height: 60px;
}
img {
  width: 80px;
}
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
.Funcao{
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  white-space: nowrap;
}
.labelX{
  justify-content: center;
  align-items: center;
}
.inputX{
  width: 20px;
  height: 20px;
}
.secaoDeElementos{
  display: table;
  align-items: center;
  width: 30%;
}
.secaoDeElementos .dadosAdicionais{
  justify-content: left;
  align-items: center;
  white-space: pre;
  line-height: 1px;
  float: left;
  width: 50%;
}

.secaoDeElementos .dadosAdicionais .epsilon{
  display: flex;
  align-items: center;
  font-size: 40px;
  white-space: nowrap;
}

.secaoDeElementos .dadosAdicionais .epsilon .labelEpsilon{
  display:flex;
  justify-content:flex-end;
  align-items:center;
  font-size:40px;
}

.secaoDeElementos .dadosAdicionais .epsilon .inputEpsilon{
  width: 40px;
  height: 30px;
}
.secaoDeElementos .dadosAdicionais .criterioDeParada{
  width: 10%;
  font-size: 15px;
  color:darkgray;
}
.secaoDeElementos .botaoCalcular{
  margin-left: 50%;
  align-items: right;
}
table, td, th {
  border: 1px solid black;
}

footer{
  bottom: 0;
  height: 40px;
  position: fixed;
  width: 100%;
  display:flex;
  justify-content:center;
  align-items:flex-end;
  width:100%;
}
</style>