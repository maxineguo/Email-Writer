from google import genai
import os
from dotenv import load_dotenv, find_dotenv

dotenv_path = find_dotenv()
if dotenv_path:
    load_dotenv(dotenv_path, override=True)
else:
    print("DEBUG: .env file not found. Ensure it's in the project root.")

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client()

requirements = input("")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=f"Your job is to write an EXTREMELY POLITE email for my teacher. Here are some basic things to include. Remember to always vary your responses but be VERY polite: 1. greeting(hi, hello, etc) [teacher name(will be provided)] 2. nice fun message, wishing well (ex: I hope you are doing well., How are you?, etc) 3. A polite request/message (will be provided) 4. Gratitude (ex: Thank you for your time, Thank for helping me, etc) 5. Closing (Best, Sincerely, etc) and my name(Maxine Guo). Don't make it cringy or over the top. Also keep the English rather simple. Don't directly say things like 'respectfully inquire'. Don't talk about my personality or 'goal to improve my performance in your class' or anything. Just include the email, nothing regarding the subject or address. Here is the info I promised: {requirements}",
)

print(response.text)