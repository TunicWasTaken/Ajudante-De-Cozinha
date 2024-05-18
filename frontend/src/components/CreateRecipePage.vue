<template>
  <div>
    <div class="topnav">
      <a class="Home" href="/">Página Inicial</a>
      <a class="login" href="/login">Login</a>
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
      <span id="Description">Descrição do prato:</span>
      <p style="white-space: pre-line"></p>
      <textarea
        v-model="description"
        placeholder="Descrição..."
        id="Description2"
      ></textarea>
      <div id="typeFood">Tipo de prato:</div>
      <input type="checkbox" id="Carne" value="Carne" v-model="typePicked" />
      <label for="Carne" id="CarneName">Carne</label>
      <input type="checkbox" id="Peixe" value="Peixe" v-model="typePicked" />
      <label for="Peixe" id="PeixeName">Peixe</label>
      <input type="checkbox" id="Vegan" value="Vegan" v-model="typePicked" />
      <label for="Vegan" id="VeganName">Vegan</label>
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
          type="text"
          placeholder="Quantidade..."
        />
        <button
          type="button"
          id="IngredienteButton"
          v-on:click="AdicionarIngrediente()"
        >
          Adicionar Ingrediente
        </button>
      </div>
      <input type="submit" value="Enviar" id="EnviarButton" />
    </form>
  </div>
  <span id="Passos">Passos:</span>
  <p style="white-space: pre-line"></p>
  <textarea
    v-model="step"
    placeholder="Descrição do passo..."
    id="AddPassos"
  ></textarea>
  <button type="button" id="PassoButton" v-on:click="AdicionarPasso()">
    Adicionar Passo {{ stepCount }}
  </button>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

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
const msg = ref([]);
const stepCount = ref(1);

const path = "http://localhost:5000/api/users";
axios
  .get(path)
  .then((res) => {
    msg.value = res.data;
  })
  .catch((err) => {
    console.log(err);
  });

function AdicionarIngrediente() {
  console.log("Ingrediente adicionado:", ingrediente.value, quantidade.value);
  ingredientesList.value.push({
    nome: ingrediente.value,
    quantidade: quantidade.value,
  });
  ingrediente.value = "";
  quantidade.value = "";
}

function AdicionarPasso() {
  console.log("Ingrediente adicionado:", ingrediente.value, quantidade.value);
  if (step.value != "") {
    steps.value.push({
      step: step.value,
    });
    step.value = "";
    stepCount.value += 1;
  }
}
</script>

<style>
body {
  background-color: #eee;
}
/* Add a black background color to the top navigation */
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
}

#Description {
  width: 100%;
  padding: 1px 5px;
  display: inline-block;
  font-weight: bold;
}

#Description2 {
  width: 90%;
  position: relative;
  left: 5px;
  top: 5px;
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
  margin-right: 20px;
  border: 1px solid black;
  border-radius: 4px;
  cursor: pointer;
  position: relative;
  bottom: 15px;
  right: 695px;
  border-radius: 10px;
}
#typeFood {
  width: 100%;
  padding: 1px 5px;
  display: inline-block;
  font-weight: bold;
  position: relative;
  top: 15px;
}

#CarneName {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 30px;
  left: 3px;
  border: 2px solid #616161;
  padding: 10px;
  margin: 10px;
}

#Carne {
  height: 15px;
  width: 15px;
  background-color: white;
  position: relative;
  top: 30px;
  left: 3px;
}

#PeixeName {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 30px;
  left: 3px;
  border: 2px solid #616161;
  padding: 10px;
  margin: 10px;
}

#Peixe {
  height: 15px;
  width: 15px;
  margin-left: 20px;
  background-color: white;
  position: relative;
  top: 30px;
}

#VeganName {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 30px;
  left: 3px;
  border: 2px solid #616161;
  padding: 10px;
  margin: 10px;
}

#Vegan {
  height: 15px;
  width: 15px;
  margin-left: 20px;
  background-color: white;
  position: relative;
  top: 30px;
}

#Duration {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 40px;
  left: 3px;
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
  top: 120px;
}

#IngredientesText {
  width: 100%;
  font-weight: bold;
  font-size: 20px;
  position: relative;
  top: 120px;
}

#Ingrediente {
  position: relative;
  width: 500px;
  top: 115px;
  right: 745px;
  right: 455px;
  font-size: 16px;
}

#Quantidade {
  width: 500px;
  position: relative;
  top: 165px;
  right: 955px;
  font-size: 16px;
}

#IngredienteButton {
  width: 250px;
  color: black;
  background-color: #00ff2b;
  font-weight: bold;
  border-radius: 10px;
  border-width: 2px;
  border-color: black;
  position: relative;
  top: 150px;
  right: 455px;
  font-size: 15px;
}

#EnviarButton {
  position: relative;
  top: 500px;
  right: 915px;
  font-size: 16px;
}
#Passos {
  position: relative;
  top: 120px;
  width: 100%;
  padding: 1px 5px;
  display: inline-block;
  font-weight: bold;
  font-size: 25px;
}

#AddPassos {
  width: 90%;
  position: relative;
  left: 5px;
  top: 120px;
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
  top: 125px;
  right: -5px;
  font-size: 15px;
}
</style>
