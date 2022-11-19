import axiosCall from "@/axiosCall/axiosCall"
import router from "@/router"

const User = {
  state: {
    token: null,
  },
  mutations: {
    SAVE_TOKEN(state, token) {
      state.token = token
      router.push({ name: "home" })
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
        context.commit("SAVE_TOKEN", res.key)
      })
    },
  },
}
export default User
