*** Settings ***
Library    resources.practice.PrintJobKeywords    WITH NAME  PJ

*** Test Cases ***
Color Job Display Should Contain Username
    ${job}=    PJ.Create Color Job
    ...    skadi  park.pdf  100kb  05/05/2026  IM307+  red
    ${result}=    PJ.get_display    ${job}
    Should Contain    ${result}    skadi

Print Job Contains Black and White
    ${job}=     PJ.Create BW Job
    ...     potchi  dagat.docx  18kb    11/05/2026  MP3055
    ${result}=  PJ.get_display  ${job}
    Should Contain  ${result}   Black and White print 

Cancel Contains Keyword 
    ${job}=     PJ.Create Color Job
    ...     skadi  park.pdf  100kb  05/05/2026  IM307+  red
    ${result}=  PJ.get_cancel_message   ${job}
    Should Contain  ${result}   red

Keyword Test
    ${color}=     Set Variable    red
    Should Be Equal     ${color}    red
    Run Keyword If    '${color}' == 'red'    Log    Match found