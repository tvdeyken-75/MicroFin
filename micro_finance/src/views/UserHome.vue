<template>
  <div class="home">
    <h1>Welcome to the Home Page!</h1>
    <p>You are logged in as {{ $store.state.user.username }}</p>
    <router-link to="/create-factuur">Create Factuur</router-link>
    <button @click="logout">Logout</button>
  </div>
</template>

<script>
export default {
  methods: {
    logout() {
      if (localStorage.getItem('token')) {
        localStorage.removeItem('token');  // Verwijder het token
        // Optioneel: Clear state in Vuex of een andere state management oplossing
        // this.$store.commit('clearToken');
        this.$router.push('/login');  // Navigeer terug naar login
        alert('Logout successful'); // Feedback aan gebruiker
      } else {
        alert('No active session found'); // Gebruiker is al uitgelogd of sessie is al verlopen
      }
    }
  }
}
</script>
