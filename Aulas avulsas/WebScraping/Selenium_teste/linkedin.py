'''
Codigo criado assistindo ao video ensinando sobre automação web

usa biblioteca selenium

'''

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

# executavel do navegador
browser = webdriver.Chrome(r'.\chromedriver.exe')

# site que quero logar
browser.get('https://www.linkedin.com/login')
sleep(1)

# localização do campo de login e o que escrever lá
input_email = browser.find_element(By.ID, 'username')
input_email.send_keys('pagliarinrafael@gmail.com')
sleep(1)

# localização do campo senha e o que escrever lá
input_password = browser.find_element(By.ID, 'password')
input_password.send_keys('automaT1C_b1tCh!')
sleep(1)

# localização do botão de login e clique.
button_login = browser.find_element(By.XPATH, '//button[@type="submit"]')
button_login.click()
sleep(2)

# buscar por python e dar enter no campo de pesquisa

search = browser.find_element(By.XPATH, '//input[@placeholder="Pesquisar"]')
search.send_keys('Python')
search.send_keys(Keys.RETURN)
sleep(2) # pode usar um wait element, não sei fazer (cara do video q falou)

filter_vagas = browser.find_element(By.XPATH, '//*[@id="search-reusables__filters-bar"]/ul/li[3]/button')
filter_vagas.send_keys(Keys.RETURN)

input('')

