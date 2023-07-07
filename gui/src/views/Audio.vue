<template>
  <div class="layout-width">
    <div class="aside">

      <div class="update_puput" v-if="showupdatepoput == true">
        <input type="file" name="import_file" v-on:change="selectedFile($event)">
        <div class="button-li">
          <div class="button" @click="updatefile">Update</div>
          <div class="button" @click="showupdatepoput = false">Close</div>
          
        </div>
      </div>

      <div v-if="pageIndex == 0" class="page0">
        <div class="main">
            <div class="bar">
                <div class="title">Audio File List</div>
                <div class="button" @click="showupdatepoput = true">Update Audio</div>
            </div>
            <div class="filelist">
              <div class="item" v-for="(item, index) in page0data.table" :key="index + 'page0list'">
                <div class="del" @click="deleteFile(item.data)">Delete</div>
                <!-- <div class="edit">Edit</div> -->
                <div class="sourcefile">SourceFileName: {{item.data.source_name}}</div>
                <div class="storagefile_name">StorageFileName: {{item.data.storagefile_name}}</div>
                <div class="rename">Out reset name: {{item.sort}}</div>
              </div>
            </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { upload, audio_create, audio_query, audio_delete } from "@/api/common";
export default {
  name: 'HomeView',
  components: {
  },
  data() {
    return {
      showupdatepoput:false,
      file: null,
      pageIndex: 0,
      page0data:{
        table:[
        ]
      },
    }
  },
  created(){
    this.getList()
  },
  methods:{
    getList(){
      audio_query({}).then((res) => {
        console.log(res)
        if (res.code == 200){
          this.page0data.table = res.data
        }
      });
    },
    updatefile(){
      const formData = new FormData();
      formData.append("file", this.file);
      formData.append("uploadKey", 'audio');
      this.$http(upload(formData), (res) => {
        console.log(res)
        if (res.code == 200) {

          audio_create({
                source_name: res.data.sourcefilename,
                storagefile_name: res.data.filename
          }).then((res) => {
            if (res.code == 200){
                this.showupdatepoput = false
                this.getList()
            }
          });

        }
      })
    },
    deleteFile(item){
      audio_delete({
        fileid: item.id
      }).then((res) => {
        if (res.code == 200){
          this.getList()
        }
      });
    },
    selectedFile(event) {
      this.file = event.target.files[0]
    },
  }
}
</script>
<style rel="stylesheet/scss" lang="scss" scoped>

.update_puput{
  width: 400px;
  height: 160px;
  position: absolute;
  left: 0;
  right: 0;
  top: 0;
  bottom: 0;
  margin: auto;
  background-color: #272727;
  input{color: #ffffff;padding: 25px;}
  border-radius: 8px;
  .button-li{
    padding: 25px;
    .button{
      padding: 15px;
      padding-top: 10px;
      padding-bottom: 10px;
      float: right;
      background-color: #000000;
      font-size: 14px;
      color: #ffffff;margin-left: 15px;
    }
  }
}

.page0{
    .main{
        .bar{
            display: flow-root;
            padding-top: 15px;
            width: 100%;
            .title{
                font-size: 14px;
                color: #ffffff;
                line-height: 45px;
                float: left;
            }
            .button{
                line-height: 45px;padding-left: 25px;padding-right: 25px;
                background-color: #1F1F1F;
                float: right;
                color: #ffffff;
                font-size: 14px;
                cursor: pointer;
            }
        }
        .filelist{
          overflow-y: scroll;
          height: calc(100vh - 165px);
          margin-top: 15px;
          .item{
            margin-bottom: 15px;
            display: flow-root;
            width: calc(100% - 30px);
            background-color: #1F1F1F;
            line-height: 50px;
            padding-left: 15px;
            padding-right: 0px;
            color: #ffffff;
            font-size: 14px;
            .edit{
              float: right;
              margin-right: 30px;
              cursor: pointer;
            }
            .del{
              float: right;
              background-color: #262626;
              line-height: 50px;
              padding-left: 30px;
              padding-right: 30px;
              cursor: pointer;
            }
            .sourcefile{
              float: left;
            }
            .storagefile_name{
              margin-right: 10%;
              float: right;
            }
            .rename{
              margin-right: 5%;
              float: right;
            }
          }
        }
    }
}
</style>