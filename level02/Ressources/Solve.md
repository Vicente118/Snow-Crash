There is a .pcap file in the home of level02 user.

Let's first get this file on our local machine :
```bash
 > scp -P 4242 level02@192.168.56.101:/home/user/level02/level02.pcap ./Ressources 
```

Let's analyze this file with Wireshark :
1. We can see that at time 13.827. A password was asked, it's written in clear in the TCP packet.
2. The following packets data are all 1 byte, so each packets would possibly be a character from the password entered.
3. Let's decrypt the password by checking each bytes entered

Password : ft_waNDReL0L

```bash
> su flag02

> getflag
kooda2puivaav1idi4f57q8iq
```