<!-- src/views/Recommendations.vue -->
<template>
  <div class="recommendations-page">
    <h1 class="page-title">🎯 ИИ-рекомендации для вас</h1>
    <p class="page-subtitle">Наши алгоритмы подобрали идеальные места для вашего свидания</p>

    <!-- Фильтры -->
    <div class="filters">
      <div class="filter-group">
        <label>💰 Бюджет:</label>
        <select v-model="filters.budget" class="filter-select">
          <option value="">Любой</option>
          <option value="low">Эконом (до 2000₽)</option>
          <option value="medium">Средний (2000-5000₽)</option>
          <option value="high">Премиум (5000₽+)</option>
        </select>
      </div>

      <div class="filter-group">
        <label>🎭 Тип:</label>
        <div class="type-tags">
          <span v-for="type in dateTypes" 
                :key="type"
                :class="['type-tag', { active: filters.types.includes(type) }]"
                @click="toggleType(type)">
            {{ type }}
          </span>
        </div>
      </div>

      <div class="filter-group">
        <label>📍 Локация:</label>
        <input v-model="filters.location" 
               type="text" 
               placeholder="Введите район или город..." 
               class="location-input">
      </div>
    </div>

    <!-- Рекомендации -->
    <div class="recommendations">
      <h2 v-if="filteredPlaces.length > 0" class="section-title">
        🏆 Топ рекомендаций ({{ filteredPlaces.length }})
      </h2>
      <p v-else class="no-results">😔 По вашим фильтрам ничего не найдено. Попробуйте другие настройки!</p>

      <div class="places-grid">
        <DateCard 
          v-for="place in filteredPlaces" 
          :key="place.id"
          :place="place"
          @favorite="addToFavorites"
          @visit="planVisit"
        />
      </div>
    </div>

    <!-- AI Insights -->
    <div class="ai-insights">
      <h3>🤖 ИИ аналитика:</h3>
      <p>На основе ваших предпочтений, мы рекомендуем места типа <strong>"{{ getTopType() }}"</strong></p>
      <p>Средний бюджет рекомендаций: <strong>{{ getAveragePrice() }}₽</strong></p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import DateCard from '../components/ui/DateCard.vue'

// Данные мест
const places = ref([
  {
    id: 1,
    name: 'Ресторан "Ла Скала"',
    type: 'Романтический',
    address: 'ул. Тверская, 24',
    image: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400',
    rating: 4.8,
    reviewCount: 127,
    priceLevel: 3,
    budget: 'high',
    tags: ['Романтический', 'Гастрономический']
  },
  {
    id: 2,
    name: 'Парк "Зарядье"',
    type: 'Активный',
    address: 'ул. Варварка, 6',
    image: 'https://images.unsplash.com/photo-1551632811-561732d1e306?w-400',
    rating: 4.7,
    reviewCount: 356,
    priceLevel: 1,
    budget: 'low',
    tags: ['Активный', 'Природа']
  },
  {
    id: 3,
    name: 'Кофейня "Уют"',
    type: 'Уютный',
    address: 'ул. Арбат, 32',
    image: 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=400',
    rating: 4.9,
    reviewCount: 89,
    priceLevel: 2,
    budget: 'medium',
    tags: ['Уютный', 'Кофе']
  },
  {
    id: 4,
    name: 'Кинотеатр "Октябрь"',
    type: 'Веселый',
    address: 'Новый Арбат, 24',
    image: 'https://images.unsplash.com/photo-1489599809516-9827b6d1cf13?w=400',
    rating: 4.5,
    reviewCount: 234,
    priceLevel: 2,
    budget: 'medium',
    tags: ['Веселый', 'Кино']
  },
  {
    id: 5,
    name: 'Спа-центр "Релакс"',
    type: 'Спокойный',
    address: 'ул. Поварская, 8',
    image: 'https://images.unsplash.com/photo-1544161515-4ab6ce6db874?w=400',
    rating: 4.6,
    reviewCount: 156,
    priceLevel: 3,
    budget: 'high',
    tags: ['Спокойный', 'СПА']
  },
  {
    id: 6,
    name: 'Квест-рум "Тайна"',
    type: 'Приключение',
    address: 'ул. Льва Толстого, 16',
    image: 'https://images.unsplash.com/photo-1534423861386-85a16f5d13fd?w=400',
    rating: 4.8,
    reviewCount: 189,
    priceLevel: 2,
    budget: 'medium',
    tags: ['Приключение', 'Игры']
  }
])

