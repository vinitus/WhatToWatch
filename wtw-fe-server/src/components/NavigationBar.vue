<template>
  <nav>
    <router-link :to="{ name: 'Home' }">뭐봄</router-link> |
    <router-link :to="{ name: 'Movies' }">영화</router-link> |
    <router-link :to="{ name: 'Series' }">시리즈</router-link> |
    <input type="text" @keyup.enter="navInputSubmit"> |
    <router-link v-if="!token" :to="{ name: 'Login' }">로그인</router-link> |
    <router-link v-if="!token" :to="{ name: 'SignUp' }">회원가입</router-link>
    <a v-if="token" @click.prevent="logout">로그아웃</a>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar',
  methods: {
    navInputSubmit(event) {
      const keyword = event.target.value
      if (this.$route.name != 'Search') {
        this.$router.push({ name: 'Search', params: { keyword: keyword } })
      } else {
        if (this.$route.params.keyword != keyword) {
          this.$router.push({ name: 'Search', params: { keyword: keyword } })
        }
      }
    },
    logout() {
      this.$store.dispatch('logout', '', { root: true })
    }
  },
  computed: {
    token() {
      return this.$store.state.user.token
    }
  }
}
</script>

<style>

</style>