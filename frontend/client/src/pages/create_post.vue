<template>
  <div class="page-container">
    <div class="hk-card create-post-card">
      <h1 class="hk-title text-center mb-4">Create a New Post</h1>
      <form @submit.prevent="submitPost">
        <div class="form-group mb-3">
          <label for="title" class="form-label">Title:</label>
          <input type="text" id="title" v-model="post.title" class="form-control" required>
        </div>
        <div class="form-group mb-3">
          <label for="category" class="form-label">Category:</label>
          <input type="text" id="category" v-model="post.category" class="form-control" required>
        </div>
        <div class="form-group mb-3">
          <label for="text" class="form-label">Content:</label>
          <textarea id="text" v-model="post.text" class="form-control" rows="6" required></textarea>
        </div>
        <div class="form-group mb-3">
          <label for="image" class="form-label">Image URL (Optional):</label>
          <input type="text" id="image" v-model="post.image" class="form-control">
        </div>
        <button type="submit" class="hk-button w-100">Create Post</button>
      </form>
    </div>
  </div>
</template>

<script>
import ApiService from '../services/api.js';

export default {
  data() {
    return {
      post: {
        title: '',
        category: '',
        text: '',
        image: ''
      }
    };
  },
  methods: {
    async submitPost() {
      try {
        const response = await ApiService.createPost(this.post);
        if (response && response.id) { // Check if post creation was successful (e.g., by presence of an ID)
          alert('Post created successfully!');
          this.$router.push('/home');
        } else {
          alert(response.error || 'Failed to create post. Please try again.');
        }
      } catch (error) {
        console.error("Error creating post:", error);
        alert("An error occurred while creating the post.");
      }
    }
  }
};
</script>

<style scoped>
.page-container {
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: flex-start; /* Align to top if content is shorter than view height */
}

.create-post-card {
  width: 100%;
  max-width: 700px; /* Wider card for create post form */
  background-color: rgba(255, 255, 255, 0.95); /* Slightly more opaque */
}

.hk-title {
  /* Uses global styles */
}

.form-label {
  display: block;
  margin-bottom: 8px;
  color: #e75480; /* Pink labels */
  font-weight: bold;
  text-align: left;
  font-size: 1.1rem;
}

/* Inputs, textarea, and button will use global styles from style.css */
.form-control {
  /* Global styles apply, can add specific margin if needed */
  margin-bottom: 1rem; /* Consistent spacing */
}

.w-100 {
  width: 100%;
}

.text-center {
  text-align: center;
}

.mb-3 {
  margin-bottom: 1.5rem !important; /* More spacing for form groups */
}

.mb-4 {
  margin-bottom: 2rem !important; /* More spacing for title */
}
</style>