<template>
    <div class="logo">
        <img src="../image/logo.png" alt="Логотип РЖД">
    </div>
    <div class="video">
        <video-player :options="videoOptions" />
    </div>
</template>

<style>
.video {
    width: 600px;
    margin: auto;
    padding: 10px;
    border-bottom: 1px solid #ddd;
}
</style>
  
<script>
import VideoPlayer from '@/components/VideoPlayer.vue';

export default {
    name: 'VideoExample',
    components: {
        VideoPlayer
    },
    data() {
        return {
            videoOptions: {
                autoplay: true,
                controls: true
            }
        };
    }
};
</script>