from minimalcluster import WorkerNode

your_host = '127.0.0.1'
your_port= 8888
your_authkey = 'ming-auth'
N_processors_to_use = 1

worker = WorkerNode(your_host, your_port, your_authkey, nprocs = N_processors_to_use)

worker.join_cluster()