import Vue from "vue"
import App from "./App.vue"
import store from "./store"
import router from "./router"
import { BootstrapVue, IconsPlugin } from "bootstrap-vue"
import "bootstrap/dist/css/bootstrap.css"
import "bootstrap-vue/dist/bootstrap-vue.css"
// import "@/assets/custom.scss"

Vue.use(BootstrapVue)
Vue.use(IconsPlugin)

Vue.config.productionTip = false

window.Kakao.init("ea6b7340c3047bd44235c5bb07f152aa")

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app")
