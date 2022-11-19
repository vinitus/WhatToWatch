import axiosCall from "@/axiosCall/axiosCall"
import router from "@/router"

const user = {
  state: {
    token: null,
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
  },
  actions: {
    signUp(context, payload) {
      const data = {
        username: payload.username,
        password1: payload.password1,
        password2: payload.password2,
      }
      const res = axiosCall("accounts/signup/", "post", data)
      res.then((res) => {
        context.commit("SAVE_TOKEN", res.key)
      })
    },
    login(context, payload) {
      const data = {
        username: payload.username,
        password: payload.password,
      }
      const res = axiosCall("accounts/login/", "post", data)
      res.then((res) => {
        console.log(res)
        context.commit("SAVE_TOKEN", res)
      })
    },
    logout(context) {
      const res = axiosCall("accounts/logout/", "post")
      res.then(() => context.commit("DELETE_TOKEN"))
    },
  },
  getters: {
    isLogin(state) {
      return state.token ? true : false
    },
  },
}
export default user
