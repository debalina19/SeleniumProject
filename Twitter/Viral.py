from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait

#class selenium.webdriver.support.select.Select(webelement)
from selenium.webdriver.support.select import Select


#CREATE THE WEBDRIVER OBJECT
driver = webdriver.Chrome()

#OPEN THE OFFERPOP WEBSITE
driver.get("http://www.offerpop.com")


#CLICK ON LOGIN
elem = driver.find_element_by_xpath(".//*[@id='globalTop']/li[6]/a")

elem.send_keys(Keys.RETURN)


#SWICTH TO THE LOGIN OPTION ALERT

alert = driver.switch_to_alert()

#SELECT TWITTER
driver.find_element_by_xpath(".//*[@id='loginbuttons']/div[2]/a/img").click()

#FILL IN USER NAME AND PASSWORD
elem = driver.find_element_by_id("username_or_email")
elem.send_keys("debalina19")
elem = driver.find_element_by_id("password")
elem.send_keys("abcd4321")

#CLICK ON ALLOW TO LOGIN

driver.find_element_by_id("allow").click()

#OPEN THE VIRAL APP

driver.find_element_by_xpath(".//*[@id='viral']/span").click();

#COPY THE BIT.LY LINK
elem = driver.find_element_by_xpath(".//*[@id='createCoupon']/table/tbody/tr[1]/td[2]/div[3]/span/span[1]/b");

elem_tweet = driver.find_element_by_name("form_tweet");
elem_tweet.send_keys(elem.text);

#FILL TIPPING POINT

driver.find_element_by_id("form_tp").send_keys("1234");

#SELECT THE TIME AND TIMEZONE

driver.find_element_by_id("form_to_time").click()
time= driver.find_element_by_id("form_to_time")
timelist = Select(time)
timelist.select_by_value("2:00am")

driver.find_element_by_id("form_to_tz").click()
time = driver.find_element_by_id("form_to_tz")
timelist = Select(time)
timelist.select_by_value("US/Pacific")


#CODE FOR DATE
driver.find_element_by_id("form_to_date").click()
#time.sleep(.2)
basetable = driver.find_element_by_class_name("ui-datepicker-calendar")
rows = basetable.find_elements_by_tag_name("tr")
tds = rows[5].find_elements_by_tag_name("td")
td = tds[6]

#ActionChains(driver).move_to_element(basetable).move_to_element(td).perform()
#driver.find_element_by_xpath(".//*[@id='ui-datepicker-div']/table/tbody/tr[4]/td[6]/a").click()


#NEW LINE

ActionChains(driver).move_to_element(basetable).move_to_element(td).send_keys(Keys.RETURN)

##END OF NEW LINE



#LOAD THE PICTURE
driver.find_element_by_id("form_pic").send_keys("/Users/debalina/Desktop/Untitled DVD.fpbf/BAZAAR AND NYC/USA0290.jpg")

#driver.find_element_by_id("form_pic").send_keys("/Users/debalina/Downloads/DEB4.jpg")


#POPULATE THE FORM DESCRIPTION
desc=driver.find_element_by_id("form_description")

ActionChains(driver).move_to_element(desc).perform()
driver.find_element_by_id("form_description").click()
driver.find_element_by_id("form_description").send_keys("This is a part of Regression Test")

#CLICK ON REEDEM

redeem=driver.find_element_by_id("form_redeem")
redeemlist=Select(redeem)
redeemlist.select_by_value("code")
driver.find_element_by_id("form_code").send_keys("OFF1")

#CLICK ON TWEET

driver.find_element_by_class_name("RedButton").send_keys(Keys.RETURN)
alert.accept();

conf=driver.find_element_by_class_name("OnLoadMessage").text

assert conf=="Tweet sent. The coupon is now live"
driver.quit()

#OnLoadMessage
'''
<div id="OnLoadMessage" class="OnLoadMessage" style="left: 459px; width: 347px;">
<div class="OnLoadMessageContent">Tweet sent.  The coupon is now live.</div>
</div>'''

print conf




