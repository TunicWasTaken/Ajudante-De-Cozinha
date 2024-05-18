import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomePage from "../components/HomePage.vue";
import LoginPage from "../components/LoginPage.vue";
import SignUpPage from "../components/SignUpPage.vue";
import CreateRecipePage from "../components/CreateRecipePage.vue";

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
  {
    path: "/sign-up",
    name: "SignUpPage",
    meta: { title: "Sign Up" },
    component: SignUpPage,
  },
  {
    path: "/create-recipe",
    name: "CreateRecipePage",
    meta: { title: "Create Recipe" },
    component: CreateRecipePage,
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
