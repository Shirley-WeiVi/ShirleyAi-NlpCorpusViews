import Vue from 'vue'
import App from './App.vue'
import router from './router'
import '@/styles/main.scss' // global css
import Common from './Common'

Vue.config.productionTip = false
Vue.prototype.Common = Common

Object.defineProperty(Vue.prototype, '$http', {
  value: function(requestPromise, successCallback) {
    requestPromise.then(res => {
      console.log("Load:",res)
      if (!res) return
      successCallback && successCallback(res)
    })
  }
})

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
