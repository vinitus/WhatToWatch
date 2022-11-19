<template>
  <div>
    <form @submit.prevent="createReview">
      <input type="text" v-model="content">
      <br>
      <input type="text" v-model="score">
      <br>
      <input type="checkbox" name="watched" id="watched" v-model="watched">
      <br>
      <button type="submit">제출</button>
    </form>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';

export default {
  name: 'ReviewForm',
  data() {
    return {
      content: '',
      score: 10,
      watched: true,
    }
  },
  methods: {
    createReview() {
      const content = this.content
      const score = this.score
      const watched = this.watched
      const data = {
        content,
        score,
        watched,
        movie_id: this.$route.params.movieId
      }
      console.log(this.token)
      const headers = { Authorization: `Bearer ${this.token.access_token}` }
      const res = axiosCall(`feed/reviews/`, 'post', data, headers)
      res
    }
  },
  computed: {
    token() {
      return this.$store.state.user.token
    }
  }
}
</script>

<style>

</style>