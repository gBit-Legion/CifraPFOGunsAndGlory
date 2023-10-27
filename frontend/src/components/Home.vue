<template>
    <div class="logo">
        <img src="../image/logo.png" alt="Логотип РЖД">
    </div>
    <Drag />
</template>

<style>
@font-face {
    font-family: "TTFirsNeue-Regular";
    src: url("../fonts/TTFirsNeue-Regular.ttf");
}

@font-face {
    font-family: "TTFirsNeue-bold";
    src: url("../fonts/TTFirsNeue-Bold.ttf");
}

* {
    font-family: TTFirsNeue-Regular;
}

.logo {
    width: 143px;
    margin: 0 auto;
}
</style>

<script>
import Drag from './Drag.vue';

export default {
    components: {
        Drag
    },

    methods: {

    }
}
</script>