
import time

def highlight_flash(driver, element, duration=.2, color="beige", border="2px solid BurlyWood"):
    # Scroll the element into view first
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'auto', block: 'center'});", element)

    # Save the original style
    original_style = element.get_attribute("style")
    # Apply highlight style
    for i in range(3):
        highlight_style = f"border: {border}; background-color: {color};"
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, highlight_style)
        time.sleep(duration)
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, original_style)
        time.sleep(duration)
    # driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, highlight_style)


def highlight(driver, element):
    driver.execute_script("arguments[0].style.border='2px solid red'", element)
