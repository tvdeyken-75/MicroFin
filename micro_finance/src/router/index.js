import { createRouter, createWebHistory } from 'vue-router';
import UserHome from '../views/UserHome.vue';
import UserLogin from '../views/UserLogin.vue';

const routes = [
  {
    path: '/',
    name: 'UserHome',
    component: UserHome,
    meta: { requiresAuth: true } // Vereist authenticatie om deze pagina te bekijken
  },
  {
    path: '/login',
    name: 'UserLogin',
    component: UserLogin
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    // Controleer of er een token in de localStorage is
    if (!localStorage.getItem('token')) {
      // Als er geen token is, redirect naar de login pagina
      next({ name: 'UserLogin' });
    } else {
      // Als er een token is, ga door naar de route
      next();
    }
  } else {
    // Voor routes die geen authenticatie vereisen, ga direct door
    next();
  }
});

export default router;
