<template>
  <div class="page-container">
    <h1 class="hk-title text-center mb-4">Welcome to the News Board!</h1>
    <div v-if="loading" class="loading-message hk-card">
      <p>Loading posts... 🎀</p>
    </div>
    <div v-else-if="error" class="error-message hk-card">
      <p>😿 Oh no! {{ error }}</p>
      <button @click="fetchPosts" class="hk-button">Try Again</button>
    </div>
    <div v-else-if="posts.length === 0" class="no-posts-message hk-card">
      <p>No news posts yet! Be the first to create one. 💖</p>
      <router-link to="/create_post" class="hk-button">Create Post</router-link>
    </div>
    <div v-else class="posts-grid">
      <PostItem 
        v-for="post in posts" 
        :key="post.id" 
        :post="post"
        @refresh="fetchPosts"
      />
    </div>
  </div>
</template>

<script>
    import PostItem from '../components/post_item.vue'
    import ApiService from '../services/api.js'

    export default {
        components: {PostItem},
        data() {
            return { 
                posts: [],
                loading: false,
                error: null
            }
        },
        methods: {
            async fetchPosts() {
                this.loading = true;
                this.error = null;
                try {
                    const fetchedPosts = await ApiService.getPosts();
                    this.posts = fetchedPosts.map(post => ({
                        ...post,
                        is_author: post.user_id === (sessionStorage.getItem('user_id') ? parseInt(sessionStorage.getItem('user_id')) : null)
                    }));
                } catch (error) {
                    this.error = 'Could not load posts. Please try again later.';
                    console.error("Error fetching posts:", error);
                } finally {
                    this.loading = false;
                }
            },
        },
        mounted() {
            this.fetchPosts();
        }
    }
</script>

<style scoped>
  .page-container {
    padding: 20px;
  }

  .hk-title {
    /* Uses global styles, can be adjusted if needed */
  }

  .loading-message p,
  .error-message p,
  .no-posts-message p {
    font-size: 1.2rem;
    color: #e75480; /* Pink text */
    margin-bottom: 20px;
  }

  .loading-message,
  .error-message,
  .no-posts-message {
    text-align: center;
    padding: 30px;
  }

  .posts-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); /* Adjusted minmax for cards */
    gap: 25px;
  }

  .hk-button {
    padding: 0.5em 1em;
    font-size: 0.9em;
    border-radius: 15px;
    background-color: #ffb6c1; /* LightPink */
    color: #5e3505; /* Dark text for contrast */
    border: 1px solid #f48fb1;
    font-weight: bold;
  }

  .hk-button:hover {
    background-color: #f48fb1; /* Pink */
    color: white;
  }
</style>