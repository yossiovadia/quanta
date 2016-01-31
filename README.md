# Quanta / Nokia Airframe / SuperMicro(?)

python-reequest requried : 
rpm -qa | grep python-requests || yum -y install python-requests

Sample: 
[root@localhost ~]# cat ilos.txt
10.21.19.153
10.21.19.154
10.21.19.155
10.21.19.156


[root@localhost ~]# cat ilos.txt  | xargs -i python get_mac_addr.py {}
192.21.19.153 54:AB:3A:AA:CC:01
192.21.19.154 54:AB:3A:BB:DD:02
192.21.19.155 54:AB:3A:CC:EE:03
192.21.19.156 54:AB:3A:DD:FF:04
