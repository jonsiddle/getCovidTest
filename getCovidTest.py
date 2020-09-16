#!/usr/bin/env python3 -u
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from fake_useragent import UserAgent
import random
import json

SW = 1363
SH = 1054

with open("getCovidTest.json") as f:
    props = json.load(f)


def checkProp(p):
    if p == "REPLACE":
        raise ValueError("Please replace (or delete) all 'REPLACE' values in properties file")
    if isinstance(p, list):
        for entry in p:
            checkProp(entry)
    elif isinstance(p, dict):
        for k, v in p.items():
            checkProp(v)


checkProp(props)


genderMap = {"m": "gender", "f": "gender-2"}


def expandProps():
    props["gender"] = genderMap[props["gender"].lower()]
    for a in props["additional"]:
        a["gender"] = genderMap[a["gender"].lower()]


def retry(fn, times):
    for i in range(times-1):
        try:
            return fn()
        except:
            pass
    return fn()


def getCovidTest():
    ua = UserAgent()

    if props["browser"] == "chrome":
        options = webdriver.ChromeOptions()
        options.add_argument('window-size=%sx%s' % (SW, SH))
        options.add_argument("user-agent=" + ua.random)
        browser = webdriver.Chrome(chrome_options = options)
    elif props["browser"] == "firefox":
        profile = webdriver.FirefoxProfile()
        profile.set_preference("general.useragent.override", ua.random)
        browser = webdriver.Firefox(firefox_profile=profile)
        browser.set_window_size(SW, SH)
    else:
        raise KeyError("browser")



    try:
        browser.get("https://self-referral.test-for-coronavirus.service.gov.uk/antigen/name")

        WebDriverWait(browser, 5).until(EC.visibility_of_element_located((By.ID, "first-name")))

        inputFirstName = browser.find_element(By.ID, "first-name")
        inputFirstName.send_keys(props["forename"])

        inputSurname = browser.find_element(By.ID, "last-name")
        inputSurname.send_keys(props["surname"])

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        mobileAvailable = browser.find_element(By.ID, "mobile-available")
        mobileAvailable.click()

        mobileNumber = browser.find_element(By.ID, "mobile")
        mobileNumber.send_keys(props["mobile"])

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        emailAvailable = browser.find_element(By.ID, "email-available")
        emailAvailable.click()

        emailNumber = browser.find_element(By.ID, "email")
        emailNumber.send_keys(props["email"])

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        reason = browser.find_element(By.ID, "test-reason-3")  # Someone I live with has symptoms
        reason.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        reason = browser.find_element(By.ID, "condition-2")  # No symptoms myself
        reason.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        postcode = browser.find_element(By.ID, "postcode")
        postcode.send_keys(props["postcode"])

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        haveCar = browser.find_element(By.ID, "car-accessibility")
        haveCar.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Save and continue')]")
        continueButton.click()


        def waitForDriveThrough():
            WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "//.[contains(., 'At a drive-through test site')]")))

        retry(waitForDriveThrough, 5)

        driveThrough = browser.find_element(By.ID, "chosen-channel")
        driveThrough.click()

        ## Next page

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        continueButton = browser.find_element(By.XPATH, "//button[contains(@href, '/register/') and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        dobDay = browser.find_element(By.ID, "date-day")
        dobDay.send_keys(props["dobDay"])
        dobMonth = browser.find_element(By.ID, "date-month")
        dobMonth.send_keys(props["dobMonth"])
        dobYear = browser.find_element(By.ID, "date-year")
        dobYear.send_keys(props["dobYear"])

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        landlineAvailable = browser.find_element(By.ID, "landline-available")
        landlineAvailable.click()

        landlineAvailable = browser.find_element(By.ID, "landline")
        landlineAvailable.send_keys(props["landline"])

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        gender = browser.find_element(By.ID, props["gender"])
        gender.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        enthicity = browser.find_element(By.ID, "ethnicity-group-4")
        enthicity.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        enthicity = browser.find_element(By.ID, "ethnicity")
        enthicity.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        enthicity = browser.find_element(By.ID, "currently-working-3")  # no
        enthicity.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        country = browser.find_element(By.ID, "country")  # England
        country.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        nhsNo = browser.find_element(By.ID, "nhs-number-option-2")  # Don't know NHS No.
        nhsNo.click()

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
        continueButton.click()

        ## Next page

        continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Save and continue')]")
        continueButton.click()

        ## Next page

        for a in props["additional"]:
            addButton = browser.find_element(By.XPATH, "//button[contains(., 'Add person you live with')]")
            addButton.click()

            ## Next page

            inputFirstName = browser.find_element(By.ID, "first-name")
            inputFirstName.send_keys(a["forename"])

            inputSurname = browser.find_element(By.ID, "last-name")
            inputSurname.send_keys(a["surname"])

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            dobDay = browser.find_element(By.ID, "date-day")
            dobDay.send_keys(a["dobDay"])
            dobMonth = browser.find_element(By.ID, "date-month")
            dobMonth.send_keys(a["dobMonth"])
            dobYear = browser.find_element(By.ID, "date-year")
            dobYear.send_keys(a["dobYear"])

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            symptoms = browser.find_element(By.ID, "condition")  # Have symptoms
            symptoms.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            symptomDay = browser.find_element(By.ID, "date-day")
            symptomDay.send_keys(props["symptomDay"])
            symptomMonth = browser.find_element(By.ID, "date-month")
            symptomMonth.send_keys(props["symptomMonth"])
            symptomYear = browser.find_element(By.ID, "date-year")
            symptomYear.send_keys(props["symptomYear"])

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            mobileNumber = browser.find_element(By.ID, "mobile")
            mobileNumber.send_keys(props["mobile"])
            mobileNumber2 = browser.find_element(By.ID, "mobile-confirmation")
            mobileNumber2.send_keys(props["mobile"])

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            landlineAvailable = browser.find_element(By.ID, "landline-available")  # same as entered
            landlineAvailable.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            landlineAvailable = browser.find_element(By.ID, "email-available-2")  # no
            landlineAvailable.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            gender = browser.find_element(By.ID, a["gender"])
            gender.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            enthicity = browser.find_element(By.ID, "ethnicity-group-4")
            enthicity.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            enthicity = browser.find_element(By.ID, "ethnicity")
            enthicity.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            enthicity = browser.find_element(By.ID, "currently-working-3")  # no
            enthicity.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            country = browser.find_element(By.ID, "country")  # England
            country.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            postcode = browser.find_element(By.ID, "postcode-option")  # Same
            postcode.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            nhsNo = browser.find_element(By.ID, "nhs-number-option-2")  # Don't know NHS No.
            nhsNo.click()

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Continue')]")
            continueButton.click()

            ## Next page

            continueButton = browser.find_element(By.XPATH, "//button[@type='submit' and contains(., 'Save and continue')]")
            continueButton.click()

        continueButton = browser.find_element(By.XPATH, "//button[contains(., 'Save and continue')]")
        continueButton.click()

        ## Next page

        noTestSites = True
        tries = 0

        while noTestSites:

            findButton = browser.find_element(By.XPATH, "//button[contains(., 'Find a test site')]")
            findButton.click()

            noTestSites = False

            try:
                WebDriverWait(browser, 30).until(EC.presence_of_element_located((By.XPATH, "//p[text()='No test sites found']")))
                noTestSites = True
                tries += 1
                w = random.randint(30, 110)
                print("Try %d failed." % tries)
                print("Waiting for %ds..." % w)
                time.sleep(w)

                findLink = browser.find_element(By.XPATH, "//a[contains(@href, '/register/find-test-centre')]")
                findLink.click()
            except:
                raise

        print("Couldn't find failure notice - test sites might be available?")

    finally:
        pass


if __name__ == "__main__":
    expandProps()
    print("Will try to streamline the registration process. You will probably have to pass a captcha. If no tests are available, this will refresh until it appears that tests are available. You will need to actually make the booking once this is done.")
    getCovidTest()

