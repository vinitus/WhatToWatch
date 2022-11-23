<template>
  <div>
    <h3>Detail</h3>
    <!-- <div class="img-div" :style="{ backgroundImage: 'url(' + this.imgURL + ')' }">
    </div> -->
    <!-- <div>{{ movieInfo }}</div> -->
    <!-- background-image: linear-gradient(to top, rgb(0, 0, 0) 2%, rgba(0, 0, 0, 0) 50%), linear-gradient(to right, rgb(0, 0, 0)
    20%, rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.1) 100%),
    url("https://img.coupangstreaming.com/titles/c9fc3bc8-de1d-45e8-9347-adf1514487ff/hero-largescreen/5fc3aa26-bcf6-4bd1-9598-a619f9387f71.jpeg?imwidth=1200&imheight=300&imscalingMode=aspectFit"); -->
    <!-- <img :src="imgURL" alt=""> -->
    <div
      :style="{ backgroundImage: 'url(' + this.imgURL + ')', 'width': '300px', 'height': '450px', 'background- size': 'cover' }">
      <img :style="{ 'width': '40px', 'height': '40px', 'margin-top': '400px', 'float': 'right' }"
        :class="{ 'checked': !watched }" :src="seeIcon" alt="" @click="makeWatched">
      <img :style="{ 'width': '40px', 'height': '40px', 'margin-top': '400px', 'float': 'right' }" :src="wishesIcon"
        :class="{ 'checked': !wishes }" alt="" @click="makeWishes">
    </div>
    <div v-for="(logo, logoIndex) in logoList" :key="'logo' + logoIndex">
      <img :src="`https://image.tmdb.org/t/p/original/${logo.logo_path}`" style="width:50px; height:50px;" alt="">
    </div>
    <review-form @review-is-change="getReviewList"></review-form>
    <review-item v-for="(review, reviewIndex) in reviewList" :key="reviewIndex" :review="review"></review-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall'
import ReviewForm from '../components/review/ReviewForm.vue'
import ReviewItem from '../components/review/ReviewItem.vue'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewForm,
    ReviewItem
  },
  data() {
    return {
      movieInfo: '',
      reviewList: [],
      seeIcon: require('@/assets/see.png'),
      wishesIcon: require('@/assets/wishes.png'),
      logoList: [],
    }
  },
  methods: {
    getMovieDetail() {
      // console.log(this.$route.params)
      const movieId = this.$route.params.movieId
      const res = axiosCall(`api/movies/${movieId}/`)
      res.then((data) => this.movieInfo = data)
    },
    getReviewList() {
      const movieId = this.$route.params.movieId
      const res = axiosCall(`feed/reviews/movie/${movieId}/`)
      res.then((data) => this.reviewList = data)
    },
    makeWatched() {
      const movieId = this.$route.params.movieId
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall(`api/movies/${movieId}/`, 'post', '', headers)
      res.then(this.$store.dispatch('requestWatched', '', { root: true }))
    },
    makeWishes() {
      const movieId = this.$route.params.movieId
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall(`api/movies/${movieId}/wishes/`, 'post', '', headers)
      res.then(res.then(this.$store.dispatch('requestWishes', '', { root: true })))
    },
    getLogo() {
      const res = axiosCall(`api/provider/${this.$route.params.movieId}`)
      res.then((data) => this.logoList = data.providers)
    }
  },
  computed: {
    imgURL() {
      return `https://image.tmdb.org/t/p/w300${this.movieInfo.poster_path}`
    },
    watched() {
      for (const movie of this.$store.state.user.watchedMovies) {
        if (movie.title === this.movieInfo.title) {
          return true
        }
      }
      return false
    },
    wishes() {
      for (const movie of this.$store.state.user.wishesMovies) {
        if (movie.title === this.movieInfo.title) {
          return true
        }
      }
      return false
    }
  },
  created() {
    this.getMovieDetail()
    this.getReviewList()
    this.getLogo()
  },
}
</script>

<style>
.img-div {
  width: 100vw;
  height: 20vw;
  background-size: cover;
  background-repeat: no-repeat;
}

.checked {
  filter: opacity(0.2) !important;
}
</style>