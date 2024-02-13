import { createApp } from "vue";
import App from "./App.vue";
import VueRouter from "vue-router";
import "./index.css";
import router from './router'
import { setupCalendar } from 'v-calendar';

const app = createApp(App).use(router);

app.use(VueRouter);

app.mount("#app");

app.use(setupCalendar, {})
