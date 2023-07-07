<template>
    <div class="layout-header">
      <div class="layout-width">
        <div class="logo">
          <div class="ShirleyAi">ShirleyAi</div>
        </div>
        <div class="logo">
          <div class="NlpCorpusViews">NlpCorpusViews</div>
        </div>

        <div class="nav">
          <div class="nav-item Transition-03s" :class="{'nav-item-activate':index === 'Corpus'}" @click="toRoute('Corpus')">Corpus</div>
          <div class="nav-item Transition-03s" :class="{'nav-item-activate':index === 'Audio'}" @click="toRoute('Audio')">Audio</div>
        </div>

        <div class="about" @click="oepnAbout">About ▼</div>

        <div class="about_popot" v-if="about">
          <div class="item"><a target="_black" href="https://github.com/Shirley-WeiVi">About ShirleyAi</a></div>
          <div class="item"><a target="_black" href="https://www.weivird.com/#/">Author ©WeiVi</a></div>
          <div class="item"><a target="_black" href="https://github.com/weivis">Author Github</a></div>
          <div class="item"><a target="_black" href="https://github.com/Shirley-WeiVi/ShirleyAi-NlpCorpusViews">About NlpCorpusViews</a></div>
        </div>

        <div class="toOutputPage" :class="{'toOutputPage-activate':index === 'Output'}" @click="toRoute('Output')">Output Set</div>

      </div>
    </div>
</template>

<script>
export default {
  name: 'Header',
  data() {
    return {
      index: 'Corpus',
      about: false
    };
  },
  created(){
  },
  methods:{
    toRoute(routename){
      this.index = routename
      this.$router.push({name:routename})
    },
    oepnAbout(){
      if (this.about == true){
        this.about = false
      }else{
        this.about = true
      }
    }
  }
}
</script>
<style rel="stylesheet/scss" lang="scss" scoped>
</style>