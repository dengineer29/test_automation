***Settings***
Library    practice.PrintJobKeywords    WITH NAME    PJ
Variables    variable.py

***Keywords***
Validate Print Job
    [Arguments]    ${job_data}

    ${job}=    PJ.Create Print Job    ${job_data}

    Should Not Be Empty    ${job}

***Test Cases***
Validate Color Print Jobs
    [Template]    Validate Print Job

    ${PRINT_JOBS}[0]
    ${PRINT_JOBS}[1]