<template>
<div class="app">
  <div id="app">
    <!--- 
    <img src="https://vuejs.org/images/logo.png">
    --->
  </div>

  <div id="funcaoPrincipal" class="Funcao">
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

  </div>

  <div id="dadosAdicionais">
    <div id="epsilon" >

    </div>

    <div id="criterioDeParada">

    </div>

  </div>

</div>
</template>

<script>
import { VueMathjax } from 'vue-mathjax'
export default {
  components: {
    'vue-mathjax': VueMathjax
  },
  name: 'App',
  data () {
    return {
      fdex: '$$f(x)=$$',
    }
  }
}
</script>

<style scoped>
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
a {
  color: #42b983;
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
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>