<template>
  <div id="wrapper">
    <div class="topnav">
      <router-link class="Home" to="/">Home</router-link>
      <router-link class="login" to="/login">Login</router-link>
    </div>
  </div>
  <h1 id="Title">NOME DA RECEITA</h1>
  <h2 id="Subtitle">Tempo de preparação: time</h2>
  <h2 id="Subtitle">Dificuldade: dificuldade</h2>
  <h2 id="Subtitle">Porção: porção</h2>
  <img id="ImagemReceita" src="../assets/logo.png" height="45" />
  <h2 id="Description">Descrição:</h2>
</template>

<script></script>

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
  position: relative;
  top: 120px;
}
</style>
