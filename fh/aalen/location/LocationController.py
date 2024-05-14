class VideoController:
    def __init__(self, app, res):
        self.app = app
        self.res = res

        self.app.add_route('/videos', self.res, suffix='videos')

        self.app.add_route('/video/{vnr}', self.res, suffix='video')

        self.app.add_route('/video', self.res, suffix='video')

        self.app.add_route('/videosbygenre/{genre}', self.res, suffix='videosbygenre')

        self.app.add_route('/videosbyagerating/{agerating}', self.res, suffix='videosbyagerating')

        self.app.add_route('/videogenres', self.res, suffix='videogenres')