<template>
  <nav>
    <router-link :to="{ name: 'home' }">뭐봄</router-link> |
    <router-link :to="{ name: 'movies' }">영화</router-link> |
    <router-link :to="{ name: 'series' }">시리즈</router-link> |
    <input type="text" @keyup.enter="navInputSubmit"> |
    <router-link :to="{ name: 'login' }">로그인</router-link> |
    <router-link :to="{ name: 'signup' }">회원가입</router-link>
  </nav>
</template>

<script>
export default {
  name: 'NavigationBar',
  methods: {
    navInputSubmit(event) {
      const keyword = event.target.value
      if (this.$route.name === 'search') {
        if (this.$route.params.keyword != keyword) {
          this.$router.push({ name: 'search', params: { keyword: keyword } })
        }
      }
    }
  }
}
</script>

<style>

</style>