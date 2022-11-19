<template>
  <div>
    <h3>Detail</h3>
    <div>{{ movieInfo }}</div>
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
    }
  },
  created() {
    this.getMovieDetail()
    this.getReviewList()
  },

}
</script>

<style>

</style>