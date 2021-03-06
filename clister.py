
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.file_detector import LocalFileDetector
import requests
import time
import datetime
import os
import shutil
import sys
import imaplib
import json
import email
from email.header import decode_header
import webbrowser
# import os
from inspect import getsourcefile
from os.path import abspath
from datetime import date
from PIL import Image
# from gmail import Gmail
from io import StringIO
from html.parser import HTMLParser
import warnings

warnings.filterwarnings('ignore')
# sys.stdout = open(os.devnull, 'w')

class gettingInfoParse(object):
    def __init__(self):
        self.title = ""

#------------------------------- Set Up Necessary Directories ---------

class listingInfoParse():
    def __init__(self):
        self.loc = ''

class MLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.strict = False
        self.convert_charrefs= True
        self.text = StringIO()
    def handle_data(self, d):
        self.text.write(d)
    def get_data(self):
        return self.text.getvalue()

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()
#------------------------------  Driver Navigation -----------------

def clickDoneOnImageUploading(listing):
	listing.driver.find_element_by_css_selector("button.bigbutton").click()

# Don't always have to do this
def clickAbideByGuidelines(listing):
    try:
        listing.driver.find_element_by_css_selector("div.submit_button button.pickbutton").click()
    except:
        pass

def clickClassImageUploader(listing):
	
    listing.driver.find_element_by_id("classic").click()

def clickListingType(listing):
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.type+"')]]").click()
    except:
        pass
# //span[text()[contains(.,'job offered')]]
def clickListingCategory(listing):
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.type+"')]]").click()
    except:
        pass
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.type+"')]]").click()
    except:
        pass
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.category+"')]]").click()
    except:
        pass
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.type+"')]]").click()
    except:
        pass
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.category+"')]]").click()
    except:
        pass
    try:
        listing.driver.find_element_by_css_selector("button.pickbutton").click()
    except:
        pass
    try:
        listing.driver.find_element_by_xpath("//span[text()[contains(.,'"+listing.category+"')]]").click()
    except:
        pass
    

def uploadImagePath(listing,image):
	# listing.driver.find_element_by_xpath(".//*[@id='uploader']/form/input[3]").send_keys(Keys.CONTROL + "a")
	listing.driver.find_element_by_xpath(".//*[@id='uploader']/form/input[3]").send_keys(image)

