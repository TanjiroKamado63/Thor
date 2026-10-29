@echo off
title AI & Jira Practical Library

:MENU
cls
echo ===============================================================================
echo                   AI AND JIRA PRACTICAL LIBRARY MANAGER
echo ===============================================================================
echo.
echo --- Python Code Files (1-16) [Opens in Notepad] ---
echo  1. 01_Table_Driven_Vacuum_Agent.py
echo  2. 02_Eight_Puzzle_BFS.py
echo  3. 03_Water_Jug_DFS.py
echo  4. 04_Romania_Map_Uniform_Cost_Search.py
echo  5. 05_Eight_Puzzle_Greedy_Best_First.py
echo  6. 06_Bayes_Disease_Probability.py
echo  7. 07_Naive_Bayes_Spam_Detection.py
echo  8. 08_Bayesian_Network_Burglary_Alarm.py
echo  9. 09_Iris_SVM_Classification.py
echo 10. 10_Diabetes_Linear_Regression.py
echo 11. 11_Digit_5_Logistic_Regression.py
echo 12. 12_Random_Forest_KFold_Cross_Validation.py
echo 13. 13_Iris_Decision_Tree_Classifier.py
echo 14. 14_Diabetes_Decision_Tree_Regressor.py
echo 15. 15_Iris_KNN_Classifier.py
echo 16. 16_Iris_Multiclass_Logistic_Regression.py
echo.
echo --- Practical PDFs (17-29) [Opens as PDF] ---
echo 17. All_AI_CODES.pdf
echo 18. Jira_Practical_11.pdf
echo 19. Jira_Practical_12.pdf
echo 20. Jira_Practical_2_Team_Creation_Role_Assignment.pdf
echo 21. Jira_Practical_3_Issue_Types_Configuration.pdf
echo 22. Jira_Practical_4_Issue_Management.pdf
echo 23. Practical_10_Jira.pdf
echo 24. Practical_5_Jira.pdf
echo 25. Practical_6_Jira.pdf
echo 26. Practical_7_Jira.pdf
echo 27. Practical_8_Jira.pdf
echo 28. Practical_9_Jira.pdf
echo 29. practical_01_Jira.pdf
echo.
echo ===============================================================================
echo D. Download ALL files
echo Q. Quit
echo ===============================================================================
echo.

set /p "choice=Enter choice (1-29, D, or Q): "

if /i "%choice%"=="Q" exit
if /i "%choice%"=="D" goto DOWNLOAD_ALL

if "%choice%"=="1" set "FILE=01_Table_Driven_Vacuum_Agent.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="2" set "FILE=02_Eight_Puzzle_BFS.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="3" set "FILE=03_Water_Jug_DFS.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="4" set "FILE=04_Romania_Map_Uniform_Cost_Search.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="5" set "FILE=05_Eight_Puzzle_Greedy_Best_First.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="6" set "FILE=06_Bayes_Disease_Probability.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="7" set "FILE=07_Naive_Bayes_Spam_Detection.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="8" set "FILE=08_Bayesian_Network_Burglary_Alarm.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="9" set "FILE=09_Iris_SVM_Classification.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="10" set "FILE=10_Diabetes_Linear_Regression.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="11" set "FILE=11_Digit_5_Logistic_Regression.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="12" set "FILE=12_Random_Forest_KFold_Cross_Validation.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="13" set "FILE=13_Iris_Decision_Tree_Classifier.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="14" set "FILE=14_Diabetes_Decision_Tree_Regressor.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="15" set "FILE=15_Iris_KNN_Classifier.py" & set "TYPE=py" & goto PROCESS
if "%choice%"=="16" set "FILE=16_Iris_Multiclass_Logistic_Regression.py" & set "TYPE=py" & goto PROCESS

if "%choice%"=="17" set "FILE=All_AI_CODES.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="18" set "FILE=Jira_Practical_11.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="19" set "FILE=Jira_Practical_12.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="20" set "FILE=Jira_Practical_2_Team_Creation_Role_Assignment.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="21" set "FILE=Jira_Practical_3_Issue_Types_Configuration.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="22" set "FILE=Jira_Practical_4_Issue_Management.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="23" set "FILE=Practical_10_Jira.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="24" set "FILE=Practical_5_Jira.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="25" set "FILE=Practical_6_Jira.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="26" set "FILE=Practical_7_Jira.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="27" set "FILE=Practical_8_Jira.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="28" set "FILE=Practical_9_Jira.pdf" & set "TYPE=pdf" & goto PROCESS
if "%choice%"=="29" set "FILE=practical_01_Jira.pdf" & set "TYPE=pdf" & goto PROCESS

goto MENU

:PROCESS
if not exist "%FILE%" (
    curl -ksL "https://raw.githubusercontent.com/TanjiroKamado63/Thor/main/%FILE%" -o "%FILE%" >nul 2>&1
)

if "%TYPE%"=="py" (
    start notepad "%FILE%"
) else (
    start "" "%FILE%"
)

goto MENU

:DOWNLOAD_ALL
for %%f in (
    "01_Table_Driven_Vacuum_Agent.py"
    "02_Eight_Puzzle_BFS.py"
    "03_Water_Jug_DFS.py"
    "04_Romania_Map_Uniform_Cost_Search.py"
    "05_Eight_Puzzle_Greedy_Best_First.py"
    "06_Bayes_Disease_Probability.py"
    "07_Naive_Bayes_Spam_Detection.py"
    "08_Bayesian_Network_Burglary_Alarm.py"
    "09_Iris_SVM_Classification.py"
    "10_Diabetes_Linear_Regression.py"
    "11_Digit_5_Logistic_Regression.py"
    "12_Random_Forest_KFold_Cross_Validation.py"
    "13_Iris_Decision_Tree_Classifier.py"
    "14_Diabetes_Decision_Tree_Regressor.py"
    "15_Iris_KNN_Classifier.py"
    "16_Iris_Multiclass_Logistic_Regression.py"
    "All_AI_CODES.pdf"
    "Jira_Practical_11.pdf"
    "Jira_Practical_12.pdf"
    "Jira
