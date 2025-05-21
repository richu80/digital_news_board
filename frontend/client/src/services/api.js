// API сервис для всех запросов к бэкенду

const API_BASE_URL = '/api';

export default {
  // Аутентификация
  async login(credentials) {
    try {
      const response = await fetch(`${API_BASE_URL}/sign_in`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(credentials),
      });
      return await response.json();
    } catch (error) {
      console.error('Login error:', error);
      throw error;
    }
  },

  async register(userData) {
    try {
      const response = await fetch(`${API_BASE_URL}/sign_up`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData),
      });
      return await response.json();
    } catch (error) {
      console.error('Register error:', error);
      throw error;
    }
  },

  async logout() {
    try {
      const response = await fetch(`${API_BASE_URL}/logout`, {
        method: 'POST',
        credentials: 'include',
      });
      return await response.json();
    } catch (error) {
      console.error('Logout error:', error);
      throw error;
    }
  },

  // Посты
  async getPosts() {
    try {
      const response = await fetch(`${API_BASE_URL}/home`, {
        method: 'GET',
        credentials: 'include',
      });
      return await response.json();
    } catch (error) {
      console.error('Get posts error:', error);
      throw error;
    }
  },

  async createPost(postData) {
    try {
      const response = await fetch(`${API_BASE_URL}/create_post`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(postData),
      });
      return await response.json();
    } catch (error) {
      console.error('Create post error:', error);
      throw error;
    }
  },

  async deletePost(postId) {
    try {
      const response = await fetch(`${API_BASE_URL}/post/${postId}/delete`, {
        method: 'DELETE',
        credentials: 'include',
      });
      return await response.json();
    } catch (error) {
      console.error('Delete post error:', error);
      throw error;
    }
  },

  // Лайки и комментарии
  async likePost(postId) {
    try {
      const response = await fetch(`${API_BASE_URL}/post/${postId}/like`, {
        method: 'POST',
        credentials: 'include',
      });
      return await response.json();
    } catch (error) {
      console.error('Like post error:', error);
      throw error;
    }
  },

  async unlikePost(postId) {
    try {
      const response = await fetch(`${API_BASE_URL}/post/${postId}/unlike`, {
        method: 'DELETE',
        credentials: 'include',
      });
      return await response.json();
    } catch (error) {
      console.error('Unlike post error:', error);
      throw error;
    }
  },

  async createComment(postId, commentData) {
    try {
      const response = await fetch(`${API_BASE_URL}/post/${postId}/create_comment`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        credentials: 'include',
        body: JSON.stringify(commentData),
      });
      return await response.json();
    } catch (error) {
      console.error('Create comment error:', error);
      throw error;
    }
  },

  async deleteComment(commentId) {
    try {
      const response = await fetch(`${API_BASE_URL}/post/comment/${commentId}/delete`, {
        method: 'DELETE',
        credentials: 'include',
      });
      return await response.json();
    } catch (error) {
      console.error('Delete comment error:', error);
      throw error;
    }
  }
} 