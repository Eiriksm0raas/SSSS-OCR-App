<script>
export default {
    emits: {
        cancelEvent() { return true; }
    },
    methods: {
        cancel() {
            this.$emit('cancelEvent');
        }
    }
};
</script>
<template>
    <aside @click="cancel">
        <main class="position-fixed start-50 top-50 translate-middle d-flex flex-column bg-dark-subtle rounded shadow">
            <header class="d-flex flex-row justify-content-end p-2">
                <button @click="cancel" class="btn-close"></button>
            </header>
            <slot></slot>
        </main>
    </aside>
</template>
<style scoped>
    aside {
        position: fixed;
        top: 0;
        left: 0;
        width: 100vw;
        height: 100vh;
        background-color: rgba(0, 0, 0, 0.5);
        z-index: 4;
    }

    main {
        z-index: 6;
        min-width: 200px;
    }
</style>