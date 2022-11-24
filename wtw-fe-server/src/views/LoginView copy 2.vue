<template>
  <div>
    <h1>로그인</h1>
    <form @submit.prevent="login">
      <label for="email">email</label>
      <input type="text" id="email" v-model="email">
      <br>
      <label for="password">password</label>
      <input type="password" id="password" v-model="password">
      <br>
      <input type="submit" value="login">
    </form>
    <a id="kakao-login-btn" href="http://127.0.0.1:8000/accounts/kakao/login/">
      <img src="https://k.kakaocdn.net/14/dn/btroDszwNrM/I6efHub1SN5KCJqLm1Ovx1/o.jpg" width="222" alt="카카오 로그인 버튼" />
    </a>
    <p id="token-result"></p>
  </div>
</template>

<script>
export default {
  name: 'LoginView',
  data() {
    return {
      email: '',
      password: '',
    }
  },
  methods: {
    login() {
      const email = this.email
      const password = this.password

      const payload = {
        email,
        password
      }
      this.$store.dispatch('login', payload, { root: true })
    },
  }
}

</script>

<style>

</style>