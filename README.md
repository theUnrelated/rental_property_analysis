# Analysis of Rental Property
Data was first obtained via scrapping with [selenium](https://selenium-python.readthedocs.io/) and saved to excel file (looking back, I probably should have used csv instead..)
Data was then cleaned, processed. 
They are then further processed with [Google Geopy](https://geopy.readthedocs.io/en/stable/) for finding distances, coordinates etc. 

I did this in python notebooks but I guess they are still kinda buggy in github. Thus I will be saving all my files in .py here. 

### Objective
Primary objective is to analyze if there are any relations between distance to ammenities, racial/ethnic preferences and prices of rental listings. 

## Scraping
Scraping was done with a rather manual way of paginating. The items of interest were then picked out with a mix of some regex and slicing and semi-hard-coded way (horrible, I know).

## Extra variables
Coordinates were calculated with geopy and distances with googlemaps using their API. 

There is a limit to the API calls when using, so do take note! I remember I was using free credits for being new user, thus did not pay anything. 

## Analysis
Uploaded in ipynb files and they are probably kind of messy. Will probably tidy them up when I have the time in the future. 

## DISCLAIMER
This is something I did some time back and there are probably better ways to go about doing it, best practices etc etc now that Im looking at it again. Nevertheless, I'm probably going to leave much of it as it is unless there is a need for me to use this again. 