def fillOutListing(listing, flag):
    time.sleep(5)
    listing.driver.find_element_by_css_selector("[name='FromEMail']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='FromEMail']").send_keys(listing.email)
    # listing.driver.find_element_by_css_selector("[name='ConfirmEMail']").send_keys(listing.email)
    title = strip_tags(listing.title)
    listing.driver.find_element_by_css_selector("[name='PostingTitle']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='PostingTitle']").send_keys(title)
    listing.driver.find_element_by_css_selector("[name='geographic_area']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='geographic_area']").send_keys(listing.city)
    listing.driver.find_element_by_css_selector("[name='postal']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='postal']").send_keys(listing.postal)
    print("#######postal code#######"+listing.postal)
    body = strip_tags(listing.body)
    listing.driver.find_element_by_css_selector("[name='PostingBody']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='PostingBody']").send_keys(body)
    listing.driver.find_element_by_css_selector("[name='price']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='price']").send_keys(listing.price)
    listing.driver.find_element_by_css_selector("[name='surface_area']").send_keys(Keys.CONTROL + "a")
    listing.driver.find_element_by_css_selector("[name='surface_area']").send_keys(listing.sqft)
    listing.driver.find_element_by_css_selector("label.housing_type span.ui-selectmenu-text").click()
    time.sleep(1)
    if(listing.category == "real estate - by broker"):
        if (listing.housing_type == "apartment"):
            listing.driver.find_element_by_css_selector("li[id='ui-id-9']").click()#9,14
        else:
            listing.driver.find_element_by_css_selector("li[id='ui-id-14']").click()#9,14

        listing.driver.find_element_by_css_selector("label.laundry span.ui-selectmenu-text").click()
        time.sleep(1)
        listing.driver.find_element_by_css_selector("li[id='ui-id-26']").click()
        listing.driver.find_element_by_css_selector("label.parking span.ui-selectmenu-text").click()
        time.sleep(1)
        listing.driver.find_element_by_css_selector("li[id='ui-id-32']").click()
        listing.driver.find_element_by_css_selector("label.bedrooms span.ui-selectmenu-text").click()
        time.sleep(1)
        if(listing.bedrooms != None):
            numbed = int(listing.bedrooms)+36
            listing.driver.find_element_by_css_selector("li[id='ui-id-"+str(numbed)+"']").click()
        else:
            listing.driver.find_element_by_css_selector("li[id='ui-id-"+str(36)+"']").click()
        if(listing.bathrooms != None):
            numbath = int(listing.bathrooms)*2+46
            listing.driver.find_element_by_css_selector("label.bathrooms span.ui-selectmenu-text").click()
            time.sleep(1)
            listing.driver.find_element_by_css_selector("li[id='ui-id-"+str(numbath)+"']").click()
        else:
            time.sleep(1)
            listing.driver.find_element_by_css_selector("li[id='ui-id-"+str(46)+"']").click()
        
        if (listing.furnished == "1"):
            listing.driver.find_element_by_xpath("//span[text()[contains(.,'furnished')]]").click()

        today = date.today()
        tod = today.strftime("%a, %d %b %Y")
        listing.driver.find_element_by_css_selector("input.movein_date").send_keys(Keys.CONTROL + "a")
        listing.driver.find_element_by_css_selector("input.movein_date").send_keys(tod)
        # if(flag != "recursive"):
        #     listing.driver.find_element_by_xpath("//span[text()[contains(.,'no replies to this email')]]").click()
        #     listing.driver.find_element_by_xpath("//span[text()[contains(.,'show my phone number')]]").click()
        #     listing.driver.find_element_by_xpath("//span[text()[contains(.,'text/sms OK')]]").click()
        #     listing.driver.find_element_by_css_selector("[name='contact_phone']").send_keys(listing.telephone)
    else:
        if (listing.housing_type == "apartment"):
            listing.driver.find_element_by_css_selector("li[id='ui-id-11']").click()#9,14
        else:
            listing.driver.find_element_by_css_selector("li[id='ui-id-16']").click()#9,14

        listing.driver.find_element_by_css_selector("label.laundry span.ui-selectmenu-text").click()
        time.sleep(1)
        listing.driver.find_element_by_css_selector("li[id='ui-id-28']").click()
        listing.driver.find_element_by_css_selector("label.parking span.ui-selectmenu-text").click()
        time.sleep(1)
        listing.driver.find_element_by_css_selector("li[id='ui-id-34']").click()
        listing.driver.find_element_by_css_selector("label.bedrooms span.ui-selectmenu-text").click()
        time.sleep(1)
        numbed = int(listing.bedrooms)+38
        listing.driver.find_element_by_css_selector("li[id='ui-id-"+str(numbed)+"']").click()
        numbath = int(listing.bathrooms)*2+48
        listing.driver.find_element_by_css_selector("label.bathrooms span.ui-selectmenu-text").click()
        time.sleep(1)
        listing.driver.find_element_by_css_selector("li[id='ui-id-"+str(numbath)+"']").click()
        if (listing.furnished == "1"):
            listing.driver.find_element_by_xpath("//span[text()[contains(.,'furnished')]]").click()

        today = date.today()
        tod = today.strftime("%a, %d %b %Y")
        listing.driver.find_element_by_css_selector("input.movein_date").send_keys(Keys.CONTROL + "a")
        listing.driver.find_element_by_css_selector("input.movein_date").send_keys(tod)
        # if(flag != "recursive"):
        #     # listing.driver.find_element_by_xpath("//span[text()[contains(.,'no replies to this email')]]").click()
        #     listing.driver.find_element_by_xpath("//span[text()[contains(.,'show my phone number')]]").click()
        #     listing.driver.find_element_by_xpath("//span[text()[contains(.,'text/sms OK')]]").click()
        #     listing.driver.find_element_by_css_selector("[name='contact_phone']").send_keys(listing.telephone)
    
    listing.driver.find_element_by_css_selector("div.submit_button button").click()
    time.sleep(1)
def fillOutGeolocation(listing):
    # time.sleep(3)
    listing.driver.find_element_by_css_selector("button.bigbutton").click()
    # time.sleep(10)
    time.sleep(1)
    try:
        listing.driver.find_element_by_css_selector("button[name='area_change_ok']").click()
    except:
        pass
    try:
        listing.driver.find_element_by_css_selector("ul.selection-list li").click()
    except:
        pass
    try:
        listing.driver.find_element_by_css_selector("button.pickbutton").click()
        return "recursive"
    except:
        pass
    time.sleep(1)
    return "success"
