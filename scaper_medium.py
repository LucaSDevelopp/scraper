import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
import time

def inception(driver):
    driver.maximize_window()
    driver.get('https://www.booking.com/index.it.html')

    # Booking Search 1
    try:
        driver.find_element(By.ID, "ss").send_keys('Hotel Giotto Padova')
        pass
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "ce45093752").send_keys('Hotel Giotto Padova')
        pass
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "c-autocomplete__input.sb-searchbox__input.sb-destination__input").send_keys('Hotel Giotto Padova')
        pass
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "sb-date-field.b-datepicker").send_keys('Hotel Giotto Padova')
        pass
    except:
        raise Exception('Booking Search failed ... 1')

    # Checkin, Checkout window 2
    try:
        driver.find_element(By.CLASS_NAME, "b91c144835").click()
        driver.find_element(By.CLASS_NAME, "sb-date-field.b-datepicker").click()
    except NoSuchElementException:
        driver.find_element(By.CLASS_NAME, "d47738b911.e246f833f7.fe211c0731").click()
    except:
        raise Exception('Checkin and Checkout window failed ... 2')

    # Bui Calendar 3
    try:
        driver.find_element(By.CSS_SELECTOR, "td[data-date = '{}']".format(today)).click()
        driver.find_element(By.CSS_SELECTOR, "td[data-date = '{}']".format(tmr)).click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[3]").click()
        driver.find_element(By.XPATH, "//*[@id='frm']/div[1]/div[2]/div[2]/div/div/div[3]/div[1]/table/tbody/tr[1]/td[4]").click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/div/div/form/div[1]/div[2]/div/div[2]div/div/div[1]/div[1]/table/tbody/tr[3]/td[6]/span").click()
        driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/div/div/form/div[1]/div[2]/div/div[2]div/div/div[1]/div[1]/table/tbody/tr[3]/td[7]/span").click()
    except:
        raise Exception('Bui Calendar failed ... 3')
    
    
    # Search Button 4
    driver.find_element(By.CLASS_NAME, "sb-searchbox__button ").click()
    print('----- Searching 4 ... Success -----')
    print()
        
    # Search on Listing 5 -- after navigating to the listing page
    try:
        driver.find_element(By.XPATH, "//*[@id='left_col_wrapper']/div[1]/div/div/form/div/div[6]/div/button").click()
    except NoSuchElementException:
        driver.find_element(By.XPATH, "//*[@id='indexsearch']/div[2]/div/div/div/form/div[1]/div[4]/button").click()
    except: 
        raise Exception('')

    driver.find_element(By.XPATH, "//div[text()='台北寒舍艾美酒店']").click()
    driver.close()
    driver.switch_to.window(driver.window_handles[-1])

def roomtype():
    room_type = []
    for i in range(len(col_count)):
        try:
            if col_count[i] == 5:
                i = i + 1
                room_temp = "//*[@id='hprt-table']/tbody/tr[" + str(i) + "]/td[1]/div/div[1]"
                room_type.append(driver.find_element(By.XPATH, room_temp).text)
            elif col_count[i] == 4:
                room_type.append("")
        except:
            if col_count[i] == 5:
                i = i + 1
                room_temp = "//*[@id='room_type_id_33385826']/span"
                room_type.append(driver.find_element(By.XPATH, room_temp).text)
            elif col_count[i] == 4:
                room_type.append("")
    return(room_type)

df = pd.DataFrame({
    'Record Time':recordTime(),
    'Check-In Date':checkin(),
    'Check-Out Date':checkout(),
    'Room Type':roomtype(),
    'Occupancy':occupancy(),
    'Breakfast':breakfast(),
    'Remains':remaining(),
    'Rate':rate(),
    'Tax':tax(),})

df['Room Type'] = df['Room Type'].fillna(method = 'ffill')

