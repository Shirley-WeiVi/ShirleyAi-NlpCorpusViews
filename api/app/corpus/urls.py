from app.corpus import CorpusApi, index_views, data_views, session_index
from app.Middleware import MiddlewareNormal

# index ---------------------------------------------------

@CorpusApi.route('/index/crate', methods=["POST"])
@MiddlewareNormal
def index_create(request):
    """normaldata"""
    return index_views.index_create(request.json)


@CorpusApi.route('/index/query', methods=["POST"])
@MiddlewareNormal
def index_query(request):
    """normaldata"""
    return index_views.index_query(request.json)


@CorpusApi.route('/index/update', methods=["POST"])
@MiddlewareNormal
def index_update(request):
    """normaldata"""
    return index_views.index_update(request.json)


@CorpusApi.route('/index/delete', methods=["POST"])
@MiddlewareNormal
def index_delete(request):
    """normaldata"""
    return index_views.index_delete(request.json)

# session ---------------------------------------------------

@CorpusApi.route('/session/crate', methods=["POST"])
@MiddlewareNormal
def session_create(request):
    """normaldata"""
    return session_index.session_create(request.json)


@CorpusApi.route('/session/query', methods=["POST"])
@MiddlewareNormal
def session_query(request):
    """normaldata"""
    return session_index.session_query(request.json)


@CorpusApi.route('/session/delete', methods=["POST"])
@MiddlewareNormal
def session_delete(request):
    """normaldata"""
    return session_index.session_delete(request.json)

# ----------------------------------------------------------

@CorpusApi.route('/data/text/create', methods=["POST"])
@MiddlewareNormal
def data_text_create(request):
    """normaldata"""
    return data_views.data_text_create(request.json)


@CorpusApi.route('/data/emoji/create', methods=["POST"])
@MiddlewareNormal
def data_emoji_create(request):
    """normaldata"""
    return data_views.data_emoji_create(request.json)


@CorpusApi.route('/data/image/create', methods=["POST"])
@MiddlewareNormal
def data_image_create(request):
    """normaldata"""
    return data_views.data_image_create(request.json)


@CorpusApi.route('/data/query', methods=["POST"])
@MiddlewareNormal
def data_query(request):
    """normaldata"""
    return data_views.data_query(request.json)


@CorpusApi.route('/data/delete', methods=["POST"])
@MiddlewareNormal
def data_delete(request):
    """normaldata"""
    return data_views.data_delete(request.json)

@CorpusApi.route('/data/withdraw', methods=["POST"])
@MiddlewareNormal
def data_withdraw(request):
    """normaldata"""
    return data_views.data_withdraw(request.json)
