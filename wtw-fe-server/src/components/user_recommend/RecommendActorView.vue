<template>
  <div>
    <h1>{{ actor }}</h1>
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
  name: 'RecommendActorView',
  components: {
    movieItem
  },
  data() {
    return {
      actor: '',
      movieList: []
    }
  },
  methods: {
    getActorRecommendData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/recommend_based_actors/', 'get', '', headers)
      res.then((data) => {
        this.actor = data.actor
        this.movieList = data.movies
      })
    }
  },
  created() {
    this.getActorRecommendData()
  }
}
</script>

<style>

</style>