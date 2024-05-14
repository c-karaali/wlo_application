import json
import falcon

from fh.aalen.video.VideoService import VideoService


class VideoRessource:
    def on_get_videos(self, req, resp):
        videolist = VideoService.get_videos();
        resp.text = json.dumps([v.to_dict() for v in videolist], ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_get_video(self, req, resp, vnr):
        resp.text = None
        v = VideoService.get_video(int(vnr))
        resp.text = json.dumps(v.to_dict(), ensure_ascii=False, indent=2)
        resp.status = falcon.HTTP_200

    def on_post_video(self, req, resp):
    # Return value is an object of type dict
        video_json = json.load(req.bounded_stream)
        VideoService.create_video(video_json)
        resp.text = "Video added successfully."
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_put_video(self, req, resp, vnr):
        video_json = json.load(req.bounded_stream)
        # Convert the dict to an object of the class video
        VideoService.update_video(vnr, video_json)
        resp.text = "Video updated successfully."
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_delete_video(self, req, resp, vnr):
        VideoService.delete_video(vnr)
        resp.text = "Video deleted successfully."
        resp.status = falcon.HTTP_OK
        resp.content_type = falcon.MEDIA_TEXT

    def on_get_videosbygenre(self, req, resp, genre):
        videolist = VideoService.get_videos_bygenre(genre);
        resp.text = json.dumps([v.to_dict() for v in videolist], ensure_ascii=False, indent=2)

    def on_get_videosbyagerating(self, req, resp, agerating):
        videolist = VideoService.get_videos_byagerating(agerating);
        resp.text = json.dumps([v.to_dict() for v in videolist], ensure_ascii=False, indent=2)

    def on_get_videogenres(self, req, resp):
        genrelist = VideoService.get_videos_genres()
        #convert the resulting rows in a dict to be able to jsonify it
        resultset = [dict(row) for row in genrelist]
        resp.text = json.dumps(resultset, ensure_ascii=False, indent=2)