<template>
  <div class="topnav">
    <router-link class="Home" to="/">Home</router-link>
    <router-link class="login" to="/login">Login</router-link>
    <router-link class="Create Recipe" to="/create-recipe"
      >Create Recipe</router-link
    ><router-link class="MyRecipes" to="/my-recipes">My Recipes</router-link>
  </div>
  <div v-if="authStore.user">
    <h1>{{ authStore.user.name }}</h1>
  </div>
</template>

<script setup>
import { onMounted } from "vue";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();

onMounted(async () => {
  if (authStore.user != null) {
    await authStore.getUser();
  }
});
</script>

<style>
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
.topnav a.MyRecipes {
  float: right;
  background-color: black;
  text-align: center;
  padding: 15px 16px;
  text-decoration: none;
  font-size: 18px;
}
</style>
