
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def view_item(request):
    item_id = request.matchdict['id']
    request.predictionio.record_action_on_item("view", item_id)
    return Response('Hello %(name)s!' % request.matchdict)


def rate_item(request):
    item_id = request.matchdict['id']
    rating = request.POST.get('rating')

    request.predictionio.record_action_on_item("rate", item_id,
                                               {"pio_rate": rating})
    return {'status': 'OK'}


def main(global_config, **settings):
    config = Configurator(settings=settings)
    config.include('pyramid_predictionio')

    config.add_route('view_item', '/items/{id}')
    config.add_route('rate_item', '/rate/{id}', request_method='POST')

    config.add_view(view_item, route_name='view_item')
    config.add_view(rate_item, route_name='rate_item')

    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()


if __name__ == '__main__':
    settings = {'predictionio.appkey': 'YOUR APP KEY',
                'predictionio.threads': 2}
    main({}, **settings)
