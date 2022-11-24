<template>
  <div>
    <h1>{{ genre }}</h1>
    <div v-if="movieList.length != 0" class="horizontal_scroll">
      <b-row>
        <movie-item class="child" v-for="(movieItem, index) in movieList" :key="index" :movieItem="movieItem">
        </movie-item>
      </b-row>
    </div>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';
import movieItem from '@/components/MovieItem.vue'

export default {
  name: 'RecommendGenreView',
  components: {
    movieItem
  },
  data() {
    return {
      genre: '',
      movieList: []
    }
  },
  methods: {
    getGenreRecommendData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/recommend_based_users/', 'get', '', headers)
      res.then((data) => {
        console.log(data)
        this.genre = data.genre
        this.movieList = data.movies
      })
    }
  },
  created() {
    this.getGenreRecommendData()
  }
}
</script>

<style>

</style>