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
  data() {
    return {
      score: 0
    }
  },
  created() {
    this.score = this.review.score
  }
}

</script>

<style>

</style>