import random

def banner():
      green = '\033[92m'
      lightyellow = '\033[93m'
      yellow = '\033[33m'
      red = '\033[91m'
      white = '\033[0m'
      blue = '\033[94m'

      num = random.randint(1, 4)


      if num==1:
            print(yellow+"""

            (                                                   
            )\ )            )     *   )                       ) 
           (()/(    (    ( /(   ` )  /(  (        )        ( /( 
            /(_))  ))\   )\())   ( )(_)) )(    ( /(    (   )\())
           (_))   /((_) ((_)\   (_(_()) (()\   )(_))   )\ ((_)\ 
          \033[91m / __| \033[33m(_))(  \033[91m| |\033[33m(_)  \033[91m|_   _| \033[33m ((_) ((_)_   ((_)\033[91m| |\033[33m(_)\033[91m
           \__ \ | || | | '_ \    | |   | '_| / _` | / _| | / / 
           |___/  \_,_| |_.__/    |_|   |_|   \__,_| \__| |_\_\ 
                                               \033[92m(developed by RACHIT)                                                                          

      """+white)

      if num==2:
            print(red+"""
                  ███████\033[33m╗\033[91m██\033[33m╗   \033[91m██\033[33m╗\033[91m██████\033[33m╗ \033[91m████████\033[33m╗\033[91m██████\033[33m╗  \033[91m█████\033[33m╗  \033[91m██████\033[33m╗\033[91m██\033[33m╗  \033[91m██\033[33m╗
                  \033[91m██\033[33m╔════╝\033[91m██\033[33m║   \033[91m██\033[33m║\033[91m██\033[33m╔══\033[91m██\033[33m╗╚══\033[91m██\033[33m╔══╝\033[91m██\033[33m╔══\033[91m██\033[33m╗\033[91m██\033[33m╔══\033[91m██\033[33m╗\033[91m██\033[33m╔════╝\033[91m██\033[33m║ \033[91m██\033[33m╔╝
                  \033[91m███████\033[33m╗\033[91m██\033[33m║  \033[91m ██\033[33m║\033[91m██████\033[33m╔╝   \033[91m██\033[33m║  \033[91m ██████\033[33m╔╝\033[91m███████\033[33m║\033[91m██\033[33m║     \033[91m█████\033[33m╔╝ 
                  ╚════\033[91m██\033[33m║\033[91m██\033[33m║   \033[91m██\033[33m║\033[91m██\033[33m╔══\033[91m██\033[33m╗   \033[91m██\033[33m║   \033[91m██\033[33m╔══\033[91m██\033[33m╗\033[91m██\033[33m╔══\033[91m██\033[33m║\033[91m██\033[33m║     \033[91m██\033[33m╔═\033[91m██\033[33m╗ 
                  \033[91m███████\033[33m║╚\033[91m██████\033[33m╔╝\033[91m██████\033[33m╔╝   \033[91m██\033[33m║   \033[91m██\033[33m║  \033[91m██\033[33m║\033[91m██\033[33m║  \033[91m██\033[33m║╚\033[91m██████\033[33m╗\033[91m██\033[33m║  \033[91m██\033[33m╗
                  \033[33m╚══════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
                                                                  \033[92m(developed by RACHIT)                                                                          

            """+white)

      if num==3:
            print(red+"""
                  █████████             █████     ███████████                              █████     
                 ███\033[33m░░░░░\033[91m███           \033[33m░░\033[91m███     \033[33m░\033[91m█\033[33m░░░\033[91m███\033[33m░░░\033[91m█                            \033[33m ░░\033[91m███      
                \033[33m░\033[91m███    \033[33m░░░  \033[91m█████ ████ \033[33m░\033[91m███████\033[33m ░   ░\033[91m███ \033[33m ░ \033[91m ████████   ██████    ██████  \033[33m░\033[91m███ █████
                \033[33m░░\033[91m█████████ \033[33m░░\033[91m███ \033[33m░\033[91m███  \033[33m░\033[91m███\033[33m░░\033[91m███    \033[33m░\033[91m███    \033[33m░░\033[91m███\033[33m░░\033[91m███ \033[33m░░░░░\033[91m███  ███\033[33m░░\033[91m███\033[33m ░\033[91m███\033[33m░░\033[91m███ 
                 \033[33m░░░░░░░░\033[91m███ \033[33m░\033[91m███ \033[33m░\033[91m███  \033[33m\033[91m░███ \033[33m░\033[91m███    \033[33m░\033[91m███     \033[33m░\033[91m███ \033[33m░░░  \033[91m ███████ \033[33m░\033[91m███ \033[33m░░░  ░\033[91m██████\033[33m░  
                 \033[91m███    \033[33m░\033[91m███ \033[33m░\033[91m███\033[33m ░\033[91m███ \033[33m ░\033[91m███\033[33m ░\033[91m███   \033[33m ░\033[91m███     \033[33m░\033[91m███      ███\033[33m░░\033[91m███ \033[33m░\033[91m███  ███ \033[33m░\033[91m███\033[33m░░\033[91m███ 
                \033[33m░░\033[91m█████████  \033[33m░░\033[91m████████ ████████     █████    █████    \033[33m░░\033[91m████████\033[33m░░\033[91m██████  ████ █████
                 \033[33m░░░░░░░░░    ░░░░░░░░ ░░░░░░░░     ░░░░░    ░░░░░      ░░░░░░░░  ░░░░░░  ░░░░ ░░░░░ 

                                                                                          \033[92m(developed by RACHIT)                                                                          

            """+white)

      if num==4:
            print(red+"""

               d888888o.   8 8888      88 8 888888888o 8888888 8888888888 8 888888888o.            .8.           ,o888888o.    8 8888     ,88' 
             .`8888:' `88. 8 8888      88 8 8888    `88.     8 8888       8 8888    `88.          .888.         8888     `88.  8 8888    ,88'  
             8.`8888.   Y8 8 8888      88 8 8888     `88     8 8888       8 8888     `88         :88888.     ,8 8888       `8. 8 8888   ,88'   
             `8.`8888.     8 8888      88 8 8888     ,88     8 8888       8 8888     ,88        . `88888.    88 8888           8 8888  ,88'    
              `8.`8888.    8 8888      88 8 8888.   ,88'     8 8888       8 8888.   ,88'       .8. `88888.   88 8888           8 8888 ,88'     
               `8.`8888.   8 8888      88 8 8888888888       8 8888       8 888888888P'       .8`8. `88888.  88 8888           8 8888 88'      
                `8.`8888.  8 8888      88 8 8888    `88.     8 8888       8 8888`8b          .8' `8. `88888. 88 8888           8 888888<       
            8b   `8.`8888. ` 8888     ,8P 8 8888      88     8 8888       8 8888 `8b.       .8'   `8. `88888.`8 8888       .8' 8 8888 `Y8.     
            `8b.  ;8.`8888   8888   ,d8P  8 8888    ,88'     8 8888       8 8888   `8b.    .888888888. `88888.  8888     ,88'  8 8888   `Y8.   
             `Y8888P ,88P'    `Y88888P'   8 888888888P       8 8888       8 8888     `88. .8'       `8. `88888.  `8888888P'    8 8888     `Y8. 

                                                                                                                               \033[92m(developed by RACHIT)                                                                          

            """+white)


