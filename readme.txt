Oringal script  by smuggod https://github.com/TheSmugGod/qb2ox
---Added by dotslash
Adjusted the script to handle mixed itemlist cases such as: "Brackets [""] and [''].  
Added some new regex logic to handle off spaces, oddly tabulated gaps, and shouleClose checks causing it to fail.  
Thanks for the original script TheSmugGod, 
I hope this change helps others with a giant screwed up item list from tons of plugin readme's ;)  

Example Use:
python3 qb2ox.py 

Example Bash quickie to compare: 
&& cat output.lua | grep { | awk '{print $1}' | awk -F"'" '{print $2}' | wc -l && cat input.txt | grep { | awk '{print $1}' | awk -F"'" '{print $1}' | wc -l

https://github.com/dahtslash


--------Original Readme
This tool converts items from QB Inventory format to the Ox Inventory format,
just put the list in the input.txt file and then run the python script, it will send them to the output.lua file.

