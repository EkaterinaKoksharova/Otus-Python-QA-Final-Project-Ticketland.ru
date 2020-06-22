*** Settings ***
Documentation   Suite description

Library     ../robottest/RobotFixturesLib.py
Library     ../pages/LoginPage.py   ${chrome_logger}     ${browser}
Library     Selenium2Library
Library     RequestsLibrary

*** Keywords ***

browser
    chrome

logger
    chrome logger

*** Variables ***

${BaseUrl}   http://www.ticketland.ru
${browser}=    browser
${chrome_logger}=



*** Test Cases ***
Test Open Site
    go to login page
