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
          <h4 class="diff">
            {{
              difficulties.filter((diff) => diff.value === recipe.difficulty)[0]
                .text
            }}
          </h4>
          <h4 class="time">
            {{ Math.floor(recipe.time / 60 / 60) }} Hr
            {{ recipe.time / 60 - Math.floor(recipe.time / 60 / 60) * 60 }}
            Min
          </h4>
        </div>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const recipeList = ref([]);
const difficulties = ref([
  { text: "Fácil", value: "F" },
  { text: "Médio", value: "M" },
  { text: "Díficil", value: "D" },
]);

axios
  .get("http://localhost:5000/api/recipe", { withCredentials: true })
  .then((res) => {
    recipeList.value = res.data.recipes;
  })
  .catch((err) => {
    console.log(err);
  });
</script>

<style>
.container {
  display: flex;
  justify-content: center;
  height: calc(100vh - 59px);
  display: block;
  padding: 15px;
}

.card-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.card {
  margin-top: 75px;
  height: 250%;
  padding: 0px 20px;
  text-decoration: none;
  transform: scale(1.2);
  transition: transform 0.2s ease-in-out;
}

.img-container {
  overflow: auto;
  border-style: solid;
  border-radius: 5px 5px 0px 0px;
  border-color: rgb(0, 0, 0);
  padding: 3px 3px;
  height: 45%;
  width: 100%;
}

.info-container {
  height: 55%;
  padding: 5px 5px;
  display: block;
  text-align: left;
  border-style: solid;
  border-radius: 0px 0px 5px 5px;
  border-color: rgb(0, 0, 0);
  background-color: rgb(86, 253, 170);
}

.popular-card:hover {
  transform: scale(1.3);
}

.info-container h3 {
  color: rgb(0, 0, 0);
  font-size: 25px;
  padding: 5px 0px 15px;
}

.info-container h4 {
  color: rgb(0, 0, 0);
  font-size: 15px;
  padding-bottom: 5px;
}
</style>
