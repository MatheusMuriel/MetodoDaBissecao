import Vue from 'vue'
import BootstrapVue from 'bootstrap-vue'
import VueMathjax from 'vue-mathjax'
import VueInputAutowidth from 'vue-input-autowidth'
import axios from 'axios'
import VueAxios from 'vue-axios'
import LoadScript from 'vue-plugin-load-script'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

import App from './App'

Vue.use(BootstrapVue)
Vue.use(VueMathjax)
Vue.use(VueInputAutowidth)
Vue.use(VueAxios, axios)
Vue.use(LoadScript)

Vue.config.productionTip = false

/* eslint-disable */
new Vue({
  el: '#app',
  components: { App },
  template: '<App/>'
})
