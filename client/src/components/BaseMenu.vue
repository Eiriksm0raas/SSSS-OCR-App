<script>
export default {
    props: {
        title: {
            type: String,
            default: () => ("Menu")
        },
        menuSettings: {}, // MenuSetting
    },
    emits: { 
        visitMenuEvent(payload) { return true; }
    }
}
</script>
<template>
    <main class="ocr-menu d-flex flex-column m-auto bg-light p-5 mt-0 mt-md-5 rounded">
        <h2 class="text-center">{{ title }}</h2>
            <button
                v-for="setting of menuSettings"
                @click="() => $emit('visitMenuEvent', setting.index)" 
                class="btn btn-primary mt-5"
                >{{ setting.text }}</button>

            <slot></slot>
    </main>
</template>
<style scoped>
@media (min-width: 576px) {
  .ocr-menu {
    width: 100vw;
  }
}

@media (min-width: 768px) {
  .ocr-menu {
    width: 70vw;
  }
}

@media (min-width: 992px) {
  .ocr-menu {
    width: 50vw;
  }
}

@media (min-width: 1200px) {
  .ocr-menu {
    width: 45vw;
  }
}

@media (min-width: 1400px) {
  .ocr-menu {
    width: 40vw;
  }
}
</style>