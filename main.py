import sys
import system_simulator as ss

filename = sys.argv[1]
network = ss.Network(filename, "result" + filename[:-4] + ".csv")
network.converge()
