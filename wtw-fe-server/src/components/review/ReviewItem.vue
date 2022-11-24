<template>
  <div style="color:white; margin-top:50px; display: flex; align-items: center;">
    <b-form-rating v-model="score" variant="warning" class="" style="background-color:black; border:none; width:200px">
    </b-form-rating>
    <div style="">
      {{ review.content }}
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewItem',
  props: {
    review: Object
  },
  computed: {
    score() {
      return this.review.score / 2
    }
  }
}

</script>

<style>

</style>