<template>
  <div id="app">
    <nav>
      <router-link :to="{name:'home'}">뭐봄</router-link> |
      <router-link :to="{name:'movies'}">영화</router-link> |
      <router-link :to="{name:'series'}">시리즈</router-link> |
      <router-link :to="{name:'login'}">로그인</router-link> |
      <router-link :to="{name:'signup'}">회원가입</router-link>
    </nav>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
