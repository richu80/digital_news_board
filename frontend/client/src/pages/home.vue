<template>
    <div>
        <h1>Лента</h1>
        <div v-for= "post in posts" :key = "post.id"> 
                <PostItem :post="post" @refresh = "fetchPosts"/>
        </div>
    </div>
</template>


<script>
    import PostItem from '../components/post_item.vue'
    export default {
        components: {PostItem},
        data() {
            return { posts: [] }
        },
        methods: {
            async fetch_post() {
                const response = await fetch('/api/home',
                {
                    method : "GET",
                    credentials: 'include'
                })

                this.posts = await response.json();
            }
        },
        mounted() {
            this.fetch_post()
        }
    }
</script>