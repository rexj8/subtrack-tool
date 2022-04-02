import discord
import subprocess
from dotenv import load_dotenv
import os
import time
import asyncio
import threading
import subprocess
from apscheduler.schedulers.background import BackgroundScheduler
from discord.ext import tasks
from shell import *
from datetime import datetime
from banner import banner

green = '\033[92m'
lightyellow = '\033[93m'
yellow = '\033[33m'
red = '\033[91m'
white = '\033[0m'
blue = '\033[94m'


root_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = root_dir + '/output/'
if os.path.isdir(output_folder) == False:
    mkdir = 'mkdir ' + output_folder
    subprocess.Popen(mkdir, shell=True).wait()

intents = discord.Intents.default()
intents.members = True 

sched = BackgroundScheduler()
sched.start()
load_dotenv()
TOKEN=os.getenv('DISCORD_TOKEN')
SERVER=os.getenv('SERVER_ID')

banner()

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    # print(f'Logged in as {client.user}\n')
    # print(client.guilds)
    print(blue+"<--Ignore all the debug info below! You can now background the process-->"+white)	
    user=client.get_user(int(os.getenv('USER_ID')))
    await user.send('Hello!👋')
    await user.send('SubTrack Bot🤖 has awaken')
    await user.send('> subtrack help')
    # in_sec=int(os.getenv('DELAY'))*60*60                        
    in_sec=int(os.getenv('DELAY'))*60                        
    # print(in_sec)
    out.start()
    # chec=sched.add_job(execute,'interval', seconds = in_sec)        
    # chec2=sched.add_job(takeover,'interval',seconds= in_sec)

@client.event
async def on_message(message):
    if message.author == client.user:      #Ignore messages by bot itself
	    return

    try:
        if os.path.isdir(output_folder) == False:
            mkdir = 'mkdir ' + output_folder
            subprocess.Popen(mkdir, shell=True).wait()
        if os.path.isdir(root_dir+'/required/') == False:
            mkdir = 'mkdir ' + root_dir + '/required/'
            subprocess.Popen(mkdir, shell=True).wait()
        if os.path.isfile(root_dir+'/required/domains_list') == False:
            subprocess.Popen('touch '+root_dir+'/required/domains_list', shell=True).wait()
        if os.path.isfile(root_dir+'/required/commands_list') == False:
            subprocess.Popen('touch '+root_dir+'/required/commands_list', shell=True).wait()

        # prefix="subtrack"
        if message.author==client.get_user(int(os.getenv('USER_ID'))):
            words=message.content.split()
            if words[0].lower() == "subtrack":

                if len(words) == 1:
                        await message.author.send("See Help Menu")
                        await message.author.send("> subtrack h")

                elif words[1].lower() == "help" or words[1].lower() == "h":
                    await message.author.send("♦subtrack list domain\n♦subtrack list command\n♦subtrack add domain <domain.tld>\n♦subtrack rm domain <domain.tld>\n♦subtrack add command <full-command>\n♦subtrack rm command <full-exact-command>")
                    await message.author.send("For more clearance, follow 🧾Documentation -\nhttps://github.com/rexj8/SubTrack/blob/main/README.md")

                elif words[1].lower() == "add" or words[1].lower() == "a":
                    if len(words) == 2:
                        await message.author.send("‼ Wrong Command")
                        await message.author.send("subtrack r d <domain>")
                        await message.author.send("subtrack r c <full-command>")
                    elif words[2].lower() == "domain" or words[2].lower() == "d":
                        dom=words[3]
                        domain_file=open("./required/domains_list","a+")
                        domain_file.write(dom+'\n')			     
                        await message.author.send("✅👍 Domain Added")
                        crate_file_cmd = 'touch '+output_folder+dom+'_sub'
                        subprocess.Popen(crate_file_cmd, shell=True).wait()
                        print(green+'Domain Added'+white)
                        domain_file.close()
                    elif words[2].lower() == "command" or words[2].lower() == "c":
                        a=' '
                        com=a.join(words[3:])
                        command_file=open("./required/commands_list","a+")
                        command_file.write(com+'\n')
                        await message.author.send("✅👍 Command Added")
                        print(green+'Command Added'+white)
                        command_file.close()
                    else:
                        await message.author.send("subtrack a d <domain>")
                        await message.author.send("subtrack a d <full-command>")


                elif words[1].lower() == "rm" or words[1].lower() == "r":
                    fl=False
                    if len(words) == 2:
                        await message.author.send("‼ Wrong Command")
                        await message.author.send("subtrack r d <exact_domain>")
                        await message.author.send("subtrack r c <exact_command>")
                    elif words[2].lower() == "domain" or words[2].lower() == "d":
                        rem=words[3].lower()
                        domain_file=open("./required/domains_list","r")
                        lines=domain_file.readlines()
                        domain_file=open("./required/domains_list","w")
                        for line in lines:
                            if line.strip('\n')==rem:
                                fl=True
                                continue
                            else:
                                domain_file.write(line)
                        if fl:
                            await message.author.send("🛑 Domain has been Removed!")
                            print(red+'Domain Removed'+white)
                            fl=False
                        else:
                            await message.author.send("⚠ Domain not Found in the List ⚠")
                            print(red+'Domain not Found in the List'+white)
                        domain_file.close()
                    elif words[2].lower() == "command" or words[2].lower() == "c":
                        a=' '
                        rem=a.join(words[3:])
                        command_file=open("./required/commands_list","r")
                        lines=command_file.readlines()
                        command_file=open("./required/commands_list","w")
                        for line in lines:
                            if line.strip('\n')==rem:
                                fl=True
                                continue
                            else:
                                command_file.write(line)
                        if fl:
                            await message.author.send("🛑 Command has been Removed!")
                            print(red+'Command Removed'+white)
                            fl=False
                        else:
                            await message.author.send("⚠ Command not Found in the List ⚠")
                            print(red+"Command not Found in the List"+white)
                        command_file.close()
                    else:
                        await message.author.send("subtrack r d <exact_domain>")
                        await message.author.send("subtrack r c <exact_command>")

                elif words[1].lower() == "list" or words[1].lower() == "l":
                    fl=False
                    if len(words) == 2:
                        await message.author.send("‼ Wrong Command")
                        await message.author.send("subtrack l d")
                        await message.author.send("subtrack l c")
                    elif words[2].lower() == "domain" or words[2].lower() == "domains" or words[2].lower() == "d":
                        domain_file=open("./required/domains_list","r")
                        lines=domain_file.readlines()
                        domains=''
                        for line in lines:
                            domains = domains + 'https://' + line
                        if domains=='':
                            domains = domains + '❌ 0 Domains in list'
                        else:
                            domains = domains + '\n----------------------------\nTOTAL Domains 👉 '+str(len(lines))
                        await message.author.send(domains)
                        domain_file.close()
                    elif words[2].lower() == "command" or words[2].lower() == "commands" or words[2].lower() == "c":
                        a=' '
                        rem=a.join(words[3:])
                        command_file=open("./required/commands_list","r")
                        lines=command_file.readlines()
                        commands=''
                        for line in lines:
                            commands = commands + line + '\n'
                        if commands=='':
                            commands = commands + '❌ 0 Commands in list'
                        else:
                            commands = commands + '\n----------------------------\nTOTAL Commands 👉 '+str(len(lines))
                        await message.author.send(commands)
                        command_file.close()
                    else:
                        await message.author.send("‼ Wrong Command")
                        await message.author.send("subtrack l d")
                        await message.author.send("subtrack l c")

                else:
                    await message.author.send("‼ Wrong Command")

            else:
                await message.author.send("‼ Wrong Command")

    # except Exception as e:
    except Exception as e:
        import traceback
        await message.author.send("‼ __Wrong Command__")
        await message.author.send(traceback.format_exc())
        await message.author.send("‼ __Wrong Command__")





