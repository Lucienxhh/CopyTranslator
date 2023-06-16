# CopyTranslator
A GUI is provided to show the original text and translated text. And when you copy a text, the GUI will display the text and its translated one. what's more, the GUI is on the top state. So there is no worry that any window will cover it, unless you minimize it. Additionally, you can resize it as you need.

# Enviroment
## Chrome

If you don't have Chrome, go to [Chrome's official website](https://www.google.cn/chrome/index.html). 

If you prefer older ones, you can find them [here](https://www.slimjet.com/chrome/google-chrome-old-version.php#).

## Chrome Driver

1. Enter in the URL bar [chrome://version/](url) and view browser version.
2. Go [website1](https://npm.taobao.org/mirrors/chromedriver/) or [website2](https://npm.taobao.org/mirrors/chromedriver/), find the corresponding version and download it.

### Windows
3. Modify Lines 7-9 of translator.py, so as to let computer know where the chrome and its driver are.
4. Run main.py
### Ubuntu
3. Put the extracted chromedriver into any folder and open the terminal in that folder.
4. Enter the following commands:
    ```
    sudo mv chromedriver /usr/bin   # move chromedriver to /usr/bin
    cd /usr/bin                     # go to /usr/bin
    sudo chmod +x chromedriver      # give permission to the driver
    sudo apt-get install xsel xclip # install required plug-ins
    ```
5. Modify Lines 7-9 of translator.py, so as to let computer know where the chrome and its driver are.
6. Run main.py

### MacOS
To be continued

# One More Thing

You can pack it up using pyinstaller.

## For Windows
1. Set Lines 7-9 of transtator.py as:
    ```
    BASE_DIR = os.path.dirname(os.path.abspath(__file__)) 
    chrome_path = BASE_DIR + '\Application\chrome.exe'         
    driver_path = BASE_DIR + '\Application\chromedriver.exe'
    ```
2. Go to C:\Program Files\Google\Chrome or C:\Program Files (x86)\Google\Chrome, copy the folder **Application** to the folder where **main.py** locates.
3. Copy chromedriver.exe to **Application**
4. Open CMD in the folder where **main.py** locates, type:
    ```
    pyinstaller -F -w -i ui.ico main.py --add-data Application;Application
    ```
