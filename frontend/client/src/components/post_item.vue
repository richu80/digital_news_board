<template>
    <div class="hk-card post-card p-3 mb-3">
        <img v-if="post.image" :src="post.image" alt="Post image" class="post-image-item">
        <div class="post-content-item">
            <h3 class="post-title">{{ post.title }}</h3>
            <p class="post-category">Category: {{ post.category }}</p>
            <p class="post-text-item">{{ post.text }}</p>
            <small class="post-meta">By User ID: {{ post.user_id }} on {{ formatDate(post.created_at) }}</small>
            <div class="post-actions-item mt-2">
                <button @click="toggleLike" :class="likeButtonClass">
                    <span v-if="localIsLiked">💖 Un-kitty Like</span>
                    <span v-else>🤍 Kitty Like</span>
                    <span class="like-count">({{ localLikesCount }})</span>
                </button>
                <button 
                    v-if="post.is_author"
                    @click="deletePost" 
                    class="hk-button-icon hk-button-delete">
                    🗑️ Delete
                </button>
            </div>
        </div>
    </div>
</template>

<script>
import ApiService from '../services/api.js';

export default {
    props: {
        post: {
            type: Object,
            required: true
        }
    },
    data() {
        return {
            localIsLiked: this.post.is_liked,
            localLikesCount: this.post.likes_count
        };
    },
    computed: {
        likeButtonClass() {
            return [
                'hk-button-icon',
                this.localIsLiked ? 'hk-button-unlike-style' : 'hk-button-like-style'
            ];
        }
    },
    methods: {
        async toggleLike() {
            try {
                if (this.localIsLiked) {
                    await ApiService.unlikePost(this.post.id);
                    this.localIsLiked = false;
                    this.localLikesCount--;
                    alert('Post unliked!');
                } else {
                    await ApiService.likePost(this.post.id);
                    this.localIsLiked = true;
                    this.localLikesCount++;
                    alert('Post liked!');
                }
                // Optionally, emit refresh if global state needs update
                // this.$emit('refresh'); 
            } catch (error) {
                console.error('Error toggling like:', error);
                alert(error.message || 'Failed to update like status.');
            }
        },
        async deletePost() {
            if (confirm('Are you sure you want to delete this post?')) {
                try {
                    await ApiService.deletePost(this.post.id);
                    this.$emit('refresh');
                    alert('Post deleted successfully!');
                } catch (error) {
                    console.error('Error deleting post:', error);
                    alert(error.message || 'Failed to delete post.');
                }
            }
        },
        formatDate(dateString) {
            if (!dateString) return '';
            const options = { year: 'numeric', month: 'long', day: 'numeric' };
            return new Date(dateString).toLocaleDateString(undefined, options);
        }
    },
    watch: {
        post: {
            handler(newPost) {
                this.localIsLiked = newPost.is_liked;
                this.localLikesCount = newPost.likes_count;
            },
            deep: true
        }
    }
}
</script>

<style scoped>
/* Using global .hk-card and .post-card styles from style.css and home.vue */
/* Specific styles for post_item.vue elements */

.post-image-item {
  width: 100%;
  max-height: 250px; /* Control image height */
  object-fit: cover;
  border-radius: 18px 18px 0 0; /* Match card rounding */
  border-bottom: 2px solid #f8b1d5;
  margin-bottom: 15px;
}

.post-content-item {
  padding: 0; /* Padding is handled by .hk-card */
}

.post-title {
  /* Uses styles from home.vue or global */
  font-size: 1.6rem; /* Ensure consistency */
  color: #d13e6a;
  margin-bottom: 5px;
}

.post-category {
  /* Uses styles from home.vue or global */
  font-size: 0.9rem;
  color: #f48fb1;
  margin-bottom: 10px;
}

.post-text-item {
  font-size: 1rem;
  line-height: 1.5;
  color: #5e3505;
  margin-bottom: 15px;
  white-space: pre-wrap; /* Preserve line breaks in post text */
}

.post-meta {
    font-size: 0.85rem;
    color: #e75480;
    margin-bottom: 15px;
}

.post-actions-item {
  display: flex;
  gap: 10px;
  margin-top: auto; /* Pushes to bottom if card is flex column */
  flex-wrap: wrap; /* Allow buttons to wrap on smaller screens */
}

.hk-button-icon {
  /* Base style for icon buttons, can extend .hk-button-small or .hk-button */
  padding: 8px 12px;
  font-size: 0.9em;
  border-radius: 15px;
  border: 1px solid transparent;
  cursor: pointer;
  transition: all 0.2s ease;
  font-weight: bold;
  display: inline-flex;
  align-items: center;
  gap: 8px; /* Increased gap for icon and text */
}

.hk-button-like-style {
  background-color: #ffeff4; /* Very light pink */
  color: #e75480; /* Pink text */
  border-color: #f8b1d5; /* Light pink border */
}
.hk-button-like-style:hover {
  background-color: #f8b1d5; /* Light pink bg */
  color: white;
}

.hk-button-unlike-style {
  background-color: #f48fb1; /* Pink, indicating it's liked, action is to unlike */
  color: white;
  border-color: #e75480; /* Darker pink border */
}
.hk-button-unlike-style:hover {
  background-color: #e75480; /* Darker pink bg */
  color: white;
}

.like-count {
    margin-left: 5px;
    font-weight: normal;
    font-size: 0.9em;
}

.hk-button-delete {
  background-color: #ffeeee; /* Light red */
  color: #c62828; /* Dark red text */
  border-color: #ffcdd2; /* Reddish border */
}
.hk-button-delete:hover {
  background-color: #ffcdd2; /* Darker red bg */
  color: #b71c1c;
}

</style>