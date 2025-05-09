<!-- <template>
    <div>
        <input v-model='username' placeholder="Username">
        <input v-model="phone" placeholder="Phone">
        <input v-model="password" placeholder="Password">
        <button @click="sign_up">Sign_up</button>
    </div>

    <div>
        <input v-model="phone" placeholder="Phone">
        <input v-model="password" placeholder="Password">
        <button @click='sign_in'>Sign_in</button>
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
                try{
                    const response = await fetch('/api/sign_up', 
                    {
                        method: 'POST',
                        credentials: 'include',
                        headers: { 'Content-Type': 'application/json' },

                        body: JSON.stringify({
                        username: this.username,
                        phone_number: this.phone,
                        password: this.password
                        })
                    })
                    const data = await response.json();
                    alert("Пользователь зарегистрирован")
                } catch (error) {
                console.error("Ошибка при загрузке данных с сервера:", error);
                }
            },

            async sign_in() {
                try{
                    const response = await fetch('/api/sign_in', 
                    {
                        method: 'POST',
                        credentials: 'include',
                        headers: { 'Content-Type': 'application/json' },

                        body: JSON.stringify({
                        phone_number: this.phone,
                        password: this.password
                        })
                    })
                    const data = await response.json();
                    if (response.ok) this.$router.push('/home')
                    else alert("Вход запрещен")
                } catch (error) {
                console.error("Ошибка при загрузке данных с сервера:", error);
                }
            }


        }

    }
</script> -->

<template>
    <div class="d-flex flex-column align-items-center justify-content-center vh-100 bg-pink-light">
      <!-- Заголовок -->
      <div class="text-center mb-5">
        <h1 class="h3 mb-3 font-weight-normal text-pink-dark">Welcome</h1>
      </div>
  
      <!-- Форма регистрации -->
      <div class="w-100 mx-auto p-4 mb-4 bg-pink-lighter rounded-3 shadow-sm" style="max-width: 400px;">
        <h2 class="h5 mb-3 text-center text-pink-dark">Create your account</h2>
        <div class="mb-3">
          <input 
            v-model="username" 
            type="text" 
            class="form-control text-center bg-pink-very-light border-pink" 
            placeholder="Username"
          >
        </div>
        <div class="mb-3">
          <input 
            v-model="phone" 
            type="tel" 
            class="form-control text-center bg-pink-very-light border-pink" 
            placeholder="Phone number"
          >
        </div>
        <div class="mb-3">
          <input 
            v-model="password" 
            type="password" 
            class="form-control text-center bg-pink-very-light border-pink" 
            placeholder="Password"
          >
        </div>
        <button 
          @click="sign_up" 
          class="btn w-100 bg-pink text-white border-0 py-2"
        >
          Sign Up
        </button>
      </div>
  
      <!-- Форма входа -->
      <div class="w-100 mx-auto p-4 bg-pink-lighter rounded-3 shadow-sm" style="max-width: 400px;">
        <h2 class="h5 mb-3 text-center text-pink-dark">Sign in</h2>
        <div class="mb-3">
          <input 
            v-model="phone" 
            type="tel" 
            class="form-control text-center bg-pink-very-light border-pink" 
            placeholder="Phone number"
          >
        </div>
        <div class="mb-3">
          <input 
            v-model="password" 
            type="password" 
            class="form-control text-center bg-pink-very-light border-pink" 
            placeholder="Password"
          >
        </div>
        <button 
          @click="sign_in" 
          class="btn w-100 bg-pink text-white border-0 py-2"
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
  .bg-pink-light {
    background-color: #fff5f7 !important;
  }
  .bg-pink-lighter {
    background-color: #ffebee !important;
  }
  .bg-pink-very-light {
    background-color: #fce4ec !important;
  }
  .bg-pink {
    background-color: #f48fb1 !important;
  }
  .bg-pink:hover {
    background-color: #f06292 !important;
  }
  .text-pink-dark {
    color: #ad1457 !important;
  }
  .border-pink {
    border: 1px solid #f8bbd0 !important;
  }
  
  .btn {
    font-weight: 500;
    border-radius: 6px !important;
    transition: all 0.3s;
  }
  .form-control {
    padding: 12px;
    border-radius: 6px !important;
    transition: all 0.3s;
  }
  .form-control:focus {
    box-shadow: 0 0 0 0.2rem rgba(244, 143, 177, 0.25) !important;
    border-color: #f48fb1 !important;
  }
  </style>