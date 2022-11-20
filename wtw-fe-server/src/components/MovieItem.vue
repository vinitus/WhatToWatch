<template>
  <div>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: movieItem.movie_id } }">
      <b-card :title="movieItem.title" :img-src="`https://image.tmdb.org/t/p/w300/${movieItem.poster_path}`"
        img-alt="Image" img-top tag="article" style="max-width: 20rem;" class="mb-2">
      </b-card>
    </router-link>
    <!-- <router-link :to="{ name: 'MovieDetail', params: { movieId: movieItem.movie_id } }">
      {{ movieItem.title }} -->
    <!-- <img :src="`https://image.tmdb.org/t/p/w300/${movieItem.poster_path}`" alt=""> -->
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
a {
  text-decoration: none;
  color: black;
}
</style>