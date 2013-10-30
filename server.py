import lightshow
import os
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

port = int(os.environ.get('PORT', '8080'))
from tornado.options import define, options
define("port", default=port, help="run on the given port", type=int) #port options for webServer


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/on", on),
            (r"/off", off),
            (r"/blink", blink),
            (r"/blinkfast", blinkfast),
            (r"/blinkrandom", blinkrandom),

            (r"/(.*)", tornado.web.StaticFileHandler, {"path": "static"})
        ]
        tornado.web.Application.__init__(self, handlers, debug=True)


class indexhtmlhandler(tornado.web.RequestHandler):
	def get(self):
		self.render("static/index.html")



class on(tornado.web.RequestHandler):
    def get(self):
        lightshow.on()
        self.write('Resistance Is Futile !!!!  Surrender human!')

class off(tornado.web.RequestHandler):
    def get(self):
        lightshow.off()
        self.write(' i am losing power.....  1010111100101001011101010100111010100101010101010')

class blink(tornado.web.RequestHandler):
    def get(self):
        lightshow.blink()
        self.write('1010111100101001011101010100111010100101010101010')

class blinkfast(tornado.web.RequestHandler):
    def get(self):
        lightshow.blink()
        self.write('1010111100101001011101010100111010100101010101010')

class blinkrandom(tornado.web.RequestHandler):
    def get(self):
        lightshow.blink()
        self.write('1010111100101001011101010100111010100101010101010')



if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
