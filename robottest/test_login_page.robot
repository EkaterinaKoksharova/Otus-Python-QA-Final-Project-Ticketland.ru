*** Settings ***
Documentation   Suite description

Library     RobotFixturesLib.py
Library     ../pages/LoginPage.py   browser     browser
Library     Selenium2Library
Library     RequestsLibrary


*** Variables ***

${BaseUrl}   http://www.ticketland.ru

*** Test Cases ***
Test Open Site
    go to login page
