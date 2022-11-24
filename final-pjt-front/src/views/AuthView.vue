<template>
  <div>test
    <div id="" style="display: none">test</div>
  </div>
</template>

<script>
import getKakaoToken from "@/modules/kakaoLogin.js";
import getKakaoUserInfo from "@/modules/kakaoGetUser.js";
import axios from "axios";
import axiosCall from "@/axiosCall/axiosCall";

export default {
  name: 'AuthView',
  created() {
    if (this.$route.query.code) {
      this.setKakaoToken();
    }
  },
  data() {
    return {
      code: '',
      access_token: ''
    }
  },
  methods: {
    async setKakaoToken() {
      console.log('카카오 인증 코드', this.$route.query.code);
      this.code = this.$route.query.code
      const res = await getKakaoToken(this.$route.query.code);
      if (res.statusText != 'OK') {
        alert('카카오톡 로그인 오류입니다.');
        this.$router.replace('/login');
        return;
      }
      window.Kakao.Auth.setAccessToken(res.data.access_token);
      console.log(res.data.access_token)
      this.access_token = res.data.access_token
      axios.get(
        "https://kapi.kakao.com/v2/user/me", {
        headers: {
          'Authorization': `Bearer ${res.data.access_token}`,
        }
      })
        .then((res) => {
          const access_token = this.access_token
          const code = this.code
          const data = {
            access_token,
            code,
            res: res.data
          }
          const axiosRes = axiosCall('accounts/kakao/login/finish/', 'post', data)
          axiosRes.then((res) => {
            this.$store.commit('SAVE_TOKEN', res)
          })
        })
    },
    async setUserInfo() {
      const res = await getKakaoUserInfo();
      const userInfo = {
        name: res.kakao_account.profile.nickname,
        platform: 'kakao',
      };
      this.$store.commit('setUser', userInfo);
    },
  }
}
</script>