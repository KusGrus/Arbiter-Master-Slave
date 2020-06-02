from DataBaseControl import *

hostMaster = '192.168.149.155'  # IP адрес Master
hostSlave = '192.168.149.155'  # IP адрес Slave
hostArbiter = '192.168.149.155'  # IP адрес Arbiter
username, password = 'student', '12345'  # Данные для подключение по SSH
# Инициализируем хосты и проводим первоначальную настройку
arbiter = Arbiter(hostArbiter, username, password, hostMaster)
master = Master(hostMaster, username, password, hostSlave, hostArbiter)
slave = Slave(hostSlave, username, password, hostMaster, hostArbiter)
for obj in [arbiter, master, slave]:
	obj.runBash(obj.config)
