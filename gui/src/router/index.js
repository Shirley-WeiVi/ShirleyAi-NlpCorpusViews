import Vue from 'vue'
import VueRouter from 'vue-router'
import layout from '@/layout/Layout.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '',
    component: layout,
    nav: true,
    children: [
      {
        path: '/',
        name: 'Corpus',
        component: () => import('@/views/Corpus.vue'),
        meta: { title: 'ShirleyAi NlpCorpusViews Gui'}
      },
      {
        path: '/audio',
        name: 'Audio',
        component: () => import('@/views/Audio.vue'),
        meta: { title: 'ShirleyAi NlpCorpusViews Gui'}
      },
      {
        path: 'output',
        name: 'Output',
        component: () => import('@/views/Output.vue'),
        meta: { title: 'ShirleyAi NlpCorpusViews Gui'}
      },
    ]
  }
]

let originPush=VueRouter.prototype.push;

VueRouter.prototype.push=function(location,resolve,reject){
  if(resolve && reject){
     //如果成功 调用原来的push方法  
          originPush.call(this,location,resolve,reject); 
              }else{
          originPush.call(this,location,()=>{},()=>{}); }    
 }

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
