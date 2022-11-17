<template>
  <div v-if="netflixList.length != 0">
    <h1>netflix</h1>
    <netflix-item v-for="(netflixItem, index) in netflixList" :key="index" :netflixItem="netflixItem"></netflix-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall.js'
import NetflixItem from '@/components/netflix/NetflixItem.vue'

export default {
  name: 'NetflixTop10',
  components: {
    NetflixItem
  },
  data() {
    return {
      netflixList: []
    }
  },
  methods: {
    getNetflixData() {
      const promiseRes = axiosCall('api/netflix/', 'get')
      promiseRes.then((data) => this.netflixList = data)
    }
  },
  created() {
    this.getNetflixData()
  }
}
</script>

<style>

</style>