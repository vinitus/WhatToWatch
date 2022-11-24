import axiosCall from "@/axiosCall/axiosCall"
import router from "@/router"

const user = {
  state: {
    token: null,
    watchedMovies: [],
    wishesMovies: [],
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: "Home" })
    },
    DELETE_TOKEN(state) {
      state.token = null
      // router.push({ name: "Home" })
    },
    SAVE_WATCHED_MOVIES(state, data) {
      state.watchedMovies = data.movies
    },
    SAVE_WISHES_MOVIES(state, data) {
      state.wishesMovies = data.movies
    },
    CLEAR(state) {
      state.watchedMovies = null
      state.wishesMovies = null
    },
  },
  actions: {
    signUp(context, payload) {
      const data = {
        email: payload.email,
        password1: payload.password1,
        password2: payload.password2,
      }
      const res = axiosCall("accounts/signup/", "post", data)
      res.then((res) => {
        context.commit("SAVE_TOKEN", res.key)
      })
    },
    login({ commit, dispatch }, payload) {
      const data = {
        email: payload.email,
        password: payload.password,
      }
      const res = axiosCall("accounts/login/", "post", data)
      res.then((res) => {
        commit("SAVE_TOKEN", res)
        dispatch("requestWatched")
        dispatch("requestWishes")
      })
    },
    logout(context) {
      const res = axiosCall("accounts/logout/", "post")
      res.then(() => context.commit("DELETE_TOKEN"))
    },
    appCreated({ state, dispatch, commit }) {
      if (state.token) {
        dispatch("requestWatched").then(dispatch("requestWishes"))
      } else {
        commit("CLEAR")
      }
    },
    requestWatched({ commit, state }) {
      const headers = {
        Authorization: `Bearer ${state.token.access_token}`,
      }
      const res = axiosCall("api/watched/", "get", "", headers)
      res.then((data) => commit("SAVE_WATCHED_MOVIES", data))
      res.catch((err) => console.log(err))
    },
    requestWishes({ state, commit }) {
      const headers = {
        Authorization: `Bearer ${state.token.access_token}`,
      }
      const res = axiosCall("api/wishes/", "get", "", headers)
      res.then((data) => commit("SAVE_WISHES_MOVIES", data))
      res.catch((err) => console.log(err))
    },
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
}
export default user
