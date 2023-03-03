<script>
import BaseMenu from './BaseMenu.vue';
import MenuSetting from '../data/menuSetting';

export default {
    emits: { 
        visitMenuEvent(payload) { return true; }
    },
    components: { BaseMenu },
    data() {
        return {
            settings: [
                new MenuSetting("Picture from PI", 1),
                new MenuSetting("Picture from URL", 2),
            ]
        }
    },
    methods: {
        handleMenuVisit(menuIndex) {
            this.$emit('visitMenuEvent', menuIndex);
        }
    }
}
</script>
<template>
    <BaseMenu title="OCR main menu" :menuSettings="settings" @visit-menu-event="handleMenuVisit">
    </BaseMenu>
</template>
<style scoped>

</style>