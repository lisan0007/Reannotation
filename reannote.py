import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys


def sleeping3sec ( func ) :
    def wrapper():
        time.sleep(3)
        print("Waiting 3 sec before executing the function")
        result = func()
        time.sleep(3)
        print("Waiting 3 sec after executing the function")
        return result

    return wrapper


def sleeping1sec(func) :
    def wrapper():
        time.sleep(1)
        print("Waiting 1 sec before executing the function")
        result = func()
        time.sleep ( 1 )
        print ( "Waiting 1 sec after executing the function" )
        return result

    return wrapper


# Specify the path to the GeckoDriver executable
gecko_driver_path = "/bin/geckodriver"  # Replace with the actual path

# Set Firefox options and set the executable path
options = Options ( )
options.binary_location = "/usr/bin/firefox"  # Replace with the actual path

# Create a new instance of the Firefox driver
driver = webdriver.Firefox ( executable_path = gecko_driver_path , options = options )
driver.get ( "https://annotation.dotkom.io" )  # Make sure to use the correct URL

# Find the email and password input fields by their IDs
email_input = driver.find_element ( "id" , "Email" )  # Replace with the actual ID
password_input = driver.find_element ( "id" , "Password" )  # Replace with the actual ID

# Enter your email and password
email_input.send_keys ( input("Enter Your Email : ") )
password_input.send_keys ( input("Enter Your password : ") )
timesToIterate = int(input("Enter how many times u wanna repeat the Process : "))

# Submit the form (you may need to adjust this part based on the actual form structure)
password_input.submit ( )
time.sleep ( 3 )

# After completing your actions on the current page, go to the specified URL
new_url = "https://annotation.dotkom.io/ProjectAnnotation/RejectAnnotationList#"
driver.get ( new_url )
time.sleep ( 2 )


# Select FROM Date
def selectTime () :
    from_element = driver.find_element_by_id ( "fromDate" )
    from_element.clear ( )  # Clear existing content
    from_element.send_keys ( "2024-01-01 00:00" )
    from_element.send_keys ( Keys.RETURN )

    # Select TO Date
    to_element = driver.find_element_by_id ( "toDate" )
    to_element.clear ( )  # Clear existing content
    to_element.send_keys ( "2024-02-29 23:55" )
    to_element.send_keys ( Keys.RETURN )


def selectProject () :
    # Make Dropdown POST
    post_dropdown = Select ( driver.find_element_by_id ( "projectId" ) )
    post_dropdown.select_by_value ( "0c277d79-f261-44a5-84a4-4db588e3009c" )  # Selecting the value for "bKash"
    # Find the button by ID
    show_dropdown = Select ( driver.find_element_by_id ( "show" ) )

    # Select the option with the value "100"
    show_dropdown.select_by_value ( "50" )

    filter_button = driver.find_element_by_id ( "btnfilter" )

    # Press enter using the return key
    filter_button.send_keys ( Keys.RETURN )
    time.sleep(2)
    # Find the button by class name


def reannotBTN():
    button_xpath = "/html/body/div[1]/div[2]/div/div/main/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[4]/div/a"
    button_element = driver.find_element_by_xpath ( button_xpath )

    # Click the button
    button_element.click ( )


def reAnnote():

    # Find the select element by ID
    brand_dropdown = Select ( driver.find_element_by_id ( "brandId" ) )

    # Select "bKash" by visible text
    brand_dropdown.select_by_visible_text ( "bKash" )

    sentiment_dropdown = Select ( driver.find_element_by_id ( "SentimentId" ) )

    # Select "Positive" by visible text
    sentiment_dropdown.select_by_visible_text ( "Positive" )

    category_dropdown = Select ( driver.find_element_by_id ( "categoryId" ) )

    # Select "Brand" by visible text
    category_dropdown.select_by_visible_text ( "Brand" )

    time.sleep(2)

    category_dropdown = Select ( driver.find_element_by_id ( "subcategoryId" ) )

    # Select "Brand" by visible text
    category_dropdown.select_by_visible_text ( "Associated" )

    category_dropdown = Select ( driver.find_element_by_id ( "EmotionId" ) )

    # Select "Brand" by visible text
    category_dropdown.select_by_visible_text ( "Neutral" )

    category_dropdown = Select ( driver.find_element_by_id ( "ProfileTagId" ) )

    # Select "Brand" by visible text
    category_dropdown.select_by_visible_text ( "Loyalty:Passive User" )

    comment_reject_button = driver.find_element_by_id ( "btnCommentReject" )

    # Click the button
    comment_reject_button.click ( )


selectTime()
selectProject()
reannotBTN()
reAnnote()

for _ in range(timesToIterate):
    time.sleep(2)
    reannotBTN()
    reAnnote()
