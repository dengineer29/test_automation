#Write a full .robot test file that imports your library, creates a color job, adds it to the queue, checks the queue size is 1, and logs the job display. Run it and check log.html.

***Settings***
Library     resources.practice.PrintJobKeywords     WITH NAME   PJ

***Test Cases***
Queue Is empty
    ${empty}=    PJ.Queue Is Empty
    Run Keyword If    '${empty}' == 'True'    Log    Match found

Create Color Job
    ${job}=     Create Color Job
    ...     potchi  imissskadi.pdf  18kb    today   MP3055  red
    PJ.Add Job To Queue     ${job}
    ${result}=  PJ.Get Queue Size
    Run Keyword If    '${result}' == '1'    Log    Match found

Black And White
    ${job}=     Create BW Job
    ...     potchi  imissskadi.pdf  18kb    today   MP3055
    ${display}=     PJ.Get Display    ${job}
    Should Contain      ${display}      Black and White

# Test 3: Cancel message contains job color
# Create ColorPrintJob with color "blue", get cancel message,
# Should Contain "blue"

Cancel Job Color
    ${job}=     Create Color Job
    ...     potchi  imissskadi.pdf  18kb    today   MP3055  blue
    ${message}=     PJ.Get Cancel Message   ${job}
    Should Contain      ${message}      blue