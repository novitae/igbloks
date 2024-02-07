# IGBloks
### 🧱 A library to work with instagram `bloks` technology
See [the KNOWLEDGES](./KNOWLEDGES/) for further explaination on what this is about.
### ⚠️ This library is currently being develloped, <u>it is unstable</u>.
## Installation 🔌
```
# Easy install
pip install git+https://github.com/novitae/igbloks.git

# If you want to also access to the tools
git clone https://github.com/novitae/igbloks
cd igbloks
pip install .
```
## Usage
### Mapping 🗺️
Due to the way instagram bloks are working, with **keys changing based on the bkid**, the mapping tool is here to **identify objects with the different keys the might be identified by**. It works using a set of responses to same requests, but with different bkids. It produces a file that the library will take as a reference to know which object has which values, their types, their required values, their names, keys, etc ... .

**Steps:**
1. Create a directory (you will need it since the program iterates through each sub directories of it). It will be our list of responses set directory.
2. Capture some blok requests with an http proxy. *The example is request is the one you get from the "About this account" page on iOS*.
  ![](src/Capture%20d’écran%202023-12-21%20à%2014.46.10.png)
  *Here I have one from my iOS device, we can see the fields name being very small.*
3. Save the json response body in a new directory inside the created directory, name it whatever you want. *For the example, I will name mine with the appid of the blok request*. Name the request with the bkid used to send it. For me, it is `ae6e4040481b1c3ecd691a99c8cd3849d4a4b4b05259fb9ae75c92c4b6a722ca`, as you can see on the upper screenshot.
  ![](src/Capture%20d’écran%202023-12-21%20à%2014.31.04.png)
4. Now, replay the request with a different bkid. You can change only the one in the body, the one in the headers (if there is) is taken only if the one in the body is missing. To find new bkid, you can check the requests of the web instagram, or from another device / version. Here I will use `456a06cb008a2f6d72f04e94d26242d4607e80d5cf8d9a5aa34ec109117071c6`, which is a web one. Sometimes, certain requests with different bkid are returning response 404, with the message "Payload returned is null. A server error field_exception occured. Check server logs for details.". It means that the appid doesn't support the given bkid, we can't do anything about it ... .
  ![](src/Capture%20d’écran%202023-12-21%20à%2014.45.32.png)
  With the different bkid, you can see the names of fields are completely different from the first response, but the composition stay the same, with the same values.
5. Save this new response body to the same subdirectory you made, and name the json file with the bkid used.
  ![](src/Capture%20d’écran%202023-12-21%20à%2015.00.42.png)
- *You can repeat the steps `4` and `5` as many times you want with different bkid.*
6. 