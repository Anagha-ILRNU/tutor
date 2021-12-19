class buyplan:
    buyplan_button_XPATH = "// div[text() = 'Buy Plan']".click()
    buyplan_Skip_button_XPATH = "//button[text()='Skip']".click()
    plan_details_skip_button_XPATH = "// button[text() = 'Skip']".click()

    viewdetails_button_XPATH = "// button[text() = 'View details']".click()
    Closeviewdetails_XPATH = "// div[text() = 'X']".click()

    buy_now_button_XPATH = "//button[text()='Buy now']".click()

    Click_CreditCard_XPATH = "// span[normalize - space() = 'Cards (Credit/Debit)']".click()

    ####### Credit card details ##########################

    Entercardnumber_XPATH = "// input[ @ placeholder = 'Enter Card Number']".send_keys()
    Expiry_XPATH = "//input[@placeholder='MM/YY']".send.keys()
    CVV_XPATH = "//input[@placeholder='Enter CVV']".send.keys()
    Nameoncard_XPATH = "//input[@placeholder='Enter name as on card']".send.keys()
    Proceed_XPATH = "//button[@type='submit']//div".click()

    enterOTP_XPATH = ""
    pay_XPATH = "".click()
