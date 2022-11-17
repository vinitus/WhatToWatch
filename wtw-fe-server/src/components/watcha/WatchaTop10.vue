<template>
  <div>
    <h1>watcha</h1>
    <watch-item v-for="(watcha, index) in watchaList" :key="index"></watch-item>
  </div>
</template>

<script>
import WatchItem from './WatchItem.vue'
import axiosCall from '@/axiosCall/axiosCall.js'

export default {
  name: 'WatchaTop10',
  components: {
    WatchItem
  },
  data() {
    return {
      watchaList: []
    }
  },
  methods: {
    getWatchaData() {
      this.watchaList = axiosCall('api/watcha/', 'get')
      console.log(this.watchaList)
    }
  },
  created() {
    this.getWatchaData()
  }
}
</script>

<style>

</style>