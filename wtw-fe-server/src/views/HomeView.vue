<template>
  <div class="home">
    <watcha-top-10></watcha-top-10>
    <netflix-top-10></netflix-top-10>
    <recommend-actor-view v-if="isLogin"></recommend-actor-view>
    <recommend-director-view v-if="isLogin"></recommend-director-view>
    <recommend-genre-view v-if="isLogin"></recommend-genre-view>
  </div>
</template>

<script>
import NetflixTop10 from '../components/netflix/NetflixTop10.vue'
import WatchaTop10 from '../components/watcha/WatchaTop10.vue'
import RecommendActorView from '@/components/user_recommend/RecommendActorView'
import RecommendDirectorView from '@/components/user_recommend/RecommendDirectorView'
import RecommendGenreView from '@/components/user_recommend/RecommendGenreView'

export default {
  name: 'HomeView',
  components: {
    WatchaTop10,
    NetflixTop10,
    RecommendActorView,
    RecommendDirectorView,
    RecommendGenreView,
  },
  computed: {
    isLogin() {
      return this.$store.getters["isLogin"]
    }
  }
}
</script>
