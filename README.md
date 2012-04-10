# askBOSS

askBoss retrieves images to questions posed in natural language. askBoss attempts to enhance image results for queries around factual question answering. It uses Yahoo Boss (Search) APIs (http://developer.yahoo.com/search/boss/) through Boss Mashup framework (http://developer.yahoo.com/search/boss/mashup.html) and is deployed on Google App Engine.

This hack is an extension of Vik Singh’s qna service (http://bossy.appspot.com/), which finds answer (http://zooie.wordpress.com/2008/08/04/yahoo-boss-google-app-engine-integrated/) using the popular phrases in the top search results for a query. I do image search for the best answers and blend them with the regular image search results. The hack is a basic prototype and natural language image search gets triggered only for questions (queries including who/what/which).

Try askBoss: http://ask-boss.appspot.com


##Installation
Steps to use this code:

1. Install and configure Google App Engine (GAE) 

2. In the config file supply your BOSS consumer key and secret. That can be obtained from http://developer.yahoo.com/search/boss/

3. In the app.yaml file change the application name to your Google App Engine name

Then you're done!


##Contact
Saurabh Sahni 
Email: contact@saurabhsahni.com
Twitter: http://twitter.com/saurabhsahni
Web: http://www.saurabhsahni.com
