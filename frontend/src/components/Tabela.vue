<template>
  <div>
    <b-table ref="tableBase" striped hover :items="items" :fields="fields">
    </b-table>
  </div>
</template>

<script>
export default {
  name: 'tabela',
  data () {
    return {
      fields: {
        iteracao: {
          label: 'Iteração',
          sortable: true
        },
        x: {
          label: 'X',
          sortable: false
        },
        fDeX: {
          label: 'f(x)',
          sortable: false
        },
        bMenosA: {
          label: 'b - a',
          sortable: false
        }
      }
    }
  },
  props: ['items']
}
</script>

<style>

</style>
