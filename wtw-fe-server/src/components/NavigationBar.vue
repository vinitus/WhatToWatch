<!-- <template>
  <nav>
    <input type="text" @keyup.enter="navInputSubmit"> |
    <router-link v-if="!token" :to="{ name: 'Login' }">로그인</router-link> |
    <router-link v-if="!token" :to="{ name: 'SignUp' }">회원가입</router-link>
    <a v-if="token" @click.prevent="logout">로그아웃</a>
  </nav>
</template> -->


<!-- <b-nav-form @submit.stop.prevent="navInputSubmit">
      <b-form-input aria-label="Input" class="mr-1 "></b-form-input>
      <b-button type="submit">Ok</b-button>
    </b-nav-form> -->

<template>
  <div>
    <!-- <b-navbar toggleable="lg"> -->
    <nav style="display:flex; align-items:center;">
      <router-link class="text-danger" :to="{ name: 'Home' }">
        <img :src="logoURL" id="logo">
      </router-link>
      <router-link class="text-danger" :to="{ name: 'Movies' }">영화</router-link>
      <router-link class="text-danger" :to="{ name: 'Series' }">시리즈</router-link>

      <!-- Right aligned nav items -->
      <form @submit.prevent="navInputSubmit" @focusin="makeDivShow" @focusout="makeDivHide">
        <input @input="autoComplete" size="sm" class="mr-sm-2" placeholder="Search" id="search-bar">
        <button size="sm" class="my-2 my-sm-0 mr-2" type="submit">z</button>
        <div :class="{ 'search-bar-div': divHide }"
          style="width:250px; background-color: white; position:absolute; z-index: 10;">
          <ul style="list-style:none; padding:0px;">
            <li v-for="(autoCompleteEx, searchBarIndex) in autoCompleteArr" :key="searchBarIndex">
              {{
              autoCompleteEx
              }}
            </li>
          </ul>
        </div>
      </form>

      <!-- <b-nav-item-dropdown text="Lang" right>
            <b-dropdown-item href="#">EN</b-dropdown-item>
            <b-dropdown-item href="#">ES</b-dropdown-item>
            <b-dropdown-item href="#">RU</b-dropdown-item>
            <b-dropdown-item href="#">FA</b-dropdown-item>
          </b-nav-item-dropdown> -->

      <!-- <b-nav-item-dropdown right> -->
      <!-- Using 'button-content' slot -->
      <!-- <template #button-content>
              <em>User</em>
            </template> -->
      <!-- <b-dropdown-item href="#">Profile</b-dropdown-item> -->
      <!-- <b-dropdown-item href="#">Sign Out</b-dropdown-item> -->
      <!-- </b-nav-item-dropdown> -->
      <div v-if="!token">
        <router-link class="text-danger" :to="{ name: 'Login' }">로그인</router-link>
      </div>
      <div v-else>
        <a class="text-danger" @click.prevent="logout">로그아웃</a>
      </div>
      <div v-if="!token">
        <router-link class="text-danger" :to="{ name: 'SignUp' }">회원가입</router-link>
      </div>
      <div v-else>
        <router-link class="text-danger" :to="{ name: 'Profile' }">나</router-link>
      </div>
    </nav>
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
      divHide: true
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
    },
    logout() {
      this.$store.dispatch('logout', '', { root: true })
    },
    autoComplete(event) {
      // console.log(searchBarDiv)
      const query = event.target.value
      if (query.length > 0) {
        const regex = createFuzzyMatcher(query)
        const words = this.movieList
        const result = []
        // console.log(searchBarDiv.classList.contains('deactive'))
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
  height: 40px
}

nav {
  background: black !important;
}

nav * {
  margin: 0px 5px;
}

/* .navbar-nav {
  align-items: center;
} */
#search-bar {
  width: 250px
}

.search-bar-div {
  display: none !important;
}

.deactive {
  display: none;
}
</style>