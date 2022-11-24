<template>
  <div id="signup-form">
    <h1>회원가입</h1>
    <form @submit.prevent="signUp">
      <input type="text" id="email" v-model="email" placeholder="email">
      <br>
      <input type="password" id="password1" v-model="password1" placeholder="password1" :class="{'password1-margin':isSame}">
      <br>
      <div :class="{'password-same-div':isSame,'isDeactive':!isSame}">비밀번호가 일치하지 않습니다!</div>
      <input type="password" id="password2" v-model="password2" placeholder="password2" :class="{'password2-margin':isSame}">
      <br>
      <input type="submit" value="회원가입" id="signup-button">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignupView',
  data() {
    return {
      email: '',
      password1: '',
      password2: '',
    }
  },
  methods: {
    signUp() {
      const email = this.email
      const password1 = this.password1
      const password2 = this.password2

      if (password1 == password2) {

      const payload = {
        email, password1, password2
      }
      this.$store.dispatch('signUp', payload, { root: true })
      } else {
        alert('비밀번호가 일치하지 않습니다.')
      }
    }
  },
  computed: {
    isSame() {
      return this.password1 != this.password2
    }
  }
}
</script>

<style>
#signup-form {
  text-align: center;
  padding-top: 100px;
}

#signup-form * {
  color: white;
  margin: 10px;
}

#email {
  color: black !important;
  width:300px;
  padding:5px;
}

#password1 {
  color: black !important;
  width:300px;
  padding:5px;
}

.password1-margin {
  margin-bottom: 0px !important;
}

#password2 {
  color: black !important;
  width:300px;
  padding:5px;
}

.password2-margin {
  margin-top: 0px !important;
}

#signup-button {
  color: black !important;
  width:300px;
  padding:5px;
}

.password-same-div {
  color: red !important;
  margin: 0px !important;
  font-size:13px;
}

.isDeactive {
  display:none;
}
</style>