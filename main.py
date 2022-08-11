
from selenium import webdriver
from time import sleep

i = 1
while (i > 0):

    i += 1


    case = input("Enter link to case in SF:")
    driver = webdriver.Chrome()
    driver.maximize_window()


    driver.get(case)
    driver.implicitly_wait(20)


    log = driver.find_element("id","i0116")
    log.send_keys("b.libera@mmm.com")
    go = driver.find_element("id","idSIButton9")
    go.click()

    sleep(3)



    get_more_info = driver.find_element('xpath',"/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sales_-automation_-l-e-x_-case___-case___-v-i-e-w/forcegenerated-flexipage_sales_automation_lex_case_case__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-left-sidebar-template-desktop2/div/div[2]/div[2]/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/div/ul/li[5]/a/span[2]")
    driver.execute_script("arguments[0].click();", get_more_info)

    sleep(5)



    insert_template = driver.find_element("xpath", "/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sales_-automation_-l-e-x_-case___-case___-v-i-e-w/forcegenerated-flexipage_sales_automation_lex_case_case__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-left-sidebar-template-desktop2/div/div[2]/div[2]/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/section[2]/div/div[3]/div/div/div[2]/div[1]/div/div[1]/div/ul/li[3]/div/div[1]/div/div/a")
    driver.execute_script("arguments[0].click();", insert_template)

    sleep(5)


    choose_template = driver.find_element("xpath","/html/body/div[8]/div/ul/li[4]/a")
    driver.execute_script("arguments[0].click();", choose_template)


#     sleep(5)
    #
    # add = driver.find_element("xpath", "/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sales_-automation_-l-e-x_-case___-case___-v-i-e-w/forcegenerated-flexipage_sales_automation_lex_case_case__view_js/record_flexipage-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-left-sidebar-template-desktop2/div/div[2]/div[2]/slot/flexipage-component2/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/section[2]/div/div[3]/div/div/div[2]/div[2]/button")
    # driver.execute_script("arguments[0].click();", add)
    #
    # driver.close()