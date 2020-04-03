import logging

from aiohttp import web
from tartiflette_aiohttp import register_graphql_handlers

from apps.settings import config
from apps.db import init_db, close_db


def app_factory() -> web.Application:
    '''
    Config APP 
    '''
    app = web.Application()
    app['config'] = config
    app['logger'] = logging.getLogger()

    app.on_startup.append(init_db)
    app.on_cleanup.append(close_db)
    handler_config = {
        'app': app,
        'engine_sdl': 'sdl',
        'executor_http_endpoint': '/graphql',
        'executor_http_methods': ['GET', 'POST'],
        'engine_modules': [
            'apps.resolvers.query_resolvers',
            'apps.resolvers.mutation_resolvers',
            'apps.resolvers.subscription_resolvers',
            'apps.directives.rate_limiting',
            'apps.directives.auth'
        ],
        'graphiql_enabled': True
    }
    handler_app = register_graphql_handlers(**handler_config)
    
    return handler_app
