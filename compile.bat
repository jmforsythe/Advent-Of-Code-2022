@echo off

for %%f in (*.cpp) do (
    g++ -std=c++20 %%~nf.cpp -o %%~nf.exe
)