def removeImgExifData(path):
    filename, extension = os.path.splitext(path)
    fullFilename = filename+extension
    image = Image.open(fullFilename)
    data = list(image.getdata())
    imageNoExif = Image.new(image.mode, image.size)
    imageNoExif.putdata(data)
    imageNoExif.save(filename + "copy" + extension)
    os.remove(filename + extension)
    os.rename(filename + "copy" + extension,fullFilename)

def uploadListingImages(listing):
    time.sleep(1)
    # print("uploading image..")
    clickClassImageUploader(listing)
    for image in listing.images:
        removeImgExifData(image)
        # print("image: "+image)
        uploadImagePath(listing,image)
        time.sleep(1)
    clickDoneOnImageUploading(listing)
    time.sleep(1)

def clickAcceptTerms(listing):
    listing.driver.find_element_by_xpath("//*[@id='pagecontainer']/section/section[1]//button[contains(.,'ACCEPT the terms of use')]").click()

def clickPublishListing(listing):
	listing.driver.find_element_by_css_selector("button[type='submit']").click()

def postListing(listing):
    listing.driver.find_element_by_css_selector("a#post").click()
    clickListingType(listing)
    clickListingCategory(listing)
    clickAbideByGuidelines(listing)
    fillOutListing(listing, "normal")
    res = fillOutGeolocation(listing)
    if(res == 'recursive'):
        # return
        clickListingType(listing)
        clickListingCategory(listing)
        clickAbideByGuidelines(listing)
        fillOutListing(listing, "recursive")
        res = fillOutGeolocation(listing)
    uploadListingImages(listing)
    clickPublishListing(listing)
    return

# --------------------------- Emails ---------------------

def getFirstCraigslistEmailUrl(listing,emails):
    for email in emails:
        email.fetch()
        email.read()
        if listing.title[0:15] in email.subject:
            emailMessage = email.body
            email.archive()
            acceptTermsLink = emailMessage.split("https")
            acceptTermsLink = acceptTermsLink[1].split("\r\n")
            return acceptTermsLink[0]

def acceptTermsAndConditions(listing,termsUrl):
    listing.driver.get("https" + termsUrl)
    clickAcceptTerms(listing)

def acceptEmailTerms(listing):
    
    # print('Enter the gmailid and password')
    gmailId, passWord = listing.email, listing.password
    # try:
        
    listing.driver.get(r'https://accounts.google.com/signin/v2/identifier?continue='+'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1'+'&flowName=GlifWebSignIn&flowEntry = ServiceLogin')
    listing.driver.implicitly_wait(15)

    loginBox = listing.driver.find_element_by_xpath('//*[@id ="identifierId"]')
    loginBox.send_keys(gmailId)

    nextButton = listing.driver.find_elements_by_xpath('//*[@id ="identifierNext"]')
    nextButton[0].click()
    time.sleep(2)
    passWordBox = listing.driver.find_element_by_xpath(
        '//*[@id ="password"]/div[1]/div / div[1]/input')
    passWordBox.send_keys(passWord)

    nextButton = listing.driver.find_elements_by_xpath('//*[@id ="passwordNext"]')
    nextButton[0].click()

    # print('Login Successful...!!')
    # listing.driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
    time.sleep(3)

    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(gmailId, passWord)
    mail.list()
    # Out: list of "folders" aka labels in gmail.
    mail.select("inbox") # connect to inbox.
    
    result, data = mail.search(None, "FROM 'robot@craigslist.org'")
    
    ids = data[0] # data is a list.
    id_list = ids.split() # ids is a space separated string
    latest_email_id = id_list[-1] # get the latest
    
    result, data = mail.fetch(latest_email_id, "(RFC822)") # fetch the email body (RFC822) for the given ID
    
    raw_email = data[0][1] # here's the body, which is raw text of the whole email
    # including headers and alternate payloads
    raw_email = str(raw_email)
    acctermurl = raw_email.split("https://")[1].split(r'\r\n')[0]
    listing.driver.get(r'https://'+ acctermurl)
    time.sleep(2)
    listing.driver.find_element_by_xpath("//a[text()[contains(.,'log out')]]").click()
    time.sleep(5)


# --------------------------- Craigslist Posting Actions ---------------

