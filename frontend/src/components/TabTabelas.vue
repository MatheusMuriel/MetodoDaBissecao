<template>
  <div>
    <b-container>
      <b-row align-h="center">
          <h5>Intervalos Encontrados</h5>
      </b-row>

      <b-row align-h="center">
        <div ref="tabsConteiner">
          <b-tabs ref="tabs" content-class="mt-3" fill>
            <b-tab v-for="i in tabs" :key="'dyn-tab-' + i" :title="i.nome">
              <tabela :items="i.dados"></tabela>
            </b-tab>
          </b-tabs>
        </div>
      </b-row>

    </b-container>
  </div>
</template>

<script>
import Tabela from './Tabela'
import Vue from 'vue'

export default {
  name: 'TabTabelas',
  props: ['intervalos'],
  components: {
    Tabela
  },
  data () {
    return {
      tabs: []
    }
  },
  created: function () {
    for (let i = 0; i < this.intervalos.length; i++) {
      // Gerar Tab
      let dadosBrutosIntervalo = this.intervalos[i]

      let iteracoesIntervalo = dadosBrutosIntervalo.split('#')

      let valoresIntervalo = iteracoesIntervalo.shift().split('::')

      let nomeTab = String(valoresIntervalo[0]) + ' : ' + String(valoresIntervalo[1])

      this.criarTab(i, nomeTab, iteracoesIntervalo)
    }
  },
  methods: {
    criarTab (id, nome, iteracoes) {
      iteracoes = this.tratarIteracoes(iteracoes)
      console.log('Iteracoes filtradas ', iteracoes)

      let tab = {cod: id, nome: nome, dados: iteracoes}
      // console.log('Nova Tab: ', tab)
      let tabela = this.criarTabela(iteracoes)
      console.log('Tabela', tabela)
      this.tabs.push(tab)
    },
    criarTabela (dados) {
      let TabelasClass = Vue.extend(Tabela)
      let instanciaTabelas = new TabelasClass({
        propsData: {items: dados}
      })
      instanciaTabelas.$mount()
      return instanciaTabelas
    },
    tratarIteracoes (iteracoesBrutas) {
      // console.log(iteracoesBrutas)
      let arrSaida = []
      for (let i = 0; i < iteracoesBrutas.length; i++) {
        let strIteracao = iteracoesBrutas[i]
        // console.log("Iteracao da vez: " + str_da_vez)

        let numeroIteracao = strIteracao.substring(0, strIteracao.indexOf('['))
        // console.log("Numero da iteração: " + num_iteracao)

        let valoresLista = strIteracao.substring(strIteracao.indexOf('[') + 1, strIteracao.indexOf(']')).split(';')
        // console.log("Lista de valores: " + valores_lista)

        let valorX = valoresLista[0]
        let valorFdex = valoresLista[1]
        let valorBA = valoresLista[2]

        let dadosFiltrados = {iteracao: numeroIteracao, x: valorX, fDeX: valorFdex, bMenosA: valorBA}
        arrSaida.push(dadosFiltrados)
      }
      return arrSaida
    }
  }
}
</script>

<style>

</style>
