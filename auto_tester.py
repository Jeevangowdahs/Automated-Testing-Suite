from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# ==========================================
# PART 1: SETUP THE ROBOT (SIMPLIFIED)
# ==========================================
def setup_driver():
    print("🤖 Starting Test Bot (Microsoft Edge)...")
    options = webdriver.EdgeOptions()
    
    # NEW: We removed the "Manager" install command. 
    # Selenium now finds Edge automatically on Windows.
    driver = webdriver.Edge(options=options) 
    return driver

# ==========================================
# PART 2: THE LOGGER
# ==========================================
def log_result(test_name, status, details=""):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"[{timestamp}] {test_name}: {status} | {details}\n"
    print(log_message.strip())
    with open("test_execution_log.txt", "a") as f:
        f.write(log_message)

# ==========================================
# PART 3: THE TEST SCRIPTS
# ==========================================
def run_tests():
    try:
        driver = setup_driver()
    except Exception as e:
        print(f"❌ ERROR: {e}")
        print("Try updating your 'selenium' library: pip install selenium --upgrade")
        return

    url = "https://www.saucedemo.com/" 
    
    # Clear old logs
    with open("test_execution_log.txt", "w") as f:
        f.write("--- DELOITTE AUTOMATED TEST SUITE ---\n")

    try:
        # TEST 1: LOGIN SUCCESS
        driver.get(url)
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(2)
        
        if "inventory" in driver.current_url:
            log_result("TC_01 Login Success", "PASSED", "Redirected to inventory.")
        else:
            log_result("TC_01 Login Success", "FAILED", "Redirect failed.")

        # TEST 2: DATA VALIDATION
        items = driver.find_elements(By.CLASS_NAME, "inventory_item")
        if len(items) == 6:
            log_result("TC_02 Inventory Count", "PASSED", f"Verified {len(items)} items.")
        else:
            log_result("TC_02 Inventory Count", "FAILED", f"Found {len(items)} items.")

        # LOGOUT
        driver.find_element(By.ID, "react-burger-menu-btn").click()
        time.sleep(1)
        driver.find_element(By.ID, "logout_sidebar_link").click()
        
        # TEST 3: SECURITY CHECK (Bad Login)
        driver.get(url)
        driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
        driver.find_element(By.ID, "password").send_keys("secret_sauce")
        driver.find_element(By.ID, "login-button").click()
        time.sleep(1)
        
        error_msg = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
        if "locked out" in error_msg.text:
             log_result("TC_03 Locked User Check", "PASSED", "Error caught successfully.")
        else:
             log_result("TC_03 Locked User Check", "FAILED", "Error message missing.")

    except Exception as e:
        log_result("System Error", "CRITICAL", str(e))
    
    finally:
        driver.quit()
        print("\n✅ Testing Complete. Open 'test_execution_log.txt' to see the report.")

if __name__ == "__main__":
    run_tests()