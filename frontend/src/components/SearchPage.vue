<template>
  <div>
    <div :class="['sidebar', { 'sidebar-hidden': !isSidebarVisible }]">
      <button class="toggle-button" @click="toggleSidebar">
        <span v-if="isSidebarVisible">←</span>
        <span v-else>→</span>
      </button>
      <div v-if="isSidebarVisible">
        <div class="filter-category">
          <h3>Tipo de Prato</h3>
          <label
            ><input type="checkbox" name="tipo-prato" value="Carne" />
            Carne</label
          >
          <label
            ><input type="checkbox" name="tipo-prato" value="Peixe" />
            Peixe</label
          >
          <label
            ><input type="checkbox" name="tipo-prato" value="Vegetariano" />
            Vegetariano</label
          >
        </div>
        <div class="filter-category">
          <h3>Duração</h3>
          <label
            ><input type="checkbox" name="duracao" value="<60min" />
            &lt;60min</label
          >
          <label
            ><input type="checkbox" name="duracao" value="1h-6h" /> Entre 1h e
            6h</label
          >
          <label
            ><input type="checkbox" name="duracao" value=">6h" /> &gt; 6h</label
          >
        </div>
        <div class="filter-category">
          <h3>Calorias</h3>
          <label
            ><input type="checkbox" name="calorias" value="<600kcal" /> &lt;600
            kcal</label
          >
          <label
            ><input type="checkbox" name="calorias" value="600-1200kcal" />
            Entre 600 e 1200kcal</label
          >
          <label
            ><input type="checkbox" name="calorias" value=">1200kcal" />
            &gt;1200 kcal</label
          >
        </div>
        <div class="filter-category">
          <h3>Dificuldade</h3>
          <label
            ><input type="checkbox" name="dificuldade" value="Fácil" />
            Fácil</label
          >
          <label
            ><input type="checkbox" name="dificuldade" value="Médio" />
            Médio</label
          >
          <label
            ><input type="checkbox" name="dificuldade" value="Difícil" />
            Difícil</label
          >
        </div>
        <div class="filter-category">
          <h3>Tipo de Sabor</h3>
          <label
            ><input type="checkbox" name="sabor" value="Picante" />
            Picante</label
          >
          <label
            ><input type="checkbox" name="sabor" value="Azedo" /> Azedo</label
          >
          <label
            ><input type="checkbox" name="sabor" value="Doce" /> Doce</label
          >
          <label
            ><input type="checkbox" name="sabor" value="Salgado" />
            Salgado</label
          >
        </div>
        <div class="filter-category">
          <h3>Outros</h3>
          <label
            ><input type="checkbox" name="outros" value="Sem gluten" /> Sem
            gluten</label
          >
          <label
            ><input type="checkbox" name="outros" value="Sem lactose" /> Sem
            lactose</label
          >
          <label
            ><input type="checkbox" name="outros" value="Sem frutos secos" />
            Sem frutos secos</label
          >
        </div>
      </div>
    </div>
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
const isSidebarVisible = ref(false);

const toggleSidebar = () => {
  isSidebarVisible.value = !isSidebarVisible.value;
};

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

<style>
.sidebar {
  float: left;
  background-color: #f4f4f4;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  position: relative;
}
.toggle-button {
  position: absolute;
  top: 10px;
  right: -30px;
  background-color: #04bb78;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
}
</style>
