<template>
  <div>
    <div class="recipe-container">
      <div class="recipe-img" v-if="!started && !done">
        <img :src="recipe.img" />
      </div>
      <div class="recipe-content" v-if="!started && !done">
        <h1 class="name">{{ recipe.name }}</h1>
        <div class="details">
          <div class="time">
            <h3 id="hours" v-if="Math.floor(recipe.time / 60 / 60) > 0">
              {{ Math.floor(recipe.time / 60 / 60) }} Hr
            </h3>
            <h3 id="minutes">
              {{ recipe.time / 60 - Math.floor(recipe.time / 60 / 60) * 60 }}
              Min
            </h3>
          </div>
          <h3 class="type">
            {{
              types.filter((type) => type.value === recipe.type)?.[0]?.text ??
              ""
            }}
          </h3>
          <h3
            class="diff"
            :style="{
              background:
                difficulties.filter(
                  (diff) => diff.value === recipe.difficulty
                )?.[0]?.color ?? '',
            }"
          >
            {{
              difficulties.filter(
                (diff) => diff.value === recipe.difficulty
              )?.[0]?.text ?? ""
            }}
          </h3>
        </div>
        <h2 class="description">{{ recipe.description }}</h2>
        <h1 class="ingredients-title">Ingredientes</h1>
        <div class="ingredients-list">
          <p
            class="ingredient"
            v-for="ingredient in recipe.ingredients"
            :key="ingredient.name"
          >
            {{ ingredient.name }}: {{ ingredient.quantity }}
            {{
              measures.filter(
                (measure) => measure.value === ingredient.measure
              )[0].text
            }}
          </p>
        </div>
        <button
          class="delete-button"
          v-on:click="deleteRecipe()"
          v-if="
            authStore.user?.role == 'admin' ||
            authStore.user?.name == recipe.user
          "
        >
          Eliminar
        </button>
        <button class="helper-button" v-on:click="start()">
          Iniciar Ajudante
        </button>
      </div>
      <div class="step-container" v-if="started">
        <div class="step">
          {{ recipe.steps[step_index]?.description ?? "" }}
        </div>
        <button v-if="shownTime != 0" id="timer" @click="toggleTimer">
          {{ playing ? "⏸️" : "▶️" }}{{ secondsAsString(shownTime) }}
        </button>
        <button class="next-step" @click="next_step()">Próximo Passo</button>
        <button class="previous-step" @click="previous_step()">
          Passo Anterior
        </button>
      </div>
      <div class="done-container" v-if="done">
        Receita acabada e bom apetite!

        <button
          @click="
            started = false;
            done = false;
            step_index = 0;
          "
        >
          Voltar
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRoute, useRouter } from "vue-router";
import axios from "axios";
import { useAuthStore } from "@/stores/auth";

const route = useRoute();
const router = useRouter();
const authStore = useAuthStore();
const recipe = ref({});
const started = ref(false);
const step_index = ref(0);
const done = ref(false);
const recipe_id = route.params.id;

const types = ref([
  { text: "Carne", value: "C" },
  { text: "Peixe", value: "P" },
  { text: "Vegetariana", value: "V" },
]);

const difficulties = ref([
  { text: "Fácil", value: "F", color: "green" },
  { text: "Médio", value: "M", color: "#FFBF00" },
  { text: "Díficil", value: "D", color: "red" },
]);

const measures = ref([
  { text: "Unidades", value: "U" },
  { text: "Doses", value: "D" },
  { text: "Chávenas", value: "C" },
  { text: "Colheres De Sopa", value: "CDS" },
  { text: "Colheres De Chá", value: "CDC" },
  { text: "mg", value: "MG" },
  { text: "ml", value: "ML" },
  { text: "g", value: "G" },
]);

const shownTime = ref(0);
const playing = ref(false);

function start() {
  started.value = true;
}

function next_step() {
  if (step_index.value < recipe.value.steps.length - 1) {
    step_index.value++;
    shownTime.value = recipe.value.steps[step_index.value].timed
      ? recipe.value.steps[step_index.value].time
      : 0;
  } else {
    started.value = false;
    done.value = true;
  }
}

function previous_step() {
  if (step_index.value == 0) {
    started.value = false;
  } else {
    step_index.value--;
    shownTime.value = recipe.value.steps[step_index.value].timed
      ? recipe.value.steps[step_index.value].time
      : 0;
  }
}

