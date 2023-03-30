pyinstaller --name mathex -i src\resources\favicon.ico -D --noconsole src\app.py
cd dist\mathex\
mkdir resources
cd ..\..\
copy src\resources\favicon.ico dist\mathex\resources\