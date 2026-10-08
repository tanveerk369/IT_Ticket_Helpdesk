from django.shortcuts import render, redirect
from .models import Ticket

def ticket_list(request):
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    priority = request.GET.get('priority', '')
    
    tickets = Ticket.objects.all()
    
    if search:
        tickets = tickets.filter(
            title__icontains=search
        )
    if status:
        tickets = tickets.filter(
            status=status
        )
    if priority:
        tickets = tickets.filter(
            priority=priority
        )
   
    return render(request, 'tickets/ticket_list.html', {'tickets':tickets, 'search':search, 'status':status, 'priority':priority})


def ticket_create(request):
    if request.method == 'POST':
        Ticket.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            category=request.POST['category'],
            priority=request.POST['priority'],
            status=request.POST['status']
        )

        return redirect('ticket_list')

    return render(request, 'tickets/ticket_create.html')

def ticket_detail(request, id):
    ticket = Ticket.objects.get(id=id)
    
    return render (request, 'tickets/ticket_detail.html', {'ticket':ticket})
        
        
def ticket_update(request, id):
    ticket = Ticket.objects.get(id=id)
    
    if request.method == 'POST':
        ticket.status = request.POST['status']
        ticket.save()
        
        return redirect('ticket_detail', id=ticket.id)
    
    return render(request,'tickets/ticket_update.html', {'ticket':ticket})


def ticket_delete(request, id):
    ticket = Ticket.objects.get(id=id)
    
    if request.method == 'POST':
        ticket.delete()
        return redirect('ticket_list')
    
    return render(request,'tickets/ticket_delete.html', {'ticket':ticket})