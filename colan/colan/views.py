from django.http import HttpResponse
from django.shortcuts import render



def main_page(request):
    strings = request.POST.get('strings','Default')
    print(strings)
    return render(request,'index.html')


def validate(request):
    strings = request.POST.get('strings','Default')
    print(strings)
    check = request.POST.get('valid','off')
    print(check)
    uppercase = request.POST.get('uppercase','off')
    charlen = request.POST.get('charlen','off')
    digits = ''
    alphas = ''
    symbols = ''
    if check == 'on': 
        for i in strings:
            if i.isalpha():
                alphas+=i
            elif i.isdigit():
                digits+=i
            else:
                symbols+=i
        strings = alphas   
        params = {'digit': digits,'alpha':alphas,'symbol':symbols,'original_text':strings,'char':charlen,}
        #return render(request,'validation.html',params)
    if uppercase == 'on':
        alphas  = ''
        for i in strings:
            if i.isalpha():
                i.lower()
                alphas =alphas+i.upper()
        strings = alphas
        params = {'digit': digits,'alpha':alphas,'symbol':symbols,'original_text':strings,'char':charlen,}   
        # return render(request,'validation.html',params)
    if charlen == 'on':
        charlen = sum(1 for char in strings if char.isalpha())
    
        params = {'digit': digits,'char':charlen,'symbol':symbols,'original_text':strings,'alpha':alphas}
        
    return render(request,'validation.html',params)
    
    
        
    # else:
    #     return HttpResponse('error')

