<template>
  <div class="topnav">
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
    <router-link v-if="authStore.user" class="Create Recipe" to="/create-recipe"
      >Create Recipe</router-link
    ><router-link v-if="authStore.user" class="MyRecipes" to="/my-recipes"
      >My Recipes</router-link
    >
    <div class="search-container">
      <form action="SearchBar">
        <input type="text" placeholder="Pesquisa.." name="SearchBar" />
      </form>
    </div>
  </div>
  <div v-if="authStore.user">
    <h1>{{ authStore.user.name }}</h1>
    <h1>{{ authStore.user.role }}</h1>
  </div>
  <div class="main-container">
    <div :class="['sidebar', { 'sidebar-hidden': !isSidebarVisible }]">
      <button class="toggle-button" @click="toggleSidebar">
        <span v-if="isSidebarVisible">←</span>
        <span v-else>→</span>
      </button>
      <div v-if="isSidebarVisible">
        <div class="filter-category">
          <h3>Tipo de Prato</h3>
          <label
            ><input type="checkbox" name="tipo-prato" value="Carne" />
            Carne</label
          >
          <label
            ><input type="checkbox" name="tipo-prato" value="Peixe" />
            Peixe</label
          >
          <label
            ><input type="checkbox" name="tipo-prato" value="Vegetariano" />
            Vegetariano</label
          >
        </div>
        <div class="filter-category">
          <h3>Duração</h3>
          <label
            ><input type="checkbox" name="duracao" value="<60min" />
            &lt;60min</label
          >
          <label
            ><input type="checkbox" name="duracao" value="1h-6h" /> Entre 1h e
            6h</label
          >
          <label
            ><input type="checkbox" name="duracao" value=">6h" /> &gt; 6h</label
          >
        </div>
        <div class="filter-category">
          <h3>Calorias</h3>
          <label
            ><input type="checkbox" name="calorias" value="<600kcal" /> &lt;600
            kcal</label
          >
          <label
            ><input type="checkbox" name="calorias" value="600-1200kcal" />
            Entre 600 e 1200kcal</label
          >
          <label
            ><input type="checkbox" name="calorias" value=">1200kcal" />
            &gt;1200 kcal</label
          >
        </div>
        <div class="filter-category">
          <h3>Dificuldade</h3>
          <label
            ><input type="checkbox" name="dificuldade" value="Fácil" />
            Fácil</label
          >
          <label
            ><input type="checkbox" name="dificuldade" value="Médio" />
            Médio</label
          >
          <label
            ><input type="checkbox" name="dificuldade" value="Difícil" />
            Difícil</label
          >
        </div>
        <div class="filter-category">
          <h3>Tipo de Sabor</h3>
          <label
            ><input type="checkbox" name="sabor" value="Picante" />
            Picante</label
          >
          <label
            ><input type="checkbox" name="sabor" value="Azedo" /> Azedo</label
          >
          <label
            ><input type="checkbox" name="sabor" value="Doce" /> Doce</label
          >
          <label
            ><input type="checkbox" name="sabor" value="Salgado" />
            Salgado</label
          >
        </div>
        <div class="filter-category">
          <h3>Outros</h3>
          <label
            ><input type="checkbox" name="outros" value="Sem gluten" /> Sem
            gluten</label
          >
          <label
            ><input type="checkbox" name="outros" value="Sem lactose" /> Sem
            lactose</label
          >
          <label
            ><input type="checkbox" name="outros" value="Sem frutos secos" />
            Sem frutos secos</label
          >
        </div>
      </div>
    </div>
    <div class="content">
      <div class="caixas">
        <div class="card">
          <img class="background" src="../assets/tiago.png" alt="" />
          <div class="card-content">
            <h3 class="title">Tiago</h3>
          </div>
          <div class="backdrop"></div>
        </div>
        <div class="card">
          <img class="background" src="../assets/tiago.png" alt="" />
          <div class="card-content">
            <h3 class="title">Tiago</h3>
          </div>
          <div class="backdrop"></div>
        </div>
        <div class="card">
          <img class="background" src="../assets/tiago.png" alt="" />
          <div class="card-content">
            <h3 class="title">Tiago</h3>
          </div>
          <div class="backdrop"></div>
        </div>
        <div class="card">
          <img class="background" src="../assets/tiago.png" alt="" />
          <div class="card-content">
            <h3 class="title">Tiago</h3>
          </div>
          <div class="backdrop"></div>
        </div>
        <div class="card">
          <img class="background" src="../assets/tiago.png" alt="" />
          <div class="card-content">
            <h3 class="title">paneleiros</h3>
          </div>
          <div class="backdrop"></div>
        </div>
      </div>
      <div class="body">
        <div class="Novidades">
          <!--<h1>Novidades</h1>-->
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { ref } from "vue";