let timerInterval;

function toggleTimer() {
  playing.value = !playing.value;

  if (!playing.value) {
    clearInterval(timerInterval);
  } else {
    timerInterval = setInterval(renderTimer, 1000);
  }
}

function renderTimer() {
  if (shownTime.value - 1 == 0) {
    clearInterval(timerInterval);
    playing.value = false;
    return;
  }

  shownTime.value -= 1;
}

function secondsAsString(seconds) {
  return `${Math.floor(seconds / 60)}:${Math.floor(seconds % 60)}`;
}

function deleteRecipe() {
  axios
    .delete("http://localhost:5000/api/recipe/delete/" + recipe_id, {
      withCredentials: true,
    })
    .then(() => {
      router.push("/");
    })
    .catch((err) => {
      console.log(err);
    });
}

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
.recipe-container {
  display: flex;
  padding: 50px;
  flex-flow: column;
}

.recipe-img {
  position: absolute;
  top: 150px;
  right: 150px;
  max-width: 300px;
  border-radius: 10px 0px 0px 10px;
  border: 1px solid #ccc;
  border-radius: 6px;
  box-shadow: 0 0 2px 0px rgba(0, 0, 0, 0.25);
}

.recipe-img img {
  max-height: 100%;
  max-width: 100%;
}

.recipe-content {
  border-radius: 0px 10px 10px 0px;
}

.recipe-content .name {
  color: #131313;
  font-size: 28px;
  font-weight: 500;
  text-transform: capitalize;
}

.recipe-content .details {
  display: flex;
  font-weight: 400;
  gap: 10px;
  font-size: 14px;
  margin: 10px 0;
}

.details .time {
  background: #131313 !important;
  color: white;
  font-weight: 400;
  padding: 5px 15px;
  border-radius: 15px;
  display: flex;
  gap: 10px;
}

.details .type {
  background: rgba(20, 219, 111);
  padding: 5px 15px;
  border-radius: 15px;
  color: #131313;
  font-weight: 400;
}

.details .diff {
  color: white;
  padding: 5px 15px;
  border-radius: 15px;
  font-weight: 400;
}

.recipe-content .description {
  margin: 10px 0;
  color: #333;
  font-weight: 400;
  width: 800px;
  font-size: 16px;
}

.recipe-content .ingredient-list {
  display: flex;
  gap: 10px;
  padding: 5px;
}

.delete-button {
  padding: 10px 25px;
  font-size: 16px;
  color: #131313;
  font-weight: 500;
  border-radius: 6px;
  background: rgb(224, 22, 22);
  position: absolute;
  bottom: 50px;
  left: 50px;
  cursor: pointer;
  border: none;
}

.helper-button {
  padding: 10px 25px;
  font-size: 16px;
  color: #131313;
  font-weight: 500;
  border-radius: 6px;
  background: rgba(20, 219, 111);
  position: absolute;
  bottom: 50px;
  right: 50px;
  animation: wiggle 3s infinite ease-in-out;
  cursor: pointer;
  border: none;
}

.ingredients-title {
  color: #131313;
  font-size: 28px;
  font-weight: 500;
  border-bottom: 1px solid #131313;
  padding: 5px 0;
  margin-bottom: 10px;
  width: fit-content;
}

.ingredient {
  font-size: 16px;
  color: black !important;
}

.step-container {
  width: 100%;
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column;
}

#timer,
.done-container button,
.next-step {
  margin-top: 10px;
  background: rgba(20, 209, 111);
  color: white;
  right: 50px;
  padding: 10px 25px;
  border-radius: 6px;
  border: none;
  font-size: 16px;
  cursor: pointer;
}

.previous-step {
  margin-top: 10px;
  background: rgba(20, 209, 111);
  color: white;
  left: 50px;
  padding: 10px 25px;
  border-radius: 6px;
  border: none;
  font-size: 16px;
  cursor: pointer;
}

#timer {
  padding: 10px !important;
  background: #131313;
}

.step {
  font-size: 32px;
  color: #131313;
}

.done-container {
  width: 100%;
  height: 80vh;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column;
  font-size: 28px;
  color: #131313;
}

@keyframes wiggle {
  0% {
    transform: rotate(5deg);
  }
  20% {
    transform: rotate(-5deg);
  }
  30% {
    transform: rotate(0);
  }
  100% {
    transform: rotate(0);
  }
}
</style>
