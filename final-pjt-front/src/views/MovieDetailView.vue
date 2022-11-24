<template>
  <div class="detail">
    <b-row style="margin-bottom:50px;">
      <b-col style="flex-basis: unset !important; width:300px">
        <div v-if="movieInfo"
          :style="{ backgroundImage: 'url(' + this.imgURL + ')', 'width': '300px', 'height': '450px', 'background- size': 'cover' }">
          <img :style="{ 'width': '40px', 'height': '40px', 'margin-top': '400px', 'float': 'right' }"
            :class="{ 'checked': !watched }" :src="seeIcon" alt="" @click="makeWatched">
          <img :style="{ 'width': '40px', 'height': '40px', 'margin-top': '400px', 'float': 'right' }" :src="wishesIcon"
            :class="{ 'checked': !wishes }" alt="" @click="makeWishes">
        </div>
      </b-col>
      <div style="margin:0px 20px; flex-grow: 1;" id="movie-detail-col">
        <div>
          <h2>{{ movieInfo.title }}</h2>
          <span v-for="(genre, genreIndex) in genreList" :key="genreIndex">
            {{ genre }}
          </span>
          <div>{{ movieInfo.overview }}</div>
          <div>개봉일 : {{ movieInfo.release_date }}</div>
        </div>
      </div>
    </b-row>
    <div v-if="logoList.length != 0">
      <div v-for="(logo, logoIndex) in logoList" :key="'logo' + logoIndex">
        <img :src="`https://image.tmdb.org/t/p/original/${logo.logo_path}`" style="width:50px; height:50px;" alt="">
      </div>
    </div>
    <review-form @review-is-change="getReviewList"></review-form>
    <review-item v-for="(review, reviewIndex) in reviewList" :key="reviewIndex" :review="review"></review-item>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall'
import ReviewForm from '../components/review/ReviewForm.vue'
import ReviewItem from '../components/review/ReviewItem.vue'

export default {
  name: 'MovieDetailView',
  components: {
    ReviewForm,
    ReviewItem
  },
  data() {
    return {
      movieInfo: '',
      reviewList: [],
      seeIcon: require('@/assets/see.png'),
      wishesIcon: require('@/assets/wishes.png'),
      logoList: [],
      genreList: []
    }
  },
  methods: {
    getMovieDetail() {
      // console.log(this.$route.params)
      const movieId = this.$route.params.movieId
      const res = axiosCall(`api/movies/${movieId}/`)
      res.then((data) => {
        this.movieInfo = data
        this.getGenreList()
      })

    },
    getReviewList() {
      const movieId = this.$route.params.movieId
      const res = axiosCall(`feed/reviews/movie/${movieId}/`)
      res.then((data) => this.reviewList = data)
      res.catch(() => this.reviewList = ['아직 리뷰가 없어요..'])
    },
    makeWatched() {
      const movieId = this.$route.params.movieId
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall(`api/movies/${movieId}/`, 'post', '', headers)
      res.then(() => {
        this.$store.dispatch('requestWatched', '', { root: true })
        this.watched
      })
      res.catch((err) => console.log(err))
    },
    makeWishes() {
      const movieId = this.$route.params.movieId
      const headers = { Authorization: `Bearer ${this.$store.state.user.token.access_token}` }
      const res = axiosCall(`api/movies/${movieId}/wishes/`, 'post', '', headers)
      res.then(() => {
        res.then(this.$store.dispatch('requestWishes', '', { root: true }))
        this.wishes
      })
      res.catch((err) => console.log(err))
    },
    getLogo() {
      const res = axiosCall(`api/provider/${this.$route.params.movieId}`)
      res.then((data) => this.logoList = data.providers)
      res.catch((err) => console.log(err))
    },
    getGenreList() {
      const data = []
      const genres = this.$store.state.movie.genreList
      const movieInfoGenre = []
      for (const genre of this.movieInfo.genres) {
        movieInfoGenre.push(genre)
      }

      for (const genre of genres) {
        if (movieInfoGenre.indexOf(genre.id) != -1) {
          data.push(genre.name)
        }
      }

      this.genreList = data
    }
  },
  computed: {
    imgURL() {
      return `https://image.tmdb.org/t/p/w300${this.movieInfo.poster_path}`
    },
    watched() {
      if (this.$store.getters["isLogin"]) {
        for (const movie of this.$store.state.user.watchedMovies) {
          if (movie.title === this.movieInfo.title) {
            return true
          }
        }
        return false
      }
      return false
    },
    wishes() {
      if (this.$store.getters["isLogin"]) {
        for (const movie of this.$store.state.user.wishesMovies) {
          if (movie.title === this.movieInfo.title) {
            return true
          }
        }
        return false
      }
      return false
    },
  },
  created() {
    this.getMovieDetail()
    this.getReviewList()
    this.getLogo()
  },
}
</script>

<style>
.img-div {
  width: 100vw;
  height: 20vw;
  background-size: cover;
  background-repeat: no-repeat;
}

.checked {
  filter: opacity(0.2) !important;
}

.detail {
  margin: 50px
}

#movie-detail-col * {
  color: white;
  margin: 20px 10px;
}
</style>