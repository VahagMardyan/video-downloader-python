const video_url = document.getElementById('video-url');
document.addEventListener('keyup',(event)=>{
    event.altKey && event.key==='Enter' ? video_url.focus() : null;
});