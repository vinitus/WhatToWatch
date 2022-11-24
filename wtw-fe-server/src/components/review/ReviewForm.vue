<template>
  <div>
    <form @focusin="checkLogin" @submit.prevent="createReview">
      <input type="text" v-model="content"
        style="background-color:black; border:none; border-bottom:1px solid white; color:white;" placeholder="리뷰">
      <br>
      <div style="width:220px; display: flex; align-items: center; margin-top:20px">
        <input type="text" style="width:25px; background-color:black; border:none; color:white;" v-model="score">
        <b-form-rating v-model="score" variant="warning" class="" style="background-color:black; border:none;">
        </b-form-rating>
        <button type="submit" class="btn btn-light" style="width: 60px; padding:1px">쓰기</button>
      </div>
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
      score: 5,
      watched: true,
    }
  },
  methods: {
    createReview() {
      const content = this.content
      const score = this.score * 2
      const watched = this.watched
      const data = {
        content,
        score,
        watched,
        movie_id: this.$route.params.movieId
      }
      const headers = { Authorization: `Bearer ${this.token.access_token}` }
      const res = axiosCall(`feed/reviews/`, 'post', data, headers)
      res.then(() => {
        this.$emit('review-is-change')
        console.log(1)
      })
      res.catch((err) => console.log(err))
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
    },
  },
}
</script>

<style>

</style>