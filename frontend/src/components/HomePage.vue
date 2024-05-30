<template>
  <div class="container">
    <h1>Populares:</h1>
    <div class="popular-container">
      <div class="popular-cards-container">
        <router-link
          class="popular-card"
          v-for="recipe in top5"
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
        </router-link>
      </div>
    </div>
    <h2>Novidades:</h2>
    <div class="new-container">
      <div class="new-cards-container">
        <router-link
          class="new-card"
          v-for="recipe in newest"
          :key="recipe._id"
          :to="recipe._id"
        >
          <div class="img-container">
            <img class="img" :src="recipe.img" />
          </div>
          <div class="info-container">
            <h3 class="title">{{ recipe.name }}</h3>
            <h4 class="diff">
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
        </router-link>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const top5 = ref([]);
const newest = ref([]);

const difficulties = ref([
  { text: "Fácil", value: "F" },
  { text: "Médio", value: "M" },
  { text: "Díficil", value: "D" },
]);

axios
  .get("http://localhost:5000/api/recipes/homepage")
  .then((res) => {
    top5.value = res.data.top5;
    newest.value = res.data.new;
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

.container .popular-container {
  height: 55%;
}

.container h1 {
  justify-content: left;
  text-align: left;
}

.popular-cards-container {
  display: flex;
  align-items: center;
  justify-content: center;
}

.popular-card {
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

.container .new-container {
  height: 35%;
}

.container h2 {
  justify-content: left;
  text-align: left;
}

.new-cards-container {
  display: flex;
  align-items: center;
  justify-content: center;
  transform: scale(0.75);
}

.new-card {
  height: 150%;
  padding: 0px 5px;
  text-decoration: none;
  transition: transform 0.2s ease-in-out;
}

.new-card:hover {
  transform: scale(1.1);
}
</style>
