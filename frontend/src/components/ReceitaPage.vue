<template>
  <div>
    {{ recipe }}
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";

const route = useRoute();
const router = useRouter();
const recipe = ref({});
const recipe_id = route.params.id;

axios
  .get("http://localhost:5000/api/recipe/" + recipe_id, {
    withCredentials: true,
  })
  .then((res) => {
    recipe.value = res.data.recipe;
    document.title = res.data.recipe.name;
  })
  .catch((err) => {
    console.log(err);
    router.push("/");
  });
</script>

<style>
#Title {
  color: black;
  font-size: 300%;
  text-align: center;
  position: relative;
  top: 50px;
}
#Subtitle {
  color: black;
  font-size: 140%;
  text-align: center;
  position: relative;
  top: 50px;
  margin-left: 50px;
  margin-right: 50px;
}
#ImagemReceita {
  display: block;
  margin-left: auto;
  margin-right: auto;
  width: 3%;
  position: relative;
  top: 70px;
}
#Description {
  margin-top: 300px;
  margin-left: 40px;
}
.DescriptionText {
  margin-top: 10px;
  margin-left: 80px;
  font-size: 20px;
  border: 2px solid black;
  border-radius: 10px;
  padding: 20px;
  width: 1700px;
  text-align: left;
}
#IngredientesTitle {
  margin-top: 50px;
  margin-left: 40px;
}
#body {
  font-family: Arial, sans-serif;
  margin: 0;
  padding: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f5f5f5;
}

.container {
  text-align: center;
  background: white;
  padding: 100px;
  border-radius: 8px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
}

h1 {
  font-size: 2.5em;
  margin-bottom: 20px;
}

.info {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin-top: 100px;
}

.info-item {
  display: flex;
  align-items: center;
  font-size: 30px;
}

.info-item .icon {
  margin-right: 5px;
}

#imagem {
  display: block;
  margin-left: auto;
  margin-right: auto;
  margin-top: -200px;
  width: 50%;
  height: 200px;
  border-radius: 8px;
}
</style>
