<template>
  <div id="counters">
    <p>Count(s): {{ count }}</p>
    <button v-on:click="count += 1">Add 1</button>
    <button v-on:click="count -= 1">Substract 1</button>
  </div>

</template>

<script>
export default {
  props : ["count"],
  data() {
    return {
      counter: this.count
    };
  }
};
</script>

<style>
</style>

