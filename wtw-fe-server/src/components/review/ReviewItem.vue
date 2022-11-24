<template>
  <div style="color:red;">
    {{ review.content }}
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: Object
  }
}
</script>

<style>

</style>