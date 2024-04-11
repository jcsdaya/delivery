from django.shortcuts import render
from .forms import riderForm
from django.shortcuts import redirect,get_object_or_404
from .models import Rider

def riderhome(request):
    form_type = request.POST.get('form_type')
    if request.method == 'POST':
        
        if form_type == 'riderhome':
            form = riderForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('riderhome')
        elif form_type == 'rideredit':
            pk = request.POST.get('pk')
            rider = get_object_or_404(Rider, pk=pk)
            form = riderForm(request.POST, instance=rider)
        
            if request.method == 'POST':
                
                if form.is_valid():
                    form.save()
                    return redirect('riderhome')
            else:
                form = riderForm(instance=rider)
                
        elif form_type =='riderdelete':
            rider = get_object_or_404(Rider, pk=pk)
            if request.POST:
                    rider.delete()
            return redirect('riderhome')
    else:
        form = riderForm()
    all_rider = Rider.objects.all()
    context = {'all_rider': all_rider, 'form': form}
    return render(request, 'riderhome.html', context)


def rideredit(request,pk):
    rider = get_object_or_404(Rider, pk=pk)
    form = riderForm(instance=rider)

    if request.POST:
        rider = get_object_or_404(Rider, pk=pk)
        form = riderForm(request.POST, instance=rider)
        if form.is_valid():
            form.save()
            return redirect('riderhome')
    context = {'form': form, 'rider': rider} 
    return render(request, 'rideredit.html', context)

def riderdelete(request,pk):
    rider = get_object_or_404(Rider, pk=pk)
    if request.POST:
            rider.delete()
            return redirect('riderhome')
    context={'rider':rider}
    return render(request,'riderdelete.html',context)
        