# @tasks.loop(seconds=1.0)
@tasks.loop(hours=12)
# @tasks.loop(minutes=1.0)
async def out(): 
    print(yellow+'Inside out() Function'+white)
    execute_tools()
    print(yellow+'Completed out() Function - '+str(datetime.now().strftime("%d %B, %Y %H:%M:%S"))+white)
    
#     print("Inside out1")                  
#     data=check("new")
#     if(data):
#         user=client.get_user(int(os.getenv('USER_ID')))
#         await user.send("New Subdomain/s Found")
#         for l in data:
#             await user.send(l.strip())         
#     print("Inside out2")
#     data=check("to")
#     if(data):
#         user=client.get_user(int(os.getenv('USER_ID')))
#         await user.send("Subdomain Takeover Vulnerable Domain Found")
#         for l in data:
#             await user.send(l.strip())  


# def check(con):
#     print("Inside check")  
#     data=[]                                              
#     if(con=="new"):
#         print("debug")
#         if os.path.isfile("./required/domains_list") :
#             sites=open("./required/domains_list","r+")
#             sites_lines=sites.readlines()
#             loc="./output/"
#             for site in sites_lines:
#                 fname=site.strip()+"_sub.txt"
#                 f2name="."+fname
#                 subprocess.Popen("touch "+loc+"changes",shell=True).wait()
#                 # print('=====')
#                 # print(loc+f2name)
#                 # print('=====')
#                 if os.path.isfile(loc+f2name) :
#                     subprocess.Popen("diff "+loc+fname+" "+loc+f2name+" | grep '<' | sed 's/^< //g' > ./required/changes",shell=True).wait()          
#                     subprocess.Popen("cp "+loc+fname+" "+loc+f2name,shell=True).wait()
#                 else:
#                     subprocess.Popen("cp "+loc+fname+" "+loc+f2name,shell=True).wait()
#                 if(os.stat(loc+"changes").st_size != 0):
#                     f=open("./required/changes","r")
#                     data=f.readlines()
#                     f.close()
#                     subprocess.Popen("rm ./required/changes",shell=True).wait()                                                       
#             sites.close()
#     if(con=="to"):
#         if(os.path.isfile("./required/takeover")):
#             if(os.stat("./required/takeover").st_size != 0):
#                 file1=open("./required/takeover","r")
#                 data=file1.readlines()
#                 file1.close()
#                 subprocess.Popen("rm ./required/takeover",shell=True).wait()
#     return data






# print(TOKEN)
client.run(TOKEN)