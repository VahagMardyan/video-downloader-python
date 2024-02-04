const video_url = document.getElementById('video-url');
document.addEventListener('keyup',(event)=>{
    event.altKey && event.key==='Enter' ? video_url.focus() : null;
});

fetch('../main.py')
.then(response=>response.json())
.then((data)=>{
    if(data.error) {
        window.alert(data.error);
    }
})
.catch((error)=>{
    console.error(`Error: ${error}`);
});