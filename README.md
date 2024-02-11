# try-xserver
Try out XServer protocol

## Display using the host XQuartz Server (MacOS Only):
**Requirements:**
* [XQuartz](https://www.xquartz.org/)
* [Docker](http://docker.io) 

1. Start XQuartz, go to `Preferences` -> `Security`, and check the box `Allow connections from network clients`
2. Restart XQuartz
3. In the terminal, run 
```
xhost +
```
