<!-- src/views/CoupleDashboard.vue -->
<template>
  <div class="dashboard-page">
    <!-- Заголовок -->
    <div class="page-header">
      <h1>💑 Панель управления парой</h1>
      <p>Здесь вы можете управлять вашим профилем, историей свиданий и предпочтениями</p>
    </div>

    <!-- Профиль пары -->
    <div class="couple-profile">
      <div class="profile-header">
        <div class="avatar">
          <div class="avatar-placeholder">👫</div>
          <div class="avatar-upload" @click="uploadPhoto">📷</div>
        </div>
        <div class="profile-info">
          <h2>{{ couple.name }}</h2>
          <p>Вместе с {{ couple.togetherSince }}</p>
          <div class="couple-stats">
            <span class="stat">
              <strong>{{ visitedPlaces }}</strong> мест посещено
            </span>
            <span class="stat">
              <strong>{{ averageRating.toFixed(1) }}</strong> средний рейтинг
            </span>
            <span class="stat">
              <strong>{{ couple.daysTogether }}</strong> дней вместе
            </span>
          </div>
        </div>
        <button class="edit-profile" @click="editProfile">✏️ Редактировать профиль</button>
      </div>

      <div class="profile-tabs">
        <button :class="['tab', { active: activeTab === 'dates' }]" @click="activeTab = 'dates'">
          📅 История свиданий
        </button>
        <button :class="['tab', { active: activeTab === 'preferences' }]" @click="activeTab = 'preferences'">
          ⚙️ Предпочтения
        </button>
        <button :class="['tab', { active: activeTab === 'favorites' }]" @click="activeTab = 'favorites'">
          ❤️ Избранное
        </button>
        <button :class="['tab', { active: activeTab === 'ai' }]" @click="activeTab = 'ai'">
          🤖 ИИ-анализ
        </button>
      </div>
    </div>

    <!-- Контент вкладок -->
    <div class="tab-content">
      <!-- История свиданий -->
      <div v-if="activeTab === 'dates'" class="dates-history">
        <h3>Последние свидания</h3>
        <div v-if="recentDates.length > 0" class="dates-list">
          <div v-for="date in recentDates" :key="date.id" class="date-card">
            <div class="date-image">
              <div class="img-placeholder">{{ date.emoji }}</div>
            </div>
            <div class="date-info">
              <h4>{{ date.place }}</h4>
              <p>{{ date.date }} • {{ date.time }}</p>
              <div class="date-rating">
                <span v-for="n in 5" :key="n" class="star">
                  {{ n <= date.rating ? '★' : '☆' }}
                </span>
                <span class="rating-text">{{ date.rating }} из 5</span>
              </div>
              <p class="date-note">{{ date.note }}</p>
            </div>
          </div>
        </div>
        <p v-else class="no-data">У вас пока нет запланированных свиданий</p>
        <button class="btn-primary" @click="addNewDate">➕ Добавить свидание</button>
      </div>

      <!-- Предпочтения -->
      <div v-if="activeTab === 'preferences'" class="preferences">
        <h3>Настройки предпочтений</h3>
        <div class="preferences-grid">
          <div class="preference-category">
            <h4>💰 Бюджет</h4>
            <div class="preference-options">
              <label v-for="option in budgetOptions" :key="option.value">
                <input type="radio" v-model="preferences.budget" :value="option.value">
                {{ option.label }}
              </label>
            </div>
          </div>
          
          <div class="preference-category">
            <h4>🎭 Типы мест</h4>
            <div class="preference-options">
              <label v-for="type in preferenceTypes" :key="type">
                <input type="checkbox" v-model="preferences.types" :value="type">
                {{ type }}
              </label>
            </div>
          </div>
          
          <div class="preference-category">
            <h4>📍 Районы</h4>
            <input v-model="preferences.locations" 
                   type="text" 
                   placeholder="Введите предпочитаемые районы..."
                   class="locations-input">
          </div>
        </div>
        <button class="btn-primary" @click="savePreferences">💾 Сохранить предпочтения</button>
      </div>

      <!-- Избранное -->
      <div v-if="activeTab === 'favorites'" class="favorites">
        <h3>Избранные места</h3>
        <div v-if="favoritePlaces.length > 0" class="favorites-grid">
          <DateCard 
            v-for="place in favoritePlaces" 
            :key="place.id"
            :place="place"
            @favorite="removeFromFavorites"
            @visit="planVisit"
          />
        </div>
        <p v-else class="no-data">У вас пока нет избранных мест</p>
      </div>

      <!-- ИИ-анализ -->
      <div v-if="activeTab === 'ai'" class="ai-analysis">
        <h3>🤖 ИИ-анализ вашей пары</h3>
        <div class="ai-insights">
          <div class="insight-card">
            <h4>🎯 Типичные свидания</h4>
            <p>Вы чаще всего выбираете <strong>{{ aiInsights.topType }}</strong> места</p>
          </div>
          <div class="insight-card">
            <h4>💰 Средние расходы</h4>
            <p>За свидание вы тратите примерно <strong>{{ aiInsights.avgSpending }}₽</strong></p>
          </div>
          <div class="insight-card">
            <h4>⭐ Любимые места</h4>
            <p>Лучше всего оцениваете <strong>{{ aiInsights.topCategory }}</strong> заведения</p>
          </div>
          <div class="insight-card">
            <h4>📅 Рекомендация</h4>
            <p>Попробуйте места типа <strong>{{ aiInsights.recommendation }}</strong> для разнообразия!</p>
          </div>
        </div>
        <button class="btn-primary" @click="refreshAI">🔄 Обновить анализ</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, reactive } from 'vue'
