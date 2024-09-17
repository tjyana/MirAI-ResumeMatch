import requests
from bs4 import BeautifulSoup
import streamlit as st


def get_url(url):
    # Fetch the main page
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup


def scrape_description(soup):

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


def scrape_title(soup):

    # Find the h1 element with the class sg-corporate-name
    jd_title = soup.find('h1', class_='sg-corporate-name').text

    return jd_title


# Orchestrating the scraping functions
def scrape_jd(url):

    # Error handling for invalid URLs
    if 'hrmos.co/pages/moneyforward/jobs/' not in url:
        st.error('''\n
                Invalid URL. Please make sure the URL is for one JD from the Money Forward careers page: \n
                Japanese page: https://recruit.moneyforward.com/#job \n
                English page: https://recruit.moneyforward.com/en/ \n
                \n
                The correct format of the URL is: \n
                https://moneyforward.com/careers/jobs/{job_id}\n
                where {job_id} is a placeholder for a series of numbers.\n
                ------------------------------ \n
                無効なURLです。マネーフォワード採用ページの求人URLを入力してください。\n
                日本語採用ページ: https://recruit.moneyforward.com/#job \n
                英語採用ページ: https://recruit.moneyforward.com/en/ \n
                \n
                こちらのURLの正しい形式は以下の通りです: \n
                https://moneyforward.com/careers/jobs/{job-id}
                {job-id} は一連の数字を表すプレースホルダーです \n
                 ''')

    # Else, scrape the job description
    else:
        soup = get_url(url)
        jd_title = scrape_title(soup)
        jd_text = scrape_description(soup)

        return jd_title, jd_text
