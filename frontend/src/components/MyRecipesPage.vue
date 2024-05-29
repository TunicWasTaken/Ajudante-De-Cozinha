<template>
  <div>
    <div class="recipe-container">
      <router-link
        class="recipe-card"
        v-for="recipe in recipeList"
        :key="recipe._id"
        :to="'/recipes/' + recipe._id"
      >
        <img id="recipe-img" :src="recipe.img" />
        <h2>
          <b>{{ recipe.name }}</b>
        </h2>
      </router-link>
      <router-link class="card" to="/create-recipe">
        <img id="plus" src="../assets/plus.png" width="90%" />
        <h4><b>Nova Receita</b></h4>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const recipeList = ref([]);

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
#plus {
  padding: 5%;
  width: 200px;
}
.cards-container {
  display: flex;
  flex-wrap: wrap;
  gap: 110px;
}
.card {
  box-sizing: border-box;
  width: 370px;
  height: 454px;
  background: rgba(217, 217, 217, 0.58);
  border: 1px solid white;
  box-shadow: 12px 17px 51px rgba(0, 0, 0, 0.22);
  backdrop-filter: blur(6px);
  border-radius: 17px;
  text-align: center;
  cursor: pointer;
  transition: all 0.5s;
  display: flex;
  align-items: center;
  justify-content: center;
  user-select: none;
  font-weight: bolder;
  color: black;
  position: relative;
  left: 50px;
  top: 50px;
}

.card:hover {
  border: 1px solid black;
  transform: scale(1.05);
}

.card:active {
  transform: scale(0.95) rotateZ(1.7deg);
}

.container {
  padding: 2px 16px;
}
</style>
