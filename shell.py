import os
import subprocess
import requests 
import discord
from dotenv import load_dotenv

green = '\033[92m'
lightyellow = '\033[93m'
yellow = '\033[33m'
red = '\033[91m'
white = '\033[0m'
blue = '\033[94m'

load_dotenv()

root_dir = os.path.dirname(os.path.abspath(__file__))
output_folder = root_dir + '/output/'


def execute_tools():
    print(yellow+'Executing execute_tools() Function'+white)

    # if os.path.isdir(output_folder) == False:
    #     mkdir = 'mkdir ' + output_folder
    #     subprocess.Popen(mkdir, shell=True).wait()

    commands_file=open("./required/commands_list","r+")   
    command_lines=commands_file.readlines()
    domains_file=open("./required/domains_list","r+")
    domain_lines=domains_file.readlines()
    files = {}
    icounter=0
    for domain_line in domain_lines:
        icounter+=1
        domain=domain_line.strip()
        temp_output_files = []
        # threads=[]
        jcounter=0
        for command_line in command_lines:
            jcounter+=1
            command=command_line.strip()

            file = output_folder + domain + str(icounter) + str(jcounter)
            temp_output_files.append(file)

            exec_command = command.replace('$1', domain)
            exec_command = exec_command.replace('$2', file)

            # print(file)

            subprocess.Popen(exec_command, shell=True).wait()

        files[domain]=(temp_output_files)

        if os.path.isfile(output_folder+domain+'_new') == False:
            subprocess.Popen('touch '+output_folder+domain+'_new', shell=True)

#     t=threading.Thread(target=run, args=(command,domain,counter,))
#     threads.append(t)
#     t.start()
# for x in threads:
#     x.join()
# domains.seek(0)

    commands_file.close()
    domains_file.close()


    get_new_subdomains(files)



def get_new_subdomains(files):

    print(yellow+'Executing get_new_subdomains() Function'+white)

    for domain in files:
        main_file=open(output_folder+domain+'_sub',"r+")
        main_file_list=main_file.readlines()
        main_file.close()


        for subenum_file in files[domain]:
            new_subdomains_cmd = 'cat '+subenum_file+' | anew '+output_folder+domain+'_sub | tee -a '+output_folder+domain+'_new'
            subprocess.Popen(new_subdomains_cmd, shell=True).wait()


        for subenum_file in files[domain]:
            subprocess.Popen('rm -rf '+subenum_file, shell=True)


        # print(subenum_file)


        if main_file_list:
            new_subdomains_file=open(output_folder+domain+'_new',"r+")
            new_subdomain_lines=new_subdomains_file.readlines()
            subdomains=''
            for subdomain in new_subdomain_lines:
                subdomains = subdomains + 'https://' + subdomain
            new_subdomains_file.close()
            send_new_subdomains(domain, subdomains)


        subprocess.Popen('rm -rf '+output_folder+domain+'_new', shell=True)



                                        

     
    # command = '~/tools_pentesting/subenum_tools/./findomain-linux -t $1 -u $2'
    # command = "curl -s https://crt.sh/\?q\=%.$1\&output\=json | jq -r '.[].name_value' | sed 's/\*\.//g' | sort -u | tee -a $2"



def send_new_subdomains(domain, subdomains):
    print(yellow+'Executing send_new_subdomains() Function'+white)

    if subdomains == '':
        return

    url = os.getenv('WEBHOOK_URL') #webhook url, from here: https://i.imgur.com/f9XnAew.png

    #for all params, see https://discordapp.com/developers/docs/resources/webhook#execute-webhook
    data = {
        # "content" : "message content",
        "username" : "⚡⚡ Subdomain Alert"
    }

    #for all params, see https://discordapp.com/developers/docs/resources/channel#embed-object
    data["embeds"] = [
        {
            "title" : domain,
            "description" : subdomains
        }
    ]

    result = requests.post(url, json = data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("\033[92mSubdomains for "+domain+" delivered successfully, code {}.\033[0m".format(result.status_code))

    

# send_new_subdomains('google.com', 'https://google.com\nhttps://google.com')   ## For testing function



# execute_tools()

