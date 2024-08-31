import requests
from bs4 import BeautifulSoup
import streamlit as st


# URL of the careers page
url = 'https://hrmos.co/pages/moneyforward/jobs/1877612029521268793'


def scrape_description(url):

    if 'hrmos.co/pages/moneyforward/jobs/' not in url:
        st.error('Invalid URL. Please enter a valid MoneyForward job description.')
        return None

    else:
        # Fetch the main page
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all job entries
        job_description_html = str(soup.find_all('div', class_='pg-main-column cf'))  # Adjust class name as needed
        # Find the position of the phrase "職種 / 募集ポジション"
        cutoff_position = job_description_html.find('職種 / 募集ポジション')

        # Truncate the content after the phrase
        if cutoff_position != -1:
            truncated_description = job_description_html[:cutoff_position]
        else:
            truncated_description = job_description_html

        # Convert the truncated HTML back to text
        soup_truncated = BeautifulSoup(truncated_description, 'html.parser')
        jd_text = soup_truncated.get_text(separator='\n').strip()

        return jd_text


def scrape_title(url):


    if 'hrmos.co/pages/moneyforward/jobs/' not in url:
        st.error('Invalid URL. Please enter a valid MoneyForward job description.')
        return None

    else:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find the h1 element with the class sg-corporate-name
        job_title = soup.find('h1', class_='sg-corporate-name').text

        return job_title


# Orchestrating the scraping functions
def scrape_jd(url):

    # Error handling for invalid URLs
    if 'hrmos.co/pages/moneyforward/jobs/' not in url:
        st.error('Invalid URL. Please enter a valid MoneyForward job description.')
        return None

    # Else, scrape the job description
    else:
        jd_text = scrape_description(url)
        job_title = scrape_title(url)
        return jd_text, job_title
