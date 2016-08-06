import os
import time

import tornado.ioloop
import tornado.web

from libfloods.io import saveFiles
from libfloods.mongo import db
from libfloods.twitter import tweetPhoto


class UploadHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def get(self):
        self.render("templates/upload.html")

    def post(self):
        location = self.get_argument('location')
        if location == "other":
            location = self.get_argument('other')
        name = self.get_argument('name')
        contact = self.get_argument('contact')
        email = self.get_argument('email')
        description = self.get_argument('desc')
        timeClicked = self.get_argument('time')

        file_range = saveFiles(self, location)
        db.submissions.insert({
            'name': name,
            'contact': contact,
            'email': email,
            'location': location,
            'timeSubmitted': time.time(),
            'timeClicked': timeClicked,
            'description': description,
            'fileRange': file_range
        })
        fileList = os.listdir("../floodimages/" + location + '/')
        for file in fileList:
            if file.startswith(str(min(file_range))):
                tweetPhoto(location, time=timeClicked, photoPath="../floodimages/" + location + '/' + file)
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
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()
