<template>
  <div class="container">
    <h3>Prikaz rezultata</h3>
    <p style="background: lightblue">Ovdje se može vidjeti koliko koji kandidat ima glasova.</p>
    <table id="results">
      <tr>
        <th>Ime</th>
        <th>Prezime</th>
        <th>Br. glasova</th>
      </tr>
      <tr class="redak" v-for="(item, index) in this.row.data" v-bind:key="index">
        <td>{{item[0]}}</td>
        <td>{{item[1]}}</td>
        <td>{{item[3]}}</td>
      </tr>
    </table>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from "axios";
export default {
  name: "Registracija",
  data() {
    return {
      row: [],
    };
  },
  mounted() {
    axios
      .get("http://127.0.0.1:5000/rezultati")
      .then((response) => {
        console.log(response.data);
        this.row = response.data;
      })
      .catch((e) => {
        console.log("Doslo je do greske: ", e);
      });
  },
};
</script>

<style>
#results {
  font-family: Arial, Helvetica, sans-serif;
  border-collapse: collapse;
  width: 100%;
}

#results td,
#results th {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: center;
}

#results td:hover {
  background-color: lightgray;
}

#results th {
  padding-top: 12px;
  padding-bottom: 12px;
  text-align: center;
  background-color: #fff;
  color: black;
}


</style>