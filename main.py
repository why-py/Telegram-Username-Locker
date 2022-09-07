# Written by why-py
#t.me/pythonmobin

from pyrogram import Client, idle, filters
from pyrogram.types import Chat
from pyrogram.errors.exceptions.bad_request_400 import UsernameNotOccupied,UsernameInvalid
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate
from apscheduler.schedulers.asyncio import AsyncIOScheduler
import json
import os
from pyrogram.enums import ParseMode
API_ID = None #int
API_HASH = ""
BOT_TOKEN = ""

me_id = None #your chat id (int)

app = Client(name='Cli-TD', api_id=API_ID, api_hash=API_HASH)

try:
    open('usernamelist.txt','x')
except:
    pass



@app.on_message(filters.me & filters.regex('-help'))
async def help(client,message):
    text = '''
<b>
Username taker by @Pythonmobin
</b><i>
commands:

-add {username} #Adds the username to the checklist.

-rm {username} #Removes the username from the checklist.

-help #Help page.
    </i>
    
    '''
    await message.reply_text(text,parse_mode=ParseMode.HTML)



@app.on_message(filters.me & filters.regex('-rm'))
async def remover(client,message):

    must_be_del = message.text.replace('@','').split()[1]


    with open("usernamelist.txt", "r") as fp:
        lines = fp.readlines()

    with open("usernamelist.txt", "w") as fp:
        for line in lines:

            if line.strip('\n') != must_be_del:
                print(f'@{must_be_del} removed from the list by user.')
                fp.write(line) 
    os.remove(must_be_del+'.json')
    
    await message.reply_text(f'🆔Username ( @{must_be_del} ) deleted from the list.')



@app.on_message(filters.me & filters.regex('-add'))
async def adder(client,message):


    must_be_added = message.text.replace('@','').split()[1]



    with open('usernamelist.txt','r') as rfile:
        data = rfile.read().split('\n')
        if must_be_added not in data:




            with open('usernamelist.txt','a+') as file:
                file.write(must_be_added+'\n')

            channel_id = await app.create_channel(must_be_added)
            channel_id = channel_id.id

            dic_data = {
                'ChannelName': must_be_added,
                'ChannelId':channel_id
            }
            print(dic_data)
            dic_data = json.dumps(dic_data,indent=4)
            with open(f"{must_be_added}.json", "w") as outfile:
                outfile.write(dic_data)

            await message.reply_text(f'🆔Username ( @{must_be_added} ) added to the list.\n\na channel created to use to lock the username in future.')
            await message.reply_text(f'Trying to take {must_be_added}')

            print(f'\n\n===> @{must_be_added} added to the list.\n\n')
        else:
            await message.reply_text(f'The Username ( @{must_be_added} ) is already on list.')


async def checker():


    with open('usernamelist.txt','r') as userfile:
        data = userfile.read().split('\n')
        # print(data)

    for uname in data:
        print(uname)
        if len(uname)>=5:
            try:

                
                info = await app.get_chat(uname)
                print(info)
                await app.send_message(me_id,f'@{uname} already exists.')



            except UsernameNotOccupied:
                print('on not occupied')
              
              
                with open(uname+'.json','r') as jf:
                    jdata = json.load(jf)
                channel_id = jdata['ChannelId']
                print(channel_id)
                await app.set_chat_username(channel_id,uname)
                await app.send_message(me_id,f'Locked the username on channel @{uname} !')
                await app.send_message(channel_id,f'the username was changed to @{uname}.')


                with open("usernamelist.txt", "r") as fp:
                    lines = fp.readlines()

                with open("usernamelist.txt", "w") as fp:
                    for line in lines:

                        if line.strip('\n') != uname:
                            print(f'@{uname} removed from the list.')
                            fp.write(line)              

            except ChannelPrivate:
                try:
                    print('on private')


                    print(f'the username {uname} seems to be on a privateChannel')
                    
                    
                    with open(uname+'.json','r') as jf:
                        jdata = json.load(jf)
                    channel_id = jdata['ChannelId']


                    await app.set_chat_username(channel_id,uname)
                    await app.send_message(me_id,f'Locked the username on channel @{uname} !')
                    await app.send_message(channel_id,f'the username was changed to @{uname}.')


                    with open("usernamelist.txt", "r") as fp:
                        lines = fp.read().split('\n')

                    with open("usernamelist.txt", "w") as fp:
                        for line in lines:

                            if line != uname:
                                print(f'@{uname} removed from the list.')
                                fp.write(line)                
                except Exception as e:

                    print(e)
                    
            except UsernameInvalid:
                try:



                    with open(uname+'.json','r') as jf:
                        jdata = json.load(jf)
                    channel_id = jdata['ChannelId']



                    await app.set_chat_username(channel_id,uname)
                    await app.send_message(me_id,f'Locked the username on channel @{uname} !')
                    await app.send_message(channel_id,f'the username was changed to @{uname}.')


                except:

                    print('telegram locked username')
            except KeyError:
                print('username not found')
    
    print(data)


            
schedule = AsyncIOScheduler()
schedule.add_job(checker, "interval", seconds=10,max_instances=1)
schedule.start()

app.run()





