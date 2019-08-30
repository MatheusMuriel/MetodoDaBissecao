import Vue from 'vue'
import App from './App.vue'
import VueMathjax from 'vue-mathjax'
import axios from 'axios'
import VueAxios from 'vue-axios'
import BootstrapVue from 'bootstrap-vue'
import { Layout } from 'bootstrap-vue/es/components';

Vue.use(BootstrapVue)
Vue.use(VueAxios, axios)
Vue.use(VueMathjax)
Vue.use(Layout);

new Vue({
  el: '#app',
  render: h => h(App)
})
