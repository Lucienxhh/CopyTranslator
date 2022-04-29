# CopyTranslator
A GUI is provided to show the original text and translated text. And when you copy a text, the GUI will display the text and its translated one. what's more, the GUI is on the top state. So there is no worry that any window will cover it, unless you minimize it. Additionally, you can resize it as you need.

# Enviroment
## Winodows
1. If you don't have Chrome, download and install it.
2. Enter in the URL bar chrome://version/ and view browser version
3. Go https://npm.taobao.org/mirrors/chromedriver/ , find the corresponding version of windows driver and download it
4. Put the extracted chrome driver into the folder where copytranslator is located.
5. Run CopyTranslator.exe

## Ubuntu
1. If you don't have Chrome, download and install it.
2. Enter in the URL bar chrome://version/ and view browser version
3. Go https://npm.taobao.org/mirrors/chromedriver/ , find the corresponding version of Linux driver and download it.
4. Put the extracted chromedriver into any folder and open the terminal in that folder.
5. Enter the following command:
```
    sudo mv chromedriver /usr/bin   # move chromedriver to /usr/bin
    cd /usr/bin                     # go to /usr/bin
    sudo chmod +x chromedriver      # give permission to the driver
    sudo apt-get install xsel xclip # install required plug-ins
```
6. Run CopyTranslator

## MacOS
To be continued
