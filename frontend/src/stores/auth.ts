import { defineStore } from "pinia";
import axios from "axios";

export const useAuthStore = defineStore("auth", {
  state: () => ({
    authUser: null,
  }),
  getters: {
    user: (state) => state.authUser,
  },
  actions: {
    async createUser(username: string, password: string) {
      await axios
        .post(
          "http://localhost:5000/api/create-user",
          { username: username, password: password },
          { withCredentials: true }
        )
        .catch((err) => {
          throw err;
        });
    },

    async loginUser(username: string, password: string) {
      await axios
        .post(
          "http://localhost:5000/api/login",
          {
            username: username,
            password: password,
          },
          { withCredentials: true }
        )
        .then(() => {
          axios.defaults.headers.common["X-CSRF-TOKEN"] =
            document.cookie.split("=")[1];
        })
        .catch((err) => {
          throw err;
        });
    },

    async getUser() {
      const data = await axios.get("http://localhost:5000/api/profile", {
        withCredentials: true,
      });
      this.authUser = data.data;
    },

    async logoutUser() {
      await axios
        .get("http://localhost:5000/api/logout", {
          withCredentials: true,
        })
        .then(() => {
          this.authUser = null;
          axios.defaults.headers.common["X-CSRF-TOKEN"] = null;
        })
        .catch((err) => {
          if (err.response.data.msg == "Token has expirer") {
            this.authUser = null;
          }
        });
    },

    async createRecipe(recipe: unknown) {
      await axios
        .post("http://localhost:5000/api/recipe", recipe, {
          withCredentials: true,
        })
        .then(async () => {
          console.log("Receita criada com sucesso");
        })
        .catch((err) => {
          throw err;
        });
    },
  },
  persist: true,
});
