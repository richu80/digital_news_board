<template>
  <router-view />
</template>

<script setup>
// You can add any global imports or setup code here if needed
</script>

<style scoped>
/* Global Hello Kitty Theme (shared between pages) */
body {
  font-family: 'Arial', sans-serif; /* Changed font */
  background-color: #fce4ec; /* Light Pink Background */
  margin: 0;
  padding: 0;
  /* Add other global styles here, if needed */
}

.hello-kitty-title {
  color: #e75480; /* Pink color */
  font-family: 'Comic Sans MS', cursive; /* Playful font */
  font-size: 1.75rem;
  margin-bottom: 1rem;
}

.form-control.hello-kitty-input {
    border-radius: 15px;
    border: 2px solid #f8b1d5; /* Lighter pink border */
    padding: 10px 15px;
    margin-bottom: 15px;
    font-family: 'Arial', sans-serif;
    background-color: #fff; /* White background for inputs */
}
</style>