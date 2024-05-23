<template>
  <div id="wrapper">
    <div class="topnav">
      <router-link class="Home" to="/">Home</router-link>
      <router-link class="login" to="/login">Login</router-link>
    </div>
  </div>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Francesinha</title>
    <link rel="stylesheet" href="styles.css" />
  </head>
  <body>
    <h1 id="Title">Wide Pedro</h1>
    <div class="info">
      <div class="info-item"><span class="icon">⏱️</span> 20 min</div>
      <div class="info-item"><span class="icon">📊</span> Média</div>
      <div class="info-item"><span class="icon">🍽️</span> 12 pessoas</div>
    </div>
    <img id="imagem" src="../assets/pedro.jpg" />
  </body>
  <h2 id="Description">Descrição:</h2>
  <div class="DescriptionText">{{ description }}</div>
  <h2 id="IngredientesTitle">Ingredientes:</h2>
  <div class="DescriptionText">{{ description }}</div>
</template>

<script setup>
import { ref } from "vue";

const description = ref("Wide Pedro");
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
