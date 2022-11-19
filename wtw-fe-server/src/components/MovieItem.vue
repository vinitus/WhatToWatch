<template>
  <div>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: movieItem.movie_id } }">
      {{ movieItem.title }}
    </router-link>
  </div>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movieItem: Object
  }
}
</script>

<style>

</style>