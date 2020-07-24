from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

driver.get("http://www.google.com/")
print(driver.title)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    render_template('index.html')

if __name__ == '__main__':
    app.run()