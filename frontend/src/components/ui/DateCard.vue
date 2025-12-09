<!-- src/components/ui/DateCard.vue -->
<template>
  <div class="date-card">
    <div class="card-image">
      <div class="image-placeholder">
        {{ getPlaceEmoji(place.type) }}
      </div>
      <div class="rating-badge">
        <RatingStars :rating="place.rating" />
        <span class="review-count">({{ place.reviewCount }})</span>
      </div>
    </div>
    
    <div class="card-content">
      <h3 class="place-name">{{ place.name }}</h3>
      <p class="place-type">{{ place.type }}</p>
      <p class="place-address">{{ place.address }}</p>
      
      <div class="price-indicator">
        <span v-for="n in place.priceLevel" :key="n">💰</span>
        <span class="price-text">{{ getPriceText(place.priceLevel) }}</span>
      </div>
      
      <div class="card-actions">
        <button @click="$emit('favorite', place.id)" class="btn-favorite">
          ❤️ В избранное
        </button>
        <button @click="$emit('visit', place.id)" class="btn-primary">
          🗓️ Запланировать
        </button>
      </div>
    </div>
  </div>
</template>

<script setup>
import RatingStars from './RatingStars.vue'

defineProps({
  place: {
    type: Object,
    required: true
  }
})

defineEmits(['favorite', 'visit'])

const getPlaceEmoji = (type) => {
  const emojiMap = {
    'Романтический': '💕',
    'Активный': '🏃‍♂️',
    'Уютный': '🏠',
    'Веселый': '😂',
    'Спокойный': '😌',
    'Приключение': '🗺️',
    'Гастрономический': '🍝'
  }
  return emojiMap[type] || '📍'
}

const getPriceText = (level) => {
  const texts = ['Эконом', 'Средний', 'Премиум']
  return texts[level - 1] || 'Средний'
}
</script>

<style scoped>
.date-card {
  background: white;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition: all 0.3s;
}

.date-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 15px 30px rgba(0, 0, 0, 0.15);
}

.card-image {
  height: 200px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
}

.image-placeholder {
  font-size: 4rem;
  filter: drop-shadow(0 5px 10px rgba(0, 0, 0, 0.3));
}

.rating-badge {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: rgba(255, 255, 255, 0.9);
  padding: 0.5rem 1rem;
  border-radius: 20px;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  backdrop-filter: blur(10px);
}

.review-count {
  color: #666;
  font-size: 0.9rem;
}

.card-content {
  padding: 1.5rem;
}

.place-name {
  font-size: 1.3rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
  font-weight: 600;
}

.place-type {
  color: #e91e63;
  font-weight: 500;
  margin-bottom: 0.5rem;
  font-size: 0.95rem;
}

.place-address {
  color: #666;
  font-size: 0.9rem;
  margin-bottom: 1rem;
}

.price-indicator {
  display: flex;
  align-items: center;
  gap: 0.3rem;
  margin-bottom: 1.5rem;
}

.price-text {
  margin-left: 0.5rem;
  color: #666;
  font-size: 0.9rem;
}

.card-actions {
  display: flex;
  gap: 0.8rem;
}

.btn-favorite, .btn-primary {
  flex: 1;
  padding: 0.8rem;
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 500;
  cursor: pointer;
  border: none;
  transition: all 0.3s;
}

.btn-favorite {
  background: #f8f9fa;
  color: #666;
}

.btn-favorite:hover {
  background: #e9ecef;
}

.btn-primary {
  background: #e91e63;
  color: white;
}

.btn-primary:hover {
  background: #d81b60;
}
</style>