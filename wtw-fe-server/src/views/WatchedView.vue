<template>
  <div>
    <button @click="submitWatchedList">제출 버튼</button>
    <b-row v-for="(contentRow, i) in contentRows" :key="i">
      <b-col v-for="(contentItem, j) in contentRow" :key="j">
        <img :data-content-id="contentItem.id" :src="`https://image.tmdb.org/t/p/w300/${contentItem.poster_path}`"
          @click="selectIMG">
        <!-- <div @click="selectIMG" :data-content-id="contentItem.id">{{ contentItem.title }}</div> -->
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';

export default {
  name: 'WatchedView',
  data() {
    return {
      contentsList: [],
      watchedList: []
    }
  },
  methods: {
    getData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/user_interection/', 'get', '', headers)
      res.then((data) => {
        console.log(data)
        this.contentsList = data
      })
      res.catch((error) => console.log(error))
    },
    selectIMG(event) {
      const contentId = event.target.dataset.contentId
      const index = this.watchedList.indexOf(contentId)
      console.log(contentId, index)
      if (index === -1) {
        this.watchedList.push(contentId)
      } else {
        this.watchedList.splice(index, 1)
      }
    },
    submitWatchedList() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const data = { 'movie_id': [...this.watchedList] }
      const res = axiosCall('api/user_interection/', 'post', data, headers)
      res.then((data) => {
        console.log(data)
      })
    }
  },
  computed: {
    contentRows() {
      return this.contentsList.reduce((acc, n, i) => {
        i % 3 ? acc[acc.length - 1].push(n) : acc.push([n])
        return acc
      }, [])
    }
  },
  created() {
    this.getData()
  }
}
</script>

<style>
.content-watched-selected {
  border: 1px solid white;
}
</style>