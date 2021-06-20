# Account Generator Bot
Account Generator Bot, runs on python (telethon), with redis as database.

# Variables
 ---------------
* Mandatory Vars -   
 `APP_ID` and `API_HASH` - Get it from [here](https://my.telegram.org)   
 `BOT_TOKEN` - Get it from [@BotFather](https://t.me/BotFather)   
 `REDIS_URI` and `REDIS_PASSWORD` - Get it from [RedisLabs](https://redislabs.com), tutorial [here](./extras/redisinfo).   
 `OWNER_ID` - Your telegram user id, get it by sending `/info` to some group management bot.   
 `ACCOUNTS` - Raw link to the accounts you need the users to generate. Tutorial [here](./extras/add_accounts.md).   
-----------------   
   
-----------------   
* Other vars -    
`ACC_NAME` - Name of the account that the bot is to generate.   
`CHANNEL` - Link/Username of your telegram group/channel. Leave empty for no force join.      
`START` - Custom start message. Use {mention} in it to mention the user who is currently using the commands.   
-----------------   
   
## Deploying
You can deploy this bot anywhere.
<details><summary>Heroku</summary>
<p>
<a href="https://heroku.com/deploy">
  <img src="https://www.herokucdn.com/deploy/button.svg" alt="Deploy">
</a>
</p>
</details>

<details><summary>Local Machine</summary>
<p>
Open a terminal. </br>
Clone the repository <code>git clone https://github.com/xditya/AccountGenBot && cd AccountGenBot</code> </br>
Install requirements:
<code>pip3 install -r requirements.txt</code> </br>
Create a <code>.env</code> file with the vars. Follow these: </br>
<code>.touch .env</code> </br>
<code>nano .env</code> </br>
Now open a notepad, copy the contents in .env.sample and edit the values as per your requirements. Copy that and paste it in the terminal. </br> 
CTRL + X and CTRL + S to save and exit. </br>
<code>python3 bot.py</code> </br>
Now send /start to you bot to see if it is running! </br>
</details>

## Support   
Join the [telegram group](https://t.me/BotzHubChat) for support and the [channel](https://t.me/BotzHub) for updates.   
   
Report bugs, give feature requests there..   
Do fork and star the repository if you liked it.

## Disclaimer
[![GNU Affero General Public License v3.0](https://www.gnu.org/graphics/agplv3-155x51.png)](https://www.gnu.org/licenses/agpl-3.0.en.html#header)    
Licensed under GNU AGPL v3.0.   
Selling the codes to other people for money is *strictly prohibited*.
