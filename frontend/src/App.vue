<template>
  <div
    class="topnav"
    v-if="$route.path != '/login' && $route.path != '/sign-up'"
  >
    <router-link class="Home" to="/">Home</router-link>
    <router-link v-if="!authStore.user" class="login" to="/login"
      >Login</router-link
    >
    <router-link
      v-if="authStore.user"
      class="logout"
      to="/"
      @click="authStore.logoutUser()"
    >
      Logout
    </router-link>
    <router-link
      v-if="authStore.user && $route.path != '/create-recipe'"
      class="Create Recipe"
      to="/create-recipe"
      >Create Recipe</router-link
    ><router-link
      v-if="authStore.user && $route.path != '/my-recipes'"
      class="MyRecipes"
      to="/my-recipes"
      >My Recipes</router-link
    >
  </div>
  <router-view></router-view>
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();
</script>
<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
}

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
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
.topnav a.logout {
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
