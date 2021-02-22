import { createRouter, createWebHistory } from 'vue-router'
import Pocetna from '../views/Pocetna.vue'


const routes = [
  {
    path: '/',
    name: 'Pocetna',
    component: Pocetna
  },
  {
    path: '/verifikacija',
    name: 'Verifikacija',
   
    component: () => import('../views/Verifikacija.vue')
  },
  {
    path: '/izbori',
    name: 'Izbori',
   
    component: () => import('../views/Izbori.vue')
  },
  {
    path: '/registracija',
    name: 'Registracija',
   
    component: () => import('../views/Registracija.vue')
  },
  {
    path: '/rezultati',
    name: 'Rezultati',
   
    component: () => import('../views/Rezultati.vue')
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
