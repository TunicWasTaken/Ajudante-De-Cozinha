<template>
  <div>
    <div class="logo">
      <router-link to="/">
        <img src="../assets/logo.png" height="45" />
      </router-link>
    </div>
    <div class="form-container">
      <form class="recipe-form" @submit.prevent="submitRecipe()">
        <input
          id="recipe-name"
          type="text"
          v-model="recipeName"
          placeholder="Nome da Receita"
          required
        />
        <input
          id="description"
          type="text"
          v-model="description"
          placeholder="Descrição do Prato"
          required
        />
        <select id="type" v-model="type" required>
          <option disabled value="">Por Favor Selecione Uma</option>
          <option
            v-for="foodType in types"
            :key="foodType.value"
            :value="foodType.value"
          >
            {{ foodType.text }}
          </option>
        </select>
        <input id="total-time" type="time" v-model="totalTime" required />
        <select id="difficulty" v-model="difficulty" required>
          <option disabled value="">Por Favor Selecione Uma</option>
          <option
            v-for="diff in difficulties"
            :key="diff.value"
            :value="diff.value"
          >
            {{ diff.text }}
          </option>
        </select>
        <select id="portion" v-model="portion" required>
          <option disabled value="0">Por Favor Selecione Uma</option>
          <option v-for="n in 12" :key="n" :value="n">{{ n }}</option>
        </select>
        <div class="ingredient-container">
          <span class="ingredient-error" v-if="error === 1"
            >É Necessário Adicionar Ingredientes</span
          >
          <form class="ingredient-form" @submit.prevent="addIngredient()">
            <input
              id="ingredient-name"
              type="text"
              v-model="ingredient.name"
              placeholder="Ingrediente"
              required
            />
            <input
              id="ingredient-quantity"
              type="number"
              v-model="ingredient.quantity"
              min="1"
              placeholder="Quantidade"
              required
            />
            <select
              id="ingredient-measure"
              v-model="ingredient.measure"
              required
            >
              <option disabled value="">Por Favor Selecione Uma</option>
              <option
                v-for="measure in measures"
                :key="measure.value"
                :value="measure.value"
              >
                {{ measure.text }}
              </option>
            </select>
            <button>Adicionar Ingrediente</button>
          </form>
          <div
            class="display-ingredients"
            v-for="(curr_ingredient, index) in ingredientList"
            :key="index"
          >
            {{
              curr_ingredient.name.length > 20
                ? curr_ingredient.name.slice(0, 20) + "..."
                : curr_ingredient.name
            }}
            :
            {{ curr_ingredient.quantity }}
            {{
              measures.find(
                (measure) => measure.value === curr_ingredient.measure
              ).text
            }}
          </div>
        </div>
        <div class="steps-container">
          <span class="ingredient-error" v-if="error === 2"
            >É Necessário Adicionar Passos</span
          >
          <form class="steps-form" @submit.prevent="addStep()">
            <input
              id="step-description"
              type="text"
              v-model="step.description"
              placeholder="Descrição do Passo"
              required
            />
            <input id="step-isTimed" type="checkbox" v-model="step.timed" />
            <label for="step-isTimed">Tem Duração?</label>
            <input
              id="step-time"
              type="time"
              v-if="step.timed"
              v-model="step.time"
              required
            />
            <button>Adicionar Passo</button>
          </form>
          <div
            class="display-steps"
            v-for="(curr_step, index) in stepList"
            :key="index"
          >
            Passo {{ index + 1 }} :
            {{
              curr_step.description.length > 20
                ? curr_step.description.slice(0, 20) + "..."
                : curr_step.description
            }}
            {{ curr_step.time != "00:00" ? curr_step.time : "" }}
          </div>
        </div>
        <div class="add-img-container">
          <span class="add-image">Adicionar Imagem de Capa:</span>
          <input
            id="image-input"
            type="file"
            name="file"
            accept="image/png, image/jpeg"
            @change="handleFileChange"
            required
          />
          <div class="display-img" v-if="img">
            <img class="preview" :src="img" />
          </div>
        </div>
        <button>Adicionar Receita</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();

const types = ref([
  { text: "Carne", value: "C" },
  { text: "Peixe", value: "P" },
  { text: "Vegan", value: "V" },
]);

const difficulties = ref([
  { text: "Fácil", value: "F" },
  { text: "Médio", value: "M" },
  { text: "Díficil", value: "D" },
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

const recipeName = ref("");
const description = ref("");
const type = ref("");
const totalTime = ref("");
const difficulty = ref("");
const portion = ref(0);
const img = ref("");
const error = ref(0);

const ingredient = ref({
  name: "",
  quantity: 0,
  measure: "",
});

const step = ref({
  description: "",
  timed: false,
  time: "00:00",
});

const ingredientList = ref([]);
const stepList = ref([]);

function addIngredient() {
  ingredientList.value.push(ingredient.value);
  ingredient.value = {
    name: "",
    quantity: 0,
    measure: "",
  };
  error.value = 0;
}

function addStep() {
  stepList.value.push(step.value);
  step.value = {
    description: "",
    timed: false,
    time: "00:00",
  };
  error.value = 0;
}

function handleFileChange(event) {
  let input = event.target.files[0];
  let reader = new FileReader();
  reader.readAsDataURL(input);
  reader.onload = function () {
    img.value = reader.result;
  };
  reader.onerror = function (error) {
    console.log("Error: ", error);
  };
}

async function submitRecipe() {
  if (ingredientList.value.length == 0) {
    error.value = 1;
  } else if (stepList.value.length == 0) {
    error.value = 2;
  }

  const recipe = {
    user: authStore.user.name,
    name: recipeName.value,
    description: description.value,
    type: type.value,
    time: totalTime.value,
    difficulty: difficulty.value,
    portion: portion.value,
    img: img.value,
    ingredients: ingredientList.value,
    steps: stepList.value,
  };

  await authStore
    .createRecipe(recipe)
    .then(() => {
      router.push("/");
    })
    .catch((err) => {
      console.log(err);
    });
}
</script>

<style></style>
