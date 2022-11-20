<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="signUp">
      <label for="username">username</label>
      <input type="text" id="username" v-model="username">
      <br>
      <label for="password1">password1</label>
      <input type="password1" id="password1" v-model="password1">
      <br>
      <label for="password2">password2</label>
      <input type="password2" id="password2" v-model="password2">
      <br>
      <input type="submit" value="signUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      username: '',
      password1: '',
      password2: '',
    }
  },
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username, password1, password2
      }
      this.$store.dispatch('signUp', payload, { root: true })
    }
  }
}
</script>

<style>

</style>