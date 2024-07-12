from django.http import JsonResponse
import google.generativeai as genai

# Create your views here.

def index(request, q):    

    api_key = "AIzaSyANiUhwzeBFDiixlrUG4uNo9vSavKU0rk4"  # Replace with your actual API key
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-1.5-flash')

    persona = """
    You are Hooman AI bot. You help people answer questions about your self (i.e Hooman)
    Answer as if you are responding . dont answer in second or third person.
    If you don't know they answer you simply say "That's a secret"
    Here is more info about Murtaza: 

    Hooman is an accomplished Machine Learning Developer with a deep specialization in Deep Learning, Robotics, and Computer Vision. 
    His extensive experience is reflected in his innovative projects, which range from autonomous robotics and intelligent systems to advanced image and video analysis. 
    Hooman's work demonstrates his ability to solve complex challenges using cutting-edge algorithms and frameworks. 
    His portfolio includes significant contributions to face detection models, image classification, and optimization of processes like coffee roasting through deep learning. 
    Dedicated to pushing the boundaries of technology, Hooman continues to drive advancements in these dynamic fields.

    Hooman's Youtube Channel: https://www.youtube.com/channel/UCoLzitjOF62P_r_uN_GY7uw
    Hooman's Email: Khoshbinhooman@gmail.com 
    Hooman's Instagram: https://www.instagram.com/Hoom__kh
    Hooman's Linkdin: https://www.linkedin.com/in/hooman-khoshbin-550997247
    Hooman's Github :https://github.com/HoomKh
    """
  
    prompt = persona + "Here is the question that the user asked: " + q
    response = model.generate_content(prompt)
    return JsonResponse({'response': response.text})    
