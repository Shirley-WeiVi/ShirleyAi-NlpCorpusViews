<template>
  <div class="layout-width">

    <div class="createNewIndex" v-if="page0data.createNewIndexFromWindwos">
      <div class="title">input you new index name</div>
      <input type="text" class="input" v-model="page0data.createNewIndexFrom.text">
      <div class="button" @click="createIndex">OK</div>
      <div class="button" @click="page0data.createNewIndexFromWindwos = false">NO</div>
    </div>

    <div class="deletePupot" v-if="page0data.deleteIndex == true">
      <div class="title">Are you sure you want to delete it? ( {{page0data.deleteItem.title}} )</div>
      <div class="button" @click="deleteIndex(page0data.deleteItem)">Delete</div>
      <div class="button" @click="page0data.deleteIndex = false,page0data.deleteItem=null">NO</div>
    </div>

    <div class="aside">

      <div v-if="pageIndex == 0" class="page0">
        <div class="main">
          <div class="PlaceCreate" v-if="page0data.table == []">Please create first</div>
          <div class="list" v-if="!page0data.table == []">
            
            <div class="table-name">
              Create a date index or click to enter the index to be edited
            </div>
            <div class="table-data">
              <div class="table-data-item" v-for="(item, index) in page0data.table" :key="index + 'page0list'" >
                <div class="span" @click="getSessionlist(item)">
                  Set: {{item.title}}
                </div>
                <div class="span" @click="getSessionlist(item)">
                  Session Count: {{item.session_count}}
                </div>
                <div class="del" @click="opendelete(item)">Delete</div>
              </div>
            </div>

          </div>
            <div class="button" @click="page0data.createNewIndexFromWindwos = true">
              Create new Date index for data set
          </div>
        </div>
      </div>

      <div v-if="pageIndex == 1" class="page1">
        <div class="lbox">
          <div class="toback" @click="backIndex">
            <div class="ico"><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" fill="none" version="1.1" width="18.000004408766472" height="18.000004408766472" viewBox="0 0 18.000004408766472 18.000004408766472"><defs><clipPath id="master_svg0_12_2009"><rect x="18.000004408766472" y="18" width="18" height="18" rx="0"/></clipPath></defs><g transform="matrix(-1,2.4493147066095844e-7,-2.4493147066095844e-7,-1,36.000013226299416,35.99999559123245)" clip-path="url(#master_svg0_12_2009)"><g><path d="M21.750004408766472,21C21.55108440876647,21,21.360324408766473,21.07902,21.219674408766473,21.21967C21.07902440876647,21.36032,21.000004408766472,21.55108,21.000004408766472,21.75C21.000004408766472,21.75,21.000004408766472,32.25,21.000004408766472,32.25C21.000004408766472,32.4489,21.07902440876647,32.6397,21.219674408766473,32.7803C21.360324408766473,32.9209,21.55108440876647,33,21.750004408766472,33C21.750004408766472,33,24.750004408766472,33,24.750004408766472,33C25.164214408766473,33,25.500004408766472,33.3358,25.500004408766472,33.75C25.500004408766472,34.1642,25.164214408766473,34.5,24.750004408766472,34.5C24.750004408766472,34.5,21.750004408766472,34.5,21.750004408766472,34.5C21.15326440876647,34.5,20.580974408766473,34.2629,20.15901440876647,33.841C19.73705640876647,33.419,19.500004408766472,32.8468,19.500004408766472,32.25C19.500004408766472,32.25,19.500004408766472,21.75,19.500004408766472,21.75C19.500004408766472,21.15326,19.73705640876647,20.58097,20.15901440876647,20.15901C20.580974408766473,19.737052,21.15326440876647,19.5,21.750004408766472,19.5C21.750004408766472,19.5,24.750004408766472,19.5,24.750004408766472,19.5C25.164214408766473,19.5,25.500004408766472,19.835786,25.500004408766472,20.25C25.500004408766472,20.66421,25.164214408766473,21,24.750004408766472,21C24.750004408766472,21,21.750004408766472,21,21.750004408766472,21C21.750004408766472,21,21.750004408766472,21,21.750004408766472,21ZM29.469674408766473,22.71967C29.76250440876647,22.42678,30.237404408766473,22.42678,30.530304408766472,22.71967C30.530304408766472,22.71967,34.28030440876647,26.46967,34.28030440876647,26.46967C34.57320440876647,26.76256,34.57320440876647,27.23745,34.28030440876647,27.53032C34.28030440876647,27.53032,30.530304408766472,31.2803,30.530304408766472,31.2803C30.237404408766473,31.5732,29.76250440876647,31.5732,29.469674408766473,31.2803C29.176804408766472,30.9874,29.176804408766472,30.5125,29.469674408766473,30.2197C29.469674408766473,30.2197,31.93930440876647,27.75,31.93930440876647,27.75C31.93930440876647,27.75,24.750004408766472,27.75,24.750004408766472,27.75C24.33579440876647,27.75,24.000004408766472,27.41422,24.000004408766472,27C24.000004408766472,26.58578,24.33579440876647,26.25,24.750004408766472,26.25C24.750004408766472,26.25,31.93930440876647,26.25,31.93930440876647,26.25C31.93930440876647,26.25,29.469674408766473,23.78033,29.469674408766473,23.78033C29.176804408766472,23.48743,29.176804408766472,23.01256,29.469674408766473,22.71967C29.469674408766473,22.71967,29.469674408766473,22.71967,29.469674408766473,22.71967Z" fill-rule="evenodd" fill="#FFFFFF" fill-opacity="1"/></g></g></svg></div>
            <div class="text" >{{page0data.selectIndexItem.title}}</div>
          </div>
          <div class="itemlist">
            <div class="itemlist-name">Session ID : Content Abstract</div>
            <div class="itemlist-item">
              <div class="itemlist-item-i" v-for="(item, index) in page1data.table" :key="index + 'page1list'" @click="getSessionData(item)">
                {{item.id}}, {{item.session_abstract}}
              </div>
            </div>
          </div>
          <div class="CreateCorpusSet" @click="sendCreateSession">
            Create New Corpus Set
          </div>
        </div>
        <div class="rbox" v-if="page1data.showInput == true">
          <div class="header">
            <div class="l"> She</div>
            <div class="r">ME</div>
          </div>
          <div class="content">
              <div class="item" v-for="(item, index) in page1data.session" :key="index + 'page1session'">
                <div v-if="item.questions_and_answers_type == 2">
                  <div class="li">
                    <div class="she">
                      {{item.data}}
                    </div>
                  </div>
                  <div class="li">
                    <div class="shesourcetext">{{item.source_msg_data}}</div>
                  </div>
                </div>
                <div v-if="item.questions_and_answers_type == 1">
                  <div class="li">
                    <div class="me">
                      {{item.data}}
                    </div>
                  </div>
                  <div class="li">
                    <div class="mesourcetext">{{item.source_msg_data}}</div>
                  </div>
                </div>
              </div>
          </div>
          <div class="sumbit">
            <div class="inputbox">
              <div class="title">Chinese</div>
              <input type="text" class="input" v-model="page1data.input">
              <div class="title">Source Msg Text</div>
              <input type="text" class="input" v-model="page1data.input_source_test">
            </div>
            <div class="control">
              <div class="info">
                Session ID: {{page1data.sessionid}}    Data len: {{page1data.datacount}}
              </div>
              <div class="delete" @click="deleteSession">Click DeleteSession</div>
              

              <div class="botton" style="background-color:#264AFF" @click="sendSession(1)">Sumbit  Me</div>
              <div class="botton" style="background-color:#FF006A" @click="sendSession(2)">Sumbit  She</div>
              <div class="botton" style="background-color:#FF006A" @click="Withdraw">Withdraw</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import { index_query, index_create, index_delete, session_query, session_create, data_query, data_create, data_withdraw, session_delete } from "@/api/common";
export default {
  name: 'HomeView',
  components: {
  },
  created(){
    this.getIndexlist()
  },
  data() {
    return {
      pageIndex: 0,
      page0data:{
        deleteItem:null,
        deleteIndex: false,
        createNewIndexFromWindwos: false,
        createNewIndexFrom:{
          text: ""
        },
        table:[
        ],
        selectIndexItem: null
      },
      page1data:{
        createSessionWind: false,
        input: "",
        input_source_test: "",
        showInput: false,
        sessionid: 0,
        datacount: 0,
        table:[
        ],
        session:[
        ],
        selectSessionItem: {}
      }
    }
  },
  methods:{
    opendelete(item){
      this.page0data.deleteItem = item
      this.page0data.deleteIndex = true
    },
    backIndex(){
      this.getIndexlist()
      this.page0data.selectIndexItem = null;
      this.page1data.showInput = false
      this.pageIndex = 0
    },
    getIndexlist(){
      index_query({}).then((res) => {
        console.log(res)
        if (res.code == 200){
          this.page0data.table = res.data
        }
      });
    },
    createIndex(){
      index_create({
        title: this.page0data.createNewIndexFrom.text
      }).then((res) => {
        console.log(res)
        if (res.code == 200){
          this.page0data.table = res.data
          this.page0data.createNewIndexFromWindwos = false
          this.page0data.createNewIndexFrom.text = ""
          this.getIndexlist()
        }
      });
    },
    deleteIndex(item){
      index_delete({
        index_id: item.id
      }).then((res) => {
        console.log(res)
        if (res.code == 200){
          this.page0data.deleteIndex = false
          this.page0data.deleteItem = null
          this.getIndexlist()
        }
      });
    },
    getSessionlist(item){
      this.page0data.selectIndexItem = item
      session_query({
        index_id : item.id
      }).then((res) => {
        if (res.code == 200){
          this.page1data.table = res.data
          this.pageIndex = 1
        }
      });
    },
    getSessionData(item){
      this.page1data.selectSessionItem = item
      data_query({
        session_id : item.id
      }).then((res) => {
        if (res.code == 200){
          console.log(res.data)
          this.page1data.session = res.data.data
          this.page1data.showInput = true
          this.page1data.datacount = res.data.datacount
          this.page1data.sessionid = item.id
        }
      });
    },
    sendCreateSession(){
      session_create({
        index_id : this.page0data.selectIndexItem.id
      }).then((res) => {
        if (res.code == 200){
          this.getSessionlist(this.page0data.selectIndexItem)
        }
      });
    },
    sendSession(questions_and_answers_type){
      data_create({
        session_id : this.page1data.selectSessionItem.id,
        questions_and_answers_type: questions_and_answers_type,
        data: this.page1data.input,
        source_msg_data: this.page1data.input_source_test
      }).then((res) => {
        if (res.code == 200){
          this.page1data.input = ""
          this.page1data.input_source_test = ""
          this.getSessionData(this.page1data.selectSessionItem)
        }
      });
    },
    deleteSession(){
      session_delete({
        session_index_id : this.page1data.selectSessionItem.id,
      }).then((res) => {
        if (res.code == 200){
          this.getSessionlist(this.page0data.selectIndexItem)
          this.page1data.showInput = false
        }
      });
    },
    Withdraw(){
      data_withdraw({
        session_id : this.page1data.selectSessionItem.id,
      }).then((res) => {
        if (res.code == 200){
          this.getSessionData(this.page1data.selectSessionItem)
        }
      });
    }
  }
}
</script>
<style rel="stylesheet/scss" lang="scss" scoped>
.aside{
  width: 100%;
  height: calc(100vh - 116px);
  margin-top: 25px;
}
.deletePupot{
  z-index: 9999;
  width: 400px;
  position: absolute;
  left: 0;
  right: 0;
  // bottom: 0px;
  top: 20%;
  height: 100px;
  padding: 25px;
  margin: auto;
  background-color: #000000;
  border-radius: 8px;
  .title{
    color: #ffffff;
    padding-bottom: 20px;
    font-size: 14px;
  }
  input{
    width: 100%;
    border: 0;
    height: 30px;
    padding: 0;
  }
  .button{
    background-color: #3f3f3f;
    float: right;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 25px;
    padding-right: 25px;
    margin-top: 25px;margin-left: 20px;
    color: #ffffff;
    font-size: 14px;
  }
}
.createNewIndex{
  z-index: 9999;
  width: 400px;
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0px;
  top: 10vh;
  height: 140px;
  padding: 25px;
  margin: auto;
  background-color: #000000;
  border-radius: 8px;
  .title{
    color: #ffffff;
    padding-bottom: 20px;
    font-size: 14px;
  }
  input{
    width: 100%;
    border: 0;
    height: 30px;
    padding: 0;
  }
  .button{
    background-color: #3f3f3f;
    float: right;
    padding-top: 10px;
    padding-bottom: 10px;
    padding-left: 25px;
    padding-right: 25px;
    margin-top: 25px;margin-left: 20px;
    color: #ffffff;
    font-size: 14px;
  }
}
.page0{
  .main{
    background-color: #1F1F1F;
    width: 100%;
    height: calc(100vh - 116px);
    position: relative;
    display: flow-root;
  }
  .list{
    width: calc(100% - 50px);
    margin: 0 auto;
    margin-top: 40px;
    .table-name{
      font-size: 18px;
      color: #8a8a8a;
      padding-bottom: 40px;
    }
    .table-data{
      overflow-y: scroll;
      height: calc(100vh - 320px);
      .table-data-item{
        width: calc(50% - 70px);
        padding-left: 25px;
        // padding-right: 25px;
        margin-right: 45px;
        line-height: 60px;
        height: 60px;
        float: left;
        background-color: #131313;
        margin-bottom: 20px;
        color: #ffffff;
        font-size: 12px;
        .span{width: 40%;float: left;}
        .del{
          padding-left: 25px;
          padding-right: 25px;
          float: right;
          background-color: #2c2c2c;
        }
      }
    }
  }
  .PlaceCreate{
    text-align: center;
    font-size: 32px;
    font-weight: bold;
    padding-top: 300px;
    color: #6e6e6e;
  }
  .button{
    height: 50px;
    width: 300px;
    text-align: center;
    min-width: 200px;
    background-color: #264AFF;
    position: absolute;
    bottom: 25px;
    left: 25px;
    line-height: 50px;
    padding-left: 25px;
    padding-right: 25px;
    color: #ffffff;
    font-size: 12px;
  }
}
.page1{
  .lbox{
    float: left;
    width: 300px;
    // height: 100vh;
    .toback{
      height: 45px;
      width: calc(100% - 30px);
      padding-left: 15px;
      padding-right: 15px;
      background-color: #323232;
      .ico{float: left;padding-top: 14px;margin-right: 15px;}
      .text{
        float: left;
        text-align: center;
        color: #ffffff;
        line-height: 45px;
        font-size: 14px;
        font-weight: bold;
      }
    }
    .itemlist{
      width: calc(100% - 30px);
      background-color: #1F1F1F;
      padding-left: 15px;
      padding-right: 15px;
      .itemlist-name{
        font-size: 10px;color: #6D6D6D;padding-top: 15px;padding-bottom: 15px;
      }
      .itemlist-item{
        overflow-y: scroll;
        height: calc(100vh - 250px);
      }
      .itemlist-item-i{
        width: 100%;
        overflow: hidden;
        white-space: nowrap;
        text-overflow: ellipsis;
        font-size: 12px;
        color: #ffffff;padding-bottom: 10px;
        cursor: pointer;
      }
    }
    .CreateCorpusSet{
      background-color: #264AFF;
      color: #ffffff;
      line-height: 45px;
      height: 45px;
      text-align: center;
      font-size: 14px;
      cursor: pointer;
    }
  }
  .rbox{
    float: right;
    width: calc(100% - 320px);
    height: 50vh;
    font-size: 14px;
    font-weight: bold;
    .header{
      background-color: #1F1F1F;
      color: #ffffff;
      padding: 25px;
      display: flow-root;
      .l{
        float: left;
      }
      .r{
        float: right;
      }
    }
    .content{
      background-color: #1F1F1F;
      padding-left: 25px;
      padding-right: 25px;
      overflow-y: scroll;
      height: calc(100vh - 470px);
      padding-bottom: 30px;
      .item{
        font-size: 12px;
        color: #ffffff;
        display: flow-root;padding-bottom: 10px;
        .li{
          display: flow-root;
        }
        .she{
          float: left;
          padding: 10px;
          background-color: #FF006A;
          border-radius: 8px;
        }
        .me{
          float: right;
          padding: 10px;
          background-color: #264AFF;
          border-radius: 8px;
        }
        .shesourcetext{
          float: left;
          padding: 10px;
          padding-top: 6px;
          color: #a3a3a3;
        }
        .mesourcetext{
          padding: 10px;
          padding-top: 6px;
          color: #a3a3a3;
          float: right;
        }
      }
    }
    .sumbit{
      padding: 25px;
      padding-top: 0;
      padding-bottom: 25px;
      background-color: #1F1F1F;
      .inputbox{
        .title{
          width: calc(100% - 40px);
          font-size: 12px;
          color: #ffffff;
          padding: 10px;
          padding-left: 0;
          font-weight: 400;
        }
        .input{
          height: 20px;
          width: calc(100% - 30px);
          background-color: #111111;
          color: #ffffff;
          border: 0px;
          padding: 15px;
        }
      }
      .control{
        height: 35px;padding-top: 25px;
        .info{
          color: #949494;
          font-size: 14px;
          font-weight: 400;
          float: left;
          line-height: 39px;
        }
        .delete{
          margin-left: 25px;
          float: left;
          line-height: 39px;
          color: #949494;
          font-size: 14px;
          font-weight: 400;
          cursor: pointer;
        }
        .botton{
          padding: 10px;
          padding-left: 25px;
          padding-right: 25px;
          color: #ffffff;
          font-weight: 400;
          float: right;
          margin-left: 25px;
          cursor: pointer;
        }
      }
    }
  }
}

</style>