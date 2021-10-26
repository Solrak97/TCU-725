import time
from selenium import webdriver
import subprocess
import threading as thr
import sys
from os import path




def kill_server():
    subprocess.run("lsof -t -i tcp:8080 | xargs kill -9", shell=True)


def start_dash_app_frozen():
    path_dir = str(path.dirname(sys.executable))
    subprocess.Popen(path_dir+"/app", shell=False)
    print(path_dir+"/app")

def start_driver():
    driver = webdriver.Chrome(executable_path='assets\chromedriver.exe')
    time.sleep(5)
    driver.get("http://0.0.0.0:8080/")
    save_browser_session(driver) 
    print("DRIVER SAVED IN TEXT FILE browsersession.txt")


def save_browser_session(input_driver):
    driver = input_driver
    executor_url = driver.command_executor._url
    session_id = driver.session_id
    browser_file = path_dir+"/browsersession.txt"
    with open(browser_file, "w") as f:
        f.write(executor_url)
        f.write("\n")
        f.write(session_id)


def keep_server_running():
    while True:
        time.sleep(60)
        print("Next run for 60 seconds")


def main():
    kill_server()
    thread = thr.Thread(target=start_dash_app_frozen) 
    thread.start()
    #start_driver()
    #keep_server_running()


if __name__ == '__main__':
    main()