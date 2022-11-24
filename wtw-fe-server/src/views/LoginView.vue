<template>
  <div id="login-form">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input type="text" id="email" v-model="email" placeholder="email">
      <br>
      <input type="password" id="password" v-model="password" placeholder="password">
      <br>
      <input type="submit" value="로그인" id="login-button">
    </form>
    <router-link :to="{name:'PasswordReset'}">비밀번호가 기억이 안나요</router-link>
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
#login-form {
  text-align: center;
  padding-top: 100px;
}

#login-form * {
  color: white !important;
  margin: 10px;
}

#email {
  color: black !important;
  width:300px;
  padding:5px;
}

#password {
  color: black !important;
  width:300px;
  padding:5px;
}

#login-button {
  color: black !important;
  width:300px;
  padding:5px;
}
</style>