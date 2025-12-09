// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'

// Импортируем компоненты (используем ленивую загрузку)
const HomePage = () => import('../views/HomePage.vue')
const Recommendations = () => import('../views/Recommendations.vue')
const CoupleDashboard = () => import('../views/CoupleDashboard.vue')

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/recommendations',
    name: 'Recommendations',
    component: Recommendations
  },
  {
    path: '/dashboard',
    name: 'CoupleDashboard',
    component: CoupleDashboard
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router