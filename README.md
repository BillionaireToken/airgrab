# airgrab

for converting grabbers.txt to unix file format use:

awk '{ sub("\r$", ""); print }' grabbers.txt > unixfile.txt
