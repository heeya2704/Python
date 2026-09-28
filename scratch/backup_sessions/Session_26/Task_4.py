# Create a Python program that fetches the latest COVID-19 case numbers for India from a public 
# COVID API and displays total cases, recovered, and deaths in a table format.

import requests

def fetch_covid_data():
    url = "https://disease.sh/v3/covid-19/countries/India"
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            country = data.get("country")
            total_cases = data.get("cases", 0)
            recovered = data.get("recovered", 0)
            deaths = data.get("deaths", 0)
            active = data.get("active", 0)
            
            print(f"+--------------------------------------------------+")
            print(f"| COVID-19 Statistics for {country:<24} |")
            print(f"+--------------------------------------------------+")
            print(f"| Total Cases : {total_cases:<34,d} |")
            print(f"| Active      : {active:<34,d} |")
            print(f"| Recovered   : {recovered:<34,d} |")
            print(f"| Deaths      : {deaths:<34,d} |")
            print(f"+--------------------------------------------------+")
        else:
            print(f"Failed to fetch COVID data. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error occurred while fetching COVID data: {e}")

if __name__ == "__main__":
    fetch_covid_data()
