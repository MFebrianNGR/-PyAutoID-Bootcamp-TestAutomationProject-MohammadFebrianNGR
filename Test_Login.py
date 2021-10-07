from selenium import webdriver
import pytest

options = webdriver.ChromeOptions()     
options.add_experimental_option('excludeSwitches', ['enable-logging'])
#options.headless =True 

@pytest.fixture
def setup():
    driver = webdriver.Chrome(options=options)
    driver.get('https://dribbble.com/session/new')
    driver.minimize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.mark.positivetest
def test_login_success(setup):  #---Test_01 : Login Success
    setup.find_element_by_id('login').send_keys('febrian0530@gmail.com')
    setup.find_element_by_id('password').send_keys('Bismillah06')
    setup.find_element_by_xpath('//*[@id="main-container"]/section[2]/main/div/div[2]/form/input[3]').click()
    
    Badge = setup.find_element_by_xpath('//*[@id="home"]/div[1]/div[1]/nav/ul/li[1]/a').text
    assert Badge == 'Inspiration'

Kunci = [
        ("febrian0530@gmail.com","12345678"),  #---Test_02 : Username benar, Pass salah
        ("nfebrian6296@gmail.com","Bismillah06"),  #---Test_03 : Username salah, Pass benar
        ("nfebrian6296@gmail.com","12345678")  #---Test_04 : Username benar, Pass salah   
        ]

@pytest.mark.negativetest #custom marker
@pytest.mark.parametrize('a,b', Kunci)  #---decorator mark parametrize
def test_login_unsuccess(setup,a,b):  #---Test_02-04 : Login Unsuccess
    setup.find_element_by_id('login').send_keys(a)
    setup.find_element_by_id('password').send_keys(b)
    setup.find_element_by_xpath('//*[@id="main-container"]/section[2]/main/div/div[2]/form/input[3]').click()

    Alert = setup.find_element_by_xpath('/html/body/div[1]').is_displayed()

    assert Alert == True