<script>
import Alert from './Alert.vue';
import BaseMenu from './BaseMenu.vue';
import MenuSetting from '../data/menuSetting';
import { getImageConverted } from '../data/requests';

export default {
    emits: {
        visitMenuEvent(payload) { return true; }
    },
    components: { BaseMenu, Alert },
    data() {
        return {
            settings: [
                new MenuSetting("Main menu", 0),
            ],
            imgSrc: '',
            result: '',
            showResult: false,
        }
    },
    methods: {
        handleMenuVisit(menuIndex) {
            this.$emit('visitMenuEvent', menuIndex);
        },
        async upload() {
            if(this.imgSrc != '') {
                this.result = '';
                let r = await getImageConverted(this.imgSrc);
                console.log(r);
                for(const word of r) {
                    this.result += Object.keys(word)[0] + ' ';
                }

                if(this.result != '') this.showResult = true;
            }
        },
    },
    computed: {
        imgToShow() {
            if(/\.(jpe?g|png)$/.test(this.imgSrc)) {
                return this.imgSrc;
            } else {
                return '/default.jpg';
            }
        }
    }
}
</script>
<template>
    <Alert v-if="showResult" @cancel-event="() => showResult = false">
        <div class="d-flex flex-column p-3">
            <h3>Result</h3>
            <p>{{ this.result }}</p>
        </div>
    </Alert>
    <BaseMenu 
        title="Convert picture from URL" 
        :menuSettings="settings"
        @visit-menu-event="handleMenuVisit">

        <form class="form-control d-flex flex-column mt-5">
            <img :src="imgToShow" class="align-self-center" />
            <div class="d-flex flex-row w-100 mt-3 justify-content-center">
                <input v-model="imgSrc" type="text" placeholder="Image url" class="form-control mx-2 w-50 align-self-center" />
                <button @click="upload" type="button" class="btn mx-2 btn-success">convert</button>
            </div>
        </form>

    </BaseMenu> 
</template>
<style scoped>
    img {
        max-height: 50vh;
        max-width: 30vw;
    }
</style>