<template>
  <div id="netflixtop10">
    <h1>NETFLIX TOP 10</h1>
    <div v-if="netflixList.length != 0" class="horizontal_scroll slider" @mousedown="scrollmousedown"
      @mouseleave="scrollmouseleave" @mouseup="scrollmouseup" @mousemove="scrollmousemove" @click="justClick">
      <b-row>
        <movie-item class="child" v-for="(movieItem, index) in netflixList" :key="index" :movieItem="movieItem">
        </movie-item>
      </b-row>
    </div>
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
      netflixList: [],
      bMove: false,
      startX: 0,
      scrollLeft: 0,
    }
  },
  methods: {
    getNetflixData() {
      const promiseRes = axiosCall('api/netflix/', 'get')
      promiseRes.then((data) => this.netflixList = data)
    },
    scrollmousedown(e) {
      const slider = document.querySelector(".slider")
      e.preventDefault()
      this.bMove = true;
      this.startX = e.pageX - slider.offsetLeft;
      this.scrollLeft = slider.scrollLeft;
    },
    scrollmouseleave() {
      this.bMove = false;
    },

    scrollmouseup() {
      this.bMove = false;
    },

    scrollmousemove(e) {
      const slider = document.querySelector(".slider")

      if (this.bMove) {
        const x = e.pageX - slider.offsetLeft;
        const walk = x - this.startX;
        slider.scrollLeft = this.scrollLeft - walk;
        this.$store.commit('SAVE_MOVING', walk)
      }
    },
    justClick() {
      this.$store.commit('SAVE_MOVING', 0)
    }
  },
  created() {
    this.getNetflixData()
  },
}
</script>

<style>
#netflixtop10 {
  color: white !important;
  margin: 20px;
}
</style>