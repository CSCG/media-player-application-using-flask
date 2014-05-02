import os
import webapp2
from flask import Flask, request, render_template

music_dir = 'static/music'
video_dir = 'static/video'

app = Flask(__name__)

@app.route('/')
@app.route('/audio')
def audio():
    music_files = [f for f in os.listdir(music_dir) if f.endswith('mp3')]
    music_files_number = len(music_files)
    return render_template("index.html",
                        title = 'Home',
                        file_type = "Audio Files",
                        music_files_number = music_files_number,
                        music_files = music_files)
@app.route('/video')
def video():
    video_files = [f for f in os.listdir(video_dir) if f.endswith('ogv')]
    video_files_number = len(video_files)
    return render_template("index.html",
                        title = 'Home',
			file_type = "Video Files",
                        music_files_number = video_files_number,
                        music_files = video_files)

@app.route('/<filename>')
def song(filename):
    if filename.endswith('mp3'):
    	return render_template('play.html',
                        title = filename,
			path =music_dir ,
                        music_file = filename)
    else:
	return render_template('play_video.html',
                        title = filename,
			path = video_dir,
                        music_file = filename)
if __name__ == '__main__':
    app=webapp2.WSGIApplication([('/.*',MainPage)],debug=True)
