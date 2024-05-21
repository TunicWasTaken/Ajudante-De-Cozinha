<template>
  <div class="wrapper">
    <div class="topnav">
      <router-link class="Home" to="/">Home</router-link>
      <router-link class="login" to="/login"> Profile </router-link>
    </div>
  </div>
  <div class="cards-container">
    <router-link class="card" to="/create-recipe">
      <img id="plus" src="../assets/plus.png" width="90%" />
      <div class="container">
        <h4><b>Nova Receita</b></h4>
      </div>
    </router-link>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";

const msg = ref([]);

const path = "http://localhost:5000/api/users";
axios
  .get(path)
  .then((res) => {
    msg.value = res.data;
  })
  .catch((err) => {
    console.log(err);
  });
</script>

<style>
#plus {
  padding: 5%;
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
