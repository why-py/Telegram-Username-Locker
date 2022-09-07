# Telegram-Username-Locker(TUL)
Telegram Username locker (Cli bot) written with pyrogram

<h1>What's going on?</h1>
<li>
<ul>Have you ever wanted to get a specific username but it was already taken?</ul>
</li>

<p>TUL is a telegram application written in python which is able to try to get the username you like and lock it for you!
The applicaton checks the username every moment and once it is "not occupied", it tries to set the username on a public channel.
You have no limits for adding usernames to the checklist.

</p>

<h1>Setting things up!</h1>
Go to <a href="https://my.telegram.org/apps">Telegram apps page</a> to get your api id and api hash.

In main.py , edit these variables with your accounts data:

<li>
<ul>API_ID = your api id</ul>
<ul>API_HASH = your api hash</ul>
<ul>me_id = chat_id of the chat that you want the self to send notifications in that.</ul>


</li>

After editing the code, run it on a server or your machine.

<h1>Usage</h1>

Run these commands by typing and sending them in any chat.
(I recommend running them in the chat with "me_id" id.)

-add {username} #Adds the username to the checklist.

-rm {username} #Removes the username from the checklist.

-help #Help page.


