from app.output import OutputApi, corpus, audio
from app.Middleware import MiddlewareNormal

@OutputApi.route('/corpus/outdataset', methods=["POST"])
@MiddlewareNormal
def corpus_outdataset(request):
    """normaldata"""
    return corpus.outdataset(request.json)

@OutputApi.route('/audio/outdata', methods=["POST"])
@MiddlewareNormal
def audio_outdata(request):
    """normaldata"""
    return audio.outdata(request.json)