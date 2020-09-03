# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 23:23:51 2020

@author: Przemek
"""

from selenium import webdriver
import time



class TinderBot():
    
    
    def __init__(self):
        self.browser = webdriver.Chrome()
    
    def login(self):
        print('Author = [Przemysław Szmaj]')
        time.sleep(0.5)
        print('GitHub = https://github.com/PSZMAJ')
        time.sleep(0.5)
        print('YouTube = https://www.youtube.com/channel/UCewT7Lr5f6LWvqSPXm0JKRw')
        time.sleep(0.5)
        print('TinderBot.py ver. 1.0')
        time.sleep(0.5)
        print('Login with data with facebook')
    
    
        
        login = input('Hi, type Your mail: ')
        time.sleep(0.5)
        password = input('Hi, type Your password : ')
        self.browser.get('https://tinder.com/')
        print(self.browser.title)
        time.sleep(4)


        #### ---> Find akcept button and click
        self.button_agreed = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button/span')
        self.button_agreed.click()
        time.sleep(1)
        
        
        #### ---> Login with Facebook account
        self.buttonLoginWithFacebook = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button')
        self.buttonLoginWithFacebook.click()
        time.sleep(1)
        
        
        #### ---> Change windows to login with Facebook
        self.base_window = self.browser.window_handles[0]
        time.sleep(1)
        self.browser.switch_to_window(self.browser.window_handles[1])
        time.sleep(1)
        
        
        #### ---> Find login form, provide login and click
        self.facebookLogin = self.browser.find_element_by_xpath('//*[@id="email"]')
        time.sleep(1)
        self.facebookLogin.send_keys(login)
        time.sleep(1)
        
        
        #### ---> Find password form, provide password and click
        self.facebookPassword = self.browser.find_element_by_xpath('//*[@id="pass"]')
        time.sleep(1.5)
        self.facebookPassword.click()
        time.sleep(1.5)
        self.facebookPassword.send_keys(password)
        time.sleep(1.5)
        
        
        #### ---> Find button 'login' and click
        self.facebookLoginButton = self.browser.find_element_by_xpath('//*[@id="u_0_0"]')
        time.sleep(1.5)
        self.facebookLoginButton.click()
        time.sleep(1.5)
        self.browser.switch_to_window(self.browser.window_handles[0])
        time.sleep(2)
        
        #### ---> Allow Tinder Localization
        time.sleep(2)
        self.tinderAllowButton = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        time.sleep(1.5)
        self.tinderAllowButton.click()
        time.sleep(3)
        
        
        #### ---> Allow Tinder notification
        self.tinderAllowNotification = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]')
        time.sleep(1.5)
        self.tinderAllowNotification.click()
        time.sleep(1.5)
        
        time.sleep(1.5)
        time.sleep(1.5)
    
        #### ---> show and download information about person
    def like(self):
       
        time.sleep(0.5)
        self.infoName_Person = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/div/span')
        self.infoAge_Person = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[1]/div/div/span')
        self.infoMoreAbout_Person = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[1]/div[3]/div[6]/div/div[2]/div/div')
        self.getPhoto = self.browser.get_screenshot_as_file(self.infoName_Person.text + ".png")
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('Imie polubionej osoby to: ', self.infoName_Person.text, " wiek:", self.infoAge_Person.text)
        print(('Informacje z profilu:', self.infoMoreAbout_Person.text.replace("\n", "")))
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        self.buttonLikePerson = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        time.sleep(2.5)
        self.buttonLikePerson.click()
        time.sleep(2.5)
        

        #### ---> funkction auto swipe. 
        #### ---> If program will meet obstacle, next check exceptions
    def autoLike(self):
         while True:
            time.sleep(0.5)
            try:
                self.like()
                # self.get_info()
            except Exception:
                try:
                    self.closeAddStartWindow()
                except Exception:
                    self.closeMatch()
                         
           
    def closeAddStartWindow(self):
        time.sleep(0.5)
        self.notificationAddStartWindow = self.browser.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[1]')
        time.sleep(0.5)
        self.notificationAddStartWindow.click()
        
    def closeMatch(self):
        time.sleep(0.5)
        self.notificationMatchAllert = self.browser.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[2]/div/div/div[1]/div/div[3]/a')
        time.sleep(0.5)
        self.notificationMatchAllert.click() 
                    
TinderBotUser = TinderBot()
TinderBotUser.login()
TinderBotUser.autoLike()