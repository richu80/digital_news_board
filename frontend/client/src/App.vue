<template>
  <div>
    <nav class="hello-kitty-navbar" v-if="isLoggedIn">
      <div class="navbar-container">
        <div class="nav-brand">
          <span class="hello-kitty-brand">Digital News Board</span>
        </div>
        <div class="nav-links">
          <router-link to="/home" class="nav-link">Главная</router-link>
          <router-link to="/create_post" class="nav-link">Создать пост</router-link>
          <a @click="logout" class="nav-link logout-link">Выйти</a>
        </div>
      </div>
    </nav>
    <router-view @login-success="checkAuthStatus" />
  </div>
</template>

<script>
import ApiService from './services/api.js';

export default {
  data() {
    return {
      isLoggedIn: false
    };
  },
  methods: {
    checkAuthStatus() {
      // Простая проверка - есть ли id пользователя в сессии
      this.isLoggedIn = document.cookie.includes('session') || sessionStorage.getItem('user_id');
    },
    async logout() {
      try {
        await ApiService.logout();
        // После выхода перенаправляем на страницу входа
        this.$router.push('/sign_in');
        this.isLoggedIn = false;
      } catch (error) {
        console.error('Ошибка при выходе:', error);
      }
    }
  },
  created() {
    this.checkAuthStatus();
  },
  watch: {
    $route() {
      this.checkAuthStatus();
    }
  }
};
</script>

<style>
/* Enhanced Hello Kitty Navbar and Global Styles */
body {
  font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', cursive, system-ui, Avenir, Helvetica, Arial, sans-serif; /* Consistent playful font */
  background-color: #fff0f5; /* Lavender blush - default page background */
  margin: 0;
  padding: 0;
  color: #5e3505; /* Default text color from style.css */
}

.hello-kitty-navbar {
  background-color: #ffb6c1; /* LightPink for navbar */
  padding: 15px 0;
  box-shadow: 0 3px 6px rgba(231, 84, 128, 0.15); /* Softer pink shadow */
  border-bottom: 2px solid #f48fb1; /* Pink border bottom */
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 30px; /* Increased padding */
}

.hello-kitty-brand {
  color: #fff; /* White brand text on pink navbar */
  font-family: 'Comic Sans MS', cursive;
  font-size: 2rem; /* Larger brand */
  font-weight: bold;
  text-shadow: 1px 1px 2px #e75480; /* Pink text shadow */
}

.nav-links {
  display: flex;
  gap: 25px; /* Increased gap */
}

.nav-link {
  color: #fff; /* White link text */
  text-decoration: none;
  font-weight: bold; /* Bolder links */
  font-size: 1.1rem;
  padding: 8px 15px;
  border-radius: 15px; /* More rounded links */
  transition: background-color 0.3s ease, color 0.3s ease, transform 0.2s ease;
}

.nav-link:hover,
.nav-link.router-link-exact-active { /* Style for active link */
  background-color: #fff; /* White background on hover/active */
  color: #e75480; /* Pink text on hover/active */
  transform: translateY(-2px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.logout-link {
  cursor: pointer;
}

/* Removing styles that are now global in style.css or component-specific */
/* .hello-kitty-title, .form-control.hello-kitty-input are handled globally or in specific components */

/* Page container for consistent padding */
.page-container {
  padding: 20px;
  margin-top: 20px; /* Add some space below navbar */
}

</style>