<template>
  <div class="wrapper">
    <div class="logo">
      <a href="/">
        <img src="../assets/logo.png" height="45" />
      </a>
    </div>
    <div class="container">
      <div class="box">
        <div class="login">
          <h2>Login</h2>
          <form @submit.prevent="loginUser()">
            <span class="error_msg" v-if="account_error"
              >User with that username and password does not exist!</span
            >
            <input
              type="text"
              placeholder="Username"
              required
              v-model="username"
            />
            <input
              type="password"
              placeholder="Password"
              required
              v-model="password"
            />
            <p>Don't have an account? <a href="/sign-up">Sign up</a></p>
            <button>Submit</button>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from "axios";
import { ref } from "vue";
import { useRouter } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const authStore = useAuthStore();
const router = useRouter();
const username = ref();
const password = ref();
const account_error = ref(false);

function loginUser() {
  axios
    .post("http://localhost:5000/api/login", {
      username: username.value,
      password: password.value,
    })
    .then(async () => {
      // Get user data since Token was already obtained
      await authStore.getUser();

      // Redirect to Home Page
      await router.push("/");
    })
    .catch((err) => {
      if (err.response.status == 401) {
        account_error.value = true;
      } else {
        console.log(err);
      }
    });
}
</script>

<style>
.wrapper {
  background-image: url("/src/assets/login-background.png");
  background-repeat: no-repeat;
  background-attachment: fixed;
  background-size: cover;
}

.logo a img {
  padding: 5px;
}

.container {
  width: 100%;
  height: calc(100vh - 49px);
  display: flex;
  align-items: center;
  justify-content: center;
}

.box {
  background-color: rgb(41, 41, 41);
  padding: 30px;
  border-radius: 10px;
}

.login h2 {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 10px;
  color: dodgerblue;
}

.error_msg {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  width: 65%;
  font-size: 15px;
  color: lightcoral;
}

form {
  display: flex;
  justify-content: center;
  align-items: center;
  flex-flow: column;
  gap: 10px;
  padding: 5px;
}

form input {
  padding: 10px 20px;
  color: white;
  background: #333;
  border: none;
  border-radius: 6px;
  font-size: 14px;
}

form p {
  color: rgb(170, 170, 170);
  font-size: 14px;
}

form a {
  color: dodgerblue;
}

form button {
  display: flex;
  justify-content: center;
  align-items: center;
  text-align: center;
  margin-top: 20px;
  width: 100px;
  border-radius: 6px;
  padding: 10px 20px;
  border: 1px solid dodgerblue;
  background: none;
  color: dodgerblue;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s;
}

form button:hover {
  background: dodgerblue;
  color: white;
}
</style>
