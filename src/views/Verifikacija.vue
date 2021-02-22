<template>
  <div class="Verifikacija">
    <h1 style="text-md-center">Ovdje ćete se verificirati</h1>
    <p style="background: lightblue">
     Dobili verifikacijski kod koji morate unijeti kako
      bi ste bili u mogućnosti vidjeti rezultate.
    </p>
    <h3>
      Molimo vas da unesete četveroznamenkasti verifikacijski kod kako bi ste mogli pristupiti rezultatima.
    </h3>
    <form @submit.prevent="onSubmit(potvrda)" class="verify">
      <h3 style="color: deepskyblue; background: lightgrey">Verifikacija</h3>
      <input
        id="input"
        type="potvrda"
        v-model="potvrda"
        placeholder="Unesite verifikacijski broj"
        class="vrf"
        maxlength="4"
        required
      /><br /><br />
      <button type="submit" class="vrf-btn">Potvrdi</button>
      <br />
    </form>
  </div>
</template>

<script>
export default {
  name: "Verifikacija",
  data() {
    return {
      potvrda: ""
    };
  },
  methods: {
    onSubmit(potvrda) {
      if (potvrda == 4444) {
        return this.$router.replace({ name: "Rezultati" });
      } 
      else{
        alert('Unijeli ste pogrešan verifikacijski broj.\n Pokušajte ponovo. ')
      }
    },
  },
};
</script>

<style >
.verify {
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
.verify input {
  display: block;
  width: 100%;
  padding: 0 16px;
  height: 45px;
  text-align: center;
  box-sizing: border-box;
  outline: none;
  border: none;
  border-radius: 10px;
  background: darkgray;
}
.vrf-btn {
  margin-top: 1px;
  margin-bottom: 10px;
  background: green;
  color: #fff;
  border-radius: 45px;
  cursor: pointer;
  transition: 0.8s;
  width: 150px;
  height: 45px;
}
</style>