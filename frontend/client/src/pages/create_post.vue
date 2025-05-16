<template>
   <h2>Создайте посn</h2>
   <input v-model="title" placeholder="Название поста" type="text">
   <select v-model="category">
        <option>опера</option>
        <option>школьные дни</option>
        <option>учеба</option>
        <option>вне школы</option>
        <option>мероприятия</option>
        <option disabled value="">Выберите категорию</option>
   </select>
   <input v-model="content" placeholder="введите текст" type="text">
   <input v-model="image" placeholder="введи имаге" type="text">
   <button @click="create_post()">создать</button>
</template>

<script>
    export default {
        data() {
            return {
                title: '',
                category: '',
                content: '',
                image: ''
            };
        },
        methods: {
            async create_post() {
                if (!this.title.trim() | !this.category.trim() | !this.content.trim()) {
                    alert("Пожалуйста, заполните все поля.");
                    return;
                }
                const body = {
                    title: this.title,
                    category: this.category,
                    text: this.content,
                    image: this.image
                }
                const response = await fetch('/api/create_post', {
                    method: 'POST',
                    credentials: 'include',
                    headers: { 'Content-Type': 'application/json' },
                    body: JSON.stringify(body)
                });

                if (response.ok) {
                    alert("Пост создан");
                    this.$router.push('/home')
                } else {
                    console.error("Пост не добавлен", error);
                }
                
            }
        }
    }
</script>

<style>

</style>