from django.shortcuts import render
from django.http import HttpResponse
import random
import string

def create_password(is_lower,is_upper,is_numbers,is_special,pw_length):
    total_pw,random_pw='',''
    remind_pw_length=pw_length
    lowercase_pw = string.ascii_lowercase
    upper_case_pw = string.ascii_uppercase
    digits_pw = string.digits
    special_pw = '!@#$%*&()'

    if is_lower:
        total_pw+=lowercase_pw
        random_pw+=random.choice(lowercase_pw)
        remind_pw_length-=1
    if is_upper:
        total_pw += upper_case_pw
        random_pw += random.choice(upper_case_pw)
        remind_pw_length -= 1
    if is_numbers:
        total_pw += digits_pw
        random_pw += random.choice(digits_pw)
        remind_pw_length -= 1
    if is_special:
        total_pw += special_pw
        random_pw += random.choice(special_pw)
        remind_pw_length -= 1

    random_pw+=''.join(random.sample(total_pw,remind_pw_length))
    return random_pw

def create_multi_passwords(is_lower,is_upper,is_numbers,
                           is_special,pw_length,groups=6):
    out=[]
    for i in range(groups):
        out.append(create_password(is_lower,is_upper,is_numbers,is_special,pw_length))
        out.append('\n')

    return ''.join(out)

def index(request):
    if request.method=='GET':
        return render(request,'generator/index.html')
    elif request.method=='POST':
        pw_length = int(request.POST.get('length'))
        is_lower = request.POST.get('lowercase')
        is_upper = request.POST.get('uppercase')
        is_numbers = request.POST.get('numbers')
        is_special = request.POST.get('special')

        password = create_password(is_lower,is_upper,is_numbers,is_special,pw_length)
        # password = create_multi_passwords(is_lower,is_upper,is_numbers,is_special,pw_length)
        return render(request, 'generator/index.html', {'password': password})
