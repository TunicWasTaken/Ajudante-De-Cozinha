<template>
  <div>
    <div class="topnav">
      <router-link class="Home" to="/">Home</router-link>
      <router-link class="login" to="/login">Login</router-link>
    </div>
    <div class="Form">
      <form>
        <label for="recipename" id="NomeReceita">Nome da Receita:</label><br />
        <input
          v-model="recipeName"
          type="text"
          id="recipename"
          name="recipename"
          placeholder="Nome da Receita.."
        /><br />
      </form>
      <h2>Descrição do prato:</h2>
      <p style="white-space: pre-line"></p>
      <textarea
        v-model="description"
        placeholder="Descrição..."
        id="Description2"
      ></textarea>
      <div id="typeFood">Tipo de prato:</div>
      <select v-model="typePicked" id="FoodTypeOption">
        <option disabled value="">Por favor selecione uma</option>
        <option>Carne</option>
        <option>Peixe</option>
        <option>Vegan</option>
      </select>
      <div>
        <label for="duration" id="Duration">Duração Total:</label>
        <input
          id="durationInput"
          type="time"
          name="appt-time"
          value="00:00"
          required
        />
      </div>
      <div>
        <div id="Difficulty">Dificuldade:</div>
        <select v-model="selectedDifficulty" id="DifficultyOption">
          <option disabled value="">Por favor selecione uma</option>
          <option>Fácil</option>
          <option>Média</option>
          <option>Difícil</option>
        </select>
      </div>
      <div id="Portion">Porção:</div>
      <select v-model="selectedPortion" id="PortionOption">
        <option disabled value="">Por favor selecione uma</option>
        <option>1</option>
        <option>2</option>
        <option>3</option>
        <option>4</option>
        <option>5</option>
        <option>6</option>
        <option>7</option>
        <option>8</option>
        <option>9</option>
        <option>10</option>
        <option>11</option>
        <option>12</option>
      </select>
      <label for="portion"></label>
    </div>
    <form id="receitaForm">
      <label for="Ingredientes" id="IngredientesText"
        >Adicionar Ingrediente e a sua quantidade:</label
      >
      <div class="Ingredientes">
        <input
          v-model="ingrediente"
          id="Ingrediente"
          type="text"
          placeholder="Ingrediente..."
        />
        <input
          v-model="quantidade"
          id="Quantidade"
          type="number"
          min="1"
          placeholder="Quantidade..."
        />
        <select v-model="measurePicked" id="measureOption">
          <option disabled value="">Por favor selecione uma</option>
          <option>Unidades</option>
          <option>Doses</option>
          <option>Chávenas</option>
          <option>Colheres de Sopa</option>
          <option>Colheres de chá</option>
          <option>mg</option>
          <option>ml</option>
          <option>g</option>
        </select>
        <br />
        <button
          type="button"
          id="IngredienteButton"
          v-on:click="AdicionarIngrediente()"
        >
          Adicionar Ingrediente
        </button>
      </div>
      <div
        id="IngredienteText"
        v-for="(ingrediente, index) in ingredientesList"
        :key="index"
      >
        {{
          ingrediente.nome.length > 20
            ? ingrediente.nome.slice(0, 20) + "..."
            : ingrediente.nome
        }}
        :
        {{
          ingrediente.quantidade.length > 10
            ? ingrediente.quantidade.slice(0, 10) + "..."
            : ingrediente.quantidade
        }}
        {{ ingrediente.medida }}
        <img
          src="../assets/5016735.png"
          width="5%"
          v-on:click="RemoverIngrediente(ingrediente.nome)"
        />
      </div>
      <div v-if="erro" class="alert">
        <span
          class="closebtn"
          onclick="this.parentElement.style.display='none';"
          >&times;</span
        >
        Por favor preencha corretamente todos os campos do ingrediente.
      </div>
    </form>
    <span id="Passos">Passos:</span>
    <p style="white-space: pre-line"></p>
    <textarea
      v-model="step"
      placeholder="Descrição do passo..."
      id="AddPassos"
    ></textarea>
    <input
      v-model="stepDuration"
      type="checkbox"
      id="stepDuration"
      @click="stepDurationFunc()"
    />
    <label id="stepDurationText"> Passo tem duração </label>
    <div v-if="stepDuration">
      <label for="duration" id="DurationOfStep">Duração Total:</label>
      <input
        v-model="duration"
        id="durationInputOfStep"
        type="time"
        name="appt-time"
        value="00:00"
        required
      />
    </div>
    <button type="button" id="PassoButton" v-on:click="AdicionarPasso()">
      Adicionar Passo
    </button>
    <div
      id="StepCount"
      v-for="{ step, stepCount, duracao } in steps"
      :key="step.id"
    >
      Passo {{ stepCount }} :
      {{ step.length > 20 ? step.slice(0, 20) + "..." : step }}
      {{ duracao }}
      <img
        src="../assets/5016735.png"
        width="5%"
        v-on:click="RemoverPasso(stepCount)"
      />
    </div>
    <span id="AddImage">Adicionar Imagem de Capa:</span>
    <input
      id="uploadButton"
      type="file"
      name="file"
      accept="image/*"
      @change="onFileChange"
    />
    <div class="image" v-if="file">
      <img :src="imageData[0].url" id="imagem" width="10%" />
    </div>
    <button id="EnviarButton" @click="postarReceita()">
      Adicionar Receita
    </button>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useAuthStore } from "@/stores/auth";
