import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from pathlib import Path

# Download entire webpage including all javascript, html, css of webpage. Replicates ctrl+s when on a webpage.

# Specify the debugging address for the already opened Chrome browser
debugger_address = "localhost:8989"

folder_url_map = {
    "Diagnosis & Disorders": "diagnosis-developmental-disorders",
    "Patient Management": "patient-management",
    "Fields of Dentistry": "fields-of-dentistry",
    "Anatomy": "anatomy",
    "Research": "research",
    "case-based-scenarios": "case-based-scenarios",
    "mock-inbde": "mock-inbde",
}

# Set up ChromeOptions and connect to the existing browser
c_options = Options()
c_options.add_experimental_option("debuggerAddress", "localhost:8989")

# Initialize the WebDriver with the existing Chrome instance
driver = webdriver.Chrome(options=c_options)
wait = WebDriverWait(driver, 10)
# Now, you can interact with the already opened Chrome browser

section = "case-based-scenarios"
sub_section_list = [
    # ("patient-management-ii",121),
    # ("emergency-care",38),
    # ("prevention-of-oral-diseases",68),
    # ("anxiety-and-pain-control",17),
    #            ("infection-control",20),
    #    ("practice-management",50)
    # ("oral-pathology", 44),
    # ("oral-pathology-ii", 99),
    # ("oral-radiology", 77),
    # ("oral-medicine", 148),
    # ("operative-dentistry", 31),
    # ("operative-dentistry-ii", 49),
    # ("endodontics", 69),
    # ("oral-surgery", 36),
    # ("periodontics", 38),
    # ("orthodontics", 32),
    # ("prosthodontics", 88),
    # ("pediatric-dentistry", 74),
    # ("head-neck-dental-anatomy",52),
    # ("dental-anatomy-occlusion",34),
    ("case-1", 5),
    ("case-2", 5),
    ("case-3", 5),
    ("case-4", 5),
    ("case-5", 5),
    ("case-6", 5),
    ("case-7", 5),
    ("case-8", 5),
    ("case-9", 5),
    ("case-10", 5),
    ("case-11", 5),
    ("case-12", 5),
    ("case-13", 5),
    ("case-14", 5),
    ("case-15", 5),
    ("case-16", 5),
    ("case-17", 5),
    ("case-18", 5),
    ("case-19", 5),
    ("case-20", 5),
    ("case-21", 5),
    ("case-22", 5),
    ("case-23", 5),
    ("case-24", 5),
    # ("day-2-test-2",70),
    # ("day-2-test-1",70),
    # ("day-1-test-4",60),
    # ("day-1-test-3",100),
    # ("day-1-test-2",100),
    # ("day-1-test-1", 100),
]
for s in sub_section_list:
    sub_section = s[0]
    inbde_url = f"https://inbdebooster.com/classroom/{folder_url_map.get(section)}/{sub_section}/"
    # inbde_url = (
    #     f"https://inbdebooster.com/classroom/past-test-results/results/?sid=79902"
    # )

    # Process the section
    driver.get(url=inbde_url)
    time.sleep(2)
    get_url = driver.current_url
    wait.until(method=EC.url_to_be(inbde_url))
    time.sleep(2)
    elements = driver.find_elements(By.CSS_SELECTOR, ".result-filter li a")
    question_count = len(
        [element for element in elements if "Question" in element.text]
    )
    print(
        f"total no. of question detected is {question_count} out of {s[1]} for section {section} and subsection {sub_section}"
    )
    for i in range(question_count):
        print(
            f"processing question {i} by clicking elements[{i}].text : text value is {elements[i].text}"
        )
        elements[i].click()
        time.sleep(1)
        check_element = driver.find_element(By.CSS_SELECTOR, ".check-action.button")
        # Assuming driver is the webdriver instance
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if check_element.is_displayed():
            check_element.click()
            # time.sleep(5)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        page_source = driver.page_source
        ques_file_path = f"/Volumes/DoogleSSD/projects/learn-python/selenium_automation/inbde_download/{section}/{sub_section}/{i+1}.html"
        Path(ques_file_path).parent.mkdir(parents=True, exist_ok=True)
        Path(ques_file_path).write_text(page_source, encoding="utf-8")


# Find all anchor tags within the menu container using BeautifulSoup
# soup = BeautifulSoup(element.get_attribute("outerHTML"), "lxml")
# menu_links = soup.find_all("a")

# Remember to close the WebDriver when you're done
driver.quit()
