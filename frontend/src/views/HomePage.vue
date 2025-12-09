<!-- src/views/HomePage.vue -->
<template>
  <div class="home-page">
    <!-- Герой секция -->
    <section class="hero">
      <div class="hero-content">
        <h1 class="hero-title">💕 Планируйте идеальные свидания</h1>
        <p class="hero-subtitle">ИИ-помощник подберет места, которые понравятся вам обоим</p>
        <div class="hero-buttons">
          <button class="btn-primary" @click="createCouple">
            👫 Создать пару
          </button>
          <button class="btn-secondary" @click="learnMore">
            📚 Узнать больше
          </button>
        </div>
      </div>
      <div class="hero-image">
        <div class="image-placeholder">
          💑
        </div>
      </div>
    </section>

    <!-- Особенности -->
    <section class="features">
      <h2 class="section-title">✨ Почему DatePlanner AI?</h2>
      <div class="features-grid">
        <div class="feature-card">
          <div class="feature-icon">🧠</div>
          <h3>ИИ-рекомендации</h3>
          <p>Умный подбор мест на основе ваших предпочтений и интересов</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">🗺️</div>
          <h3>Реальные места</h3>
          <p>Интеграция с Яндекс.Картами и Google Places</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">💑</div>
          <h3>Профили пар</h3>
          <p>Создайте уникальный профиль для вашей пары</p>
        </div>
        <div class="feature-card">
          <div class="feature-icon">⭐</div>
          <h3>Отзывы и оценки</h3>
          <p>Читайте реальные отзывы других пар</p>
        </div>
      </div>
    </section>

    <!-- Призыв к действию -->
    <section class="cta">
      <h2>Готовы к идеальному свиданию?</h2>
      <p>Присоединяйтесь к тысячам пар, которые уже доверили нам свои романтические вечера</p>
      <button class="btn-primary btn-large" @click="startNow">
        🚀 Начать сейчас
      </button>
    </section>
  </div>
</template>

<script setup>
const createCouple = () => {
  alert('Функция создания пары в разработке!')
}

const learnMore = () => {
  alert('Больше информации о проекте скоро!')
}

const startNow = () => {
  alert('Добро пожаловать в DatePlanner AI!')
}
</script>

<style scoped>
.home-page {
  max-width: 1200px;
  margin: 0 auto;
}

/* Hero section */
.hero {
  display: flex;
  align-items: center;
  gap: 4rem;
  margin-bottom: 4rem;
  background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
  border-radius: 20px;
  padding: 3rem;
  box-shadow: 0 10px 30px rgba(233, 30, 99, 0.1);
}

.hero-content {
  flex: 1;
}

.hero-title {
  font-size: 3rem;
  color: #2c3e50;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.hero-subtitle {
  font-size: 1.2rem;
  color: #555;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.hero-buttons {
  display: flex;
  gap: 1rem;
}

.hero-image {
  flex: 1;
  display: flex;
  justify-content: center;
}

.image-placeholder {
  width: 300px;
  height: 300px;
  background: white;
  border-radius: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 8rem;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
}

/* Buttons */
.btn-primary, .btn-secondary {
  padding: 0.8rem 1.8rem;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  border: none;
  transition: all 0.3s;
}

.btn-primary {
  background: #e91e63;
  color: white;
}

.btn-primary:hover {
  background: #d81b60;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(233, 30, 99, 0.3);
}

.btn-secondary {
  background: white;
  color: #e91e63;
  border: 2px solid #e91e63;
}

.btn-secondary:hover {
  background: #fce7f3;
  transform: translateY(-2px);
}

.btn-large {
  padding: 1rem 3rem;
  font-size: 1.2rem;
}

/* Features section */
.features {
  margin-bottom: 4rem;
}

.section-title {
  text-align: center;
  font-size: 2.2rem;
  color: #2c3e50;
  margin-bottom: 3rem;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 15px;
  text-align: center;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  transition: transform 0.3s;
}

.feature-card:hover {
  transform: translateY(-5px);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  color: #2c3e50;
  margin-bottom: 0.8rem;
  font-size: 1.3rem;
}

.feature-card p {
  color: #666;
  line-height: 1.5;
}

/* CTA section */
.cta {
  text-align: center;
  padding: 4rem 2rem;
  background: linear-gradient(135deg, #2c3e50 0%, #34495e 100%);
  color: white;
  border-radius: 20px;
  margin-bottom: 2rem;
}

.cta h2 {
  font-size: 2.2rem;
  margin-bottom: 1rem;
}

.cta p {
  font-size: 1.1rem;
  max-width: 600px;
  margin: 0 auto 2rem;
  color: #ecf0f1;
}

@media (max-width: 768px) {
  .hero {
    flex-direction: column;
    text-align: center;
    padding: 2rem;
  }
  
  .hero-title {
    font-size: 2.2rem;
  }
  
  .hero-buttons {
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .image-placeholder {
    width: 200px;
    height: 200px;
    font-size: 6rem;
  }
}
</style>