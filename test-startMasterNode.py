from minimalcluster import MasterNode

your_host = '0.0.0.0' # or use '0.0.0.0' if you have high enough privilege
your_port= 12345
your_authkey = 'ming-auth'

master = MasterNode(HOST = your_host, PORT = your_port, AUTHKEY = your_authkey)
master.start_master_server()