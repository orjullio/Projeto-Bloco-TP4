import psutil, platform

mem =  psutil.virtual_memory()
capacidade = round(mem.total/(1024**3),2)

print(capacidade)

print('Plataforma \n')

print('Processador na plataforma {}'.format(platform.processor()))
print('Nó {}'.format(platform.node()))
print('Plataforma {}'.format(platform.platform()))
print('Sistema {}\n'.format(platform.platform()))

print('Processamento da CPU: {}'.format(psutil.cpu_percent()))

#for i in range(10):
#    print('Porcentagem da CPU: {}'.format(psutil.cpu_percent()))
#    time.sleep(1)

print('Capturando informações básicas do Disco')

disco = psutil.disk_usage('.')
print("Total:", disco.total, "B")
print("Em uso:", disco.used, "B")
print("Livre:", disco.free, "B")

print("Total:", round(disco.total / (1024**3), 2), "GB")
print("Em uso:", round(disco.used / (1024**3), 2), "GB")
print("Livre:", round(disco.free / (1024**3), 2), "GB")

print('Percentual do disco usado: {}\n'.format(disco.percent))

print('Informações básicas da rede:')