def moveFolder(folder,listedFolderDirectory):

    now = time.strftime("%c")

    # %x >>>get the date like this 7/16/2014
    today_dir = os.path.join(listedFolderDirectory,time.strftime("%x").replace("/","-"))

    # Make todays date under the listed directory
    makeFolder(today_dir)

    # Move the folder to the listed todays date directory
    shutil.move(folder, today_dir)

def parsing(f,splits):
    fsplit = f.split(splits)
    return fsplit[1]


# If more than 24 hours passed will look like
# 1 day, 13:37:47.356000
def hasItBeenXDaysSinceFolderListed(folder,x):
    dateSplit = folder.split('-')
    folderDate = datetime.date(int(dateSplit[2]) + 2000, int(dateSplit[0]), int(dateSplit[1]))
    currentDatetime = datetime.datetime.now()
    folderTimePassed = currentDatetime - datetime.datetime.combine(folderDate, datetime.time())
    if "day" not in str(folderTimePassed):
        return False
    daysPassed = str(folderTimePassed).split('day')[0]
    if int(daysPassed.strip()) >= x:
        return True
    return False

def getOrderedListingImages(listingFolder):
    # print ('listingFolder',listingFolder)
    listingImages = [f for f in os.listdir(listingFolder) if os.path.isfile(os.path.join(listingFolder,f)) and f[0] != '.'  and f != 'info.txt' ]
    # print ('listingImages',listingImages)
    secondList = [os.path.abspath(os.path.join(listingFolder, x)) for x in listingImages if (x[1] != "_") or (x[0].isdigit() == False) and x[0] != '.']
    firstList = [os.path.abspath(os.path.join(listingFolder, x)) for x in listingImages if (x[1] == "_") and (x[0].isdigit()) and x[0] != '.']

    firstList.sort()
    secondList.sort()

    orderedListingImages = []
    for x in firstList:orderedListingImages.append(x)
    for x in secondList:orderedListingImages.append(x)
    return orderedListingImages

#------------------------------------------------------realtor.com

def getstatedataforsale(jsdata):
    
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    listingsFolderDirectory = os.path.join(application_path, "listings")
    listedFolderDirectory = os.path.join(listingsFolderDirectory,"listed")

    chromedriver = os.path.join(application_path, "chromedriver")
    os.environ["webdriver.chrome.driver"] = chromedriver

    img_src = []
    
    for i in range(1, 200):
        if "photo_"+str(i) in jsdata:
            img_src.append(jsdata["photo_"+str(i)])
        else:
            break
    # make directory
    path = 'images/'+jsdata["recno"]

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
    
        # Create a new directory because it does not exist 
        os.makedirs(path)

    # -- empty directory
    folder = 'images/'+jsdata["recno"]
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    count_image = len(img_src)
    if (count_image > 0):
        # print ("Saving Images....")
        img_src = list(dict.fromkeys(img_src))
        i = 0
        for item in img_src:
            i = i + 1
            with open(folder+'/'+str(i)+'.jpg', 'wb') as handle:
                response = requests.get(item, stream=True)

                # if not response.ok:
                #     print(response)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

    return ""

def getstatedataforrent(jsdata):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)

    listingsFolderDirectory = os.path.join(application_path, "listings")
    listedFolderDirectory = os.path.join(listingsFolderDirectory,"listed")

    chromedriver = os.path.join(application_path, "chromedriver")
    os.environ["webdriver.chrome.driver"] = chromedriver

    img_src = []
    
    for i in range(1, 200):
        if "photo_"+str(i) in jsdata:
            img_src.append(jsdata["photo_"+str(i)])
        else:
            break
    path = 'images/'+jsdata["recno"]

    # Check whether the specified path exists or not
    isExist = os.path.exists(path)

    if not isExist:
        os.makedirs(path)

    folder = 'images/'+jsdata["recno"]
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    count_image = len(img_src)
    if (count_image > 0):
        img_src = list(dict.fromkeys(img_src))
        i = 0
        for item in img_src:
            i = i + 1
            with open(folder+'/'+str(i)+'.jpg', 'wb') as handle:
                response = requests.get(item, stream=True)

                for block in response.iter_content(1024):
                    if not block:
                        break

                    handle.write(block)

    return ""

