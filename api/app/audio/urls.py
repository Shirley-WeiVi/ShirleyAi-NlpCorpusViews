from app.audio import AudioApi, views
from app.Middleware import MiddlewareNormal

# index ---------------------------------------------------

@AudioApi.route('/crate', methods=["POST"])
@MiddlewareNormal
def create(request):
    """normaldata"""
    return views.create(request.json)


@AudioApi.route('/query', methods=["POST"])
@MiddlewareNormal
def query(request):
    """normaldata"""
    return views.query(request.json)


@AudioApi.route('/delete', methods=["POST"])
@MiddlewareNormal
def delete(request):
    """normaldata"""
    return views.delete(request.json)