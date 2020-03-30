![](https://raw.githubusercontent.com/stefanmijic/COrp-VID19/master/logo.png?token=AFQO3L3G2H76Q34IVKBKBHK6RBCB4)

# COrp-VID19
Corporate COVID-19 Response Visualization

## Description
We created a database layout that allows to track when different companies and universities adopted different measures against the spread of the pandemic. We filled in some of the data manually, as our webscraper did not reach a mature state. We built a web frontend to display and cross-reference the data. This can be extended to compare measures of different companies and analyze how the actions of companies in a region impacted the spread of the virus. For now we focused only on data from Germany, Switzerland and Austria, and as of yet we have a very unfinished dataset.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

If you are using the docker container you onny require docker and docker-compose. Install these with your favourite package manager. 
If you want to run this in a development enviroment you also require python3 and the libraries detailed in the requirements.txt file

### Installing

If you want to run this localy you can use the start_local.sh script to strat it.


## Immediate Steps
- Create list of companies that publically announced their COVID19 response and find web sources where those are listed
- Decide on tag categories (e.g. [voluntary homeoffice], [mandatory homeoffice], [closed operations], etc.)


## Following Steps
- Set up DB for company entries --> decide on layout: simple e.g. (name - #employees - [Response Tags/(or just response text)]) vs complex (name - [list of countries with offices]- #employees per country - [Response Tags] - Cases of Covid19 in city of office)
- Set up Flask/Django as online platform --> look into different data visualization tools
- Set up daily scrapers that update response sheet with new measures that get published under that url


## Optional
- Use of automatic summarization for response texts (e.g. GPT-2)
- Point system based on tags --> allows for regional/international rankings


## Scope
- Focus only on DACH for now
- Focus only on major companies & universities for now

## Dependencies
- Läuft mit Python 3 und Django

https://getbootstrap.com/
http://lesscss.org/
https://datatables.net/
https://frappe.io/charts

https://covid.ourworldindata.org/data/ecdc/total_cases.csv

## Authors

* **LimeThaw** - *Setting up Django and JavaScript God* - [limethaw](https://github.com/LimeThaw)
* **stefanmijic** - *Data Analyis and NLP magic* - [stefanmijic](https://github.com/stefanmijic)
* **J-kirsch** - *Docker-compose and hunting for data3 - [j-kirsch](https://github.com/j-kirsch)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
