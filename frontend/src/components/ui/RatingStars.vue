<!-- src/components/ui/RatingStars.vue -->
<template>
  <div class="rating-stars">
    <span v-for="n in 5" :key="n" class="star">
      {{ getStar(n) }}
    </span>
    <span v-if="showNumber" class="rating-number">{{ rating.toFixed(1) }}</span>
  </div>
</template>

<script setup>
// Правильно объявляем пропсы
const props = defineProps({
  rating: {
    type: Number,
    required: true,
    default: 0
  },
  showNumber: {
    type: Boolean,
    default: true
  }
})

const getStar = (position) => {
  if (position <= Math.floor(props.rating)) {
    return '★'
  } else if (position - 0.5 <= props.rating) {
    return '⯨'
  } else {
    return '☆'
  }
}
</script>

<style scoped>
.rating-stars {
  display: flex;
  align-items: center;
  gap: 2px;
}

.star {
  color: #ffc107;
  font-size: 1.2rem;
}

.rating-number {
  margin-left: 0.5rem;
  color: #666;
  font-weight: 500;
  font-size: 0.9rem;
}
</style>