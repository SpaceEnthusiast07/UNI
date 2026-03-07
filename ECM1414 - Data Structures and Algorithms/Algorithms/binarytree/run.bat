:: Don't show the commands in the terminal, only their output
@echo off

:: Clear the terminal screen
cls

:: Inform the user which file is being executed
echo ======================
echo Executing 'TreeApp'...
echo ======================

:: Insert a new line
echo:

:: Run the .jar archive
java -jar build/BinaryTreeProject.jar %*

:: Insert a new line
echo:

:: Don't finish until the user presses enter
pause