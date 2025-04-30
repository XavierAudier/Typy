REM This script uses pyuic5 to convert all ui files in the current directory into .py files.
REM The code might not work if the folder or files have spaces in their names
call ..\env\Scripts\activate

for %%f in (*.ui) do pyuic6 -x %%f -o %%~nf_ui.py
for %%f in (*.qrc) do pyrcc6 %%f -o %%~nf_rc.py
