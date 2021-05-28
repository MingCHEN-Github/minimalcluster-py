from minimalcluster import MasterNode

your_host = '127.0.0.1' # or use '0.0.0.0' if you have high enough privilege
your_port= 8888
your_authkey = 'ming-auth'

master = MasterNode(HOST = your_host, PORT = your_port, AUTHKEY = your_authkey)
master.start_master_server()

#master.load_envir("f = lambda x: x * 2",from_file= False)

#master.register_target_function("f")


# envir_statement = '''
# from random import random
# example_pi_estimate_throw = lambda x: 1 if (random() * 2 - 1)**2 + (random() * 2 - 1)**2 < 1 else 0
# '''
# master.load_envir(envir_statement, from_file = False)
# master.register_target_function("example_pi_estimate_throw")
#
# N = int(1e6)
# master.load_args(range(N))
#
# result = master.execute()
#
# print("Pi is roughly %f" % (4.0 * sum([x2 for x1, x2 in result.items()]) / N))