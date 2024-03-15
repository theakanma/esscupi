WebDriverWait(driver, wait).until(
    EC.presence_of_element_located((By.ID, "my_id"))
)
