<template>
  <div id="profile">
    <h2 style="margin-left:30px; color:aliceblue">PROFILE</h2>
    <router-link :to="{ name: 'Watched' }" style="margin-left:30px; color:aliceblue">
      <button>본 컨텐츠 추가하러 가기</button>
    </router-link>
    <!-- <router-link :to="{ name: 'Flatform' }">구독중인 OTT 플랫폼 설정</router-link> -->
    <h1 style="margin-left:30px; color:aliceblue">봤던 컨텐츠</h1>
    <div style="text-align:left; margin-left:10px;">
      <div v-for="(watchedMovie, watchedMovieIndex) in watchedMovies" :key="'watch' + watchedMovieIndex" style="display:inline-block; margin-left: 10px;">
        <div class="" style="margin: 10px;">
          <img 
            :src="`https://image.tmdb.org/t/p/w300/${watchedMovie.poster_path}`"
            style="height:450px; width:300px;">
        </div>
      </div>
    </div>
    <h1 style="margin-left:30px; color:aliceblue">찜한 컨텐츠</h1>
    <div style="text-align:left; margin-left:10px;">
      <div v-for="(wishesMovie, wishesMovieIndex) in wishesMovies" :key="'watch' + wishesMovieIndex" style="display:inline-block; margin-left: 10px;">
        <div class="" style="margin: 10px;">
          <img 
            :src="`https://image.tmdb.org/t/p/w300/${wishesMovie.poster_path}`"
            style="height:450px; width:300px;">
        </div>
      </div>
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
  computed: {
    contentRows() {
      return this.contentsList.reduce((acc, n, i) => {
        i % 3 ? acc[acc.length - 1].push(n) : acc.push([n])
        return acc
      }, [])
    }
  },
  created() {
    this.getWatchedMoviesData()
    this.getWishesMoviesData()
  }
}
</script>

<style>
/* #profile * {
  color: white !important;
} */
</style>