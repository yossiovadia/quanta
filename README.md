# Quanta / Nokia Airframe / SuperMicro(?)

python-reequest requried :\r 
rpm -qa | grep python-requests || yum -y install python-requests\r
\r
Sample: \r
[root@localhost ~]# cat ilos.txt\r
10.21.19.153\r
10.21.19.154\r
10.21.19.155\r
10.21.19.156\r
\r
\r
[root@localhost ~]# cat ilos.txt  | xargs -i python get_mac_addr.py {}\r
192.21.19.153 54:AB:3A:AA:CC:01\r
192.21.19.154 54:AB:3A:BB:DD:02\r
192.21.19.155 54:AB:3A:CC:EE:03\r
192.21.19.156 54:AB:3A:DD:FF:04\r
