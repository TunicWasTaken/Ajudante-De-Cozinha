import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomePage from "../components/HomePage.vue";
import LoginPage from "../components/LoginPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "HomePage",
    meta: { title: "Home" },
    component: HomePage,
  },
  {
    path: "/login",
    name: "LoginPage",
    meta: { title: "Login" },
    component: LoginPage,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to) => {
  console.log(to);
  document.title = to.meta.title as string;
});

export default router;
