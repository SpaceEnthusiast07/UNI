:: Don't show the commands in the terminal, only their output
@echo off

:: Clear the terminal screen
cls

:: Output build title
echo ======================================
echo Build Started for 'binarytree' project
echo ======================================

:: Compile the java files into the bin/ directory
echo Compiling everything in src/ and test/
javac -d bin -cp bin src/tree/*.java test/*.java
if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed at this step. Stopping.
    pause
    exit /b %errorlevel%
)

:: Package everything up in the bin/ directory into a .jar archive
echo Creating .jar archive
jar cvfe build/BinaryTreeProject.jar TreeApp -C bin .

:: Output completion message
echo Completed build process