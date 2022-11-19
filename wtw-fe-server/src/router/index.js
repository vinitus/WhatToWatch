import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"
import MovieView from "../views/MovieView.vue"
import SeriesView from "../views/SeriesView.vue"
import LoginView from "../views/LoginView.vue"
import SignupView from "../views/SignupView.vue"
import SearchView from "../views/SearchView.vue"
import MovieDetailView from "../views/MovieDetailView.vue"

Vue.use(VueRouter)

const routes = [
  {
    path: "/",
    name: "Home",
    component: HomeView,
  },
  {
    path: "/series",
    name: "Series",
    component: SeriesView,
  },
  {
    path: "/movie",
    name: "Movies",
    component: MovieView,
  },
  {
    path: "/login",
    name: "Login",
    component: LoginView,
  },
  {
    path: "/signup",
    name: "SignUp",
    component: SignupView,
  },
  {
    path: "/search/:keyword",
    name: "Search",
    component: SearchView,
  },
  {
    path: "/movie/:movieId",
    name: "MovieDetail",
    component: MovieDetailView,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
