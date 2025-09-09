# Fun
. Hacking? Solving an easy challenge on tryhackme.com

![test](images/1.png)
![test](images/2.png)

**The challenge is to hack into a python server that when receiving a GET request from a client runs some of the content of that request as an input for the python interpreter running in the server.**

So the first step is to deploy the challenge machine in the tryhackme platform, we get the challenge machine ip address as 10.201.65.80, this is an ip from a private network, so we connect to the network of the tryhackme platform using the command 
`sudo openvpn Downloads/user.ovpn` after we ping the target so we can see that we have access to the target
`ping 10.201.65.80`

![test](images/3.png)

After seeing that we are in fact into the network we try to access the target server with the default server, we run nmap to scan the target with the `-sV` flag to enumerate the version of the sotware running in the ports of the server. `nmap -sV 10.201.65.80` 

![test](images/4.png)

Nmap return that the target server is running ssh in port 22 and a http server in port 8000. As in the premises of the challenge is very straight forward where to look, i'm not gonna try to bruteforce the ssh and focus in the server as the foothold point.

We see that the http server is using the simplehttp python. the command to start running this kind of server in your machine is a derivation of `python3 -m http.server PORT_TO_RUN` and the fingerprint string of the responde of the http is returning error about an object not defined in the request. When access the http service in port 8000 in a browser we receive a html file saying *Try a more basic connection!*

![test](images/5.png)



