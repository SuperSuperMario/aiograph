import sys

from aiohttp import web
from apps.main import app_factory

if __name__ == '__main__':
    app = app_factory()
    sys.exit(web.run_app(app))
