import tornado.ioloop
import tornado.web
from tornado.options import define
from tornado.options import options

from api.urls import mappings

define("port", default=8000, help="run on the given port", type=int)


def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application(mappings)
    application.listen(options.port)
    tornado.ioloop.IOLoop.current().start()


if __name__ == "__main__":
    main()
