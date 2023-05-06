import json
from selenium import webdriver
import pandas as pd
import selenium
from selenium.webdriver.common.by import By
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
website = 'https://www.foodnetwork.com/recipes/food-network-kitchen/steamed-asparagus-recipe2-1916138'
path = 'C:/Users/ghuyjgvyuyg/Desktop/Chromedriver'
driver = webdriver.Chrome(options=options,executable_path=path)
driver.get(website)
closeAdd=driver.find_element(By.XPATH,"//a[@data-dismiss='international-modal']")
closeAdd.click()
data=[]
for x in range(0, 7):
    Nom=driver.find_element(By.XPATH, "//h1[@class='o-AssetTitle__a-Headline']//span").text
    try:
        Item={
        'nom':Nom, 
        'ingrediant1':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[2]").text,
        'ingrediant2':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[3]").text,
        'ingrediant3':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[4]").text,
        'ingrediant4':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[5]").text
        }
    except:
        try:
            Item={
        'nom':Nom, 
        'ingrediant1':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[2]").text,
        'ingrediant2':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[3]").text,
        'ingrediant3':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[4]").text,
        'ingrediant4':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[5]").text,
        'ingrediant5':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[6]").text
        }  
        except:
            try:
                Item={
        'nom':Nom, 
        'ingrediant1':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[2]").text,
        'ingrediant2':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[3]").text,
        'ingrediant3':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[4]").text,
        'ingrediant4':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[5]").text,
        'ingrediant5':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[6]").text,
        'ingrediant6':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[7]").text
        }
            except:
                try:
                    Item={
        'nom':Nom, 
        'ingrediant1':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[2]").text,
        'ingrediant2':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[3]").text,
        'ingrediant3':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[4]").text,
        'ingrediant4':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[5]").text,
        'ingrediant5':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[6]").text,
        'ingrediant6':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[7]").text,
        'ingrediant7':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[8]").text
        }
                except:
                    Item={
        'nom':Nom, 
        'ingrediant1':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[2]").text,
        'ingrediant2':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[3]").text,
        'ingrediant3':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[4]").text,
        'ingrediant4':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[5]").text,
        'ingrediant5':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[6]").text,
        'ingrediant6':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[7]").text,
        'ingrediant7':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[8]").text,
        'ingrediant8':driver.find_element(By.XPATH, "//div[@class='o-Ingredients__m-Body']//p[9]").text
        }

    print(Item)
    data.append(Item)
    driver.find_element(By.XPATH, "//a[@data-type='next']").click()
with open('recipes.json','w') as f:
    json.dump(data,f)                  

               


                      






    

    





"""try:
    cars=driver.find_elements(By.XPATH,"//div[@class='car-box']")
except:
    cars = driver.find_elements(By.XPATH, "//div[@class='car-box no-show']")
data = []
data2=[]
for car in cars:
    try:
        image=car.find_element(By.XPATH,".// img[@class='lazy-load loaded']").get_attribute('data-src')
    except:
        image=car.find_element(By.XPATH,".// img[@class='lazy-load']").get_attribute('data-src')
    item3={
'nom': car.find_element(By.XPATH,".//div [@class='car-name text-24 text-bold']").text,
        'nbr_places': car.find_element(By.XPATH,".//ul [@class='dc-list dc-list-icon dc-list-md text-14 dc-list-horizontal dc-list-mt-8 car-params mt-8 text-gray-500']/li[1]").text,
        'nbr_bagage': car.find_element(By.XPATH,".//ul [@class='dc-list dc-list-icon dc-list-md text-14 dc-list-horizontal dc-list-mt-8 car-params mt-8 text-gray-500']/li[2]").text,
        'nbr_portes': car.find_element(By.XPATH,".//ul [@class='dc-list dc-list-icon dc-list-md text-14 dc-list-horizontal dc-list-mt-8 car-params mt-8 text-gray-500']/li[3]").text,
        'climatise ou pas': car.find_element(By.XPATH,".//ul [@class='dc-list dc-list-icon dc-list-md text-14 dc-list-horizontal dc-list-mt-8 car-params mt-8 text-gray-500']/li[4]").text,
        'manuelle ou pas': car.find_element(By.XPATH,".//ul [@class='dc-list dc-list-icon dc-list-md text-14 dc-list-horizontal dc-list-mt-8 car-params mt-8 text-gray-500']/li[5]").text,
        'prix': car.find_element(By.XPATH,".//div [@class='price-item-price-main']").text,
        'image': image
    }
    print(item3)
    data.append(item3)
    with open('locVoitureRabat.json','w') as f:
        json.dump(data,f)"""
#print(data)