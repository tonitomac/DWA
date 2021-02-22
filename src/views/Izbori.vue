<template>
  <div class="izb">
    <h1>Izbori</h1>
    <h2>Odaberite jednog kandidata i pristinite Vote kako bi ubrojili Vaš glas.</h2>
    <div class="table-box">
      <div class="table-row">
        <div class="table-cell">
          <p>Mark Smith</p>
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">
          <p>Marta Collins</p>
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">
          <p>Sam McNeal</p>
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">
          <p>Sarah Powels</p>
        </div>
      </div>
      <div class="table-row">
        <div class="table-cell">
          <p>Ann Flori</p>
        </div>
      </div>
    </div> 

    <select id="glasovi" style="background: lightgrey; height:30px;" v-model="glasovi" @change="onChange($event)">
      <option v-bind:value="1">Sam McNeal</option>
      <option v-bind:value="2">Sarah Powels</option>
      <option v-bind:value="3">Ann Flori</option>
      <option v-bind:value="4">Mark Smith</option>
      <option v-bind:value="5">Marta Collins</option>
    </select>
    <button v-on:click="submit()" class="vote-btn">Vote</button>
  </div>
</template>



<script>
import axios from "axios";
export default {
  name: "Izbori",
  data() {
    return {
      glasovi: '',
    };
  },

  methods: {
    submit() {
      axios.put("http://127.0.0.1:5000/izbori", {id: this.glasovi})
        .then((response) => {
          console.log("Dobro radi: ", response);
          alert('Uspiješno smo zaprimili vaš glas.');
          this.$router.replace({name: 'Pocetna'});


        })
        .catch((e) => {
          console.log("Doslo je do greske: ", e);
        });

    },
    onChange(event) {
      this.glasovi = event.target.value;

    }
    
  },
};
</script>



<style>
.vote-btn {
  height: 35px;
  width: 50px;
  margin: 2px;
  padding: 0px;
  background-color: green;
}
.table-box {
  margin: 50x auto;
  padding-left: 480px;
}

.table-row {
  display: table;
  width: 50%;
  margin: 10px;
  font-family: sans-serif;
  background: transparent;
  padding: 12px 0;
  color: #555;
  font-size: 15px;
  box-shadow: 0 1px 4px 0 rgba(0, 0, 50, 0.3);
  padding: 0.8rem;
  background: lightgrey;
}
.table-cell {
  display: table-cell;
  width: 100%;
  text-align: center;
  padding: 4px 0;
  border-right: 1px solid #d6d4d4;
  vertical-align: middle;
  background: lightgrey;

}
select {
  width: 150px;
  font-size: 18px;
  height: 31px;
  margin: 0;
  padding: 0px;
}
p, option{
    background: lightgrey;

}
</style>