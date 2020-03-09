# OINP-Updates-notification

send yourself a text message when OINP website updated

OINP website: https://www.ontario.ca/page/2020-ontario-immigrant-nominee-program-updates/

Logic: Fetch the current JSON content of the website and stored it as str. Compare every new fetch result to original str. SMS if different. 
