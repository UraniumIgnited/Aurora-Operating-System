# Having problems with the Operating System or its BIOS
### Find your solution here.


#
### Files
##### Unable to Locate the BIOS
If your system is unable to load the BIOS their is still hope for you, goto ``` System12 ``` and then ``` Repair Tools ```, you will find a file named ``` manual_repair_tool.py ```.
 Use the Command ``` python manual_repair_tool.py ``` and select the option to repair the BIOS, then the system will add the BIOS to its required locations

#
### Folders
##### Unable to Locate System12
If the system is unable to load files from System12 as it is not in the correct location or is missing, the program will load a file named ``` advanced_repair.py ```.
 From its selection of imports (```import advanced_repair.py ```), it should just add all the files it need. If the system fails to add the files you can manual add them using the ``` manual_repair_tool.py ```.
 And if that still dosent work you will have to manualy download the required folders and maybe even files if it dosent create them.
