<template>
  <div id="profile">
    <div>PROFILE</div>
    <router-link :to="{ name: 'Watched' }">본 컨텐츠 설정하러가기</router-link>
    <!-- <router-link :to="{ name: 'Flatform' }">구독중인 OTT 플랫폼 설정</router-link> -->
    <h1>봤던 컨텐츠</h1>
    <div v-for="(watchedMovie, watchedMovieIndex) in watchedMovies" :key="'watch' + watchedMovieIndex">
      <div style="display:block;">{{ watchedMovie }}</div>
    </div>
    <h1>찜한 컨텐츠</h1>
    <div v-for="(wishesMovie, wishesMovieIndex) in wishesMovies" :key="'wish' + wishesMovieIndex">
      <div style="display:block;">{{ wishesMovie }}</div>
    </div>
  </div>
</template>

<script>
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
      this.watchedMovies = this.$store.state.user.watchedMovies
    },
    getWishesMoviesData() {
      this.wishesMovies = this.$store.state.user.wishesMovies
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