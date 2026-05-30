***Settings***
Library    resources.practice.PrintJobKeywords    WITH NAME    PJ
Variables    variable.py
Suite Setup    PJ.Load Log    cups_sample.log

***Keywords***
Validate Print Job
    [Arguments]    ${job_data}

    ${job}=    PJ.Create Print Job    ${job_data}

    Should Not Be Equal    ${job}    ${None}

Validate Status Is Pending
    [Arguments]     ${job_data}
    ${job}=     PJ.Create Print Job     ${job_data}
    ${status}=  PJ.Get Status   ${job}

    Should Be Equal      ${status}   pending

Validate Status Is Cancelled
    [Arguments]     ${job_data}
    ${job}=     PJ.Create Print Job     ${job_data}
    PJ.Get Cancel Message   ${job}
    ${is_cancelled}=    PJ.Get Status   ${job}
    Should Be Equal      ${is_cancelled}    cancelled

***Test Cases***
Validate Color Print Jobs
    [Template]    Validate Print Job

    ${COLOR_PRINT_JOBS}[0]
    ${COLOR_PRINT_JOBS}[1]

Status Is Pending
    [Template]      Validate Status Is Pending

    ${COLOR_PRINT_JOBS}[0]
    ${COLOR_PRINT_JOBS}[1]

Job Is Cancelled
    [Template]      Validate Status Is Cancelled

    ${COLOR_PRINT_JOBS}[0]
    ${COLOR_PRINT_JOBS}[1]

Submit Job To VirtualPrinter
    ${result}=    PJ.Submit Job To Printer    /etc/hostname
    Should Contain    ${result}    VirtualPrinter
           
Log Has Five Jobs
    ${total}=    PJ.Get Total Jobs
    Should Be Equal As Integers    ${total}    5

Log Has Twenty One Pages
    ${pages}=    PJ.Get Total Pages
    Should Be Equal As Integers    ${pages}    21

Top User Is Skadi
    ${user}=    PJ.Get Top User
    Should Be Equal    ${user}    skadi