import { useRouter } from "vue-router";

const router = useRouter();
const authStore = useAuthStore();
const receita = ref({
  //Quando clicar em "Adicionar Receita" coloca todos os elementos nesta constante
  // e coloca na base de dados onde cliente_id = id
  cliente: authStore.authUser.name,
  descricao: "",
  tipoDePrato: "",
  duracao: "",
  dificuldade: "",
  porcao: "",
  ingredientes: [],
  passos: [],
  imagem: "",
});

const recipeName = ref("");
const description = ref("");
const typePicked = ref([]);
const selectedDifficulty = ref("");
const selectedPortion = ref("");
const ingrediente = ref("");
const quantidade = ref("");
const ingredientesList = ref([]);
const step = ref("");
const steps = ref([]);
const stepCount = ref(1);
const measurePicked = ref("");
const stepDuration = ref(false);
const duration = ref("");

const erro = ref(false);

const file = ref(null);
const imageData = ref([]);

function isNumeric(value) {
  return !isNaN(parseFloat(value)) && isFinite(value);
}

function stepDurationFunc() {
  !stepDuration.value;
}

function AdicionarIngrediente() {
  console.log(
    "Ingrediente adicionado:",
    ingrediente.value,
    quantidade.value,
    measurePicked.value
  );
  if (
    ingrediente.value != "" &&
    (quantidade.value != "" || isNumeric(quantidade.value)) &&
    measurePicked.value != ""
  ) {
    if (
      quantidade.value == 1 &&
      !(
        measurePicked.value == "mg" ||
        measurePicked.value == "g" ||
        measurePicked.value == "ml" ||
        measurePicked.value == "Colheres de Sopa" ||
        measurePicked.value == "Colheres de chá"
      )
    ) {
      ingredientesList.value.push({
        nome: ingrediente.value,
        quantidade: quantidade.value,
        medida: measurePicked.value.slice(0, -1),
      });
    } else if (
      quantidade.value == 1 &&
      measurePicked.value == "Colheres de Sopa"
    ) {
      ingredientesList.value.push({
        nome: ingrediente.value,
        quantidade: quantidade.value,
        medida: "Colher de Sopa",
      });
    } else if (
      quantidade.value == 1 &&
      measurePicked.value == "Colheres de chá"
    ) {
      ingredientesList.value.push({
        nome: ingrediente.value,
        quantidade: quantidade.value,
        medida: "Colher de chá",
      });
    } else {
      ingredientesList.value.push({
        nome: ingrediente.value,
        quantidade: quantidade.value,
        medida: measurePicked.value,
      });
    }
    ingrediente.value = "";
    quantidade.value = "";
    measurePicked.value = "";
  } else {
    erro.value = true;
  }
  setTimeout(() => {
    this.erro = false;
  }, 6000); // Alerta desaparecerá após 6 segundos
}

