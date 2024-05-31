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
            ><input
              type="checkbox"
              name="tipo-prato"
              value="C"
              v-model="selectedType"
            />
            Carne</label
          >
          <label
            ><input
              type="checkbox"
              name="tipo-prato"
              value="P"
              v-model="selectedType"
            />
            Peixe</label
          >
          <label
            ><input
              type="checkbox"
              name="tipo-prato"
              value="V"
              v-model="selectedType"
            />
            Vegetariano</label
          >
        </div>
        <div class="filter-category">
          <h3>Duração</h3>
          <input
            type="time"
            name="duracao"
            value="00:00"
            v-model="selectedDuration"
          />
        </div>
        <div class="filter-category">
          <h3>Dificuldade</h3>
          <label
            ><input
              type="checkbox"
              name="dificuldade"
              value="F"
              v-model="selectedDifficulty"
            />
            Fácil</label
          >
          <label
            ><input
              type="checkbox"
              name="dificuldade"
              value="M"
              v-model="selectedDifficulty"
            />
            Médio</label
          >
          <label
            ><input
              type="checkbox"
              name="dificuldade"
              value="D"
              v-model="selectedDifficulty"
            />
            Difícil</label
          >
        </div>
      </div>
    </div>
    <div class="container">
      <div class="cards-container">
        <router-link
          class="card"
          v-for="recipe in filteredRecipes"
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
import { ref, computed } from "vue";
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

const selectedDifficulty = ref([]);
const selectedDuration = ref(null);
const selectedType = ref([]);

const filteredRecipes = computed(() => {
  let filtered = recipeList.value;

  if (selectedDifficulty.value.length > 0) {
    filtered = filtered.filter((recipe) =>
      selectedDifficulty.value.includes(recipe.difficulty)
    );
  }

  if (selectedDuration.value) {
    let dur =
      selectedDuration.value.split(":")[0] * 60 * 60 +
      selectedDuration.value.split(":")[1] * 60;
    filtered = filtered.filter((recipe) => recipe.time <= dur);
  }

  if (selectedType.value.length > 0) {
    filtered = filtered.filter((recipe) =>
      selectedType.value.includes(recipe.type)
    );
  }

  return filtered;
});

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

.filter-category h3 {
  padding: 5px 5px;
}

.filter-category label {
  padding-right: 5px;
  padding-left: 5px;
}
</style>
