<template lang="pug">
    .body_wrapper
        p Sorry, Not Found
</template>

<style>
.body_wrapper {
    text-align: center;
}
</style>

<script>
export default {
  name: 'NotFound',
  mounted() {
      this.$store.commit('deviceStatus', { state:'잘못 왔었어'})
  },
}
</script>
