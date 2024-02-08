from bs4 import BeautifulSoup
import json

# Simulate HTML content extraction (you would replace this with actual web scraping logic)
html_content = """
<div class="user-content-block">
<p>GIVEN I have a gas contract<br>
AND it has two valid meter reads with thermal properties<br>
AND EE gpke.degreeDaysPlus.value = 0<br>
AND I let the system estimate a third meter read<br>
AND the outcome can be validated positively with the Excel attached <br>
WHEN I set EE gpke.degreeDaysPlus.value = X (other than 0)<br>
AND I let the system estimate the third meter read again<br>
THEN the results differ by the value X</p>
</div>
"""

# Use BeautifulSoup to parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the <p> tag content
user_story_content = soup.find('div', class_='user-content-block').find('p').get_text(separator='\n')

# Save into JSON
json_data = {
    "user_story": user_story_content
}

json_object = json.dumps(json_data, indent=4)

# Simulate passing the JSON data through the ChatGPT API (here we'll just print it)
print("JSON Data to be sent to ChatGPT API:")
print(json_object)

# Simulate displaying the result/output to the user on the console
# In a real scenario, this would involve using the OpenAI API to process `json_data`
print("\nSimulated ChatGPT API Response:")
print("Thank you for your input. Based on the provided user story, you may want to consider the following steps...")
