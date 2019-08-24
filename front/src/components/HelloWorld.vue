<template>
  <div class="hello">
    <h1>Bem vindo a Djanguladora</h1>
    <h2>Calculo de zero da função usando o método da bisseção</h2>
    
    <div class="Funcao">
      <a>
        F(x)= 
      </a>
      <div>
          <input class="inputX" type="text" id="x5" />
          <label class="labelInput" for="X5">X^5</label>
          <label> + </label>
      </div>
      <div>
          <input class="inputX"  type="text" id="x4"/>
          <label class="labelInput" for="X4">X^4</label>
          <label> + </label>
      </div>
      <div>
          <input class="inputX" type="text" id="x3" />
          <label class="labelInput" for="X3">X^3</label>
          <label> + </label>
      </div>
      <div>
          <input class="inputX" type="text" id="x2" />
          <label class="labelInput" for="X2">X^2</label>
          <label> + </label>
      </div>
      <div>
          <input class="inputX" type="text" id="x" />
          <label class="labelInput" for="X">X</label>
          <label> + </label>
      </div>
      <div>
          <input class="inputX" type="text" id="xf" />
      </div>
    </div>

    <div>
      <label class="labelInput" for="X">Criterio de parada = 10^</label>
      <input class="inputParada" type="text" id="criterioParada"/>
    </div>
        
    <h2>Repositorio: </h2>
    <ul>
      <li>
        <a href="https://github.com/MatheusMuriel/Djanguladora">
          GitHub
        </a>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Welcome to Your Vue.js App'
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
  font-size: 40px;
}
.labelX{
  justify-content: center;
  align-items: center;
}
.inputX{
  width: 40px;
  height: 40px;
}
</style>
