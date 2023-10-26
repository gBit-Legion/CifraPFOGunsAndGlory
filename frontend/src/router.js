import { createRouter, createWebHashHistory } from "vue-router";
import Home from "./components/Home.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/home', component: Home, alias: '/' }
    ]
})