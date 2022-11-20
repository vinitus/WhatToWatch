<template>
  <div>
    <router-link :to="{ name: 'MovieDetail', params: { movieId: searchItem.id } }">
      <b-card no-body class="overflow-hidden search-card" style="max-width: 540px;">
        <b-card-img :src="`https://image.tmdb.org/t/p/w300/${searchItem.poster_path}`" alt="Image" class="rounded-0">
        </b-card-img>
        <b-card-body :title="searchItem.title"></b-card-body>
      </b-card>
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
a {
  text-decoration: none;
  color: black !important;
}

.card-img {
  width: 69px !important;
  height: 101px !important;
}

.card-title {
  font-size: 17px !important;
}

.search-card {
  flex-direction: row !important;
}
</style>