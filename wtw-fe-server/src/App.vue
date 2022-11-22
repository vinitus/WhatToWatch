<template>
  <div id="app">
    <navigation-bar></navigation-bar>
    <router-view />
  </div>
</template>

<script>
import NavigationBar from './components/NavigationBar.vue';

export default {
  components: {
    NavigationBar
  },
  created() {
    this.$store.dispatch('appCreated', '', { root: true })
  }
}
</script>

<style>
body {
  background-color: black !important;
}

a {
  text-decoration: none;
  color: black;
}
</style>
