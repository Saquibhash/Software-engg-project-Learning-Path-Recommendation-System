import '@babel/polyfill'
import 'mutationobserver-shim'
import Vue from 'vue'
import './plugins/bootstrap-vue'
import App from './App.vue'
import router from './router'
import store from './store'
import './registerServiceWorker'
import '@fortawesome/fontawesome-free/css/all.css'



import UserNavComponent from '@/components/UserNavComponent.vue'
import AdminNavComponent from '@/components/AdminNavComponent.vue'



Vue.component('UserNavComponent', UserNavComponent)
Vue.component('AdminNavComponent', AdminNavComponent)





Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
