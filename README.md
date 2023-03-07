# CuseHacks21

[Link to Devpost](https://devpost.com/software/rhythm-wdoqfa#updates)

## Inspiration
The inspiration for this project came from our team's love of music and singing. We found that singing, especially during quarantine, was a good way to relieve stress and have fun, so we wanted to create a product that would combine the entertainment of singing with social distanced human interaction. We really believe that anyone can sing and have fun, "if you can say it, you can sing it"!

## What it does
Rhythm is a karaoke web app that allows you to sing along to your favorite tracks alone, or with your friends and people around the world. This can be used among friends or team building exercises.

## How we built it
We used Figma for the design, Flask for the backend and HTML/CSS for the frontend. To create the chat rooms, we used Flask-SocketIO for bi-direction communication. The video call is made through Twilio Programmable Video service. We wanted to have a single source of truth for the users in our rooms so we decided on trying Google Cloud's mySQL to keep track of users in each room. It proved to be effective as we were able to add and delete users efficiently and always trying to keep the database up to date. We used a couple of libraries including lyricsgenius to retrieve lyrics. We manually downloaded the music files and used jquery to add the songs in the background.

## Challenges we ran into
A big hurdle we faced was our first implementation not working: we had initially honed in on using the Spotify Web SDK to play the music after some preliminary research and due to the fact that we were familiar with Spotify. However, when we tried to actually use it, we realized that it was no longer supported. We then looked at many alternate solutions that were not ideal, such as embedding Spotify and YouTube links using iframe, using Shazam/iTunes APIs, and embedding video then hiding it with CSS. The main challenge for this was because we had not expected this to go wrong, so when it did, we had to scramble to get it fixed. It was a team effort to try to come up with the solution, which ended up being downloading the audio as mp3 and adding them to the html with jquery.

Another challenge we overcame was using Google Cloud for the first time. Although we had previously used local databases, this was a unique experience as we had to learn something new during the time crunch of a hackathon. From this, we learned more about how convenient and secure Google Cloud is compared to traditional databases.

One of the big challenges was understanding sockets. I had never previously worked with sockets before and it was initially very difficult to wrap my head around this idea. I was so used to sending http requests in order to pass information that sockets didn't make sense at first. However, through the hackathon and working with Flask-SocketIO to build the chat room and the song component of the project, I have come to appreciate the power of the socket!

## Accomplishments that we're proud of
It was a great experience to create something so fun and awesome in such a short period of time! We also got the chance to polish and learn new technical skills to create a product for something we love. We are pretty happy that we overcame so many obstacles and didn't give up halfway through.

## What we learned
* new CSS tricks
* new creative aesthetics
* Google Cloud
* Sockets
* Twilio

## What's next for Rhythm
Although we managed to create a solid foundation for Rhythm so far, we are excited for how much room for improvement there is. Some ideas we currently have include:

* Lyric highlighting synced with the music
* Colour changes/glows in the back based on the beat of the music
* Spotify integration for more song choices (This will need further investigation)
* Minigame where you sing a song in another language, and a native speaker has to guess what song it is (ie an English speaker sings a song in Mandarin using pinyin, and a Mandarin speaker has to guess it!)

## Built With
* Python
* HTML
* CSS
* Flask
* Figma
