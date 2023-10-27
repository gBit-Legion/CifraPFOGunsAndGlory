import { createRouter, createWebHashHistory } from "vue-router";
import Home from "./components/Home.vue";
import Result from "./components/Result.vue";

export default createRouter({
    history: createWebHashHistory(),
    routes: [
        { path: '/home', component: Home, alias: '/' },
        { path: '/result', component: Result }
    ]
})