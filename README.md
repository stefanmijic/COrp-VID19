![](https://raw.githubusercontent.com/stefanmijic/COrp-VID19/master/logo.png?token=AFQO3L3G2H76Q34IVKBKBHK6RBCB4)

# COrp-VID19
Corporate COVID-19 Response Visualization


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