import DateCard from '../components/ui/DateCard.vue'

// Данные пары
const couple = ref({
  name: 'Лена и Лева',
  togetherSince: '2025-09.12.2025',
  daysTogether: 30,
  photo: null
})

// Статистика
const visitedPlaces = ref(1)
const averageRating = ref(5)

// Вкладки
const activeTab = ref('dates')

// История свиданий
const recentDates = ref([
  {
    id: 1,
    place: 'Ресторан "Итальянские сны"',
    date: '10.01.2024',
    time: '19:30',
    rating: 5,
    note: 'Отличная паста и романтическая атмосфера!',
    emoji: '🍝'
  },
  {
    id: 2,
    place: 'Парк Горького',
    date: '05.01.2024',
    time: '14:00',
    rating: 4,
    note: 'Прекрасная зимняя прогулка, было холодно но весело',
    emoji: '❄️'
  },
  {
    id: 3,
    place: 'Кинотеатр "Формула Кино"',
    date: '28.12.2023',
    time: '20:15',
    rating: 4,
    note: 'Интересный фильм, удобные кресла',
    emoji: '🎬'
  }
])

// Предпочтения
const preferences = reactive({
  budget: 'medium',
  types: ['Романтический', 'Уютный'],
  locations: 'Центр, Арбат'
})

const budgetOptions = [
  { value: 'low', label: '💰 Эконом (до 2000₽)' },
  { value: 'medium', label: '💰💰 Средний (2000-5000₽)' },
  { value: 'high', label: '💰💰💰 Премиум (5000₽+)' }
]

const preferenceTypes = ['Романтический', 'Активный', 'Уютный', 'Веселый', 'Спокойный', 'Приключение', 'Гастрономический']

// Избранное
const favoritePlaces = ref([
  {
    id: 1,
    name: 'Ресторан "Ла Скала"',
    type: 'Романтический',
    address: 'ул. Тверская, 24',
    image: 'https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?w=400',
    rating: 4.8,
    reviewCount: 127,
    priceLevel: 3
  },
  {
    id: 2,
    name: 'Кофейня "Уют"',
    type: 'Уютный',
    address: 'ул. Арбат, 32',
    image: 'https://images.unsplash.com/photo-1501339847302-ac426a4a7cbb?w=400',
    rating: 4.9,
    reviewCount: 89,
    priceLevel: 2
  }
])

// ИИ анализ
const aiInsights = ref({
  topType: 'Романтические',
  avgSpending: 3500,
  topCategory: 'Рестораны',
  recommendation: 'Активный отдых'
})

// Методы
const uploadPhoto = () => {
  alert('Функция загрузки фото в разработке')
}

const editProfile = () => {
  alert('Редактирование профиля скоро будет доступно!')
}

const addNewDate = () => {
  alert('Добавление нового свидания в разработке')
}

const savePreferences = () => {
  alert('Предпочтения сохранены!')
  console.log('Сохраненные предпочтения:', preferences)
}

const removeFromFavorites = (placeId) => {
  favoritePlaces.value = favoritePlaces.value.filter(place => place.id !== placeId)
  alert('Удалено из избранного')
}

const planVisit = (placeId) => {
  const place = favoritePlaces.value.find(p => p.id === placeId)
  alert(`Запланировано посещение: ${place?.name || 'Место'}`)
}

const refreshAI = () => {
  alert('ИИ анализ обновлен!')
  // Здесь будет запрос к бэкенду для обновления анализа
}
</script>

<style scoped>
.dashboard-page {
  max-width: 1200px;
  margin: 0 auto;
}

.page-header {
  text-align: center;
  margin-bottom: 3rem;
}

