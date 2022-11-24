<template>
  <div id="password-form">
    <h1>비밀번호 초기화</h1>
    <form @submit.prevent="pageLoad">
        <input type="text" id="password-email" v-model="email" placeholder="비밀번호 초기화를 위한 email를 입력해주세요.">
        <button type="submit" id="password-button">전 송</button>
      </form>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';

export default {
  name: 'PasswordResetView',
  data() {
    return {
        email:''
    }
  },
  methods: {
    pageLoad() {
      const data = {email: this.email}
      const res = axiosCall('/accounts/password/reset/','post',data)
      res.then(() => alert('비밀번호 변경 완료!'))
      res.catch(() => alert('일치하는 이메일이 없습니다.'))
    }
  },
}
</script>

<style>
#password-form {
  text-align: center;
  padding-top: 100px;
}

#password-form * {
  color: white !important;
  margin: 10px;
}

#password-email {
  color: black !important;
  width:500px;
  height: 50px;
  padding:5px;
}

#password-button {
  width: 70px;
  font-size:20px;
  height: 54px;
  padding:5px;
  border-radius: 10%;
  background-color: #dc3545;
}
</style>