// Фильтры
const filters = ref({
  budget: '',
  types: [],
  location: ''
})

const dateTypes = ['Романтический', 'Активный', 'Уютный', 'Веселый', 'Спокойный', 'Приключение', 'Гастрономический']

// Вычисляемые свойства
const filteredPlaces = computed(() => {
  return places.value.filter(place => {
    // Фильтр по бюджету
    if (filters.value.budget && place.budget !== filters.value.budget) {
      return false
    }
    
    // Фильтр по типам
    if (filters.value.types.length > 0) {
      const hasMatchingType = place.tags.some(tag => filters.value.types.includes(tag))
      if (!hasMatchingType) return false
    }
    
    // Фильтр по локации
    if (filters.value.location) {
      const searchLocation = filters.value.location.toLowerCase()
      if (!place.address.toLowerCase().includes(searchLocation)) {
        return false
      }
    }
    
    return true
  })
})

// Методы
const toggleType = (type) => {
  const index = filters.value.types.indexOf(type)
  if (index === -1) {
    filters.value.types.push(type)
  } else {
    filters.value.types.splice(index, 1)
  }
}

const addToFavorites = (placeId) => {
  const place = places.value.find(p => p.id === placeId)
  alert(`💖 Добавлено в избранное: ${place?.name || 'Место'}`)
}

const planVisit = (placeId) => {
  const place = places.value.find(p => p.id === placeId)
  alert(`🗓️ Запланировано посещение: ${place?.name || 'Место'}`)
}

const getTopType = () => {
  if (filteredPlaces.value.length === 0) return 'Романтический'
  const typeCounts = {}
  filteredPlaces.value.forEach(place => {
    place.tags.forEach(tag => {
      typeCounts[tag] = (typeCounts[tag] || 0) + 1
    })
  })
  return Object.keys(typeCounts).reduce((a, b) => typeCounts[a] > typeCounts[b] ? a : b, 'Романтический')
}

const getAveragePrice = () => {
  if (filteredPlaces.value.length === 0) return '2000-3000'
  const prices = {
    'low': 1500,
    'medium': 3500,
    'high': 7000
  }
  const avg = filteredPlaces.value.reduce((sum, place) => sum + prices[place.budget], 0) / filteredPlaces.value.length
  return Math.round(avg)
}
</script>

<style scoped>
.recommendations-page {
  max-width: 1200px;
  margin: 0 auto;
}

.page-title {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.page-subtitle {
  color: #666;
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

/* Filters */
.filters {
  background: white;
  padding: 1.5rem;
  border-radius: 15px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  margin-bottom: 2rem;
}

.filter-group {
  margin-bottom: 1.5rem;
}

.filter-group label {
  display: block;
  font-weight: 600;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.filter-select {
  width: 100%;
  max-width: 300px;
  padding: 0.8rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  transition: border-color 0.3s;
}

.filter-select:focus {
  outline: none;
  border-color: #e91e63;
}

.type-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  margin-top: 0.5rem;
}

.type-tag {
  padding: 0.5rem 1rem;
  background: #f5f5f5;
  border-radius: 20px;
  cursor: pointer;
  transition: all 0.3s;
  font-size: 0.9rem;
}

.type-tag:hover {
  background: #e0e0e0;
}

.type-tag.active {
  background: #e91e63;
  color: white;
}

.location-input {
  width: 100%;
  max-width: 400px;
  padding: 0.8rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
}

.location-input:focus {
  outline: none;
  border-color: #e91e63;
}

/* Recommendations */
.section-title {
  font-size: 1.8rem;
  color: #2c3e50;
  margin: 2rem 0 1rem;
}

.no-results {
  text-align: center;
  font-size: 1.2rem;
  color: #666;
  padding: 3rem;
  background: #f8f9fa;
  border-radius: 10px;
}

.places-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin: 2rem 0;
}

/* AI Insights */
.ai-insights {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  padding: 2rem;
  border-radius: 15px;
  margin-top: 2rem;
}

.ai-insights h3 {
  font-size: 1.5rem;
  margin-bottom: 1rem;
}

.ai-insights p {
  margin: 0.5rem 0;
  font-size: 1.1rem;
}

@media (max-width: 768px) {
  .page-title {
    font-size: 2rem;
  }
  
  .places-grid {
    grid-template-columns: 1fr;
  }
}
</style>