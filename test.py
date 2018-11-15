import time

from selenium import webdriver
from datetime import datetime

driver = webdriver.Firefox(executable_path='/usr/local/bin/geckodriver')


# start = datetime.now()

# for i in range(1, 100):
#     driver.get('https://monolitico.herokuapp.com/voos/novo')
#     origem = driver.find_element_by_xpath('//*[@id="id_origem"]/option[2]').click()
#     destino = driver.find_element_by_xpath('//*[@id="id_destino"]/option[3]').click()
#     numero = driver.find_element_by_id("id_numero").send_keys('AA123')
#     partida = driver.find_element_by_id('id_partida').send_keys('10/10/2010')
#     chegada = driver.find_element_by_id('id_chegada').send_keys('10/10/2010')
#     driver.find_element_by_xpath("/html/body/form/input[2]").click()
#     time.sleep(1)


# end = datetime.now()
# delta = end - start
# delta.total_seconds()
# import ipdb; ipdb.set_trace()


start = datetime.now()


for i in range(1, 100):
    driver.get('http://agencia-gateway.herokuapp.com/voos/novo')
    origem = driver.find_element_by_xpath('//*[@id="id_origem"]/option[1]').click()
    destino = driver.find_element_by_xpath('//*[@id="id_destino"]/option[2]').click()
    numero = driver.find_element_by_id("id_numero").send_keys('AA123')
    partida = driver.find_element_by_id('id_partida').send_keys('10/10/2010 10:10')
    chegada = driver.find_element_by_id('id_chegada').send_keys('10/10/2010 10:10')
    driver.find_element_by_xpath("/html/body/form/input[2]").click()
    time.sleep(2)



# for x in range(1, 10):
#     driver.get('')
#     ok = False
#     while not ok:
#         try:
#             ok = driver.find_element_by_name('data_viagem')
#         except Exception:
#             continue
#         driver.get('http://agencia-gateway.herokuapp.com/vendas')


end = datetime.now()
delta = end - start
delta.total_seconds()
import ipdb; ipdb.set_trace()