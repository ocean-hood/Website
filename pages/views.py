from django.shortcuts import render

def home_view(request):
  return render(request , 'home.html')

def begineer_view(request):
  return render(request , 'beginner.html')

def intermediate_view(request):
  return render(request , 'intermediate/intermediate.html')

def expert_view(request):
  return render(request , 'expert.html')

def about_us_view(request):
  return render(request , 'about-team.html')

def intermediate1_view(request):
  return render(request , 'intermediate/1.html')

def intermediate2_view(request):
  return render(request , 'intermediate/2.html')
  
def intermediate3_view(request):
  return render(request , 'intermediate/3.html')

def intermediate4_view(request):
  return render(request , 'intermediate/4.html')

def intermediate5_view(request):
  return render(request , 'intermediate/5.html')

def intermediate6_view(request):
  return render(request , 'intermediate/6.html')

def intermediate7_view(request):
  return render(request , 'intermediate/7.html')

def advanced_view(request):
  return render(request , 'advanced/advanced.html')


def contact_view(request):
  return render(request , 'contact.html')

def data_view(request):
  return render(request , 'data.html')