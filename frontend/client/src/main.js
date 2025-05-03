import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import SignUp from './pages/sign_up.vue'
import Home from './pages/home.vue'
import Create_post from './pages/create_post.vue'

const routes = [{path : '/home', component: Home}, {path : '/sign_up', component: SignUp}, {path : '/create_post', component: Create_post}]
const router = createRouter({
    history: createWebHistory(),
    routes
  })
  
  createApp(App).use(router).mount('#app')