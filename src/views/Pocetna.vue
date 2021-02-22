<template>
    <div class="container">
      <h3>Dobrodošli na aplikaciju za izbore</h3>
      <p style="background:lightblue;">
        Za glasanje pritisnite sliku vote(lijevo), a za rezultate sliku
        results(desno).
      </p>

      <router-link to="/Registracija"
        ><img
          src="../assets/picture.png"
          style="margin: 50px auto; padding-right: 20px"
      /></router-link>
      <router-link to="/Verifikacija"
        ><img
          src="../assets/picture1.jpg"
          style="width: 180px; margin: 50px auto"
      /></router-link>
    </div>

</template>



<style>
* {
  background-color: lightblue;
}

</style>