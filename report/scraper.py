from bs4 import BeautifulSoup

import requests



url = requests.get(url='http://icu-dar-report.herokuapp.com/')

soup = BeautifulSoup(url.content, 'lxml')


##this = " ".join(this.split())  --- will 'split' the string into each word on a list, then will 'join' them by a space into a single string##


def run_daily_report_header_scraper():
    daily_report_header = []
    daily_report_header_string = ''
    report_header = soup.find_all('h3')
    for line in report_header:
        line = line.text
        line = " ".join(line.split())
        daily_report_header.append(line)
        daily_report_header_string = " \n".join(daily_report_header)
    return daily_report_header_string



def run_daily_report_scraper():
    daily_report = []
    daily_report_string = ''
    hourly_report = soup.find_all('h4')
    for line in hourly_report:
        line = line.text
        line = " ".join(line.split())
        daily_report.append(line)
        daily_report_string = "  \n\n".join(daily_report)
    return daily_report_string


    







