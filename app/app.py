import logging
import tornado.ioloop
import tornado.web
from tornado_prometheus import MetricsHandler

from classes import AuditedApplication


log = logging.basicConfig(
    level=logging.DEBUG
)


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello, world")


def make_app():
    routes = [
        (r"/", MainHandler),
        (r"/metrics", MetricsHandler),
    ]
    return AuditedApplication(
        routes,
        autoreload=True,
    )


if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
