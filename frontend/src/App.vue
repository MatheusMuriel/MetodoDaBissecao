<template>
  <div id="app">

    <div ref="funcao-completa">
      <funcao :funcao="codFuncaoCompleta"></funcao>
    </div>

    <b-container class="bv-example-row">
      <b-row align-h="center">
        <b-col cols="4">
          <div class="input-funcao">
            <funcao funcao="$$f(x)=$$"></funcao>
            <input-funcao ref="x5" formula_funcao="$$x^5$$" v-model="x5v" v-bind:valor="x5v"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x4" formula_funcao="$$x^4$$" v-model="x4v" v-bind:valor="x4v"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x3" formula_funcao="$$x^3$$" v-model="x3v" v-bind:valor="x3v"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x2" formula_funcao="$$x^2$$" v-model="x2v" v-bind:valor="x2v"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="x1" formula_funcao="$$x$$" v-model="x1v" v-bind:valor="x1v"></input-funcao>
            <funcao funcao="$$+$$"></funcao>
            <input-funcao ref="xf" formula_funcao="$$$$" v-model="xfv" v-bind:valor="xfv"></input-funcao>
          </div>
        </b-col>
      </b-row>

      <!--
      <b-row align-h="center">
        <p>Função completa: </p>
        <funcao funcao="'$$' + {{x1v}} + '$$'"></funcao>
      </b-row>
      -->

      <b-row>
        <br/>
      </b-row>

      <b-row align-h="around">
        <b-col>
          <input-funcao class="input-epsilon" ref="epsilon" formula_funcao="$$\varepsilon$$" v-model="epsilonV" v-bind:valor="epsilonV"></input-funcao>
        </b-col>
        <b-col><b-button variant="outline-primary" @click="calcular()">Calcular</b-button></b-col>
      </b-row>

      <b-row> <br/> </b-row>

      <b-row align-h="between">
        <b-col cols="6" ref="rowPlot"></b-col>

        <b-col cols="6" ref="rowTabelas"></b-col>
      </b-row>

      <!--
      <b-row ref="rowTabelas" align-h="center">

      </b-row>
      -->

    </b-container>

    <footer class="footer">
      <div>
        {{ info }}
        <a href="https://github.com/MatheusMuriel/Djanguladora">GitHub</a>
      </div>
    </footer>

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
      x5v: '0',
      x4v: '0',
      x3v: '1',
      x2v: '0',
      x1v: '-9',
      xfv: '3',
      epsilonV: '-3',
      codFuncaoCompleta: '$$$$',
      dados_resultado: ''
    }
  },
  methods: {
    calcular () {
      this.plotarGrafico()
      var arrValores = [this.x5v, this.x4v, this.x3v, this.x2v, this.x1v, this.xfv, this.epsilonV]
      this.axios.post('http://localhost:8000/calculo/', arrValores)
        .then((response) => {
          let dados = response.data

          this.processarResposta(dados)
        })
        .catch(function (error) {
          console.log(error)
        })
    },
    plotarGrafico () {
      // Plota grafico da função
      // g(x)
      // h(x)
      let arrValores = [this.x5v, 'x^5 + ', this.x4v, 'x^4 + ', this.x3v, 'x^3 + ', this.x2v, 'x^2 + ', this.x1v, 'x^1 + ', this.xfv]
      let strFuncao = arrValores.join('')

      let PlotClass = Vue.extend(Plotador)
      let instanciaPlot = new PlotClass({
        propsData: {title: 'Grafico da função', gn: strFuncao, hn: 'x', grid: true}
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
</style>
