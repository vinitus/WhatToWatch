<template>
  <div style="display:flex; flex-wrap: wrap;">
    <search-item v-for=" (searchItem, searchIndex) in expression" :key="searchIndex" :searchItem="searchItem">
    </search-item>
    <my-observer @triggerIntersected="loadMore"></my-observer>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';
import SearchItem from '../components/SearchItem.vue';
import MyObserver from '../components/MyObserver.vue';

export default {
  components: { SearchItem, MyObserver },
  name: 'SearchView',
  data() {
    return {
      searchDataArr: [],
      expression: [],
      index: false,
    }
  },
  methods: {
    loadData() {
      const res = axiosCall(`api/movies/search/${this.$route.params.keyword}/`, 'get')
      res.then((data) => {
        this.searchDataArr = data
        if (data.length > 21) {
          this.expression = this.searchDataArr.slice(0, 21)
          this.index = 21
        } else {
          this.expression = data
          this.index = false
        }
      })
    },
    loadMore() {
      if (this.index) {
        if (this.searchDataArr.length - this.index > 21) {
          const fetchArr = this.searchDataArr.slice(this.index, this.index + 21)
          console.log(fetchArr)
          this.expression.push(...fetchArr)
          this.index += 21
        } else {
          const fetchArr = this.searchDataArr.slice(this.index)
          console.log(fetchArr)
          this.expression.push(...fetchArr)
          this.index = false
        }
      } else {
        return
      }
    }
  },
  mounted() {
    this.loadData()
  },
  watch: {
    '$route'() {
      this.loadData()
    }
  },
}

</script>

<style>

</style>