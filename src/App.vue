<template>
  <div id="app">
    <div  class="position-absolute fixed-top">
      <b-img src="https://image.flaticon.com/icons/png/512/51/51661.png" alt="Logo" width="50"></b-img>
    </div>

    <b-container class="bv-example-row">
      <b-row align-h="center">
        <b-col cols="4">
          <div class="input-funcao">
            <funcao funcao="$$f(x)=$$"></funcao>
            <input-funcao ref="x5" indice="0" formula_funcao="$$x^5$$" @mudouValor="atualizaValor" v="0"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x4" indice="1" formula_funcao="$$x^4$$" @mudouValor="atualizaValor" v="0"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x3" indice="2" formula_funcao="$$x^3$$" @mudouValor="atualizaValor" v="1"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x2" indice="3" formula_funcao="$$x^2$$" @mudouValor="atualizaValor" v="0"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x1" indice="4" formula_funcao="$$x$$" @mudouValor="atualizaValor" v="-9"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="xf" indice="5" formula_funcao="$$$$" @mudouValor="atualizaValor" v="3"></input-funcao>
          </div>
        </b-col>
      </b-row>

      <b-row>
        <br/>
      </b-row>

      <b-row align-h="around">
        <b-col>
          <input-funcao class="input-epsilon" ref="epsilon" indice="6" formula_funcao="$$\varepsilon$$" @mudouValor="atualizaValor" v="-3"></input-funcao>
        </b-col>
        <b-col><b-button variant="outline-primary" @click="calcular()">Calcular</b-button></b-col>
      </b-row>

      <b-row> <br/> </b-row>

      <b-row align-h="between">
        <b-col cols="6" ref="rowPlot"></b-col>

        <b-col cols="6" ref="rowTabelas"></b-col>
      </b-row>

    </b-container>

    <div class="fixed-bottom rodape">
      Muriel e Manhani -
      <a href="https://github.com/MatheusMuriel/Djanguladora"> Github </a>
    </div>

  </div>
</template>

<script>
import InputFuncao from './components/InputFuncao'
import Funcao from './components/Funcao'
import TabTabelas from './components/TabTabelas'
import Vue from 'vue'
import Plotador from './components/Plotador'

export default {
  name: 'App',
  components: {
    InputFuncao,
    Funcao,
    TabTabelas
  },
  data () {
    return {
      valores: [0, 0, 0, 0, 0, 0, 0],
      codFuncaoCompleta: '$$$$',
      dados_resultado: ''
    }
  },
  methods: {
    calcular () {
      this.plotarGrafico()
      this.axios.post('http://matheusmuriel.pythonanywhere.com/calculo/', this.valores)
        .then((response) => {
          let dados = response.data

          this.processarResposta(dados)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    plotarGrafico () {
      let v = this.valores
      let l = ['x^5 + ', 'x^4 + ', 'x^3 + ', 'x^2 + ', 'x^1 + ', '']
      let newArr = []
      for (let i = 0; i < v.length - 1; i++) {
        newArr.push(v[i])
        newArr.push(l[i])
      }
      let strFuncao = newArr.join('')
      console.log('Funcao para plotar: ', strFuncao)

      let PlotClass = Vue.extend(Plotador)
      let instanciaPlot = new PlotClass({
        propsData: {title: 'Grafico da função', gn: strFuncao, hn: '', grid: true}
      })
      instanciaPlot.$mount()

      let rowPlot = this.$refs.rowPlot

      if (rowPlot.childNodes.length > 0) {
        rowPlot.replaceChild(instanciaPlot.$el, rowPlot.firstChild)
      } else {
        rowPlot.appendChild(instanciaPlot.$el)
      }
    },
    processarResposta (dadosBrutos) {
      // Split $$$
      // Descobre os intervalos
      // Loop pelos intervalos
      // - Gera Tab (Novo componente)
      let intervalos = this.descobrirIntervalos(dadosBrutos)

      let novaTabTabelas = this.criarTabs(intervalos)
      let rowTabs = this.$refs.rowTabelas

      if (rowTabs.childNodes.length > 0) {
        rowTabs.replaceChild(novaTabTabelas.$el, rowTabs.firstChild)
      } else {
        rowTabs.appendChild(novaTabTabelas.$el)
      }
    },
    descobrirIntervalos (dadosBrutos) {
      // Retorna uma lista com os intervalos.
      let intervalosEncontrados = dadosBrutos.split('$$$')
      intervalosEncontrados.shift() // Remove o primeiro elemento pois ele é vazio
      return intervalosEncontrados
    },
    criarTabs (intervalos) {
      let TabTabelasClass = Vue.extend(TabTabelas)
      let instanciaTabTabelas = new TabTabelasClass({
        propsData: {intervalos: intervalos}
      })
      instanciaTabTabelas.$mount()

      return instanciaTabTabelas
    },
    atualizaValor (payload) {
      this.valores[payload.indice] = payload.valor
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
  overflow:auto;
  padding-bottom:150px; /* this needs to be bigger than footer height*/
}
.input-funcao {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  white-space: nowrap;
}
.input-epsilon {
  display:flex;
  flex-direction:row-reverse;
}
.complementos-input {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  white-space: nowrap;
}
.rodape {
  background-color: white;
}
</style>
