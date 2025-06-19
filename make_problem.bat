@echo off
chcp 65001 >nul

set /p platform=플랫폼 이름 입력 (예: boj, leetcode, prog): 
set /p category=분류/난이도 입력 (예: dp, easy, level1): 
set /p problem_name=문제 이름 입력 (예: 1149, 1_two_sum): 

set base_dir=%~dp0
set folder=%base_dir%%platform%\%category%
set target_file=%folder%\%problem_name%.cpp
set readme_file=%folder%\%problem_name%_README.md

if not exist %folder% (
    mkdir %folder%
)

copy /Y %base_dir%templates\template.cpp %target_file%
echo :: 문제 링크, 설명 등 추가 >> %readme_file%

echo.
echo ✅ 생성 완료:
echo - %target_file%
echo - %readme_file%
pause
