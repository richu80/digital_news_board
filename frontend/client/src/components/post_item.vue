<template>
    <div>
        <h3>{{Post.title}}</h3>
        <p>{{ Post.text }}</p>
        <p>{{ Post.category }}</p>
        <button @click="like">🤍</button>
        <button @click="unlike">💗</button>
    </div>
</template>

<script>
    export default {
        props: ['post'],

        methods: {
            async like() {
                await fetch('/api/post/<int:post_id>/like',
                { 
                    method : "POST",
                    credentials: 'include',
                    headers: { 'Content-Type': 'application/json' }
                })
                this.$emit('refresh')
                //оповещает родительский компонент о завершении работы
            },

            async unlike() {
                await fetch('/api/post/<int:post_id>/unlike',
                { 
                    method : "DELETE",
                    credentials: 'include',
                    headers: { 'Content-Type': 'application/json' }
                })
                this.$emit('refresh')
            },


        }
    }
</script>