const authStore = useAuthStore();
const isSidebarVisible = ref(false);
const toggleSidebar = () => {
  isSidebarVisible.value = !isSidebarVisible.value;
};
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
body {
  background-color: #e1e1e1;
  margin: 0; /* Remove margens padrão do corpo */
  padding: 0; /* Remove preenchimento padrão do corpo */
}

.main-container {
  display: flex;
  flex-grow: 1;
}

.sidebar {
  width: 250px;
  height: 720px;
  background-color: #f4f4f4;
  padding: 20px;
  box-shadow: 2px 0 5px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  position: relative;
}

.sidebar-hidden {
  transform: translateX(-100%);
}

.toggle-button {
  position: absolute;
  top: 10px;
  right: -30px;
  background-color: #04bb78;
  color: white;
  border: none;
  padding: 5px 10px;
  cursor: pointer;
  border-radius: 4px;
}

.content {
  flex-grow: 1;
  padding: 0 20px 20px 20px; /* Adiciona padding para dar espaço ao conteúdo */
  display: flex;
  flex-direction: column;
  overflow-y: auto; /* Permite rolagem se o conteúdo for maior que a altura disponível */
}
/* Style the links inside the navigation bar */
.topnav a {
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

.topnav a.Home {
  background-color: #04bb78;
  color: white;
  border-radius: 2px 2px 2px 2px;
  font-size: 18px;
}

/* Center the search bar container */
.search-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
}

.search-container form {
  display: flex;
  align-items: center;
}

.search-container input[type="text"] {
  background-color: white;
  color: black;
  padding: 10px;
  font-size: 12px;
  border: 1px solid #ccc;
  border-radius: 4px 4px 4px 4px;
  width: 200%;
}
img {
  width: 100%;
  height: 100%;
  display: block;
}

.caixas {
  display: flex;
  gap: 10px;
  width: 100%;
  padding: 10px;
}
.card {
  min-width: 70px;
  height: 300px;
  border-radius: 30px;
  overflow: hidden;

  display: flex;
  align-items: flex-end;
  flex-grow: 1;
  cursor: pointer;
  position: relative;
  transition: flex-grow 0.5s cubic-bezier(0.16, 1, 0.3, 1);

  --transition-timing: 0.35s;
}

.card:hover {
  flex-grow: 7;
}

.card > .background {
  position: absolute;
  inset: 0;
  object-fit: cover;
  object-position: center;
  filter: brightness(0.4);
  z-index: -1;
  transition: var(--transition-timing) ease;
}

.card:hover > .background {
  filter: brightness(1);
}

.card > .card-content {
  flex: 1 1 calc(20% - 10px); /* Ajusta a largura dos cards para ocupar 20% da largura do container menos o espaço do gap */
  min-width: 200px; /* Define uma largura mínima para os cards */
  display: flex;
  align-items: center;
  position: absolute;
  left: 10px;
  right: 10px;
  bottom: 20px;
  overflow: hidden;
  transition: var(--transition-timing);
  z-index: 10;
}

.card:hover > .card-content {
  inset: 20px;
  top: auto;
}

.card-content > * {
  transition: var(--transition-timing);
}

.card > .card-content > .title {
  white-space: pre;
  margin-left: 10px;
  color: white;
}

.card > .backdrop {
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  height: 100px;
  z-index: 0;
  background: linear-gradient(to bottom, transparent, rgba(0, 0, 0, 0.7));
}

.filter-category {
  margin-bottom: 10px;
}

.filter-category h3 {
  margin: 0;
  font-size: 14px;
}

.filter-category label {
  display: block;
  padding: 5px 0;
}

[v-cloak] {
  display: none;
}
</style>