.page-header h1 {
  font-size: 2.5rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.page-header p {
  color: #666;
  font-size: 1.1rem;
}

/* Couple Profile */
.couple-profile {
  background: white;
  border-radius: 20px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  overflow: hidden;
  margin-bottom: 2rem;
}

.profile-header {
  display: flex;
  align-items: center;
  padding: 2rem;
  gap: 2rem;
  background: linear-gradient(135deg, #fce7f3 0%, #fbcfe8 100%);
}

.avatar {
  position: relative;
}

.avatar-placeholder {
  width: 120px;
  height: 120px;
  background: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 3rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}

.avatar-upload {
  position: absolute;
  bottom: 0;
  right: 0;
  background: #e91e63;
  color: white;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  box-shadow: 0 3px 10px rgba(233, 30, 99, 0.3);
}

.profile-info h2 {
  font-size: 2rem;
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.profile-info p {
  color: #666;
  margin-bottom: 1rem;
}

.couple-stats {
  display: flex;
  gap: 2rem;
}

.stat {
  padding: 0.5rem 1rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 3px 10px rgba(0, 0, 0, 0.05);
}

.stat strong {
  color: #e91e63;
  font-size: 1.2rem;
}

.edit-profile {
  margin-left: auto;
  background: white;
  color: #e91e63;
  border: 2px solid #e91e63;
  padding: 0.8rem 1.5rem;
  border-radius: 50px;
  cursor: pointer;
  font-weight: 600;
  transition: all 0.3s;
}

.edit-profile:hover {
  background: #e91e63;
  color: white;
}

.profile-tabs {
  display: flex;
  background: #f8f9fa;
  border-top: 1px solid #e0e0e0;
}

.tab {
  flex: 1;
  padding: 1rem;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1rem;
  font-weight: 500;
  transition: all 0.3s;
  border-bottom: 3px solid transparent;
}

.tab:hover {
  background: #e9ecef;
}

.tab.active {
  background: white;
  border-bottom: 3px solid #e91e63;
  color: #e91e63;
}

/* Tab Content */
.tab-content {
  background: white;
  border-radius: 15px;
  padding: 2rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.05);
  margin-bottom: 2rem;
}

/* Dates History */
.dates-history h3,
.preferences h3,
.favorites h3,
.ai-analysis h3 {
  font-size: 1.8rem;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}

.dates-list {
  margin-bottom: 1.5rem;
}

.date-card {
  display: flex;
  gap: 1.5rem;
  padding: 1.5rem;
  border: 2px solid #f0f0f0;
  border-radius: 10px;
  margin-bottom: 1rem;
  transition: transform 0.3s;
}

.date-card:hover {
  transform: translateX(5px);
  border-color: #e91e63;
}

.date-image {
  flex-shrink: 0;
}

.img-placeholder {
  width: 80px;
  height: 80px;
  background: #f8f9fa;
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 2rem;
}

.date-info h4 {
  color: #2c3e50;
  margin-bottom: 0.5rem;
}

.date-info p {
  color: #666;
  margin-bottom: 0.5rem;
}

.date-rating {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 0.5rem;
}

.star {
  color: #ffc107;
  font-size: 1.2rem;
}

.rating-text {
  color: #666;
  font-weight: 500;
}

.date-note {
  color: #888;
  font-style: italic;
  font-size: 0.9rem;
}

/* Preferences */
.preferences-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-bottom: 2rem;
}

.preference-category {
  padding: 1.5rem;
  background: #f8f9fa;
  border-radius: 10px;
}

.preference-category h4 {
  color: #2c3e50;
  margin-bottom: 1rem;
  font-size: 1.2rem;
}

.preference-options {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
}

.preference-options label {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  cursor: pointer;
  color: #555;
}

.locations-input {
  width: 100%;
  padding: 0.8rem;
  border: 2px solid #e0e0e0;
  border-radius: 8px;
  font-size: 1rem;
  margin-top: 0.5rem;
}

.locations-input:focus {
  outline: none;
  border-color: #e91e63;
}

/* Favorites */
.favorites-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 1.5rem;
  margin-bottom: 1.5rem;
}

/* AI Analysis */
.ai-insights {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.insight-card {
  padding: 1.5rem;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border-radius: 10px;
}

.insight-card h4 {
  margin-bottom: 0.5rem;
  font-size: 1.1rem;
}

.insight-card p {
  margin: 0;
  line-height: 1.5;
}

/* Buttons */
.btn-primary {
  background: #e91e63;
  color: white;
  border: none;
  padding: 0.8rem 1.8rem;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.btn-primary:hover {
  background: #d81b60;
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(233, 30, 99, 0.3);
}

/* No data */
.no-data {
  text-align: center;
  color: #888;
  font-style: italic;
  padding: 2rem;
  background: #f8f9fa;
  border-radius: 10px;
  margin-bottom: 1.5rem;
}

@media (max-width: 768px) {
  .profile-header {
    flex-direction: column;
    text-align: center;
  }
  
  .couple-stats {
    justify-content: center;
    flex-wrap: wrap;
  }
  
  .edit-profile {
    margin: 1rem 0 0 0;
  }
  
  .profile-tabs {
    flex-wrap: wrap;
  }
  
  .tab {
    flex: 1 0 50%;
  }
  
  .date-card {
    flex-direction: column;
  }
}
</style>