const video_ = document.getElementById('hero_video')
const home_link = document.getElementById('home_link')
const page = document.getElementById('video-container')



$("#hero_video").bind('pause', function(e) {
    console.log('stopped');
    console.log((e.target.currentTime*0.0167).toFixed(2))
});

$("#hero_video").bind('stop', function(e) {
    console.log('stopped');
    console.log((e.target.currentTime*0.0167).toFixed(2))
});
