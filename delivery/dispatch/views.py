from django.shortcuts import render,redirect,get_object_or_404
from .forms import dispatchriderForm
from .models import Dispatch


def dispatchhome(request):
    form_type = request.POST.get('form_type')
    if request.method == 'POST':
        
        if form_type == 'dispatchedit':
            pk = request.POST.get('pk')
            dispatch = get_object_or_404(Dispatch, pk=pk)
            form = dispatchriderForm(request.POST, instance=dispatch)
        
            if request.method == 'POST':
                
                if form.is_valid():
                    form.save()
                    return redirect('dispatchhome')
            else:
                form = dispatchriderForm(instance=dispatch)
                
        elif form_type =='riderdelete':
            dispatch = get_object_or_404(Dispatch, pk=pk)
            if request.POST:
                    dispatch.delete()
            return redirect('dispatchhome')
    else:
        form = dispatchriderForm()
    all_dispatch = Dispatch.objects.all()
    context = {'all_dispatch': all_dispatch, 'form': form}
    return render(request, 'dispatchhome.html', context)


def dispatchupdate(request,pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    form = dispatchriderForm(instance=dispatch)

    if request.POST:
        form = dispatchriderForm(request.POST, instance=dispatch)
        if form.is_valid():
            form.save()
            return redirect('dispatchhome')
    context = {'form': form, 'dispatch': dispatch} 
    return render(request, 'dispatchupdate.html', context)

def dispatchcomplete(request):
    all_complete = Dispatch.objects.filter(complete=True)
    context = {'all_complete':all_complete}
    return render(request, 'completedorder.html',context)



def dispatchdecline(request,pk):
    dispatch = get_object_or_404(Dispatch, pk=pk)
    if request.POST:
            dispatch.delete()
            return redirect('dispatchhome')
    context={'dispatch':dispatch}
    return render(request,'dispatchdecline.html',context)
        
        



