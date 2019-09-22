<template>
  <!-- PART 4: Add your code here -->
  <div>
    <p>{{name}}</p>
    <!-- Set count to be the number of episodes seen -->
    <Counter :count=episodes_seen></Counter>
    <br/>
  </div>
</template>

<script>
// PART 4: Add your code here
import Counter from "./Counter.vue";
export default {
  props : ['id', 'name', 'episodes_seen'],

  components: {
    Counter
  }
  };
</script>

<style>
</style>
