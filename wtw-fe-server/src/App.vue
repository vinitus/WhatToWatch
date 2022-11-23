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
  methods: {

  },
  created() {
    this.$store.dispatch('movie/appCreated')
    this.$store.dispatch('appCreated')
  }
}
</script>

<style>
/* body {
  background-color: black !important;
}

a {
  text-decoration: none;
  color: black;
} */
</style>
