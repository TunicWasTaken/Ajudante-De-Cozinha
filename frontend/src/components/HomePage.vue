<template>
  <div>
    <div class="topnav">
      <a class="Home" href="/">Home</a>
      <a class="login" href="/login">Login</a>
    </div>
    <div class="bemvindo">
      <h1>
        {{ msg }}
      </h1>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "HomePage",
  data() {
    return {
      msg: "Olá mundo",
    };
  },
  methods: {
    getResponse() {
      const path = "http://localhost:5000/api/users";
      axios
        .get(path)
        .then((res) => {
          console.log(res.data);
          this.msg = res.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
  created() {
    this.getResponse();
  },
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
</style>
