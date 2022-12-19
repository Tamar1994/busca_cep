import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
from tqdm import trange


tabela = pd.read_excel("ceps.xlsx")
#display(tabela)


options = Options()
options.add_argument("--headless")

driver = webdriver.Chrome(options=options)

for cep in trange(len(tabela)):
    cepend = tabela.loc[cep,"CEP"]
    #print(cepend)



    driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")
    driver.find_element(By.ID, 'endereco').click()
    driver.find_element(By.ID, 'endereco').send_keys(cepend)
    driver.find_element(By.ID,'btn_pesquisar').click()
    time.sleep(1)
    logradouro = driver.find_element('xpath','//*[@id="resultado-DNEC"]/tbody/tr/td[1]').text
    bairro = driver.find_element('xpath','//*[@id="resultado-DNEC"]/tbody/tr/td[2]').text
    localidade = driver.find_element('xpath','//*[@id="resultado-DNEC"]/tbody/tr/td[3]').text
    tabela.loc[cep,"Logradouro/Nome"] = logradouro
    tabela.loc[cep,"Bairro/Distrito"] = bairro
    tabela.loc[cep,"Localidade/UF"] = localidade

#driver.close()

display(tabela)


tabela.to_excel('Tabela_Ceps.xlsx')