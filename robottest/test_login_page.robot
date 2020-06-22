*** Settings ***

Resource     RobotLoginPage.robot
Test Teardown   Close browser

*** Variables ***

${login}=   koksharova3093@gmail.com
${password}=    999999

*** Test Cases ***
Test Login to tickeland.ru
    Open ticketland login page
    Enter credentials   ${login_input}  ${login}
    Enter credentials   ${password_input}   ${password}
    Click login button
    Wait logout button is visible
    Assert curent url   ${AccountUrl}
