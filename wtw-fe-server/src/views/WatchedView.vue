<template>
  <div id="watchedView">
    <button @click="submitWatchedList" class="btn btn-primary"
      style="margin-left:30px; position: fixed; right:3vw; bottom: 3vw">DONE!</button>

    <div style="text-align:left;">
      <div v-for="(contentItem, watchedMovieIndex) in expression" :key="'watch' + watchedMovieIndex"
        style="display:inline-block; margin-left: 30px; margin-top: 10px;">
        <img :data-content-id="contentItem.id" :src="`https://image.tmdb.org/t/p/w300/${contentItem.poster_path}`"
          @click="selectIMG" class="" style="height:450px; width:300px;">
      </div>
    </div>
    <my-observer @triggerIntersected="loadMore"></my-observer>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';
import MyObserver from '../components/MyObserver.vue';

export default {
  components: { MyObserver },
  name: 'WatchedView',
  data() {
    return {
      contentsList: [],
      watchedList: [],
      expression: [],
    }
  },
  methods: {
    getData() {
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall('api/user_interection/', 'get', '', headers)
      res.then((data) => {
        this.contentsList = data
        if (data.length > 21) {
          this.expression = this.contentsList.slice(0, 21)
          this.index = 21
        } else {
          this.expression = data
          this.index = false
        }
      })
    },
    loadMore() {
      if (this.index) {
        if (this.contentsList.length - this.index > 21) {
          const fetchArr = this.contentsList.slice(this.index, this.index + 21)
          console.log(fetchArr)
          this.expression.push(...fetchArr)
          this.index += 21
        } else {
          const fetchArr = this.contentsList.slice(this.index)
          console.log(fetchArr)
          this.expression.push(...fetchArr)
          this.index = false
        }
      } else {
        return
      }
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