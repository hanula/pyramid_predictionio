#
import predictionio
from pyramid.interfaces import Interface
from pyramid.security import authenticated_userid


class IDefaultIdentification(Interface):

    def __call__(request):
        """
        Return default identifier for unauthenticated users.
        When it returns None then no prediction identification will be performed.
        """


def client_from_settings(settings, prefix='predictionio.'):
    kwargs = dict((k[len(prefix):], v) for k, v in settings.items()
                  if k.startswith(prefix))
    return predictionio.Client(**kwargs)


def get_client(request):
    return client_from_settings(request.registry.settings)


def identify_user(handler, registry):
    def tween(request):
        user_id = (authenticated_userid(request)
                   or get_default_identification(request))
        if user_id:
            request.predictionio.identify(user_id)
        return handler(request)
    return tween


def default_identification(request):
    return "special:unauthenticated"


def get_default_identification(request):
    return request.registry.getUtility(IDefaultIdentification)(request)


def set_default_identification(request, identify_fn):
    request.registry.registerUtility(identify_fn, IDefaultIdentification)


def includeme(config):
    config.add_request_method(get_client, 'predictionio', reify=True)
    config.add_directive('set_default_predictionio_identification',
                         set_default_identification)
    config.set_default_predictionio_identification(default_identification)
    config.add_tween('pyramid_predictionio.identify_user')