function RemoverIngrediente(nomeIngrediente) {
  ingredientesList.value = ingredientesList.value.filter(
    (ingrediente) => ingrediente.nome !== nomeIngrediente
  );
}

function AdicionarPasso() {
  console.log("Passo adicionado:", step.value, stepCount.value), duration.value;
  if (
    (step.value != "" && !stepDuration.value) ||
    (step.value != "" && duration.value != "" && stepDuration)
  ) {
    steps.value.push({
      step: step.value,
      stepCount: stepCount.value,
      duracao: duration.value,
    });
    step.value = "";
    stepCount.value += 1;
    duration.value = "";
  }
}

function RemoverPasso(index) {
  this.steps.splice(index - 1, 1);
  // Recontar os steps após a remoção
  steps.value.forEach((stepObj, i) => {
    stepObj.stepCount = i + 1;
  });
  this.stepCount = this.steps.length + 1;
}

function onFileChange(event) {
  const ficheiro = event.target.files[0];
  file.value = ficheiro;
  imageData.value.pop();
  imageData.value.push({
    nome: ficheiro.name,
    url: URL.createObjectURL(ficheiro),
  });
  console.log(imageData);
}
async function postarReceita() {
  try {
    const response = await axios.post(
      "http://localhost:5000/api/receitas",
      receita.value
    );
    console.log("Receita postada com sucesso:", response.data);
    await router.push("/");
  } catch (error) {
    console.error("Erro ao postar a receita:", error);
  }
}
</script>

<style>
.topnav {
  background-color: rgb(0, 0, 0);
  overflow: hidden;
}

/* Style the links inside the navigation bar */
.topnav a {
  float: left;
  color: #ffffff;
  text-align: center;
  padding: 15px 16px;
  text-decoration: none;
  font-size: 18px;
}

/* Change the color of links on hover */
.topnav a:hover {
  background-color: #04bb78;
  color: black;
}

/* Add a color to the active/current link */
.topnav a.paginainicial {
  background-color: #04bb78;
  color: white;
  font-size: 18px;
}

.topnav a.login {
  float: right;
  background-color: #04bb78;
  text-align: center;
  padding: 15px 16px;
  text-decoration: none;
  font-size: 18px;
}

#NomeReceita {
  width: 100%;
  padding: 1px 5px;
  display: inline-block;
  font-weight: bold;
  color: black;
  margin-bottom: -15px;
}

#Description2 {
  width: 90%;
  margin-left: 5px;
  margin-top: 5px;
  height: 150px;
  padding: 5px 5px;
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 10px;
  background-color: white;
  font-size: 16px;
  resize: none;
}
#recipename {
  width: 500px;
  background-color: white;
  padding: 15px;
  color: black;
  border: 1px solid black;
  border-radius: 10px;
  margin-right: 1028px;
}
#typeFood {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  margin-top: 15px;
  margin-left: 3px;
  color: black;
}

#Duration {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 40px;
  left: 3px;
  color: black;
}

#durationInput {
  background-color: white;
  border-radius: 10%;
  color: black;
  padding: 10px 20px;
  position: relative;
  top: 70px;
  right: 130px;
}

#Difficulty {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 80px;
  left: 3px;
  color: black;
}
#FoodTypeOption {
  width: 200px;
  position: relative;
  top: 15px;
  left: 3px;
}
#DifficultyOption {
  width: 200px;
  position: relative;
  top: 85px;
  left: 3px;
}

