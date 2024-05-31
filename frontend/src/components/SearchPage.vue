<template>
  <div class="container">
    <div class="cards-container">
      <router-link
        class="card"
        v-for="recipe in recipeList"
        :key="recipe._id"
        :to="'/recipes/' + recipe._id"
      >
        <div class="img-container">
          <img class="img" :src="recipe.img" />
        </div>
        <div class="info-container">
          <h3 class="title">{{ recipe.name }}</h3>
          <p>{{ recipe.description }}</p>
          <div class="info-container--footer">
            <h4
              class="diff"
              :style="{
                backgroundColor: difficulties.filter(
                  (diff) => diff.value === recipe.difficulty
                )[0].color,
              }"
            >
              {{
                difficulties.filter(
                  (diff) => diff.value === recipe.difficulty
                )[0].text
              }}
            </h4>
            <h4 class="time">
              {{ Math.floor(recipe.time / 60 / 60) }} Hr
              {{ recipe.time / 60 - Math.floor(recipe.time / 60 / 60) * 60 }}
              Min
            </h4>
          </div>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useRoute } from "vue-router";
import { ref } from "vue";
import axios from "axios";

const route = useRoute();
const recipeList = ref([]);
const difficulties = ref([
  { text: "Fácil", value: "F", color: "green" },
  { text: "Médio", value: "M", color: "#FFBF00" },
  { text: "Díficil", value: "D", color: "red" },
]);

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
