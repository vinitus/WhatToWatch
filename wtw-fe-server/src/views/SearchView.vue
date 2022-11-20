<template>
  <div>
    <!-- SEARCH
    <search-item v-for="(searchItem, searchIndex) in searchDataArr" :key="searchIndex" :searchItem="searchItem">
    </search-item> -->
    <b-row v-for="(searchRow, i) in searchRows" :key="i">
      <b-col v-for="(searchItem, j) in searchRow" :key="j">
        <search-item :searchItem="searchItem"></search-item>
      </b-col>
    </b-row>
  </div>
</template>

<script>
import axiosCall from '@/axiosCall/axiosCall';
import SearchItem from '../components/SearchItem.vue';

export default {
  components: { SearchItem },
  name: 'SearchView',
  data() {
    return {
      searchDataArr: []
    }
  },
  methods: {
    loadData() {
      const res = axiosCall(`api/movies/search/${this.$route.params.keyword}/`, 'get')
      res.then((data) => this.searchDataArr = data)
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
  computed: {
    searchRows() {
      return this.searchDataArr.reduce((acc, n, i) => {
        i % 3 ? acc[acc.length - 1].push(n) : acc.push([n])
        return acc
      }, [])
    }
  }
}

</script>

<style>

</style>