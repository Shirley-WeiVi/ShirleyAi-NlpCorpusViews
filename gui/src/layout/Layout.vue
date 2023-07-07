<template>
    <div style="overflow: hidden">
        <layout-header/>
        <layout-appmain/>           
        <layout-footer/>
    </div>
</template>

<script>
import appmain from './AppMain'
import header from './Header'
import footer from './Footer.vue'
    export default {
        name:'layout',
        methods: { //事件处理器
        },
        components: { //定义组件
            'layout-appmain':appmain,
            'layout-header':header,
            'layout-footer':footer
        }
    }
</script>

<style rel="stylesheet/scss" lang="scss" scoped>
</style>