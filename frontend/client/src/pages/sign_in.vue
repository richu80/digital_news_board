<template>
  <div class="page-container hello-kitty-background-page">
    <div class="hk-card auth-card mx-auto p-4 rounded-3 shadow-sm">
      <h2 class="text-center hk-title">Sign In</h2>
      <div class="mb-3">
        <input 
          v-model="phone" 
          type="tel" 
          class="form-control text-center" 
          placeholder="Phone number"
        >
      </div>
      <div class="mb-3">
        <input 
          v-model="password" 
          type="password" 
          class="form-control text-center" 
          placeholder="Password"
        >
      </div>
      <button 
        @click="sign_in" 
        class="hk-button w-100"
      >
        Sign In
      </button>
      <p class="mt-3 text-center">
        Don't have an account? <router-link to="/sign_up">Sign Up</router-link>
      </p>
    </div>
  </div>
</template>

<script>
import ApiService from '../services/api.js';

export default {
  data() {
    return {
      phone: '',
      password: ''
    };
  },
  methods: {
    async sign_in() {
      try {
        const response = await fetch('/api/sign_in', {
          method: 'POST',
          credentials: 'include',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            phone_number: this.phone,
            password: this.password
          })
        });
        const data = await response.json();
        if (response.ok) {
          sessionStorage.setItem('user_id', data.user_id); // Assuming backend sends user_id on successful login
          this.$router.push('/home');
          this.$emit('login-success'); // Emit event for App.vue to update nav
        } else {
          alert(data.error || "Invalid phone number or password");
        }
      } catch (error) {
        console.error("Error during sign in:", error);
        alert("An error occurred. Please try again.");
      }
    }
  }
};
</script>

<style scoped>
.hello-kitty-background-page {
  background: url('https://www.itl.cat/pngfile/big/10-103389_hello-kitty-background-hello-kitty-desktop-wallpaper.jpg') center/cover no-repeat fixed;
  min-height: calc(100vh - 70px); /* Adjust if navbar height changes */
  display: flex;
  align-items: center;
  justify-content: center;
}

.auth-card {
  max-width: 450px;
  background-color: rgba(255, 255, 255, 0.95);
}

.hk-title {
  font-size: 2rem;
  color: #e75480;
}

.form-control {
  margin-bottom: 20px;
}

.w-100 {
  width: 100%;
}

.text-center {
 text-align: center;
}

.mt-3 {
 margin-top: 1rem;
}

p a {
  color: #ff69b4;
  font-weight: bold;
}
p a:hover {
  color: #ff1493;
  text-decoration: underline;
}
</style> 