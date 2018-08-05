from selenium import webdriver

def print_company_info(driver):
    # 企業情報を取得してプリントする
    company_list = driver.find_elements_by_css_selector('body > table > tbody > tr:nth-child(4) > td:nth-child(3) > table > tbody > tr > td:nth-child(1) > a')
    city_list = driver.find_elements_by_css_selector('body > table > tbody > tr:nth-child(4) > td:nth-child(3) > table > tbody > tr > td:nth-child(2)')
    del city_list[0]

    for company in company_list:
        name = company.text
        hp = company.get_attribute('href')
        num = company_list.index(company)
        city = city_list[num].text
        print(name + ',' + hp + ',' + city)

def main():
    ## Seleniumでnoteからデータを取得する処理
    driver = webdriver.Chrome()

    # 一覧画面に遷移
    driver.get("http://tantec.jp/companies/src")
    is_continue = True
    while is_continue:
        try:
            print_company_info(driver)
            # プリントできたら次のページに進む
            next_btn = driver.find_element_by_css_selector('body > table > tbody > tr:nth-child(4) > td:nth-child(3) > div:nth-child(4) > span:nth-child(11) > a')
            next_btn.click()
        except:
            is_continue = False

    driver.quit()

if __name__  == '__main__':
    main()
