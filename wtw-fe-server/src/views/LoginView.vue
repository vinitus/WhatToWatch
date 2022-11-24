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
    <a id="kakao-login-btn" @click.prevent="kakaoLogin">
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
    kakaoLogin() {
      window.Kakao.Auth.authorize({
        redirectUri: 'http://localhost:8080/auth'
      })
    }
  }
}

</script>

<style>

</style>