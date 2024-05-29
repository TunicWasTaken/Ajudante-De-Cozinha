<template>
  <div>
    {{ recipeList }}
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { ref } from "vue";
import axios from "axios";

const route = useRoute();
const recipeList = ref([]);

let query = Object.entries(route.query)
  .map((pair) => pair.join("="))
  .join("&");

axios
  .get("http://localhost:5000/api/recipes?" + query)
  .then((res) => {
    recipeList.value = res.data.recipes;
  })
  .catch((err) => {
    console.log(err);
    //router.push("/");
  });
</script>
