import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../components/Dashboard.vue'
import Reservation from '../components/Reservation.vue'
import Chambres from '../components/Chambres.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    
    {
      path: '/',
      component: Dashboard
    },
    {
      path: '/reservations',
      component: Reservation
    },
    {
      path: '/chambres',
      component: Chambres
    },


  ],
})

export default router
