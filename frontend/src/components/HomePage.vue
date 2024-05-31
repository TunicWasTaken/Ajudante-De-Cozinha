<template>
  <div class="container">
    <h1>Populares</h1>
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
    <h1>Novidades</h1>
    <div class="new-container">
      <div class="new-cards-container">
        <router-link
          class="new-card"
          v-for="recipe in newest"
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
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const top5 = ref([]);
const newest = ref([]);

const difficulties = ref([
  { text: "Fácil", value: "F", color: "green" },
  { text: "Médio", value: "M", color: "#FFBF00" },
  { text: "Díficil", value: "D", color: "red" },
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
  padding: 50px !important;
}

.container .popular-container {
  height: 65%;
}

.container h1 {
  justify-content: left;
  color: #131313;
  font-weight: 400;
  border-bottom: 1px solid #131313;
  padding: 10px 0;
  text-align: left;
}

.popular-cards-container {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 50px;
}

.popular-card {
  margin-top: 75px;
  height: 250%;
  width: 250px;
  padding: 0px 20px;
  text-decoration: none;
  transform: scale(1.2);
  transition: transform 0.2s ease-in-out;
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
  width: 200px;
  padding: 0px 5px;
  text-decoration: none;
  transition: transform 0.2s ease-in-out;
}

.new-card:hover {
  transform: scale(1.1);
}
</style>
