<template>
  <div>
    SEARCH
    <search-item v-for="(searchItem, searchIndex) in searchDataArr" :key="searchIndex" :searchItem="searchItem">
    </search-item>
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
  created() {
    const res = axiosCall(`api/movies/search/${this.$route.params.keyword}/`, 'get')
    res.then((data) => this.searchDataArr = data)
  }
}

</script>

<style>

</style>