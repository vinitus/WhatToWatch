<template>
  <div v-if="watchaList.length != 0" class="container">
    <h1>watcha</h1>
    <b-card-group deck>
      <movie-item class="child" v-for="(movieItem, index) in watchaList" :key="index" :movieItem="movieItem">
      </movie-item>
    </b-card-group>
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
      promiseRes.then((data) => {
        this.watchaList = data
        console.log(this.watchaList)
      })
    }
  },
  created() {
    this.getWatchaData()
  }
}
</script>

<style>
.container {
  scroll-snap-type: x mandatory;
  overflow: scroll;
  height: 500px;
}

.child {
  scroll-snap-align: start;
}
</style>