# Snooper_Mikrotik
A simple code that ssh to RouterOS and get snooper data

**Keywords**: Mikrotik, Snooper, SSH

Snooper is a nice tool for wireless interfaces in Mikrotik RoutersOS. You can monitor all of traffics(devices) that are in mikrotik device neighborhood.

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
3.Run this command in the terminal(In you mikrotik device):
```
user ssh-keys import public-key-file=id_rsa.pub user=[device username(default: admin)]
```
4.Now ssh to mikrotik device(first time you need to allow devices to connect[type yes and enter!])
  type quit to if you want to exit.
5.Run main.py file.

  output : 
  
  
  ![](https) 
