from flask import Flask, render_template, request,jsonify
import yt_dlp

app = Flask(__name__,static_folder='static')
@app.route('/')
def index():
    return render_template('index.html')

def script(message,link):
    return f"<script>window.alert('{message}'); window.location.href='{link}'</script>"

@app.route('/download',methods=['GET','POST'])
def download():
    video_url = request.form['video-url']
    try :
        if 'http' in video_url:
            download_from_youtube(video_url)
            message = 'Success!! Video downloaded from the source.'
            link = 'http://localhost:5000'
            return script(message,link)
        else :
            message = 'Invalid Link!!!'
            link = 'http://localhost:5000'
            return script(message,link)
    except Exception as error:
        errorMessage = f'Something went wrong: {error}'
        link = 'http://localhost:5000'
        return errorMessage

def download_from_youtube(url):
    try :
        options = {
            'format':'best',
            'outtmpl': '~/Desktop/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(options) as ydl:
            info = ydl.extract_info(url,download=True)
            print(f'Video downloaded: {info["title"]}')
    except Exception as e:
        print(f'Something went wrong: {e}')


if __name__ == '__main__' :
    app.run(host='localhost', port=5000, debug=True)