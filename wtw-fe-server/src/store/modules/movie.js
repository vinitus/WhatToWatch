import axiosCall from "@/axiosCall/axiosCall"

const movie = {
  namespaced: true,
  state: {
    movieList: [],
  },
  mutations: {
    SAVE_MOVIE_LIST(state, data) {
      state.movieList = data.movie_titles
    },
  },
  actions: {
    appCreated(context) {
      const res = axiosCall("api/movie_title/", "get")
      res.then((data) => context.commit("SAVE_MOVIE_LIST", data))
    },
  },
}

export default movie
