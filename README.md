# Quanta / Nokia Airframe / SuperMicro(?)

python-requests requried : <BR>
rpm -qa | grep python-requests || yum -y install python-requests<BR>
<BR>
Sample:<BR>
[root@localhost ~]# cat ilos.txt<BR>
10.21.19.153<BR>
10.21.19.154<BR>
10.21.19.155<BR>
10.21.19.156<BR>
<BR>
<BR>
[root@localhost ~]# cat ilos.txt  | xargs -i python get_mac_addr.py {}<BR>
192.21.19.153 54:AB:3A:AA:CC:01<BR>
192.21.19.154 54:AB:3A:BB:DD:02<BR>
192.21.19.155 54:AB:3A:CC:EE:03<BR>
192.21.19.156 54:AB:3A:DD:FF:04<BR>
