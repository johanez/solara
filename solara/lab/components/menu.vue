<template>
    <v-menu
        v-model="show_menu"
        :absolute="use_absolute"
        offset-y
    >
        <template v-if="context" v-slot:activator="{ on }">
            <div v-for="(element, index) in activator"
                :key="index"
                @contextmenu.prevent="show($event, on)">
                <jupyter-widget :widget="element"></jupyter-widget>
            </div>
        </template>
        <template v-else v-slot:activator="{ on }">
            <div v-for="(element, index) in activator"
                :key="index"
                v-on="on"
                style="width: fit-content; display: inline-block;"
                >
                <jupyter-widget :widget="element"></jupyter-widget>
            </div>
        </template>
        <v-list v-for="(element, index) in children" :key="index" style="padding: 0;">
            <jupyter-widget :widget="element"  :style="style" ></jupyter-widget>
        </v-list>
    </v-menu>
</template>

<script>
module.exports = {
    methods: {
        show(e, on) {
            // hide menu, and trigger the event on the next tick, otherwise vue does not see
            // `show_menu` changing and will no do any animation
            this.show_menu = false;
            this.$nextTick(() => {
                on.click(e)
            })
        }
    }
}
</script>
