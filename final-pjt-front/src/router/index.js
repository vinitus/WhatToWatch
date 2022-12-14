import Vue from "vue"
import VueRouter from "vue-router"
import HomeView from "../views/HomeView.vue"
import MovieView from "../views/MovieView.vue"
import SeriesView from "../views/SeriesView.vue"
import LoginView from "../views/LoginView.vue"
import AuthView from "../views/AuthView.vue"
import SignupView from "../views/SignupView.vue"
import SearchView from "../views/SearchView.vue"
import MovieDetailView from "../views/MovieDetailView.vue"
import ProfileView from "../views/ProfileView.vue"
import WatchedView from "../views/WatchedView.vue"
import PasswordResetView from "../views/PasswordResetView.vue"

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
    path: "/passwordreset",
    name: "PasswordReset",
    component: PasswordResetView,
  },
  {
    path: "/auth",
    name: "Auth",
    component: AuthView,
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
  {
    path: "/profile",
    name: "Profile",
    component: ProfileView,
  },
  {
    path: "/watched",
    name: "Watched",
    component: WatchedView,
  },
]

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
})

export default router
