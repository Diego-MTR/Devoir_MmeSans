@echo off
mvn clean package

REM Vérifier que le .war a bien été généré
IF NOT EXIST "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\programmation objet\monapp-jsp\target\monapp.war" (
    echo Le fichier .war n'a pas ete genere. Compilation echouee.
    pause
    exit /b
)

REM Supprimer l'ancien .war et le dossier s'il existe
IF EXIST "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\webapps\monapp.war" (
    del /F /Q "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\webapps\monapp.war"
)
IF EXIST "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\webapps\monapp" (
    rmdir /S /Q "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\webapps\monapp"
)

REM Copier le nouveau .war
copy /Y "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\programmation objet\monapp-jsp\target\monapp.war" "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\webapps\monapp.war"

REM Vérifier si la copie a réussi
IF EXIST "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\webapps\monapp.war" (
    echo Copie du .war reussie.
) ELSE (
    echo ECHEC de la copie du .war !
    pause
    exit /b
)

cd "C:\Users\diego\OneDrive\BACHELOR\Cours\Devoir MmeSans\apache-tomcat-9.0.105\bin"
call shutdown.bat
catalina.bat run
pause