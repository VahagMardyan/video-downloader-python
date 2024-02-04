from flask import Flask, render_template, request
import yt_dlp

app = Flask(__name__,static_folder='static')
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download',methods=['GET','POST'])
def download():
    video_url = request.form['video-url']
    try :
        if 'http' in video_url:
            download_from_youtube(video_url)
            return f'<script>const confirm = window.confirm("Success!! Video downloaded from the source.");if(confirm) open("http://localhost:5000","_self")</script>'
        else :
            return f'<script>const confirm = window.confirm("Invalid Link!!");if(confirm) open("http://localhost:5000","_self")</script>'
    except Exception as error:
        return f'Something went wrong: {error}'

def download_from_youtube(url):
    try :
        options = {
            'format':'best',
            'outtmpl': '~/Desktop/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url,download=True)
            print(f'Video downloaded: {info['title']}')
    except Exception as e:
        print(f'Something went wrong: {e}')


if __name__ == '__main__' :
    app.run(host='localhost', port=5000, debug=True)