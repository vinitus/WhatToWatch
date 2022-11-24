import axiosCall from "@/axiosCall/axiosCall"

const movie = {
  namespaced: true,
  state: {
    movieList: [],
    genreList: [],
  },
  mutations: {
    SAVE_MOVIE_LIST(state, data) {
      state.movieList = data
    },
    SAVE_GENRE_LIST(state, data) {
      state.genreList = data
    },
  },
  actions: {
    appCreated(context) {
      const res = axiosCall("api/movie_title/", "get")
      res.then((data) => context.commit("SAVE_MOVIE_LIST", data))
      const genre_res = axiosCall("api/genres/", "get")
      genre_res.then((data) => {
        // const genre_arr = {}
        // data.forEach((element) => {
        //   const id = element.id
        //   const name = element.name
        //   genre_arr[id] = name
        // })
        context.commit("SAVE_GENRE_LIST", data)
      })
    },
  },
}

export default movie
