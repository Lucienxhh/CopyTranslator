# CopyTranslator
A GUI is provided to show the original text and translated text. And when you copy a text, the GUI will display the text and its translated one. what's more, the GUI is on the top state. So there is no worry that any window will cover it, unless you minimize it. Additionally, you can resize it as you need.

提供了一个GUI来显示原始文本和翻译文本。复制文本时，GUI将显示文本及其翻译文本。此外，GUI处于顶层状态。所以不必担心任何窗口会覆盖它，除非你将其最小化。此外，您可以根据需要调整其大小。

# Enviroment
## Winodows
1. If you don't have Chrome, download and install it.
2. Enter in the URL bar chrome://version/ and view browser version
3. Go https://npm.taobao.org/mirrors/chromedriver/ , find the corresponding version of windows driver and download it
4. Put the extracted chrome driver into the folder where copytranslator is located.
5. Run CopyTranslator.exe
--------------------------
1. 如果你没有Chrome，下载并安装它
2. 在URL栏中输入 chrome://version/ 并查看浏览器版本
3. 去https://npm.taobao.org/mirrors/chromedriver/ ,找到相应版本的windows驱动程序并下载它
4. 将提取的chrome驱动程序放入copytranslator所在的文件夹
5. 运行CopyTranslator.exe

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
--------------------------
1. 如果你没有Chrome，下载并安装它
2. 在URL栏中输入chrome://version/ 并查看浏览器版本
3. 去https://npm.taobao.org/mirrors/chromedriver/ ，找到相应版本的Linux驱动程序并下载
4. 将提取的chromedriver放入任何文件夹中，然后打开该文件夹中的终端
5. 输入以下命令：
```
    sudo mv chromedriver /usr/bin   # move chromedriver to /usr/bin
    cd /usr/bin                     # go to /usr/bin
    sudo chmod +x chromedriver      # give permission to the driver
    sudo apt-get install xsel xclip # install required plug-ins
```
6. 运行CopyTranslator

## MacOS
To be continued
待续
