from selenium import webdriver
from getpass import getpass

NIM = input("Masukkan NIM anda : ")
password = getpass("Masukkan password anda : ")

driver = webdriver.Chrome("C:\\python\\chromedriver.exe")
driver.get("http://siakad.usahidsolo.ac.id/gate/index.php")

NIM_textbox = driver.find_element_by_id("userid")
NIM_textbox.send_keys(NIM)
password_textbox = driver.find_element_by_name("password")
password_textbox.send_keys(password)

login_button = driver.find_element_by_class_name("btn.btn-success.btn-block")
login_button.click()

