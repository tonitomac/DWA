<template>
<div class="all">
  <div class="text-md-center">
    <h2 style="color: darkblack">
      Unesite vaše podatke kako bi mogli nastaviti dalje.
    </h2>
    <div class="pocetna">
      <form @submit="register" class="klasaregistracija">
        <h3 style="background:lightgrey;">Registracija</h3>
        <input
          id="name"
          type="text"
          v-model="form.ime"
          placeholder="Unesi ime"
          class="txtb"
          required
        />
        <input
          id="prezime"
          type="text"
          v-model="form.prezime"
          placeholder="Unesi prezime"
          class="txtb"
          required
        />
        <input
          id="oib"
          type="number"
          v-model="form.oib"
          oninput="javascript: if (this.value.length > this.maxLength) this.value = this.value.slice(0, this.maxLength);"          
          placeholder="Unesi oib"
          class="txtb"
          maxlength="11"
          required

        />
        <input
          id="broj_mobitela"
          type="number"
          v-model="form.broj_mobitela"
          placeholder="Broj mobitela"
          class="txtb"
          required
        />
        <button type="submit" class="reg-btn">Registracija</button>
      </form>
    </div>
  </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios'
export default {
  name: "Registracija",
  data() {
    return {
      form: {
        ime: '',
        prezime: '',
        oib: '',
        broj_mobitela: '',
      },
    }
  },
    methods: {
    register(e) {
      e.preventDefault()
      axios.post("http://127.0.0.1:5000/register", this.form)
        .then((response) => {
           console.log("Dobro radi: ", response);
           this.form.ime = "";
           this.form.prezime = "";
           this.form.oib = "";
           this.form.broj_mobitela = "";
          this.$router.replace({name: 'Izbori'});
          
        })
        .catch((e) => {
          console.log("Doslo je do greske: ", e);
        });
    },
  } 
    };
  

</script>


<style>
.klasaregistracija {
  width: 300px;
  padding: 20px;
  text-align: center;
  position: absolute;
  top: 60%;
  left: 50%;
  transform: translate(-50%, -50%);
  overflow: hidden;
  background: lightgrey;
} 

.klasaregistracija h3 {
  margin-top: 100px;
  font-family: "Verdana", cursive;
  color: deepskyblue;
}

.klasaregistracija input {
  display: block;
  width: 100%;
  padding: 0 16px;
  height: 45px;
  text-align: center;
  box-sizing: border-box;
  outline: none;
  border: none;
}
.txtb {
  margin: 20px 0;
  background: rgba(255, 255, 255, 0.5);
  border-radius: 6px;
}
.reg-btn {
  margin-top: 1px;
  margin-bottom: 10px;
  background: green;
  color: #fff;
  border-radius: 45px;
  cursor: pointer;
  transition: 0.8s;
  width: 300px;
  height: 45px;
}

</style>