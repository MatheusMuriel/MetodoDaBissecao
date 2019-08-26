import Vue from 'vue'
import App from './App.vue'
import VueMathjax from 'vue-mathjax'

Vue.use(VueMathjax)

new Vue({
  el: '#app',
  render: h => h(App)
})
