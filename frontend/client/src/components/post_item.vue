<template>
    <div class="hello-kitty-post p-3 mb-3 rounded shadow">
      <h3 class="hello-kitty-title">{{ post.title }}</h3>
      <p class="hello-kitty-text">{{ post.text }}</p>
      <p class="hello-kitty-category">Категория: {{ post.category }}</p>
      <div class="d-flex justify-content-between align-items-center mt-2">
        <div>
          <button @click="like" class="hello-kitty-like-button">💗</button>
          <button @click="unlike" class="hello-kitty-unlike-button">🤍</button>
          <button v-if="post.is_auther" @click="deletePost">Удалить</button>
        </div>
        <button 
          v-if="showDeleteButton"
          @click="deletePost" 
          class="hello-kitty-delete-button">
          Удалить
        </button>
      </div>
    </div>
</template>

<script>
export default {
    props: ['post', 'currentUserId'],
    computed: {
        showDeleteButton() {
            return this.currentUserId && this.post.user_id === this.currentUserId;
        }
    },
    methods: {
        async like() {
            await fetch(`/api/post/${this.post.id}/like`, {
                method: "POST",
                credentials: 'include',
                headers: { 'Content-Type': 'application/json' }
            });
            this.$emit('refresh');
        },

        async unlike() {
            await fetch(`/api/post/${this.post.id}/unlike`, {
                method: "DELETE",
                credentials: 'include',
                headers: { 'Content-Type': 'application/json' }
            });
            this.$emit('refresh');
        },

        async deletePost() {
            if (confirm('Вы уверены, что хотите удалить этот пост?')) {
                try {
                    const response = await fetch(`/api/post/${this.post.id}/delete`, {
                        method: "DELETE",
                        credentials: 'include',
                        headers: { 'Content-Type': 'application/json' }
                    });

                    if (response.ok) {
                        this.$emit('refresh');
                    } else {
                        const error = await response.json();
                        console.error('Ошибка при удалении:', error);
                        alert('Не удалось удалить пост');
                    }
                } catch (error) {
                    console.error('Ошибка:', error);
                    alert('Произошла ошибка при удалении');
                }
            }
        }
    }
}
</script>

<style scoped>
.hello-kitty-post {
    background-color: rgba(255, 255, 255, 0.75);
    border: 2px solid #f8b1d5;
}

.hello-kitty-title {
    color: #e75480;
    font-family: 'Comic Sans MS', cursive;
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
}

.hello-kitty-text {
    font-family: 'Arial', sans-serif;
    margin-bottom: 0.75rem;
}

.hello-kitty-category {
    font-style: italic;
    color: #9e9e9e;
    font-size: 0.9rem;
}

.hello-kitty-like-button, 
.hello-kitty-unlike-button,
.hello-kitty-delete-button {
    background-color: #fce4ec;
    color: #e75480;
    border: 1px solid #f8b1d5;
    border-radius: 10px;
    padding: 5px 10px;
    margin-right: 0.5rem;
    font-family: 'Arial', sans-serif;
    cursor: pointer;
    transition: background-color 0.2s ease;
}

.hello-kitty-like-button:hover, 
.hello-kitty-unlike-button:hover,
.hello-kitty-delete-button:hover {
    background-color: #f8bbd0;
}

.hello-kitty-delete-button {
    background-color: #ffebee;
    color: #f44336;
    border-color: #ef9a9a;
}

.hello-kitty-delete-button:hover {
    background-color: #ffcdd2;
}
</style>