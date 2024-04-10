import re

def extract_image_links(html_text):
    pattern = r"\s*https?://[\w./]+.[e-p]{3,4}\s*"
    string = re.findall(pattern, html_text)
    return string


sample_html = ("<img src='https://example.com/image1.jpg'> <img src='http://example.com/image2.png'> "
               "<img src='https://example.com/image3.gif'>")

image_links = extract_image_links(sample_html)
if image_links:
  for image_link in image_links:
    print(image_link)
else:
  print("Нет ссылок с картинками в HTML тексте.")