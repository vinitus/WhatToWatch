<template>
  <div v-if="watchaList.length != 0">
    <h1>watcha</h1>
    <watcha-item v-for="(watchaItem, index) in watchaList" :key="index" :watchaItem="watchaItem"></watcha-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall.js'
import WatchaItem from '@/components/watcha/WatchaItem.vue'

export default {
  name: 'WatchaTop10',
  components: {
    WatchaItem
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