<template>
  <div>

    <h1>watcha</h1>
    <div v-if="watchaList.length != 0" class="horizontal_scroll">
      <b-row>
        <movie-item class="child" v-for="(movieItem, index) in watchaList" :key="index" :movieItem="movieItem">
        </movie-item>
      </b-row>
    </div>
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
.horizontal_scroll {
  scroll-snap-type: x mandatory;
  display: flex;
  flex-wrap: nowrap;
  width: 100vw;
  overflow: auto;
}

.row {
  flex-wrap: nowrap !important;
}

/* .container { */
/* display: flex; */
/* scroll-snap-type: x mandatory;
  overflow: scroll;
  height: 500px; */
/* } */

/* .child {
  scroll-snap-align: start;
} */
</style>