<template>
  <div class="hello-kitty-background min-vh-100 d-flex align-items-center justify-content-center">
    <div class="w-100 mx-auto p-4 mb-4 hello-kitty-card rounded-3 shadow-sm" style="max-width: 400px;">
      <h2 class="h5 mb-3 text-center hello-kitty-title">Create your account</h2>
      <div class="mb-3">
        <input 
          v-model="username" 
          type="text" 
          class="form-control hello-kitty-input text-center" 
          placeholder="Username"
        >
      </div>
      <div class="mb-3">
        <input 
          v-model="phone" 
          type="tel" 
          class="form-control hello-kitty-input text-center" 
          placeholder="Phone number"
        >
      </div>
      <div class="mb-3">
        <input 
          v-model="password" 
          type="password" 
          class="form-control hello-kitty-input text-center" 
          placeholder="Password"
        >
      </div>
      <button 
        @click="sign_up" 
        class="btn w-100 hello-kitty-button"
      >
        Sign Up
      </button>
    </div>

    <div class="w-100 mx-auto p-4 hello-kitty-card rounded-3 shadow-sm" style="max-width: 400px;">
      <h2 class="h5 mb-3 text-center hello-kitty-title">Sign in</h2>
      <div class="mb-3">
        <input 
          v-model="phone" 
          type="tel" 
          class="form-control hello-kitty-input text-center" 
          placeholder="Phone number"
        >
      </div>
      <div class="mb-3">
        <input 
          v-model="password" 
          type="password" 
          class="form-control hello-kitty-input text-center" 
          placeholder="Password"
        >
      </div>
      <button 
        @click="sign_in" 
        class="btn w-100 hello-kitty-button"
      >
        Sign In
      </button>
    </div>
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
        alert("Пользователь зарегистрирован");
      } catch (error) {
        console.error("Ошибка при загрузке данных с сервера:", error);
      }
    },

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
        if (response.ok) this.$router.push('/home');
        else alert("Вход запрещен");
      } catch (error) {
        console.error("Ошибка при загрузке данных с сервера:", error);
      }
    }
  }
}
</script>

<style scoped>
/* Hello Kitty Theme */
.hello-kitty-background {
  background: url('https://www.itl.cat/pngfile/big/10-103389_hello-kitty-background-hello-kitty-desktop-wallpaper.jpg') center/cover no-repeat; /* Hello Kitty background */
}

.hello-kitty-card {
  background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white for the card */
  border-radius: 20px; /* Rounded corners */
  box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
}

.hello-kitty-title {
  color: #e75480; /* Pink color */
  font-family: 'Comic Sans MS', cursive; /* Playful font */
  font-size: 1.75rem;
  margin-bottom: 1rem;
}

.hello-kitty-input {
  border-radius: 15px;
  border: 2px solid #f8b1d5; /* Lighter pink border */
  padding: 10px 15px;
  margin-bottom: 15px;
  font-family: 'Arial', sans-serif;
  background-color: #fff; /* White background for inputs */
}

.hello-kitty-button {
  background-color: #f48fb1; /* Main pink color */
  color: white;
  border: none;
  border-radius: 25px;
  padding: 12px 25px;
  font-family: 'Comic Sans MS', cursive;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.hello-kitty-button:hover {
  background-color: #ec407a; /* Darker pink on hover */
}
</style>