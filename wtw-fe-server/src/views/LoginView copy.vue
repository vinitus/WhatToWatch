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
    <a @click.prevent="kakaoLogin" id="kakao-login-btn">
      <img src="https://k.kakaocdn.net/14/dn/btroDszwNrM/I6efHub1SN5KCJqLm1Ovx1/o.jpg" width="222" alt="카카오 로그인 버튼" />
    </a>
    <p id="token-result"></p>
  </div>
</template>

<script>
// import axiosCall from '@/axiosCall/axiosCall'

import axiosCall from '@/axiosCall/axiosCall'

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
      // const params = {
      //   redirectUri: "http://localhost:8080/auth",
      // };
      // window.Kakao.Auth.authorize(params);

      if (window.Kakao.Auth.getAccessToken()) {
        window.Kakao.API.request({
          url: '/v1/user/unlink',
          success: function (response) {
            console.log(response)
          },
          fail: function (error) {
            console.log(error)
          },
        })
        window.Kakao.Auth.setAccessToken(undefined)
      }
      window.Kakao.Auth.login({
        success: function () {
          window.Kakao.API.request({
            url: '/v2/user/me',
            data: {
              property_keys: ["kakao_account.email"]
            },
            success: async function (response) {
              console.log(response)

              window.Kakao.API.request({
                url: '/v2/user/me',
              })
                .then(function (res) {
                  console.log(res)
                  // const data = {
                  //   'access_token': window.Kakao.Auth.getAccessToken()
                  // }
                  const apiRes = axiosCall('accounts/kakao/login/finish/', 'post', res)
                  console.log(apiRes)
                })
                .catch(function (err) {
                  alert(
                    'failed to request user information: ' + JSON.stringify(err)
                  );
                });
              // console.log(response)
              // const res = await axiosCall('accounts/kakaologin/', 'post', response)
              // res.then((data) => {
              //   console.log('keepgoing')
              //   console.log(data)
              // })
              // res.catch((err) => {
              //   console.log('error')
              //   console.log(err)
              // })
            },
            fail: function (error) {
              console.log(error)
            },
          })
        },
        fail: function (error) {
          console.log(error)
        },
      })
    },
    // kakaoLogin() {
    //   // const REST_API_KEY = '9e23cba329b4a051b6a8d2fa14e8ddf2'
    //   // const REDIRECT_URI = 'http://localhost:8080/'
    //   axiosCall('accounts/kakao/login/')
  }

}

</script>

<style>

</style>