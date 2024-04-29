import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import axios from 'axios';

// Een interceptor toevoegen om de token dynamisch in te stellen voor elke request
axios.interceptors.request.use(function (config) {
    // Haal de token uit localStorage
    const token = localStorage.getItem('token');
    // Als de token bestaat, configureer dan de Authorization header
    config.headers.Authorization = token ? `Bearer ${token}` : '';
    return config;
});

const app = createApp(App);
app.use(router);
app.mount('#app');