def craiglister(jsdata):
    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(os.path.realpath(__file__))
        # print("path: "+application_path)

    # os.path.basename(__file__)
    # print(file_path, file_dir)
    
    listingsFolderDirectory = os.path.join(application_path, "listings")
    listedFolderDirectory = os.path.join(listingsFolderDirectory,"listed")

    chromedriver = os.path.join(application_path, "chromedriver")
    os.environ["webdriver.chrome.driver"] = chromedriver
    setting_data = []
    with open('setting.json') as json_file:
        setting_data = json.load(json_file)

    # Get all the date folders of listed items
    listedItemsFolders = [folder for folder in os.listdir(listedFolderDirectory) if folder[0] != "."]

    # Moving items that are 3 days or older back into the queue to get listed again
    for dayListedFolder in listedItemsFolders:

        if (hasItBeenXDaysSinceFolderListed(dayListedFolder,3) == False):
            continue

        listedFolders = [listedFolders for listedFolders in os.listdir(os.path.join(listedFolderDirectory,dayListedFolder)) if listedFolders[0] != "."]
        dayListedFolderDirectory = os.path.join(listedFolderDirectory,dayListedFolder)

        for listedFolder in listedFolders:
            theListedFolderDirectory = os.path.join(dayListedFolderDirectory,listedFolder)
            shutil.move(theListedFolderDirectory,listingsFolderDirectory)
        shutil.rmtree(dayListedFolderDirectory)


    # List Items
    listingFolders = [listing for listing in os.listdir(listingsFolderDirectory) if listing[0] != "." and listing != "listed"]
    listingFolder = listingFolders[0]
    listing = listingInfoParse()
    listing.email = setting_data["email"]
    listing.password = setting_data["password"]
    listing.fetchurl = setting_data["fetch_url"]
    listing.updateurl = setting_data["update_url"]
    listing.interval = setting_data["interval"]
    listing.loc = "ame"
    listing.recno = jsdata["recno"]
    listing.title = jsdata["title"]
    listing.type = "housing offered"
    if(jsdata["posting_type"] == "For Sale"):
        listing.category = "real estate - by broker"
    else:
        listing.category = "apartments / housing for rent"
    # listing.email = gmailUser
    listing.street = ""
    listing.city = jsdata["city_or_neighborhood"]
    listing.xstreet = ""
    listing.state = ""
    listing.postal = jsdata["postal_code"]
    listing.body = jsdata["description"]
    listing.body = listing.body.replace("<br>", "\n")
    listing.body = listing.body.replace("<p>", "\n")
    listing.body = listing.body.replace("</p>", "\n")
    
    listing.price = jsdata["price"]
    listing.housing_type = jsdata["housing_type"]
    listing.furnished = jsdata["furnished"]
    listing.bedrooms = jsdata["bedrooms"]
    listing.bathrooms = jsdata["bathrooms"]
    listing.sqft = jsdata["sqft"]
    listing.telephone = jsdata["telephone"]

    listing.images = getOrderedListingImages("images/"+jsdata["recno"])


    options = webdriver.ChromeOptions()
    listing.driver = webdriver.Chrome(chromedriver, options=options)
    try:
        listing.driver.get("https://craigslist.org?lang=en")
    except WebDriverException:
        print("failed: "+listing.recno)
        return
    

    postListing(listing)
    acceptEmailTerms(listing)
    response = requests.request("GET", listing.updateurl+listing.recno)
    print(response.json())
    # moveFolder(listingFolder,listedFolderDirectory)
    listing.driver.close()
    time.sleep(listing.interval)
    # print ("Waiting")


def postData(jsdata):
    if(jsdata["posting_type"] == "For Sale"):
        content = getstatedataforsale(jsdata)
    else:
        content = getstatedataforrent(jsdata)
    craiglister(jsdata)

folder = 'images'
for filename in os.listdir(folder):
    file_path = os.path.join(folder, filename)
    try:
        if os.path.isfile(file_path) or os.path.islink(file_path):
            os.unlink(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)
    except Exception as e:
        print('Failed to delete %s. Reason: %s' % (file_path, e))
while True:
    setting_data = []
    with open('setting.json') as json_file:
        setting_data = json.load(json_file)
    response = requests.request("GET", setting_data["fetch_url"])
    data = response.json()
    index = 0
    for dt in data:
        index = index + 1
        postData(dt)
        if(index%25 == 0):
            # print("waiting for 5 minutes")
            time.sleep(300)