<template>
  <div class="layout-width">
    <div class="aside">

      <div v-if="pageIndex == 0" class="page0">
        <div class="main">
            <div class="lbox">
                <div class="outtype">CorPus Output</div>

                <div class="sel01-box">
                    <div class="sel01">
                        <select v-model="page0data.selectClassEnd" @change="selectClass($event)">
                            <option value="NONE">Place Select Model</option>
                            <option v-for="(options,id) in page0data.selectClassData" :key="id" :value="options.id">
                                {{options.title}}
                            </option>
                        </select>
                    </div>
                </div>

                <div class="submit" @click="corPusOutPut">
                    Output
                </div>

            </div>
            <div class="rbox">
                <div class="outtype">Audio Output</div>

                <div class="text">
                    Save audio file to Wav and use sort rename audio file
                </div>

                <div class="submit" @click="audioOutPut">
                    Output
                </div>

            </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { corpus_outdataset, audio_outdata } from "@/api/common";
export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      pageIndex: 0,
      page0data:{
        selectClassData:[
          {id:1,title:"ChatGLM-6B"},
        ],
        selectClassEnd: "NONE",
        select_class_id: ""
      },
    }
    },
    methods:{

        corPusOutPut(){
            corpus_outdataset({
                select_class_id : this.page0data.select_class_id,
            }).then((res) => {
                if (res.code == 200){
                    // alert("ok")
                }
            });
        },

        audioOutPut(){
            audio_outdata({
                select_class_id : this.page0data.select_class_id,
            }).then((res) => {
                if (res.code == 200){
                    // alert("ok")
                }
            });
        },

        //类别选中
        selectClass(event){
            this.page0data.select_class_id = event.target.value; //获取option对应的value值 select_class_id是后台约定的提交数据的名称
        },
    }
}
</script>
<style rel="stylesheet/scss" lang="scss" scoped>
.page0{

    .sel01-box{
        position: absolute;left: 0;right: 0;margin: auto;top: 150px;
        display: flex; justify-content: center; align-items: center;width: 50%;
    }

    .sel01{display:inline-block;position:relative;z-index:2;font-size:1.6rem;height:3.6rem;line-height:3.6rem;width:8rem;flex:1;background:#111111;box-sizing:border-box;border-radius:.5rem;}
    .sel01:before{content:"";position:absolute;width:0;height:0;border:.5rem solid transparent;color: #fff;
    border-top-color:#e92f26;top:50%;right:1rem;cursor:pointer;z-index:-2;margin-top:-0.25rem;color: #fff;}
    .sel01 select{width:100%;border:none;height:3.6rem;background:transparent;background-image:none;-webkit-appearance:none;-moz-appearance:none;vertical-align:top;padding-left:1rem;color: #fff;}
    .sel01 select:focus{outline:none;color: #fff;}

    .text{
        position: absolute;top: 150px;padding: 15px;color: #fff;left: 0;right: 0;margin: 0 auto;
        width: 300px;text-align: center;border-radius: 5px;cursor: pointer;
    }

    .submit{
        position: absolute;bottom: 100px;padding: 15px;background-color: #0066ff;color: #fff;left: 0;right: 0;margin: 0 auto;
        width: 100px;text-align: center;border-radius: 5px;cursor: pointer;
    }

    .main{
        margin-top: 130px;
    }
    .outtype{
        font-size: 18px;
        color: #ffffff;
        text-align: center;
        font-weight: bold;
        padding-top: 40px;
    }
    .lbox{
        position: relative;
        float: left;
        background-color: #1F1F1F;
        width: calc(40% - 50px);
        border: 1px solid #5a5772;
        height: calc(100vh - 300px);
        margin-left: 10%;
    }
    .rbox{
        position: relative;
        float: right;
        background-color: #1F1F1F;
        width: calc(40% - 50px);
        border: 1px solid #5a5772;
        height: calc(100vh - 300px);
        margin-right: 10%;
        }
}
</style>