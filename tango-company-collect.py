from selenium import webdriver
from time import sleep
import os

def main():
    ## Seleniumでnoteからデータを取得する処理
    driver = webdriver.Chrome()

    # 一覧画面に遷移
    driver.get("http://tantec.jp/companies/src")

    # 企業情報を取得してプリントする
    company_list = driver.find_elements_by_css_selector('body > table > tbody > tr:nth-child(4) > td:nth-child(3) > table > tbody > tr > td:nth-child(1) > a')
    city_list = driver.find_elements_by_css_selector('body > table > tbody > tr:nth-child(4) > td:nth-child(3) > table > tbody > tr > td:nth-child(2)')

    for company in company_list:
        name = company.text
        hp = company.get_attribute('href')
        num = company_list.index(company)
        city = city_list[num].text
        print(name + ',' + hp + ',' + city)
    # プリントが完了したら次のページに進む

    driver.quit()


if __name__  == '__main__':
    main()
