<template>
  <div class="home">
    <watcha-top-10></watcha-top-10>
    <netflix-top-10></netflix-top-10>
  </div>
</template>

<script>
import NetflixTop10 from '../components/netflix/NetflixTop10.vue'
import WatchaTop10 from '../components/watcha/WatchaTop10.vue'

export default {
  name: 'HomeView',
  components: {
    WatchaTop10,
    NetflixTop10

  }
}
</script>
