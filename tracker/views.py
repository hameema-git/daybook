from django.shortcuts import render, redirect
from .models import Entry
from django.db.models import Sum
from datetime import date
from django.core.paginator import Paginator
from datetime import datetime, date
from django.shortcuts import redirect, get_object_or_404

def dashboard(request):
    date_filter = request.GET.get('date_filter', None)

    # Filter entries by date if a date is provided
    if date_filter:
        entries = Entry.objects.filter(date=date_filter).order_by('-date')
    else:
        entries = Entry.objects.all().order_by('-date')

    # Pagination - removed as per request
    # Pagination can be re-added if necessary later

    income = entries.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
    expense = entries.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
    balance = income - expense

    return render(request, 'tracker/dashboard.html', {
        'entries': entries,
        'income': income,
        'expense': expense,
        'balance': balance,
        'date_filter': date_filter  # Pass the date filter to the template
    })

# def dashboard(request):
#     entries = Entry.objects.all().order_by('-date')
#     income = entries.filter(type='income').aggregate(Sum('amount'))['amount__sum'] or 0
#     expense = entries.filter(type='expense').aggregate(Sum('amount'))['amount__sum'] or 0
#     balance = income - expense

#     return render(request, 'tracker/dashboard.html', {
#         'entries': entries,
#         'income': income,
#         'expense': expense,
#         'balance': balance
#     })

# def add_entry(request):
#     if request.method == 'POST':
#         # Check if date is provided, otherwise use today's date
#         entry_date = request.POST.get('date', date.today())

#         # Create the entry
#         Entry.objects.create(
#             amount=request.POST['amount'],
#             category=request.POST['category'],
#             type=request.POST['type'],
#             note=request.POST.get('note', ''),
#             date=entry_date
#         )
#         return redirect('dashboard')

#     # Get today's date as default for the date input
#     today_date = date.today()

#     return render(request, 'tracker/add_entry.html', {'today_date': today_date})
def add_entry(request):
    if request.method == 'POST':
        # Get date from form or default to today's date
        date_input = request.POST.get('date', '').strip()

        if date_input:
            try:
                entry_date = datetime.strptime(date_input, '%Y-%m-%d').date()
            except ValueError:
                entry_date = date.today()  # fallback if format is wrong
        else:
            entry_date = date.today()

        Entry.objects.create(
            amount=request.POST['amount'],
            category=request.POST['category'],
            type=request.POST['type'],
            note=request.POST.get('note', ''),
            date=entry_date
        )
        return redirect('dashboard')

    return render(request, 'tracker/add_entry.html', {'today_date': date.today()})


def delete_entry(request, entry_id):
    entry = get_object_or_404(Entry, id=entry_id)
    if request.method == "POST":
        entry.delete()
        return redirect('dashboard')  # or your main page url name
    # Optional: Render a confirmation page if GET request
    return render(request, 'tracker/confirm_delete.html', {'entry': entry})