<template>
  <b-col>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: movieItem.movie_id } }">
      <b-card :title=movieItem.title :img-src="`https://image.tmdb.org/t/p/w300/${movieItem.poster_path}`"
        img-alt="Image" img-top tag="article" class="mb-2">
        <div v-if="movieItem.year">
          {{ movieItem.year }} · {{ movieItem.country }}
        </div>
      </b-card>
    </router-link>
  </b-col>
</template>

<script>
export default {
  name: 'MovieItem',
  props: {
    movieItem: Object
  },
}
</script>

<style>
a {
  text-decoration: none;
  color: black;
}

.card {
  min-width: 300px !important;
  height: 550px !important;
  object-fit: cover;
  color: black
}
</style>