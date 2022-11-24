<template>
  <div>
    <b-navbar>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
      <b-collapse id="nav-collapse" is-nav>

        <b-navbar-nav class="align-items-center">

          <b-nav-item>
            <router-link class="text-danger" :to="{ name: 'Home' }">
              <img :src="logoURL" id="logo">
            </router-link>
          </b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-form @submit.prevent="navInputSubmit" @focusin="makeDivShow" @focusout="makeDivHide">
            <b-form-input v-model="searchKeyword" @keyup.up="keyupUp" @keydown.down="keydownDown" @input="autoComplete"
              size="sm" class="mr-sm-2" placeholder="Search" id="search-bar" autocomplete="off">
            </b-form-input>
            <b-button size="sm" class="my-2 my-sm-0 mr-2" type="submit">
              <b-icon icon="search"></b-icon>
            </b-button>
            <div :class="{ 'search-bar-div': divHide }" style="font-size:0.875rem; width:250px;
                    background-color: white;
                    position:absolute;
                    z-index: 10;
                    top: 47px;
                    right: 211px;">
              <ul style="list-style:none; padding:0px;">
                <li v-for="(autoCompleteEx, searchBarIndex) in autoCompleteArr" :key="searchBarIndex">{{ autoCompleteEx
                }}</li>
              </ul>
            </div>
          </b-nav-form>
        </b-navbar-nav>


        <b-navbar-nav class="align-items-center">

          <b-nav-item v-if="!token">
            <router-link class="text-danger" :to="{ name: 'Login' }">로그인</router-link>
          </b-nav-item>

          <b-nav-item v-else>
            <a class="text-danger" @click.prevent="logout">로그아웃</a>
          </b-nav-item>

          <b-nav-item v-if="!token">
            <router-link class="text-danger" :to="{ name: 'SignUp' }">회원가입</router-link>
          </b-nav-item>

          <b-nav-item v-else>
            <router-link class="text-danger" :to="{ name: 'Profile' }">나</router-link>
          </b-nav-item>

        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import createFuzzyMatcher from "@/algorithm/autoComplete.js"

export default {
  name: 'NavigationBar',
  data() {
    return {
      logoURL: require('@/assets/logo.png'),
      autoCompleteArr: [],
      searchBarDiv: 'search-bar-div',
      divHide: true,
      searchKeyword: '',
      autoCompleteIndex: -1,
    }
  },
  methods: {
    navInputSubmit(event) {
      const keyword = event.target.firstChild.value
      if (this.$route.name != 'Search') {
        this.$router.push({ name: 'Search', params: { keyword: keyword } })
      } else {
        if (this.$route.params.keyword != keyword) {
          this.$router.push({ name: 'Search', params: { keyword: keyword } })
        }
      }
      this.searchKeyword = ''
      this.autoCompleteArr = []
      this.divHide = true
    },
    logout() {
      this.$store.dispatch('logout', '', { root: true })
    },
    autoComplete(event) {
      // console.log(searchBarDiv)
      const query = event
      if (query.length > 0) {
        const regex = createFuzzyMatcher(query)
        const words = this.movieList.movie_titles
        const result = []
        for (let i = 0; i < words.length; i++) {
          if (regex.test(words[i].toLowerCase())) result.push(words[i])
          if (result.length === 10) break
        }
        this.autoCompleteArr = result
        this.divHide = false
      } else {
        this.autoCompleteArr = []
        this.divHide = true
      }
    },
    makeDivHide() {
      this.divHide = true
    },
    makeDivShow() {
      if (this.autoCompleteArr.length > 0) {
        this.divHide = false
      }
    },
    keyupUp() {
      this.autoCompleteIndex -= 1
      if ((this.autoCompleteIndex >= 0) && (this.autoCompleteIndex < this.autoCompleteArr.length)) {
        this.searchKeyword = this.autoCompleteArr[this.autoCompleteIndex]
      } else {
        this.autoCompleteIndex += 1
        return
      }
    },
    keydownDown() {
      this.autoCompleteIndex += 1
      if ((this.autoCompleteIndex >= 0) && (this.autoCompleteIndex < this.autoCompleteArr.length)) {
        this.searchKeyword = this.autoCompleteArr[this.autoCompleteIndex]
      } else {
        this.autoCompleteIndex -= 1
        return
      }
    },
  },
  computed: {
    token() {
      return this.$store.state.user.token
    },
    isLogin() {
      return this.$store.getters.isLogin
    },
    movieList() {
      return this.$store.state.movie.movieList
    }
  }
}
</script>

<style>
#logo {
  height: 50px;
}

.nav-item a {
  padding-top: 0px;
  padding-bottom: 0px;
}

nav {
  align-items: center;
  font-size: 20px;
}

nav * {
  margin: 0px 1px;
}

#search-bar {
  width: 250px
}

.search-bar-div {
  display: none !important;
}
</style>