#Portion {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 100px;
  left: 3px;
  color: black;
}

#PortionOption {
  width: 200px;
  position: relative;
  top: 105px;
  left: 3px;
}

#PassoText {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 150px;
}

#IngredientesText {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 120px;
  color: black;
}

#Ingrediente {
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 10px;
  background-color: white;
  width: 300px;
  margin-top: 115px;
  margin-right: 765px;
  font-size: 16px;
  color: black;
  font-weight: bold;
}

#Quantidade {
  width: 300px;
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 10px;
  background-color: white;
  margin-right: 875px;
  margin-top: 5px;
  font-size: 16px;
  color: black;
  font-weight: bold;
}

#IngredienteButton {
  width: 250px;
  margin-top: 5px;
  margin-bottom: -130px;
  color: black;
  background-color: #00ff2b;
  font-weight: bold;
  border-radius: 10px;
  border-width: 2px;
  border-color: black;
  font-size: 15px;
}

#Passos {
  position: relative;
  top: 150px;
  width: 100%;
  padding: 1px 5px;
  display: inline-block;
  font-weight: bold;
  font-size: 25px;
  color: black;
}

#AddPassos {
  width: 90%;
  position: relative;
  left: 5px;
  top: 150px;
  height: 150px;
  padding: 5px 5px;
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 10px;
  background-color: white;
  font-size: 16px;
  resize: none;
}

#PassoButton {
  width: 250px;
  height: 35px;
  color: black;
  background-color: #00ff2b;
  font-weight: bold;
  border-radius: 5px;
  border-width: 3px;
  border-color: black;
  position: relative;
  top: 180px;
  right: -5px;
  font-size: 15px;
}

#AddImage {
  position: relative;
  top: 230px;
  width: 100%;
  padding: 1px 5px;
  display: inline-block;
  font-weight: bold;
  font-size: 25px;
}

#uploadButton {
  width: 305px;
  height: 25px;
  color: black;
  background-color: #ffffff;
  font-weight: bold;
  font-size: 15px;
  border-radius: 5px;
  border-width: 3px;
  border-color: black;
  position: relative;
  top: 200px;
  left: 335px;
}
#StepCount {
  width: 400px;
  height: 25px;
  color: black;
  background-color: #e6dede;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 185px;
  left: 10px;
}
#IngredienteText {
  width: 500px;
  height: 25px;
  color: black;
  background-color: #e6dede;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  border-radius: 5px;
  border-width: 3px;
  border-color: black;
  top: 150px;
  right: 705px;
}
.alert {
  padding: 20px;
  background-color: #f44336; /* Red */
  color: white;
  margin-top: 130px;
  margin-right: 1000px;
  margin-bottom: -150px;
}

.closebtn {
  margin-left: 15px;
  color: white;
  font-weight: bold;
  float: right;
  font-size: 22px;
  line-height: 20px;
  cursor: pointer;
  transition: 0.3s;
}

.closebtn:hover {
  color: black;
}
#imagem {
  position: relative;
  top: 220px;
  left: 10px;
}
#measureOption {
  margin-top: 10px;
  margin-right: 900px;
}
#stepDuration {
  position: relative;
  top: 170px;
  right: 1717px;
}
#stepDurationText {
  position: relative;
  top: 171px;
  right: 1717px;
  font-weight: bold;
}
#DurationOfStep {
  position: relative;
  top: 175px;
  left: 10px;
}
#durationInputOfStep {
  background-color: white;
  border-radius: 10%;
  color: black;
  padding: 10px 20px;
  position: relative;
  top: 175px;
  left: 10px;
}

#EnviarButton {
  height: 30px;
  width: 200px;
  position: relative;
  top: 240px;
  right: -5px;
  font-size: 16px;
  box-sizing: border-box;
  border: 1px solid black;
  border-radius: 10px;
  background-color: rgb(229, 229, 229);
}
</style>
