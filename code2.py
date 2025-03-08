
import qrcode
from datetime import datetime, timedelta
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import Paragraph
from reportlab.lib import colors
from newspaper import Article
## Newpaper requires equires lxml_html_clean and  newspaper3k

def get_headline(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.title if article.title else None


url1 = "https://www.wired.com/story/gsai-chatbot-1500-federal-workers/"

url2 = "https://www.npr.org/2025/03/07/nx-s1-5321326/trump-administration-columbia-university-400-million-cancelled"

url3 = "https://www.axios.com/2025/03/06/state-department-ai-revoke-foreign-student-visas-hamas"

story1 = get_headline(url1)
story2 = get_headline(url2)
story3 = get_headline(url3)


story3 = "State Dept. to use AI to revoke visas of foreign students who appear 'pro-Hamas' "  
## sometimes the headline doesn't load and you have to do it by hand 

story_details = [(story1,url1), (story2,url2), (story3,url3)]
current_date = datetime.now()
tomorrow = current_date + timedelta(days=1)  
tomorrow_str = tomorrow.strftime("%A, %B %d, %Y")
file_name = tomorrow_str+".pdf"

qr_urls = [url for _, url in story_details]



create_pdf(tomorrow_str,  qr_urls, story_details)


# Create a function to generate the PDF
def create_pdf(tomorrow_str , qr_urls, story_details):
    file_name = tomorrow_str+".pdf"
    # Create a canvas object
    c = canvas.Canvas(file_name, pagesize=letter)
    width, height = letter
    c.setFont("Helvetica-Bold", 26)
    c.drawString(100, height - 30, "The Daily Droplet")
    c.setFont("Helvetica-Bold", 18)
    c.drawString(150, height - 60, tomorrow_str )
    styles = getSampleStyleSheet()
    normal_style = styles['Normal']
    normal_style.fontSize = 22 # Set font size to a larger value
    qr_code_width = 100  # Define QR code width
    normal_style.leading = 30 # Adjust leading (space between lines)
    y_position = height - 150
    for text, url in story_details:
        # Create a Paragraph object for the detail text to handle wrapping
        paragraph = Paragraph(f"• {text}", normal_style)
        paragraph_width = width - 250  # set the width of the text box
        paragraph_height = paragraph.wrap(paragraph_width, 100)[1]  # calculate height based on text width
        paragraph.drawOn(c, 100, y_position - paragraph_height)
        qr = qrcode.make(url)
        qr_path = text[0:15]+".png"
        qr.save(qr_path)
        c.drawImage(qr_path, width - 150, y_position - paragraph_height - 20, width=100, height=100)
        y_position -= paragraph_height + 120  # increase space for the next detail
    c.setFont("Helvetica", 10)  # Set a smaller font 
    bottom_y = 30
    c.drawString(50, bottom_y, "#teslatakedown")  
    c.drawImage("tesla.png", 130, bottom_y - 10, width=50, height=50) 
    c.drawString(200, bottom_y, "Boycott airbnb")  
    c.drawImage("airbnb.png", 280, bottom_y - 10, width=50, height=50)
    c.drawString(370, bottom_y, "Get paid to distribute--->")  
    c.drawImage("rickroll.png", 520, bottom_y - 10, width=50, height=50)
    c.save()


#run this once to get the qr codes along the bottom 

teslatakedown = "https://actionnetwork.org/event_campaigns/teslatakedown"
airbnb = "https://www.newsweek.com/airbnb-boycott-calls-joe-gebbia-elon-musk-doge-2033847"
rickroll = " https://bit.ly/3BlS71b"

qr_tt = qrcode.make(teslatakedown)
qr_path = "tesla.png"
qr_tt.save(qr_path)

qr_airbnb = qrcode.make(airbnb)
qr_path = "airbnb.png"
qr_airbnb.save(qr_path)

qr_rickroll = qrcode.make(rickroll)
qr_path = "rickroll.png"
qr_rickroll.save(qr_path)

create_pdf(tomorrow_str,  qr_urls, story_details)



