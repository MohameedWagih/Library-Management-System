from django.shortcuts import redirect, render, get_object_or_404
from .models import Book, Category 
from .forms import BookForm, CategoryForm
from django.contrib.auth.decorators import login_required


def index(request):
    if request.method == 'POST' and request.user.is_authenticated:      
        # Senior Note: بنعمل تحقق، لو الريكويست جاي من فورم إضافة الكتاب
        if 'add_book' in request.POST:
            add_book = BookForm(request.POST, request.FILES)
            if add_book.is_valid():
                add_book.save()
        
        # لو الريكويست جاي من فورم إضافة القسم
        elif 'add_category' in request.POST:
            add_category = CategoryForm(request.POST)
            if add_category.is_valid():
                add_category.save()

    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:  
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)
    
    context = {
        'books': search,
        'category': Category.objects.all(),
        'form': BookForm(),
        'catform': CategoryForm(),
        'allbooks': Book.objects.filter(active=True).count(),
        'books_available': Book.objects.filter(status='available').count(),
        'books_rented': Book.objects.filter(status='rented').count(),
        'books_sold': Book.objects.filter(status='sold').count(),
        'search_keyword': title,
    }
    return render(request, 'pages/index.html', context)


def books(request):
    search = Book.objects.all()
    title = None
    if 'search_name' in request.GET:  
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    # ==== الإضافة الجديدة (لو اليوزر داس إضافة كتاب من الصفحة دي) ====
    if request.method == 'POST':
        if 'add_book' in request.POST:
            add_book = BookForm(request.POST, request.FILES)
            if add_book.is_valid():
                add_book.save()
    # ================================================================

    context = {
            'books': search,
            'category': Category.objects.all(),
            'catform': CategoryForm(),
            'form': BookForm(),
            'search_keyword': title, # <-- الإضافة الجديدة (بعتنا كلمة البحث للصفحة)
        }
    return render(request, 'pages/books.html', context)


@login_required
def update(request , id):
    # عشان لو حد كتب ID مش موجود في اللينك، نطلعله صفحة 404 شيك بدل ما السيرفر يضرب
    book_id = get_object_or_404(Book, id=id) 
    
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)
    
    context={'form':book_save}
    return render(request, 'pages/update.html', context)


@login_required
def delete(request, id):
    book_delete = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')
# Create your views here.
