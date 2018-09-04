import requests
from bs4 import BeautifulSoup

import sys
import os


def ParseAd(html,ad_id):  # Parses ad html trees and sorts relevant data into a dictionary
    ad_info = {}

    try:
        ad_info["Title"] = html.find('a', {"class": "title"}).text.strip()
    except:
        print('[Error] Unable to parse Title data.')

    try:
        if len(ad_id) == 6:
            ad_info["Url"] = html.get("data-vip-url")
        else:
            ad_info["Url"] = 'http://www.kijiji.ca' + html.get("data-vip-url")
    except:
        print('[Error] Unable to parse URL data.')

    try:
        ad_info["Details"] = html.find('p').text.strip()
    except:
        print('[Error] Unable to parse Details data.')

    try:
        if len(ad_id) == 6:
            ad_info["Posted"] = "Third-Party Inc"
        else:
            ad_info["Posted"] = html.find('td', {"class": "posted"}).text.strip()
    except:
        print('[Error] Unable to parse Date data.')

    return ad_info

def WriteAds(ad_dict, filename):  # Writes ads from given dictionary to given file
    file = open(filename, 'ab')
    for ad_id in ad_dict:
        file.write(ad_id.encode('utf-8'))
        file.write((str(ad_dict[ad_id]) + "\n").encode('utf-8'))
    file.close()


def ReadAds(filename):  # Reads given file and creates a dict of ads in file
    import ast
    if not os.path.exists(filename):  # If the file doesn't exist, it makes it.
        file = open(filename, 'w')
        file.close()

    ad_dict = {}
    with open(filename, 'rb') as file:
        for line in file:
            if line.strip() != '':
                index = line.find('{'.encode('utf-8'))
                ad_id = line[:index].decode('utf-8')
                dictionary = line[index:].decode('utf-8')
                dictionary = ast.literal_eval(dictionary)
                ad_dict[ad_id] = dictionary
    return ad_dict

def MailAd(ad_dict, email_title):  # Sends an email with a link and info of new ads
    import smtplib
    from email.mime.text import MIMEText

    # Fill in the variables below with your info
    # ------------------------------------------
    sender = 'ytyc2k@gmail.com'
    passwd = 'app957639'
    receiver = 'ytyc2k@gmail.com;yxzhang2046@hotmail.com;weiwei2017ca@gmail.com'
    #receiver = 'ytyc2k@gmail.com'
    smtp_server = 'smtp.gmail.com'
    smtp_port = 465
    # ------------------------------------------

    count = len(ad_dict)
    if count > 1:
        subject = str(count) + ' New ' + email_title + ' Ads Found!'
    if count == 1:
        subject = 'One New ' + email_title + ' Ad Found!'

    body = '<!DOCTYPE html> \n<html> \n<body>'
    try:
        for i,ad_id in enumerate(ad_dict,1):
            body += '<p><b>' + str(i)+': '+ \
                    '<a href="' + ad_dict[ad_id]['Url'] + '">' + ad_dict[ad_id]['Title'] + '</a>'\
                    + '</b>'+' - ' + ad_dict[ad_id]['Posted'] + '<br /></p>'
            body += '<p>' + ad_dict[ad_id]['Details'] + '<br />'
    except:
        body += '<p>' + ad_dict[ad_id]['Title'] + '<br />'
        body += ad_dict[ad_id]['Url'] + '<br /><br />' + '</p>'
        print('[Error] Unable to create body for email message')

    body += '<p>This is an automated message, please do not reply to this message.</p>'

    msg = MIMEText(body, 'html')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = receiver

    try:
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        server.ehlo()
    except:
        print('[Error] Unable to connect to email server.')
    try:
        server.login(sender, passwd)
    except:
        print('[Error] Unable to login to email server.')
    try:
        server.send_message(msg)
        server.quit()
        print('[Okay] Email message successfully delivered.')
    except:
        print('[Error] Unable to send message.')

def toUpper(title):  # Makes the first letter of every word upper-case
    new_title = list()
    title = title.split()
    for word in title:
        new_word = ''
        new_word += word[0].upper()
        if len(word) > 1:
            new_word += word[1:]
        new_title.append(new_word)
    return ' '.join(new_title)

def scrape(url, old_ad_dict, filename):  # Pulls page data from a given kijiji url and finds all ads on each page
    # Initialize variables for loop
    email_title = None
    ad_dict = {}
    third_party_ad_ids = []

    while url:

        try:
            page = requests.get(url)  # Get the html data from the URL
        except:
            print("[Error] Unable to load " + url)
            sys.exit(1)

        soup = BeautifulSoup(page.content, "html.parser")

        if not email_title:  # If the email title doesnt exist pull it form the html data
            email_title = soup.find('div', {'class': 'message'}).find('strong').text.strip('"')
            email_title = toUpper(email_title)

        kijiji_ads = soup.find_all("table", {"class": "regular-ad"})  # Finds all ad trees in page html.

        for ad in kijiji_ads:  # Creates a dictionary of all ads with ad id being the keys.
            ad_id = ad['data-ad-id']  # Get the ad id
            if ad_id == "": ad_id = ad['data-third-party-id']  # Get the ad id
            if ( ad_id not in old_ad_dict ):  # Skip third-party ads and ads already found
                print('[Okay] New ad found! Ad id: ' + ad_id)
                ad_dict[ad_id] = ParseAd(ad,ad_id)  # Parse data from ad
        url = soup.find('a', {'title': 'Next'})
        if url:
            url = 'https://www.kijiji.ca' + url['href']

    if ad_dict != {}:  # If dict not emtpy, write ads to text file and send email.
        WriteAds(ad_dict, filename)  # Save ads to file

        MailAd(ad_dict, email_title)


def main():  # Main function, handles command line arguments and calls other functions for parsing ads
    #args = sys.argv
    #args = ['Kijiji-Scraper.py', 'https://www.kijiji.ca/b-calgary/kayak/k0l1700199?price=__1000', '-f', 'kayaks.txt', '-e', 'wanted','-s']
    #args = ['Kijiji-Scraper.py', 'https://www.kijiji.ca/b-programmer-computer-jobs/winnipeg/c54l1700192', '-f', 'Winnipeg_jobs.txt']
    args = ['Kijiji-Scraper.py', 'https://www.kijiji.ca/b-programmer-computer-jobs/ottawa/c54l1700185', '-f', 'Ottawa_jobs.txt']
    url_to_scrape = args[1]
    if '-f' in args:
        filename = args.pop(args.index('-f') + 1)
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), filename)
        args.remove('-f')
    else:
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), url_to_scrape)

    old_ad_dict = ReadAds(filename)
    print("[Okay] Ad database succesfully loaded.")
    scrape(url_to_scrape, old_ad_dict, filename)

if __name__ == "__main__":
    main()