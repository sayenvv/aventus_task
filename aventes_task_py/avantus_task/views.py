from multiprocessing import context
from django.shortcuts import render
from .forms import *

# Create your views here.
def string_check(request):
    
    if(request.method=="POST"):
        
        form = BasicForm(request.POST)
        if form.is_valid():
            master_string = form.cleaned_data['master_string']
            string1 = form.cleaned_data['string1']
            string2 = form.cleaned_data['string2']
            string3 = form.cleaned_data['string3']
            string4 = form.cleaned_data['string4']
            master_data = [i for i in master_string]

            s1 = ''
            for i in string1:
                if i in master_data:
                    s1 += i
            if s1 == string1:
                
                context['str1'] = "{}: yes".format(string1)
                for i in string1:
                    try:
                        master_data.remove(i)
                    except Exception as e:
                        pass
            else:
                context['str1'] = "{}: No".format(string1)

            s2 = ''
            for j in string2:
                if j in master_data:
                    s2 += j
            if s2 == string2:
                context['str2'] = "{}: yes".format(string2)
                for j in string2:
                    try:
                        master_data.remove(j)
                    except Exception as e:
                        pass
            else:
                context['str2'] = "{}: No".format(string2)


            s3 = ''
            for k in string3:
                if k in master_data:
                    s3 += k
            if s3 == string3:
                context['str3'] = "{}: yes".format(string3)
                for k in string3:
                    try:
                        master_data.remove(k)
                    except Exception as e:
                        pass
            else:
                context['str3'] = "{}: No".format(string3)


            s4 = ''
            for l in string4:
                if l in master_data:
                    s4 += l
            if s4 == string4:
                context['str4'] = "{}: yes".format(string4)
                for l in string4:
                    try:
                        master_data.remove(l)
                    except Exception as e:
                        pass
            else:
                context['str4'] = "{}: No".format(string4)

    context['forms'] = BasicForm()
    return render(request,"index.html",context)