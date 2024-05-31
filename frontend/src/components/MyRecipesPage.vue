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
import { ref } from "vue";
import axios from "axios";

const recipeList = ref([]);
const difficulties = ref([
  { text: "Fácil", value: "F", color: "green" },
  { text: "Médio", value: "M", color: "#FFBF00" },
  { text: "Díficil", value: "D", color: "red" },
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

.cards-container {
  display: flex;
  gap: 30px;
  width: 100%;
  height: 100%;
}

.card {
  margin-top: 40px;
  width: 350px;
  height: 350px;
  text-decoration: none;
  transition: transform 0.2s ease-in-out;
  box-shadow: 0px 0px 4px 2px rgba(0, 0, 0, 0.25);
  border-radius: 6px;
}

.img-container {
  overflow: hidden;
  border-radius: 5px 5px 0px 0px;
  border: unset;
  padding: 3px 3px;
  height: 200px;
  width: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
  border-bottom: 1px solid #ccc;
}

.img-container img {
  transition: all 0.3s;
}

.img-container img:hover {
  transform: scale(1.2);
}

.info-container {
  height: fit-content;
  height: 150px;
  padding: 10px 15px;
  display: block;
  text-align: left;
  border-style: solid;
  border: unset;
  background: #efefef;
  position: relative;
}

.info-container--footer {
  position: absolute;
  bottom: 0px;
  width: 100%;
  padding: 10px;
  left: 0;
  display: flex;
  margin-top: 10px;
  justify-content: space-between;
}

.info-container--footer h4 {
  color: white !important;
  padding: 5px 15px !important;
  border-radius: 15px;
}

.info-container--footer .time {
  background: #333;
}

.info-container p {
  color: #333;
  width: 100%;
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.popular-card:hover {
  transform: scale(1.3);
}

.info-container h3 {
  color: rgb(0, 0, 0);
  font-size: 24px;
  font-weight: 500;
  margin-bottom: 5px;
  text-transform: capitalize;
  padding: 0;
}

.info-container h4 {
  color: rgb(0, 0, 0);
  font-weight: 400;
  font-size: 15px;
  padding-bottom: 5px;
}
</style>
