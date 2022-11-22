<template>
  <div>
    <form @focusin="checkLogin" @submit.prevent="createReview">
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
      const headers = { Authorization: `Bearer ${this.token.access_token}` }
      const res = axiosCall(`feed/reviews/`, 'post', data, headers)
      res
    },
    checkLogin(event) {
      if (this.isLogin) {
        console.log('keepgoing')
      } else {
        alert("리뷰는 로그인 후 작성 가능합니다!")
        event.target.blur()
      }
    }
  },
  computed: {
    token() {
      return this.$store.state.user.token
    },
    isLogin() {
      return this.$store.getters["isLogin"]
    }
  }
}
</script>

<style>

</style>