<template>
  <div>
    {{ movieItem.title }}
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