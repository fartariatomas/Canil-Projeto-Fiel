#!/usr/bin/env python
import urllib.request
import datetime
import os
import sys
from html.parser import HTMLParser
import sqlite3
from selenium import webdriver
import pyautogui
import time


def liftoff():
    print('Three, two, one, liftoff!')


def done():
    print('it\'s over kid')
    sys.exit(0)


class HTMLTableParser(HTMLParser):
    """ This class serves as a html table parser. It is able to parse multiple
    tables which you feed in. You can access the result per .tables field.
    """

    def __init__(
        self,
        decode_html_entities=False,
        data_separator=' ',
    ):

        HTMLParser.__init__(self)

        self._parse_html_entities = decode_html_entities
        self._data_separator = data_separator

        self._in_td = False
        self._in_th = False
        self._current_table = []
        self._current_row = []
        self._current_cell = []
        self.tables = []

    def handle_starttag(self, tag, attrs):
        """ We need to remember the opening point for the content of interest.
        The other tags (<table>, <tr>) are only handled at the closing point.
        """
        if tag == 'td':
            self._in_td = True
        if tag == 'th':
            self._in_th = True

    def handle_data(self, data):
        """ This is where we save content to a cell """
        if self._in_td or self._in_th:
            self._current_cell.append(data.strip())

    def handle_charref(self, name):
        """ Handle HTML encoded characters """

        if self._parse_html_entities:
            self.handle_data(self.unescape('&#{};'.format(name)))

    def handle_endtag(self, tag):
        """ Here we exit the tags. If the closing tag is </tr>, we know that we
        can save our currently parsed cells to the current table as a row and
        prepare for a new row. If the closing tag is </table>, we save the
        current table and prepare for a new one.
        """
        if tag == 'td':
            self._in_td = False
        elif tag == 'th':
            self._in_th = False

        if tag in ['td', 'th']:
            final_cell = self._data_separator.join(self._current_cell).strip()
            self._current_row.append(final_cell)
            self._current_cell = []
        elif tag == 'tr':
            self._current_table.append(self._current_row)
            self._current_row = []
        elif tag == 'table':
            self.tables.append(self._current_table)
            self._current_table = []


def selenium_saves_website_source_code():
    website_url = "http://municipium.cm-evora.pt/Canil/Adotar.aspx"
    driver = webdriver.Firefox()
    driver.get(website_url)
    driver.implicitly_wait(2)
    # gets page source and downloads table with dogs names
    # download_animals_from_website(driver.page_source)
    download_animals_photos(driver)
    # gets page links to click
    links_with_js = driver.find_elements_by_tag_name('a')
    links_with_js[-2].click()  # goto page 2 and repeat process
    # gets page source and downloads table with dogs names
    download_animals_from_website(driver.page_source)
    download_animals_photos(driver)
    # gets page links to click
    links_with_js = driver.find_elements_by_tag_name('a')
    links_with_js[-1].click()  # goto page 2 and repeat process
    # gets page source and downloads table with dogs names
    download_animals_from_website(driver.page_source)
    download_animals_photos(driver)
    # closes browser
    driver.close()


def download_animals_photos(driver):
    for j in range(10):
        pyautogui.scroll(-100)
        time.sleep(0.1)
        name_pos_x, name_pos_y = 15, 365 + 38 * j
        pyautogui.moveTo(name_pos_x, name_pos_y)
        if j == 2: done()
        pyautogui.doubleClick()
        pyautogui.hotkey('ctrl', 'c')
        button_pos_x, button_pos_y = 1250, name_pos_y
        pyautogui.moveTo(button_pos_x, button_pos_y)
        pyautogui.click()
        time.sleep(0.5)  # wait 1 sec for page to refresh with photo
        pyautogui.scroll(-500)
        time.sleep(0.1)
        photo_pos_x, photo_pos_y = 50, 700
        pyautogui.moveTo(photo_pos_x, photo_pos_y)
        pyautogui.click(button='right')
        time.sleep(0.2)
        pyautogui.moveTo(photo_pos_x + 10, photo_pos_y - 115)
        pyautogui.click()  # save image as
        time.sleep(0.2)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.1)
        pyautogui.press('enter')
        time.sleep(0.5)
        try:
            driver.refresh()
        except:
            pyautogui.press('enter')
            time.sleep(1)


def download_animals_from_website(source_code):
    xhtml = source_code
    p = HTMLTableParser()
    p.feed(xhtml)
    list_to_dict(p.tables[1][1:-1])


def list_to_dict(animals_list):
    animals_clean_list = []
    for animal in animals_list:
        mixed_race = 0 if animal[4] == '' else 1
        gender = 'M' if animal[5] == 'M' else 'F'
        animals_clean_list.append((animal[0], animal[1].lower(), animal[3].partition(' / ')[2].lower(), mixed_race, gender, animal[
                                  6].partition(' / ')[2].lower(), animal[7].partition(' / ')[2].lower(), animal[8].partition(' / ')[2].lower(), animal[9].partition(' / ')[2].lower()))
    list_to_db(animals_clean_list)


def list_to_db(animals_clean_list):

    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()
    for animal in animals_clean_list:
        cursor.execute("SELECT * FROM dogs_dog WHERE name=?", [(animal[0])])
        if cursor.fetchone():
            print('dog with the same name already exists')
        else:
            cursor.execute(
                "INSERT INTO dogs_dog (name, number_register, race, mixed_race, sex, colour, hair, tail, size) VALUES (?,?,?,?,?,?,?,?,?)", animal)
    conn.commit()


def main():
    liftoff()
    selenium_saves_website_source_code()
    print('Done biatch!')

if __name__ == "__main__":
    main()
