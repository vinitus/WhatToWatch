<template>
  <div>
    <h3>Detail</h3>
    <!-- <div class="img-div" :style="{ backgroundImage: 'url(' + this.imgURL + ')' }">
    </div> -->
    <!-- <div>{{ movieInfo }}</div> -->
    <!-- background-image: linear-gradient(to top, rgb(0, 0, 0) 2%, rgba(0, 0, 0, 0) 50%), linear-gradient(to right, rgb(0, 0, 0)
    20%, rgba(0, 0, 0, 0) 50%, rgba(0, 0, 0, 0.1) 100%),
    url("https://img.coupangstreaming.com/titles/c9fc3bc8-de1d-45e8-9347-adf1514487ff/hero-largescreen/5fc3aa26-bcf6-4bd1-9598-a619f9387f71.jpeg?imwidth=1200&imheight=300&imscalingMode=aspectFit"); -->
    <img :src="imgURL" alt="">
    <button @click="clickButton">본영화</button>
    <review-form></review-form>
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
      reviewList: []
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
    clickButton() {
      const movieId = this.$route.params.movieId
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall(`api/movies/${movieId}/`, 'post', '', headers)
      res.then((data) => console.log(data))
    }
  },
  computed: {
    imgURL() {
      return `https://image.tmdb.org/t/p/w300/${this.movieInfo.poster_path}`
    }
  },
  created() {
    this.getMovieDetail()
    this.getReviewList()
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
</style>