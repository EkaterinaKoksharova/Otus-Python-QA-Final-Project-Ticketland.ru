*** Settings ***
Documentation   Suite description

Library     pages.login_page.py
Library     Selenium2Library
Library     RequestsLibrary


*** Variables ***

${BaseUrl}   http://www.ticketland.ru

*** Test Cases ***
Test Open Site
    Go to login page
