<template>
    <div>
        <input v-model='username', placeholder="Username">
        <input v-model="phone", placeholder="Phone">
        <input v-model="password", placeholder="Password">
        <button @click="sign_up">Sign_up</button>
    </div>

    <div>
        <input v-model="phone", placeholder="Phone">
        <input v-model="password", placeholder="Password">
        <button @click='sign_in'>Sign_in</button>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                usermane: '',
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
                    alert = "Пользователь зарегистрирован"
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
</script>