<template>
<div class="app">
  <div id="app">
    <!--- --->
    <img src="https://vuejs.org/images/logo.png">
  </div>

  <header class="Funcao">
    <a>
      <vue-mathjax :formula="fdex"></vue-mathjax>
    </a>
    <div id="div-x5" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x5" />  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^5+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x4" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x4" />  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^4+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x3" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x3" />  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^3+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x2" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x2" />  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x^2+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-x1" class="Funcao">
      <div>
          <input class="inputX" type="text" id="x1" />  
      </div>
      <div>
        <vue-mathjax class="labelInput" :formula="'$$x+$$'"></vue-mathjax>  
      </div>
    </div>

    <div id="div-xf" class="Funcao">
      <div>
          <input class="inputX" type="text" id="xf" />  
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
            <input class="inputEpsilon" type="number" id="epsilon"/>  
        </div>
      </div>

      <div class="criterioDeParada">
        <div>
          <p>Criterio de parada: {{criterioDeParada}}</p>
        </div>
      </div>
    </div>

    <aside class="botaoCalcular">
      <button class="botaoCalcular" v-on:click="calcular()" >
        Calcular
      </button>
    </aside>
  </div>

  
  <footer>
    <div>
      {{ info }}
    </div>
  </footer>
  

</div>
</template>

<script>
import DjanguladoraAPI from './services/DjanguladoraAPI';
import { VueMathjax } from 'vue-mathjax';
import axios from 'axios'
import VueAxios from 'vue-axios'
import Vue from 'vue'
 
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
      criterioDeParada: 'não implementado'
    }
  },methods: {
    calcular: function(){
        const valorX5 = x5.value
        const valorX4 = x4.value
        const valorX3 = x3.value
        const valorX2 = x2.value
        const valorX1 = x1.value
        const valorXf = xf.value
        const valorEpsilon = epsilon.value

        var arr = [
          valorX5,
          valorX4,
          valorX3,
          valorX2,
          valorX1,
          valorXf,
          valorEpsilon
        ]
        axios.post('http://localhost:8000/calculo/', arr)
            .then(function (response) {
              console.log(response);
            })
            .catch(function (error) {
              console.log(error);
            });

        // DjanguladoraAPI.calculaPost(valorX5, valorX4, valorX3, valorX2, valorX1, valorXf, valorEpsilon)
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