# Snooper_Mikrotik
A simple code that ssh to RouterOS and get snooper tool data result

**Keywords**: Mikrotik, Snooper, SSH

Snooper is a nice tool of wireless interfaces in Mikrotik RoutersOS. You can monitor all of the traffics(devices) that are in mikrotik device neighborhood.

## 1\.Requirments:
  A Mikrotik device that has wireless interface (like RB951 series) & a linux pc

## 2\.Steps:
1.First you need to add your pc ssh-key to ROS.
```
ssh-key -t rsa
cd ~/.ssh
```
2.Tranfer the ssh-key (id_rsa.pub) to mikrotik device
```
ftp <mikrotik device ip> [use your device username & password]
  put id_rsa.pub
  exit
```  
3.Run this command in the terminal(In terminal):
```
user ssh-keys import public-key-file=id_rsa.pub user=[device username(default: admin)]
```
4.Now ssh to mikrotik device(At the first time you need to allow devices to connect[type yes and enter!])
  type quit to if you want to exit.
5.Run main.py file.

  output : 
  
  
  ![](https://github.com/hadi2f244/snooper_mikrotik/blob/master/output.png) 

### Problems!:
1. I think ssh connection will leave opened if you close python app. So there's an exit_handler function in py file that should be developed to close the ssh connection. 
2. I developed this code to demonstrate RSS values. But I think, Snooping in ROS doesn't work well. When I get my phone close to the router, result shows that RSS is about -60dbm or when I leave my phone far from the router the RSS is about -50 dbm. Thus, Its variations aren't related to the distance between the phone and the router! Moreover, I think there’s a time gap between the snooper results and the real condition!
