<template>
  <div id="watchatop10">
    <h1>WATCHA TOP 10</h1>
    <div v-if="watchaList.length != 0" class="horizontal_scroll slider2" @mousedown="scrollmousedown"
      @mouseleave="scrollmouseleave" @mouseup="scrollmouseup" @mousemove="scrollmousemove" @click="justClick">
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
      watchaList: [],
      bMove: false,
      startX: 0,
      scrollLeft: 0,
    }
  },
  methods: {
    getWatchaData() {
      const promiseRes = axiosCall('api/watcha/', 'get')
      promiseRes.then((data) => {
        this.watchaList = data
        console.log(this.watchaList)
      })
    },
    scrollmousedown(e) {
      const slider = document.querySelector(".slider2")
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
      const slider = document.querySelector(".slider2")

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
    this.getWatchaData()
  }
}
</script>

<style>
.horizontal_scroll {

  overflow-x: scroll;

  display: flex;
  flex-wrap: nowrap;
  width: auto;
  height: 590px;
}

.row {
  flex-wrap: nowrap !important;
}

#watchatop10 {
  color: white !important;
  margin: 20px;
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