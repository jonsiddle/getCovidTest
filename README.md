# getCovidTest
Streamline requesting a Covid test (UK).

The UK process for getting a Covid test requires *a lot* of information to be entered, and has no queueing system.

This script is designed to streamline the process of trying to get a test, leaving the user with only two tasks to perform:

 * Pass the captcha - to prove you're actually a human trying to get a test
 * Finalising the registration - picking a centre and confirming the booking are left for the user

## Requirements

 * Python 3
 * Selenium
 * Firefox and geckodriver or (untested) Chrome and chromedriver
 * Selenium and fake-useragent Python libraries

```
$ pip3 install -r requirements.txt
```

## Running

Edit `getCovidTest.json` and set everything appropriately. In particular, you MUST remove any "REPLACE" text.

Run:

```
$ python3 getCovidTest.py
```

 * It will do most of the work for you
 * You will (almost certainly) have to pass a captcha. It will likely challenge you several times due to automation detection, but it's still easily a net win.
 * Once it's gone through the process, it will try to refresh until a test centre is available
 * You will need to complete the process yourself


