<template>
  <div class="input-funcao">
    <div class="div-input">
      <b-form-input
        v-autowidth="{maxWidth: '960px', minWidth: '25px', comfortZone: 4}"
        v-bind:value="valor"
        v-on:input="$emit('input', $event.target.value)"
        type="number"/>
    </div>
    <Funcao class="label-funcao" :funcao="formula_funcao"></Funcao>
  </div>
</template>

<script>
import Funcao from './Funcao'
export default {
  components: {
    Funcao
  },
  name: 'InputFuncao',
  props: ['formula_funcao', 'valor'],
  data () {
    return {
      inputValue: 0
    }
  }
}
</script>

<style scoped>
input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
.input-funcao {
  display: flex;
  justify-content: center;
  align-items: center;
  font-size: 20px;
  white-space: nowrap;
}
.div-input input {
  height: 20px;
}
.label-funcao {
  justify-content: center;
  align-items: center;
  font-size: 25px;
}
</style>
