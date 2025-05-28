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
      this.isLoggedIn = document.cookie.includes('session') || sessionStorage.getItem('user_id');
    },
    async logout() {
      try {
        await ApiService.logout();
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
body {
  font-family: 'Comic Sans MS', 'Chalkboard SE', 'Comic Neue', cursive, system-ui, Avenir, Helvetica, Arial, sans-serif;
  background-color: #fff0f5;
  margin: 0;
  padding: 0;
  color: #5e3505;
}

.hello-kitty-navbar {
  background-color: #ffb6c1;
  padding: 15px 0;
  box-shadow: 0 3px 6px rgba(231, 84, 128, 0.15);
  border-bottom: 2px solid #f48fb1;
}

.navbar-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 30px;
}

.hello-kitty-brand {
  color: #fff;
  font-family: 'Comic Sans MS', cursive;
  font-size: 2rem;
  font-weight: bold;
  text-shadow: 1px 1px 2px #e75480;
}

.nav-links {
  display: flex;
  gap: 25px;
}

.nav-link {
  color: #fff;
  text-decoration: none;
  font-weight: bold;
  font-size: 1.1rem;
  padding: 8px 15px;
  border-radius: 15px;
  transition: background-color 0.3s ease, color 0.3s ease, transform 0.2s ease;
}

.nav-link:hover,
.nav-link.router-link-exact-active {
  background-color: #fff;
  color: #e75480;
  transform: translateY(-2px);
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.logout-link {
  cursor: pointer;
}

.page-container {
  padding: 20px;
  margin-top: 20px;
}
</style>