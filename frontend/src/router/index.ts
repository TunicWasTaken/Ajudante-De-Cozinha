import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import HomePage from "../components/HomePage.vue";
import LoginPage from "../components/LoginPage.vue";
import SignUpPage from "../components/SignUpPage.vue";
import CreateRecipePage from "@/components/CreateRecipePage.vue";
import MyRecipesPage from "../components/MyRecipesPage.vue";
import ReceitaPage from "../components/ReceitaPage.vue";
import SearchPage from "@/components/SearchPage.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "HomePage",
    meta: { title: "Ajudante De Cozinha" },
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
    meta: { title: "Criar Receita" },
    component: CreateRecipePage,
  },
  {
    path: "/my-recipes",
    name: "MyRecipesPage",
    meta: { title: "As Minhas Receitas" },
    component: MyRecipesPage,
  },
  {
    path: "/recipes/:id",
    name: "ReceitaPage",
    meta: { title: "Receita" },
    component: ReceitaPage,
  },
  {
    path: "/search",
    name: "SearchPage",
    meta: { title: "Procurar Receitas" },
    component: SearchPage,
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
