import Vue from 'vue'
import App from './App.vue'
import VueMathjax from 'vue-mathjax'
import axios from 'axios'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)
Vue.use(VueMathjax)

new Vue({
  el: '#app',
  render: h => h(App)
})
