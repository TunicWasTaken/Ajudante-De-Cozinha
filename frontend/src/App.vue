<template>
  <div
    class="topnav"
    v-if="$route.path != '/login' && $route.path != '/sign-up'"
  >
    <router-link class="home" to="/"
      ><img src="../src/assets/logo.png" height="45"
    /></router-link>
    <div class="search-container">
      <form class="search-content" @submit.prevent="search()">
        <input
          id="search-bar"
          type="text"
          v-model="query"
          placeholder="Pesquisar.."
        />
      </form>
    </div>
    <router-link v-if="!authStore.user" class="login" to="/login"
      >Login</router-link
    >
    <div class="logged-in-container" v-if="authStore.user">
      <img id="user-logo" src="../src/assets/user_icon.png" height="30" />
      <div class="dropdown-container">
        <div class="dropdown-content">
          <router-link
            v-if="authStore.user && $route.path != '/create-recipe'"
            class="create-recipe"
            to="/create-recipe"
            >Criar Receita</router-link
          ><br /><router-link
            v-if="authStore.user && $route.path != '/my-recipes'"
            class="my-recipes"
            to="/my-recipes"
            >Minhas Receitas</router-link
          ><br />
          <router-link
            v-if="authStore.user"
            class="logout"
            to="/"
            @click="authStore.logoutUser()"
          >
            Logout
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <router-view :key="$route.fullPath"></router-view>
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { ref } from "vue";
import { useRouter } from "vue-router";

const authStore = useAuthStore();
const router = useRouter();

const query = ref("");

function search() {
  router.push({ path: "search", query: { q: query.value } });
}
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

.topnav {
  background-color: rgb(0, 0, 0);
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 10px;
}

.topnav .home {
  margin: 5px 5px;
}

.topnav .login {
  float: right;
  text-align: center;
  padding: 10px 20px;
  margin: 7px 10px;
  border-radius: 6px;
  text-decoration: none;
  background: rgb(20, 219, 111, 0.8);
  color: white;
  height: 35px;
  transition: all 0.3s;
}

.topnav .login:hover {
  background-color: rgb(20, 219, 111);
  color: rgb(255, 255, 255);
}

.topnav .logged-in-container {
  float: right;
  margin-top: 5px;
  margin-right: 10px;
}

.topnav .dropdown-container {
  top: 4%;
  right: -10px;
  width: 180px;
  position: absolute;
  display: none;
}

.topnav .dropdown-container .dropdown-content {
  background: rgb(0, 0, 0);
  padding: 20px;
  margin: 10px;
}

.topnav .dropdown-content a {
  text-decoration: none;
  color: #ffffff;
  font-size: 15px;
}

.topnav .logged-in-container:hover .dropdown-container {
  display: block;
  transform-origin: top right;
  animation: scaleUp 0.2s ease-in-out;
}

.topnav .dropdown-content a:hover {
  color: rgb(3, 219, 111);
  font-weight: 550;
}

@keyframes scaleUp {
  from {
    transform: scale(0);
  }
  to {
    transform: scale(1);
  }
}

.search-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 300px;
}

.search-content {
  width: 100%;
}

.search-content #search-bar {
  background-color: #ddd;
  color: black;
  font-size: 14px;
  width: 100%;
  border-radius: 6px;
  font-size: 14px;
  outline: none;
  height: 35px;
}
</style>
