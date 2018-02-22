# Appi-Consume
🚀The objetive of this code is create an Api consume in Python, please take this points.

  - This code run just in the python Command line.
  - Only run main.py.
  - Use main.py -h to see the options to run the Api
  - If you call an id and this id doesn't exist, the HTML file not throw anything.

# Steps to use!👌

To consume the Appi go to the folder where main.py is, please run this command

```sh
main.py -h
```

The response is

```sh
usage: main.py [-h] [--rebuild] [--render RENDER]

optional arguments:
  -h, --help       show this help message and exit
  --rebuild        Create the DB and xml
  --render RENDER  Create the HtmlFile use --render [IDCategories]`  
```  
Run the command rebuild to create the DataBase
```sh
main.py --rebuild        
```
Run the command render with the parameter of ID to create the HTML file based in the database INFO.
```sh
main.py --render 20081
```

To extract all the info from the Data Base please put the comand.
```sh
main.py --render 0
```
## Developer Contact
* **category**    Api Consume
* **author**      Juan Diego Alfonso <jalfons.ocampo@gmail.com>
* **copyright**   none
* **source**      https://github.com/halcolo/Appi-Consume
