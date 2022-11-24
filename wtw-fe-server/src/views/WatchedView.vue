<template>
  <div id="watchedView">
    <button @click="submitWatchedList" style="margin-left:30px;">제출 버튼</button>
      <!-- <div style="margin-right:50px;"> -->
        <!-- <b-row v-for="(contentRow, i) in contentRows" :key="i">
          <b-col v-for="(contentItem, j) in contentRow" :key="j">
            <div class="" style="margin: 30px;">
              <img :data-content-id="contentItem.id" :src="`https://image.tmdb.org/t/p/w300/${contentItem.poster_path}`"
                @click="selectIMG" class="" style="height:450px; width:300px;">
            </div>
          </b-col>
        </b-row> -->
      <!-- </div> -->
    <div style="text-align:left;">
      <div v-for="(contentItem, watchedMovieIndex) in contentsList" :key="'watch' + watchedMovieIndex" style="display:inline-block; margin-left: 30px; margin-top: 10px;">
        <img :data-content-id="contentItem.id" :src="`https://image.tmdb.org/t/p/w300/${contentItem.poster_path}`"
        @click="selectIMG" class="" style="height:450px; width:300px;">
      </div>
    </div>
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
        this.contentsList = data
      })
      res.catch((error) => console.log(error))
    },
    selectIMG(event) {
      const contentId = event.target.dataset.contentId
      const index = this.watchedList.indexOf(contentId)
      if (index === -1) {
        this.watchedList.push(contentId)
        event.target.classList.add('divin')
        event.target.parentElement.classList.add('divout')
      } else {
        this.watchedList.splice(index, 1)
        event.target.classList.remove('divin')
        event.target.parentElement.classList.remove('divout')
      }

    },
    submitWatchedList() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const data = { 'movie_id': [...this.watchedList] }
      const res = axiosCall('api/user_interection/', 'post', data, headers)
      res.then(() => {
        this.$router.push({ name: 'Home' })
      })
      res.catch((err) => console.log(err))
    }
  },
  computed: {
    contentRows() {
      return this.contentsList.reduce((acc, n, i) => {
        i % 5 ? acc[acc.length - 1].push(n) : acc.push([n])
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

.watched-selected {
  border: 1px solid white;
}

.divout {
  width: 300px;
  height: 450px;
  flex: 1;
  background: black;
  box-shadow: 0px 0px 10px 5px white;
  border-radius: 15px;
}

.divin {
  width: 300px;
  height: 450px;
  flex: 1;
  overflow: auto;
  flex-direction: column;
  border-radius: 15px;
  background: black;
  box-shadow: inset 0px 0px 15px 5px white;
}
</style>