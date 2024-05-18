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
    async loginUser(username: string, password: string) {
      await axios.post(
        "http://localhost:5000/api/login",
        {
          username: username,
          password: password,
        },
        { withCredentials: true }
      );
    },

    async getUser() {
      const data = await axios.get("http://localhost:5000/api/profile", {
        withCredentials: true,
      });
      this.authUser = data.data;
    },
  },
});
