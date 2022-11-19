<template>
  <div>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: searchItem.id } }">
      {{ searchItem.title }}

    </router-link>
  </div>
</template>

<script>
export default {
  name: 'SearchItem',
  props: {
    searchItem: Object
  }
}
</script>

<style>

</style>