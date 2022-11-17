import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"
import SeriesView from "../views/SeriesView.vue"
import LoginView from "../views/LoginView.vue"
import SignupView from "../views/SignupView.vue"
import SearchView from "../views/SearchView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/series",
    name: "series",
    component: SeriesView,
  },
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/signup",
    name: "signup",
    component: SignupView,
  },
  {
    path: "/search/:keyword",
    name: "search",
    component: SearchView,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
