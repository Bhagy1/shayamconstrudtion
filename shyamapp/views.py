from django.shortcuts import render, redirect
from .forms import CustomerReviewForm
from .models import CustomerReview

def home(request):
    reviews = CustomerReview.objects.order_by('-created_at')[:10]  # show latest 10
    form = CustomerReviewForm()

    if request.method == 'POST':
        form = CustomerReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'shyamapp/home.html', {'form': form, 'reviews': reviews})
