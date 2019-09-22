<template>
  <div>
    <!-- PART 1: Pass in a "complete" prop here -->
    <Instructions :complete="true"></Instructions>

    <!-- PART 6 -->
    <br/>
    <input v-model="new_show" placeholder="Enter the name of the show"/>
    <button type="button" v-on:click="add_show(new_show)">Add Show</button>
    <br/>

    <!-- PART 4: Modify the Show component to accept all of these props -->
    <Show
      v-for="show in shows"
      :key="show.id"
      :id="show.id"
      :name="show.name"
      :episodes_seen="show.episodes_seen"
    />

  </div>
</template>

<script>
import Instructions from "./Instructions.vue";
import Show from "./Show.vue";

export default {
  components: {
    Instructions,
    Show
  },

  methods: {
    add_show: function add_show(new_show) {this.shows.push({id: this.shows.length + 1, name: new_show, episodes_seen: 0})
}
  },

  data() {
    return {
      shows: [
        { id: 1, name: "Game of Thrones", episodes_seen: 0 },
        { id: 2, name: "Naruto", episodes_seen: 220 },
        { id: 3, name: "Black Mirror", episodes_seen: 3 }
      ], 
      new_show: ""
    };
  }
};
</script>

<style>
</style>


