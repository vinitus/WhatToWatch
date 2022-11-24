<template>
  <div id="recommenddirector">
    <h1 v-if="movieList.length > 0">{{ director }}감독의 작품</h1>
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
  name: 'RecommendDirectorView',
  components: {
    movieItem
  },
  data() {
    return {
      director: '',
      movieList: []
    }
  },
  methods: {
    getDirectorRecommendData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/recommend_based_directors/', 'get', '', headers)
      res.then((data) => {
        this.director = data.director
        this.movieList = data.movies
      })
    }
  },
  created() {
    this.getDirectorRecommendData()
  }
}
</script>

<style>
#recommenddirector {
  color: white !important;
  margin: 20px;
}
</style>