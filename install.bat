echo off
echo

pause
echo off
echo
:start
cls
set python_ver=36
python get-pip.py
set python_ver=311
python ./get-pip.py
pip install --upgrade pip
pause
cd \
cd \python%python_ver%\Scripts\
pip install xlrd
pip install XlsxWriter
pause.
pip install BeautifulSoup4 == 4.11.1
pip install requests
pip install numpy
pip install time
pip install datetime
pip install pandas
pip install termcolor
pip install BeautifulSoup4
pip install BS4
pip install -r requirements.txt

pause