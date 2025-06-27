import time

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from Config.configuration import Config
from Locators.locators_page import LoginLocators, AdminPageLocators, AdminUserManagementPageLocators


class Action_Page:
    def __init__(self, driver):
        self.driver = driver

    def navigate_to_login_url(self, url):
        self.driver.get(url)

    def enter_username(self, username):
        enter_username = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.USERNAME))
        enter_username.send_keys(username)
        time.sleep(Config.WAIT_TIME)

    def enter_password(self, password):
        enter_password = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.PASSWORD))
        enter_password.send_keys(password)
        time.sleep(Config.WAIT_TIME)

    def click_login_button(self):
        click_login_button = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(LoginLocators.LOGIN))
        click_login_button.click()
        time.sleep(Config.WAIT_TIME)

class Admin_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_admin_job(self):
        click_AdminJob = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminPageLocators.ADMIN_JOB))
        click_AdminJob.click()
        time.sleep(Config.WAIT_TIME)

class Admin_User_Management_Page:
    def __init__(self, driver):
        self.driver = driver

    def click_user_management(self):
        click_user_management = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.USER_MANAGEMENT))
        click_user_management.click()
        time.sleep(Config.WAIT_TIME)

    def click_users(self):
        click_users = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.USERS))
        click_users.click()
        time.sleep(Config.WAIT_TIME)

    def click_job(self):
        click_job = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.JOB))
        click_job.click()
        time.sleep(Config.WAIT_TIME)

    def click_job_title(self):
        click_job_title = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.JOB_TITLE))
        click_job_title.click()
        time.sleep(Config.WAIT_TIME)

    def click_pay_grades(self):
        click_pay_grades = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.PAY_GRADES))
        click_pay_grades.click()
        time.sleep(Config.WAIT_TIME)

    def click_employment_status(self):
        click_employment_status = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.EMPLOYMENT_STATUS))
        click_employment_status.click()
        time.sleep(Config.WAIT_TIME)

    def click_job_categories(self):
        click_job_categories = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.JOB_CATEGORIES))
        click_job_categories.click()
        time.sleep(Config.WAIT_TIME)

    def click_works_shifts(self):
        click_works_shifts = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.WORK_SHIFTS))
        click_works_shifts.click()
        time.sleep(Config.WAIT_TIME)

    def click_organisation(self):
        click_organisation = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.ORGANISATION))
        click_organisation.click()
        time.sleep(Config.WAIT_TIME)

    def click_general_information(self):
        click_general_information = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.GENERAL_INFORMATION))
        click_general_information.click()
        time.sleep(Config.WAIT_TIME)

    def click_locations(self):
        click_locations = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.LOCATIONS))
        click_locations.click()
        time.sleep(Config.WAIT_TIME)

    def click_structures(self):
        click_structures = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.STRUCTURES))
        click_structures.click()
        time.sleep(Config.WAIT_TIME)

    def click_qualifications(self):
        click_qualifications = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.QUALIFICATIONS))
        click_qualifications.click()
        time.sleep(Config.WAIT_TIME)

    def click_skills(self):
        click_skills = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.SKILLS))
        click_skills.click()
        time.sleep(Config.WAIT_TIME)

    def click_education(self):
        click_education = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.EDUCATION))
        click_education.click()
        time.sleep(Config.WAIT_TIME)

    def click_licenses(self):
        click_licenses = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.LICENSES))
        click_licenses.click()
        time.sleep(Config.WAIT_TIME)

    def click_languages(self):
        click_languages = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.LANGUAGES))
        click_languages.click()
        time.sleep(Config.WAIT_TIME)

    def click_memberships(self):
        click_memberships = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.MEMBERSHIPS))
        click_memberships.click()
        time.sleep(Config.WAIT_TIME)

    def click_nationalities(self):
        click_nationalities = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.NATIONALITIES))
        click_nationalities.click()
        time.sleep(Config.WAIT_TIME)

    def click_corporate_branding(self):
        click_corporate_branding = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.CORPORATE_BRANDING))
        click_corporate_branding.click()
        time.sleep(Config.WAIT_TIME)

    def click_configuration(self):
        click_configuration = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.CONFIGURATION))
        click_configuration.click()
        time.sleep(Config.WAIT_TIME)

    def click_email_configuration(self):
        click_email_configuration = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.EMAIL_CONFIGURATION))
        click_email_configuration.click()
        time.sleep(Config.WAIT_TIME)

    def click_emai_subscriptions(self):
        click_email_subscriptions = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.EMAIL_SUBSCRIPTIONS))
        click_email_subscriptions.click()
        time.sleep(Config.WAIT_TIME)

    def click_localization(self):
        click_localization = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.LOCALIZATION))
        click_localization.click()
        time.sleep(Config.WAIT_TIME)

    def click_language_packages(self):
        click_language_packages = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.LANGUAGE_PACKAGES))
        click_language_packages.click()
        time.sleep(Config.WAIT_TIME)

    def click_modules(self):
        click_modules = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.MODULES))
        click_modules.click()
        time.sleep(Config.WAIT_TIME)

    def click_social_media_authentication(self):
        click_social_media_authentication = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.SOCIAL_MEDIA_AUTHENTICATION))
        click_social_media_authentication.click()
        time.sleep(Config.WAIT_TIME)

    def click_register_oauth_client(self):
        click_register_oauth_client = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.REGISTER_OAUTH_CLIENT))
        click_register_oauth_client.click()
        time.sleep(Config.WAIT_TIME)

    def click_ldap_configuration(self):
        click_ldap_configuration = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(AdminUserManagementPageLocators.LDAP_CONFIGURATION))
        click_ldap_configuration.click()
        time.sleep(Config.WAIT_TIME)