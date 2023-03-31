pyinstaller --name amthex -i src\resources\favicon.ico -D --noconsole src\app.py
cd dist\amthex\
mkdir resources
cd ..\..\
copy src\resources\favicon.ico dist\amthex\resources\