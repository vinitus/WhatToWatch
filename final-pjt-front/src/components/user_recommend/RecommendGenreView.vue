<template>
  <div id="recommendgenre">
    <h1 v-if="movieList.length > 0">{{ genre }} 추천 영화</h1>
    <div v-if="movieList.length != 0" class="horizontal_scroll slider4" @mousedown="scrollmousedown"
      @mouseleave="scrollmouseleave" @mouseup="scrollmouseup" @mousemove="scrollmousemove" @click="justClick">
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
      movieList: [],
      bMove: false,
      startX: 0,
      scrollLeft: 0,
    }
  },
  methods: {
    getGenreRecommendData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/recommend_based_genres/', 'get', '', headers)
      res.then((data) => {
        console.log(data)
        this.genre = data.genre
        this.movieList = data.movies
      })
    },
    scrollmousedown(e) {
      const slider = document.querySelector(".slider4")
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
      const slider = document.querySelector(".slider4")

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
    this.getGenreRecommendData()
  }
}
</script>

<style>
#recommendgenre {
  color: white !important;
  margin: 20px;
}
</style>