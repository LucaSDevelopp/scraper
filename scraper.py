from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import datetime

# Starting date is today
start_date = datetime.date.today()

# Set up the webdriver and keep chrome open after the script is finished
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)


driver.get("https://www.booking.com/searchresults.it.html?ss=Padova")

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Find the element with the string "Padova: tot strutture trovate senza data specificata"
padova_tot_strutture = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Padova:')]")))

# Extract the number after the word "Padova"
padova_text = padova_tot_strutture.text
tot_structures_padua = int(padova_text.split(":")[1].split(" ")[1])


# _tot_struttureWait for the "Reject All" button to be located
wait = WebDriverWait(driver, 10)
reject_all_button = wait.until(EC.presence_of_element_located((By.ID, "onetrust-reject-all-handler")))

# Click the "Reject All" button
reject_all_button.click()

occupancy_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='occupancy-config']")))
occupancy_button.click()

button_menouno = wait.until(EC.element_to_be_clickable((By.XPATH, '//button[@tabindex="-1" and @type="button"]')))
button_menouno.click()

# Wait for the "Fatto" button to be clickable
fatto_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//span[text()='Fatto']")))

# Click the "Fatto" button
fatto_button.click()

time.sleep(5)

# Find the element with the string "Padova: strutture trovate con data specificata"
padova_data_strutture = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[contains(text(), 'Padova:')]")))

# Extract the number after the word "Padova"
padova_text = padova_data_strutture.text
available_structures_padua = int(padova_text.split(":")[1].split(" ")[1])

class next_14_days:
    def __init__(self):
        self.nights = []
        self.occupancy_rates = []
        self.lower_prices = []

    def add_info(self, night, occupancy_rate, lower_price):
        self.nights.append(night)
        self.occupancy_rates.append(occupancy_rate)
        self.lower_prices.append(lower_price)

    def display(self):
        for i in range(len(self.nights)):
            print(f"Night: {self.nights[i]}")
            print(f"Occupancy Rate: {self.occupancy_rates[i]}%")
            print(f"Lower Price: ${self.lower_prices[i]}")
            print("---------------------------")

info = next_14_days()

# for loop to change the date of the check-in adding 1 day each loop: from today to 14 days from today:

for i in range(14):
    check_in_date = start_date + datetime.timedelta(days=i)
    start_date_str = start_date.strftime('%d %B %Y').replace('January', 'gennaio').replace('February', 'febbraio').replace('March', 'marzo').replace('April', 'aprile').replace('May', 'maggio').replace('June', 'giugno').replace('July', 'luglio').replace('August', 'agosto').replace('September', 'settembre').replace('October', 'ottobre').replace('November', 'novembre').replace('December', 'dicembre')
    print(check_in_date, start_date_str)
    # Click the "Data del check-in" button
    checkin_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='date-display-field-start']")))
    checkin_button.click()

    # Select the check-in date (e.g. September 11, 2023)
    checkin_date_xpath = f"//span[@aria-label='{start_date_str}']"
    argument_checkin_date = wait.until(EC.element_to_be_clickable((By.XPATH, checkin_date_xpath)))
    checkin_date = argument_checkin_date
    checkin_date.click()

    # Attendi che il pulsante "Cerca" diventi cliccabile e poi fai clic su di esso
    search_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Cerca']]")))
    search_button.click()

    # wait 5 seconds
    time.sleep(5)

        # find the % occupancy rate using the variables tot_structures_padua and available_structures_padua
    occupancy_rate = round(((tot_structures_padua-available_structures_padua) / tot_structures_padua) * 100, 2)
    print("float occupancy rate: "+ str(occupancy_rate) )


    print("tot stutture a Padova: " + str(tot_structures_padua))
    print(f"stutture a Padova in data:{start_date_str} " + str(available_structures_padua))
    print(f"percentuale occupazione Padova in data{start_date_str}: " + str(occupancy_rate) + "%" )


    ignore_button = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label=\"Ignora le informazioni sull'accesso.\"]")))
    ignore_button.click()

    # Click the "Ordina" button
    sort_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='sorters-dropdown-trigger']")))
    sort_button.click()

    prezzo_piu_basso = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Prezzo (prima il più basso)']]"))) 
    prezzo_piu_basso.click()

    lower_price = 120 - i  # Another example calculation
    info.add_info(start_date_str, occupancy_rate, lower_price)

    # Example usage:
   # info = next_14_days(night="2023-09-15", occupancy_rate=95, lower_price=120)

info.display()




