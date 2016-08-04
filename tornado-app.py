import os
from libfloods.locations import checkPath, filecount
import tornado.ioloop
import tornado.web


class UploadHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("templates/upload.html")

    def post(self):
        file1 = self.request.files['file1'][0]
        original_fname = file1['filename']
        location = self.get_argument('location')
        name = self.get_argument('name')
        contact = self.get_argument('contact')
        email = self.get_argument('email')
        other = self.get_argument('other', '')

        path = "../floodimages/" + location + '/'
        checkPath(path)
        filec = filecount(path)
        output_file = open(path + str(filec+1) + original_fname[-4:], 'wb')
        output_file.write(file1['body'])

        self.render('templates/thankyou.html')


settings = {
    'static_path': os.path.join(os.path.dirname(__file__), "static")
}

if __name__ == "__main__":
    app = tornado.web.Application([
        # (r"/", LandingHandler),
        # (r"/help", HelpHandler)
        (r"/", UploadHandler)
    ],
        static_path=os.path.join(os.path.dirname('.'), "static")
    )
    app.listen(80)
    tornado.ioloop.IOLoop.current().start()
