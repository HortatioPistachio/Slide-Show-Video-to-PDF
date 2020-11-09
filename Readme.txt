Conor Barry 2020

program sorta works for some tests

this program is designed ot take a slide show presentation and convert those slides to a pdf format
for easy viewing. 
Motivation is that half the time the lectures dont release the slides with the lectures and I dont wanna
rewatch an hour long lecture just to find the 1 slide I need to understand stuff

cannot use wsl, due to no graphical capability
use power shell instead


things to improve:
    - must make tolerance adaptive, an all white video will score difference to an all black and cause frame 
        inconsientieces. changing video size and quality does this also

    -betterslide regognition and ways to tests
    -increase speed
    -add parrallel proccesing, maybe gpu acceleralation, likely best way to speed up, can split video up into 
        parts using set
    -be able to recognise when a video is being played and skip over it/ make 1 side with message
    -recognise when a slide is repeated, maybe use a sum or some form of hash stored in table
    -intergrate into web app
    -reduce memory usage
    -freeze a beta
    
