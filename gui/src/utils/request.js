import axios from 'axios'
import { HttpRoot } from '@/api/config'

// 创建axios实例
const service = axios.create({
  baseURL: HttpRoot, // api 的 base_url
  timeout: 50000, // 请求超时时间
})

service.interceptors.response.use(
  response => {
    const res = response.data
    if(res.code == 400){
      alert(res.msg)
      return res
    }else{
      return res
    }
  },
  error => {
    console.log('err' + error) // for debug
    alert("网络异常")
    return Promise.reject(error)
  }
)

export default service
