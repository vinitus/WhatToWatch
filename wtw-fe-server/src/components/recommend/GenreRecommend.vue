<template>
  <div v-if="genreBasedList.length != 0">
    <h1>genre based</h1>
    <movie-item v-for="(movieItem, index) in genreBasedList" :key="index" :movieItem="movieItem"></movie-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall.js'
import MovieItem from '@/components/MovieItem.vue'


export default {
  name: 'GenreRecommend',
  components: {
    MovieItem
  },
  data() {
    return {
      genreBasedList: []
    }
  },
  methods: {
    getGenreBasedData() {
      const reco_data = {
      }
      const promiseRes = axiosCall('api/recommend_based_genres/', 'get', reco_data)
      promiseRes.then((data) => this.netflixList = data)
    }
  },
  created() {
    this.getGenreBasedData()
  }
}
</script>

<style>

</style>