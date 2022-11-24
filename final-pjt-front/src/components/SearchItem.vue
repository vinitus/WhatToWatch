<template>
  <div id="search-item" style="margin:20px auto;">
    <router-link :to="{ name: 'MovieDetail', params: { movieId: searchItem.id } }">
      <b-card no-body class="overflow-hidden search-card"
        style="width: 200px !important; min-width: 200px !important; height: auto !important; background-color: black;">
        <b-card-img :src="`https://image.tmdb.org/t/p/w300/${searchItem.poster_path}`" alt="Image" class="rounded-0"
          style="width:200px; height:300px;">
        </b-card-img>
        <b-card-body style="font-size:1rem !important; width:200px; color: white; text-align: center;">{{
            searchItem.title
        }}
        </b-card-body>
        <!-- <b-card-body style="font-size:1rem !important; width:150px" :title="searchItem.title">{{ searchItem.title }}
        </b-card-body> -->
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
/*#search-item a {
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
}*/
</style>