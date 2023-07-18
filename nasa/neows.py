#!/usr/bin/python3
import requests
import os
from dotenv import load_dotenv

## Load the environment variables from .env file
load_dotenv()

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

def returncreds():
    ## Grab the NASA API key from environment variables
    nasacreds = "api_key=" + os.getenv("NASA_API_KEY")
    return nasacreds

def main():
    ## Grab credentials
    nasacreds = returncreds()

    ## Ask the user for start date and end date (optional)
    startdate = input("Enter the start date (YYYY-MM-DD): ")
    enddate = input("Enter the end date (optional - leave empty for no end date): ")

    ## Construct the date parameters
    date_params = f"start_date={startdate}"
    if enddate:
        date_params += f"&end_date={enddate}"

    # Make a request with the request library
    neowrequest = requests.get(NEOURL + date_params + "&" + nasacreds)

    # Strip off JSON attachment from our response
    neodata = neowrequest.json()

    ## Display NASA's NEOW data
    print(neodata)

if __name__ == "__main__":
    main()

