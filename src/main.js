import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'

import axios from 'axios'

createApp(App).config.productionTip = false;


window.axios = axios.create({
    baseURL: 'http://127.0.0.1:5000/'
})


createApp(App).use(store).use(router).mount('#app')
