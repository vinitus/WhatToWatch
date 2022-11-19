<template>
  <div v-if="netflixList.length != 0">
    <h1>netflix</h1>
    <movie-item v-for="(movieItem, index) in netflixList" :key="index" :movieItem="movieItem"></movie-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall.js'
import MovieItem from '@/components/MovieItem.vue'

export default {
  name: 'NetflixTop10',
  components: {
    MovieItem
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