
<template>
    <div class="hello-kitty-background min-vh-100 d-flex align-items-center justify-content-center">
      <div class="hello-kitty-card p-4 rounded shadow" style="width: 80%;">
        <h1 class="hello-kitty-title text-center mb-4">Home</h1>
            <div v-for= "post in posts" :key = "post.id"> 
                    <PostItem :post="post" @refresh = "fetchPosts"/>
            </div>
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

<style scoped>
  .hello-kitty-background {
    background: url('https://i.pinimg.com/originals/95/a3/8f/95a38f6a2f368dd598a4592f35940731.jpg') center/cover no-repeat; /* Hello Kitty background */
  }

  .hello-kitty-card {
    background-color: rgba(255, 255, 255, 0.8); /* Semi-transparent white for the card */
    border-radius: 20px; /* Rounded corners */
    box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2); /* Subtle shadow */
  }

  .hello-kitty-title {
    color: #e75480; /* Pink color */
    font-family: 'Comic Sans MS', cursive; /* Playful font */
    font-size: 2.0rem; /* Increased font size */
  }

</style>