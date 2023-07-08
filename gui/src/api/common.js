import request from '@/utils/request'

// index ----------------------------------------------------------------------------

export function index_create(data) {
    return request({
        url: '/CorpusApi/index/crate',
        method: 'post',
        data: data
    })
}

export function index_query(data) {
    return request({
        url: '/CorpusApi/index/query',
        method: 'post',
        data: data
    })
}

export function index_update(data) {
    return request({
        url: '/CorpusApi/index/update',
        method: 'post',
        data: data
    })
}

export function index_delete(data) {
    return request({
        url: '/CorpusApi/index/delete',
        method: 'post',
        data: data
    })
}

// session ----------------------------------------------------------------------------

export function session_create(data) {
    return request({
        url: '/CorpusApi/session/crate',
        method: 'post',
        data: data
    })
}

export function session_query(data) {
    return request({
        url: '/CorpusApi/session/query',
        method: 'post',
        data: data
    })
}

export function session_delete(data) {
    return request({
        url: '/CorpusApi/session/delete',
        method: 'post',
        data: data
    })
}

// data ----------------------------------------------------------------------------

export function data_text_create(data) {
    return request({
        url: '/CorpusApi/data/text/create',
        method: 'post',
        data: data
    })
}

export function data_emoji_create(data) {
    return request({
        url: '/CorpusApi/data/emoji/create',
        method: 'post',
        data: data
    })
}

export function data_image_create(data) {
    return request({
        url: '/CorpusApi/data/image/create',
        method: 'post',
        data: data
    })
}

export function data_query(data) {
    return request({
        url: '/CorpusApi/data/query',
        method: 'post',
        data: data
    })
}

export function data_delete(data) {
    return request({
        url: '/CorpusApi/data/delete',
        method: 'post',
        data: data
    })
}

export function data_withdraw(data) {
    return request({
        url: '/CorpusApi/data/withdraw',
        method: 'post',
        data: data
    })
}


// audio ----------------------------------------------------------------------------

export function audio_create(data) {
    return request({
        url: '/AudioApi/crate',
        method: 'post',
        data: data
    })
}

export function audio_query(data) {
    return request({
        url: '/AudioApi/query',
        method: 'post',
        data: data
    })
}

export function audio_delete(data) {
    return request({
        url: '/AudioApi/delete',
        method: 'post',
        data: data
    })
}

// output ----------------------------------------------------------------------------

export function corpus_outdataset(data) {
    return request({
        url: '/OutputApi/corpus/outdataset',
        method: 'post',
        data: data
    })
}

export function audio_outdata(data) {
    return request({
        url: '/OutputApi/audio/outdata',
        method: 'post',
        data: data
    })
}

//文件上传
export function upload(data) {
    return request({
        url: '/upload_api/file',
        method: 'post',
        data: data,
        headers: {
            'Content-Type': 'multipart/form-data'
        }
    })
}