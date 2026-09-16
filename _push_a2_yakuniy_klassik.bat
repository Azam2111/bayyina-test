@echo off
chcp 65001 >nul
cd /d "%~dp0"

echo ===============================================
echo   Bayyina-test: A2 YAKUNIY IMTIHON (klassik guruh)
echo   a2_yakuniy_klassik.html + 3 ta istima audio
echo   Repo: Azam2111/bayyina-test
echo ===============================================
echo Papka: %cd%
echo.

git --version
echo.

if exist ".git\index.lock" del /f /q ".git\index.lock"
if exist ".git\HEAD.lock" del /f /q ".git\HEAD.lock"
if exist ".git\objects\maintenance.lock" del /f /q ".git\objects\maintenance.lock"

echo === MUHIM: faqat quyidagi fayllar qoshiladi ===
echo   a2_yakuniy_klassik.html
echo   audio/a2_3_istima.mp3
echo   audio/a2_4_istima.mp3
echo   audio/a2_11_istima.mp3
echo   gen_a2_yakuniy_klassik.py, content_qiroat_kitoba.py, _a2_klassik_template.html
echo Boshqa saqlanmagan ozgarishlar BU skript bilan commit qilinmaydi.
echo.

git status -s a2_yakuniy_klassik.html audio/a2_3_istima.mp3 audio/a2_4_istima.mp3 audio/a2_11_istima.mp3
echo.

git add a2_yakuniy_klassik.html
git add audio/a2_3_istima.mp3
git add audio/a2_4_istima.mp3
git add audio/a2_11_istima.mp3
git add gen_a2_yakuniy_klassik.py
git add content_qiroat_kitoba.py
git add _a2_klassik_template.html

git commit -m "feat a2: klassik guruh uchun mustaqil yakuniy imtihon (252 savol)" -m "5 bolim: qovaid 100, mufradot 100, istima 30 (3 audio), qiroat 12 (2 yangi matn), kitoba 10 (avtomatik tekshiriladi). Bolim taymerlari, progress saqlash, natija kartasi. Botga bogliq emas - havola orqali ishlaydi."

echo.
echo === PUSH boshlanmoqda ===
git push origin main
echo.

echo Havola (push muvaffaqiyatli bolsa 1-2 daqiqada tayyor):
echo https://azam2111.github.io/bayyina-test/a2_yakuniy_klassik.html
echo.
echo Bu oyna OZI YOPILMAYDI - oqib bolgach istalgan tugmani bosing.
pause
