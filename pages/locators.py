
class ElementLocators():

    print("Element Locators")

    # navigation bar
    _all_course, by_link = "All Courses", "link"
    _my_course, by_link = "My Course", "link"
    _to_practice, by_link = "Practice", "link"
    _to_setting, by_class = "gravatar", "class"
    _home_logo, by_xpath = "//div[@id='navbar']//img", "xpath"

    # Login element locator
    (login_link, by_link) = ("Login", "link")
    (email_field, by_id) = ("user_email", "id")
    _pass_field, by_id = "user_password", "id"
    _login_btn, by_name = "commit", "name"
    _valid_login, by_xpath = "//*[@id='navbar']//span[text()='Test']", "xpath"
    _invalid_login, by_xpath = "//div[contains(text(),'Invalid email')]", "xpath"
    _log_out, by_link = "Log Out", "link"

    # courses page element locator
    _search_box, by_name = "query", "name"
    _search_btn, by_xpath = "//*[@title='Search']", "xpath"
    _course_text, by_xpath = "//div[contains(text(),'JavaScript for beginners')]", "xpath"
    _all_courses, by_xpath = "//div[@class='course-listing-title", "xpath"
    _enroll_btn, by_name = "commit", "name"

    # credit card info
    # _cc_num, by_id = "//div[@id='credit_card_number']", "by_id"
    _cc_num, by_xpath = "//div[starts-with(@class,'CardNumber')]//input[@name='cardnumber']", "xpath"
    _cc_exp, by_name = "exp-date", "name"
    _cc_cvv, by_name = "cvc", "name"

    _country_cd, by_id = "//select[@id='country_code_credit_card-cc']", "id"
    _postal_cd, by_name = "postal", "name"
    _save_card, by_id = "save-payment-details", "id"
    _term_agree, by_id = "agreed_to_terms_checkbox", "id"

    _submit_enroll, by_id = "confirm-purchase", "id"
    _enroll_error_msg, by_xpath= "//div[@class='payment-error-box']//span", "xpath"

