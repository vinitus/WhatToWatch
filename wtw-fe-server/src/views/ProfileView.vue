<template>
  <div id="profile">
    <div>PROFILE</div>
    <router-link :to="{ name: 'Watched' }">본 컨텐츠</router-link>
  </div>
</template>

<script>
export default {

}
</script>

<style>
#profile * {
  color: white !important;
}
</style>