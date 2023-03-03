<script>
import Alert from './components/Alert.vue';
import MainMenu from './components/MainMenu.vue';
import UrlMenu from './components/UrlMenu.vue';

export default {
  components: { Alert, MainMenu, UrlMenu },
  data() {
    return {
      menuMain: true,
      menuUpload: false,
      menuUrl: false,
    }
  },
  methods: {
    setAllMenusToFalse() {
      this.menuMain = false;
      this.menuUpload = false;
      this.menuUrl = false;
    },
    handleMenuVisit(menuIndex) {
      this.setAllMenusToFalse();

      switch(menuIndex) {
        case 0:
          this.menuMain = true;
          break;

        case 1:
          this.menuUpload = true;
          break;

        case 2:
          this.menuUrl = true;
          break;
      }

    }
  }
}
</script>
<template>
  <MainMenu v-if="menuMain" @visit-menu-event="handleMenuVisit" />
  <UrlMenu v-if="menuUrl" @visit-menu-event="handleMenuVisit" />
</template>
<style scoped>

</style>
