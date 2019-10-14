from tornado.web import Application as _Application
from tornado_prometheus import PrometheusMixIn


class AuditedApplication(PrometheusMixIn, _Application):
    pass
