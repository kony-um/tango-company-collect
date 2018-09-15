from selenium import webdriver

def print_company_info(driver):
    # 企業情報を取得してプリントする
    company_name_list = driver.find_elements_by_css_selector('#content > div > section > div > div.col-sm-8.col-xs-8 > h3')
    url_list = driver.find_elements_by_css_selector('#content > div > section > div > div.col-sm-8.col-xs-8 > div > a')


    for company in company_name_list:
        name = company.text
        num = company_name_list.index(company)
        url = ''
        index = 5+num*2

        add = 0
        if (index >= 173): index += 16
        elif (index >= 161): index += 14
        elif (index >= 127): index += 12
        elif (index >= 117): index += 10
        elif (index >= 99): index += 8
        elif (index >= 83): index += 6
        elif (index >= 61): index += 4
        elif (index >=  23): index += 2

        try :
            url = driver.find_element_by_css_selector('#content > div > section > div:nth-child(' + str(index) + ') > div.col-sm-8.col-xs-8 > div:nth-child(7) > a').get_attribute('href')
#content > div > section > div:nth-child(175) > div.col-sm-8.col-xs-8 > div:nth-child(7) > a
        except:
            url = ''

        print(name + ',' + url)

def main():
    ## Seleniumでnoteからデータを取得する処理
    driver = webdriver.Chrome()

    # 一覧画面に遷移
    driver.get("http://yumetajima-fair.jp/company/")

    print_company_info(driver)

    driver.quit()

if __name__  == '__main__':
    main()
