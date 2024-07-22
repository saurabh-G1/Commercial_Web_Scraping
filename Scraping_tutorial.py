from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager # type: ignore
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
import time
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd

import openpyxl
from selenium.webdriver.common.by import By

path = r"C:\Users\saurabh.gaud\Desktop\Scraped data storage\webdata.xlsx"

# url='https://books.toscrape.com/'

# 'chrome-win64 (1)\chrome-win64\chrome.exe'
chrome_options = Options()
chrome_options.add_experimental_option('detach',True)
chrome_options_binary_location = r'C:\Users\saurabh.gaud\Desktop\Corner String\chrome-win64 (1)\chrome-win64\chrome.exe'
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("--no-sandbox")  

driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=chrome_options)
# driver.get(url)
# driver.maximize_window()
# -------------------------------------------------------------------------------
# page_title = driver.find_element(By.XPATH, "//li[@class='current']").text
# # print(page_title)
# page_Last_number=page_title.split()[-1]

# pages_count = int(page_Last_number)
# print(pages_count)
# --------------------------------------------------------------------------------------
def scrape_titles_from_page():
            Books = driver.find_elements(By.XPATH,'//a[@title]')
            books = []
            for i in Books:
                i.click()
                book_title=driver.find_element(By.XPATH, "//h1").text
                print(book_title)
               
                books.append(book_title)
                # book_info = driver.find_elements(By.XPATH,"//tr/th")
                # for i in book_info:
                #     print(i.text)
                # book_val = driver.find_elements(By.XPATH, "//tr/td")
                # for j in book_val:
                #     print(j.text)
                # books_per_page=len(Books)
                # print(books_per_page)
                driver.back()
            return books
                
                # books_per_page=len(Books)
                # print(books_per_page)
                # print(i.text)
                
            # Move to the next page
def main():
    book_tit=[] 
    url='https://books.toscrape.com/'
    driver.get(url)
    driver.maximize_window() 
    
    
#     page_title = driver.find_element(By.XPATH, "//li[@class='current']").text
#     print(page_title)   
#    # print(page_title)
#     page_Last_number=page_title.split()[-1]
#     pages_count = int(page_Last_number)
    for page in range(1, 4):
        
        # book_tit = scrape_titles_from_page()
        titles = scrape_titles_from_page()
        book_tit.extend(titles)
        
        
        
        try:
            next_button=driver.find_element(By.XPATH,"//li[@class='next']/a")
            # next_button = WebDriverWait(driver, 10).until(
                # EC.element_to_be_clickable((By.XPATH, "//li[@class='next']/a"))
            # )
            if next_button.is_displayed() and next_button.is_enabled():
                next_button.click()
                time.sleep(6)  # Adjust sleep time if necessary
            else:
                print("Next button is not interactable.")
                break
        except Exception as e:
            print(f"An error occurred while moving to the next page: {e}")
            break
    
    df = pd.DataFrame(book_tit, columns=["Book Title"])

    # Save the DataFrame to an Excel file
    df.to_excel("book_titles.xlsx", index=True)
        
     
        # try:
        #     next_button = WebDriverWait(driver, 10).until(
        #         EC.element_to_be_clickable((By.XPATH, "//li[@class='next']"))
        #     )
        #     next_button.click()
        #     time.sleep(2)  # Adjust sleep time if necessary
        # except Exception as e:
        #     print(f"An error occurred while moving to the next page: {e}")
        #     break

    
        # driver.quit()


    
if __name__ == "__main__":
    main()
    
    
    
    
    
    
    
    












