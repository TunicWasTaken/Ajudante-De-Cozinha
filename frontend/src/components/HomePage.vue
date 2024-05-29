<template>
  <div v-if="authStore.user">
    <h1>{{ authStore.user.name }}</h1>
    <h1>{{ authStore.user.role }}</h1>
  </div>
  {{ top5 }}
  <br />
  <br />
  <br />
  {{ newest }}
</template>

<script setup>
import { useAuthStore } from "@/stores/auth";
import { ref } from "vue";
import axios from "axios";

const authStore = useAuthStore();
const top5 = ref([]);
const newest = ref([]);

axios
  .get("http://localhost:5000/api/recipes/homepage")
  .then((res) => {
    top5.value = res.data.top5;
    newest.value = res.data.new;
  })
  .catch((err) => {
    console.log(err);
  });
</script>

<style></style>
