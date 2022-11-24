<template>
  <div id="recommendactor">
    <h1 v-if="movieList.length > 0">{{ actor }}가 출연한 영화</h1>
    <div v-if="movieList.length != 0" class="horizontal_scroll slider3" @mousedown="scrollmousedown"
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
  name: 'RecommendActorView',
  components: {
    movieItem
  },
  data() {
    return {
      actor: '',
      movieList: [],
      bMove: false,
      startX: 0,
      scrollLeft: 0,
    }
  },
  methods: {
    getActorRecommendData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/recommend_based_actors/', 'get', '', headers)
      res.then((data) => {
        this.actor = data.actor
        this.movieList = data.movies
        console.log(data)
      })
    },
    scrollmousedown(e) {
      const slider = document.querySelector(".slider3")
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
      const slider = document.querySelector(".slider3")

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
    this.getActorRecommendData()
  }
}
</script>

<style>
#recommendactor {
  color: white !important;
  margin: 20px;
}
</style>