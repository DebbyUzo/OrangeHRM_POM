from selenium.webdriver.common.by import By


class LoginLocators:
    USERNAME = (By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[1]/div/div[2]/input")
    PASSWORD = (By.XPATH, "/html/body/div/div[1]/div/div[1]/div/div[2]/div[2]/form/div[2]/div/div[2]/input")
    LOGIN = (By.CSS_SELECTOR, "#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div.oxd-form-actions.orangehrm-login-action > button")

class AdminPageLocators:
    ADMIN_JOB = (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")

class AdminUserManagementPageLocators:
    USER_MANAGEMENT = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.oxd-topbar-body-nav-tab.--parent.--visited > span")
    USERS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[1]/ul/li")

    JOB = (By.XPATH, "//*[@id=]/div[1]/div[1]/header/div[2]/nav/ul/li[2]")
    JOB_TITLE = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > ul > li:nth-child(1)")
    PAY_GRADES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[2]")
    EMPLOYMENT_STATUS = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > ul > li:nth-child(3)")
    JOB_CATEGORIES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[2]/ul/li[4]")
    WORK_SHIFTS = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent.--visited > ul > li:nth-child(5)")

    ORGANISATION = (By.CSS_SELECTOR, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/span")
    GENERAL_INFORMATION = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[1]")
    LOCATIONS = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > ul > li:nth-child(2)")
    STRUCTURES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[3]/ul/li[3]")

    QUALIFICATIONS = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li:nth-child(4) > span")
    SKILLS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[1]")
    EDUCATION = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > ul > li:nth-child(2)")
    LICENSES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[3]")
    LANGUAGES = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab.--parent > ul > li:nth-child(4)")
    MEMBERSHIPS = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[4]/ul/li[5]")

    NATIONALITIES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/a")
    CORPORATE_BRANDING = (By.CSS_SELECTOR, "a.oxd-topbar-body-nav-tab-item")

    CONFIGURATION = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[7]/span")
    EMAIL_CONFIGURATION = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/div[3]/ul/li[1]")
    EMAIL_SUBSCRIPTIONS = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab > ul > div:nth-child(3) > ul > li:nth-child(2)")
    LOCALIZATION = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/div[3]/ul/li[3]")
    LANGUAGE_PACKAGES = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab > ul > div:nth-child(3) > ul > li:nth-child(4)")
    MODULES = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/div[3]/ul/li[5]")
    SOCIAL_MEDIA_AUTHENTICATION = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab > ul > div:nth-child(3) > ul > li:nth-child(6)")
    REGISTER_OAUTH_CLIENT = (By.XPATH, "/html/body/div/div[1]/div[1]/header/div[2]/nav/ul/li[5]/ul/div[3]/ul/li[7]")
    LDAP_CONFIGURATION = (By.CSS_SELECTOR, "#app > div.oxd-layout.orangehrm-upgrade-layout > div.oxd-layout-navigation > header > div.oxd-topbar-body > nav > ul > li.--active.oxd-topbar-body-nav-tab > ul > div:nth-child(3) > ul > li:nth-child(8)")
