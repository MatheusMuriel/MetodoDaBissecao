<template>
  <div>
    <vue-mathjax
    unselectable="on"
    class="label"
    :formula="funcao"
    :options="{menuOptions: {settings: {inTabOrder: false}}}"/>
  </div>
</template>

<script>
// https://www.npmjs.com/package/vue-mathjax
export default {
  name: 'Funcao',
  props: {
    funcao: String
  }
}
</script>

<style scoped>
.label {
  pointer-events: none;
}
</style>
