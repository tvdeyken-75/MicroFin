<template>
  <div>
    <h1>Login</h1>
    <input v-model="username" type="text" placeholder="Username" @keyup.enter="login">
    <input v-model="password" type="password" placeholder="Password" @keyup.enter="login">
    <button @click="login" :disabled="isLoading">
      Login
      <span v-if="isLoading">...</span>
    </button>
    <p v-if="errorMessage" class="error">{{ errorMessage }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      password: '',
      isLoading: false,
      errorMessage: ''
    };
  },
  methods: {
    async login() {
      if (!this.username || !this.password) {
        this.errorMessage = 'Please enter both username and password';
        return;
      }
      this.isLoading = true;
      try {
        const { data: { access: token } } = await axios.post('http://localhost:9000/token', {
          username: this.username,
          password: this.password
        });
        localStorage.setItem('token', token); // Overweeg veiligere opslagmethodes
        this.$router.push('/');
      } catch (error) {
        console.error('Error during login:', error);
        this.errorMessage = 'Failed to login. Check your credentials.';
      } finally {
        this.isLoading = false;
      }
    }
  }
};
</script>

<style scoped>
.error {
  color: red;
}
</style>
