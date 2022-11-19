<template>
  <div v-if="watchaList.length != 0">
    <h1>watcha</h1>
    <movie-item v-for="(movieItem, index) in watchaList" :key="index" :movieItem="movieItem"></movie-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall.js'
import MovieItem from '@/components/MovieItem.vue'

export default {
  name: 'WatchaTop10',
  components: {
    MovieItem
  },
  data() {
    return {
      watchaList: []
    }
  },
  methods: {
    getWatchaData() {
      const promiseRes = axiosCall('api/watcha/', 'get')
      promiseRes.then((data) => this.watchaList = data)
    }
  },
  created() {
    this.getWatchaData()
  }
}
</script>

<style>

</style>