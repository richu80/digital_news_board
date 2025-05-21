<template>
  <div class="page-container hello-kitty-background-page">
    <div class="hk-card auth-card mx-auto p-4 mb-4 rounded-3 shadow-sm">
      <h2 class="text-center hk-title">Create your account</h2>
      <div class="mb-3">
        <input 
          v-model="username" 
          type="text" 
          class="form-control text-center" 
          placeholder="Username"
        >
      </div>
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
        @click="sign_up" 
        class="hk-button w-100"
      >
        Sign Up
      </button>
      <p class="mt-3 text-center">
        Already have an account? <router-link to="/sign_in">Sign In</router-link>
      </p>
    </div>

    <!-- The second card for Sign In was redundant here as there's a separate sign_in.vue -->
    <!-- I have removed it for clarity on the sign_up page -->

  </div>
</template>

<script>
export default {
  data() {
    return {
      username: '',
      phone: '',
      password: ''
    };
  },
  methods: {
    async sign_up() {
      try {
        const response = await fetch('/api/sign_up', {
          method: 'POST',
          credentials: 'include',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.username,
            phone_number: this.phone,
            password: this.password
          })
        });
        const data = await response.json();
        if (response.ok) {
            alert("User registered successfully!");
            this.$router.push('/sign_in');
        } else {
            alert(data.error || "Failed to register.");
        }
      } catch (error) {
        console.error("Error during sign up:", error);
        alert("An error occurred. Please try again.");
      }
    },
    // Removed sign_in method as this is sign_up.vue
  }
}
</script>

<style scoped>
/* Scoped styles for sign_up.vue */
.hello-kitty-background-page {
  background: url('https://www.itl.cat/pngfile/big/10-103389_hello-kitty-background-hello-kitty-desktop-wallpaper.jpg') center/cover no-repeat fixed;
  min-height: calc(100vh - 70px); /* Adjust based on navbar height if fixed */
  display: flex;
  align-items: center;
  justify-content: center;
}

.auth-card {
  max-width: 450px; /* Slightly wider card */
  background-color: rgba(255, 255, 255, 0.95); /* More opaque for better readability */
}

.hk-title {
  /* Uses global h1-h6 styles but can be overridden */
  font-size: 2rem; /* Specific size for auth titles */
  color: #e75480;
}

/* Inputs and buttons will use global styles from style.css by default */
/* .form-control will use global input styles */
/* .hk-button will use global button styles */

/* Add spacing and specific styles if needed */
.form-control {
  margin-bottom: 20px; /* More space between inputs */
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
  color: #ff69b4; /* Link color consistent with global */
  font-weight: bold;
}
p a:hover {
  color: #ff1493;
  text-decoration: underline;
}
</style>