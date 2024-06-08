import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

def get_outage_info(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        outages = []
        for item in soup.find_all('div', class_='indepth-thumbnail'):
            title = item.find('h3').get_text(strip=True) if item.find('h3') else 'No title'
            description = item.find('p').get_text(strip=True) if item.find('p') else 'No description'
            link = item.find('a')['href'] if item.find('a') else 'No link'
            outages.append({'title': title, 'description': description, 'link': link})
        return outages
    else:
        return None

def send_email(subject, body, to_email):
    from_email = "your_email@gmail.com"
    from_password = "your_password"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(from_email, from_password)
        server.sendmail(from_email, to_email, msg.as_string())

# Configuration
url = 'https://www.rri.co.id/sprint?query=pemadaman+listrik'
outage_info = get_outage_info(url)

if outage_info:
    body = "\n".join([f"Title: {outage['title']}\nDescription: {outage['description']}\nLink: {outage['link']}\n" for outage in outage_info])
    print(body)  # Display information before sending email
    
    # Send email
    send_email(
        "Power Outage Alert",
        body,
        "recipient_email@example.com"
    )
else:
    print("No outage information found or failed to fetch data.")