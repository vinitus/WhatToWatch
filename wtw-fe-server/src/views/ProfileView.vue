<template>
  <div id="profile">
    <div>PROFILE</div>
    <router-link :to="{ name: 'Watched' }">본 컨텐츠 설정하러가기</router-link>
    <h1>봤던 컨텐츠</h1>
    <div v-for="(watchedMovie, watchedMovieIndex) in watchedMovies" :key="watchedMovieIndex">
      <div style="display:block;">{{ watchedMovie }}</div>
    </div>
    <h1>찜한 컨텐츠</h1>
    <div v-for="(wishesMovie, wishesMovieIndex) in wishesMovies" :key="wishesMovieIndex">
      <div style="display:block;">{{ wishesMovie }}</div>
    </div>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';

export default {
  name: 'ProfileView',
  data() {
    return {
      watchedMovies: [],
      wishesMovies: []
    }
  },
  methods: {
    getWatchedMoviesData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/watched/', 'get', '', headers)
      res.then((data) => this.watchedMovies = data.movies)
      res.catch((err) => console.log(err))
    },
    getWishesMoviesData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/wishes/', 'get', '', headers)
      res.then((data) => this.wishesMovies = data.movies)
      res.catch((err) => console.log(err))
    },
  },
  created() {
    this.getWatchedMoviesData()
    this.getWishesMoviesData()
  }
}
</script>

<style>
#profile * {
  color: white !important;
}
</style>