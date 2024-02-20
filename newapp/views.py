from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import MinistriesModel, Daily_Mass, Special_Masses,Obituary_Model, Blog_News_Model, Contact_Model,UploadedImage,Event_Details_Model,GalleryModel,Category,Gallery,UserRegisterModel,UserLoginModel,St_Vincent_Association,Stars_Pithruvedi_Association,Mathrujyothi_Association,Styf_Association,Auditorium_Booking
from .forms import  MinistriesForm, Daily_Mass_Form, Special_Masses_Form,Obituary_Form, Blog_News_Form, Contact_Form,Event_Form,Gallery_Form,CategoryForm,GalleryForm,UserRegisterForm,UserLoginForm,St_Vincent_Association_Form,Stars_Pithruvedi_Form,Mathrujyothi_Association_Form,Styf_Association_Form,Auditorium_Booking_Form
from django.shortcuts import get_object_or_404

from datetime import date
from django.utils import timezone


import os


# Create your views here.

def index(request):
    # active_events = Event_Details_Model.objects.filter(end_date__gte=timezone.now())
    active_events = Event_Details_Model.objects.filter(notification_end_date__gte=timezone.now())
    # events = Event_Details.objects.all()
    category = Category.objects.filter(status=0) 
    ministries = MinistriesModel.objects.all()
    blog = Blog_News_Model.objects.all()
    return render(request, 'index.html',{'active_events':active_events,'ministries': ministries, 'blog': blog,'category':category})


def about(request):
    return render(request, 'about-us.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin_dashboard')
        else:
            messages.success(request, ("There Was An Error Loging In, Try Again..."))
            return redirect('login')
    return render(request, 'authenticate/login.html')


def admin_dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'admin-dashboard.html')
    else:
        return redirect('login_user')


def logout_user(request):
    logout(request)
    messages.success(request, ("You Were Logged Out"))
    return redirect('index')


def bishop_message(request):
    return render(request, 'bishop-message.html')


def vicar_message(request):
    return render(request, 'vicar-message.html')


def image_shadow(request):
    return render(request, 'image-shadow.html')


def january(request):
    return render(request, 'months/january.html')


def february(request):
    return render(request, 'months/2feb.html')


def march(request):
    return render(request, 'months/march.html')


def april(request):
    return render(request, 'months/april.html')


def may(request):
    return render(request, 'months/may.html')


def june(request):
    return render(request, 'months/june.html')


def july(request):
    return render(request, 'months/july.html')


def auguest(request):
    return render(request, 'months/auguest.html')


def september(request):
    return render(request, 'months/september.html')


def october(request):
    return render(request, 'months/october.html')


def november(request):
    return render(request, 'months/november.html')


def december(request):
    return render(request, 'months/december.html')

@login_required(login_url='login_user')
def admin_add_events(request):
    if request.method == 'POST':
        form = Event_Form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('admin_event_view')  # Redirect to a page showing all products
    else:
        form = Event_Form()

    return render(request, 'admin_add_events.html', {'form': form})

@login_required(login_url='login_user')
def admin_event_view(request):
    events = Event_Details_Model.non_deleted_objects.all()
    return render(request, 'admin_event_view.html', {'events': events})

@login_required(login_url='login_user')
def admin_update_events(request, id):
    events = get_object_or_404(Event_Details_Model, id=id)
    if request.method == 'POST':
        form = Event_Form(request.POST, instance=events)
        if form.is_valid():
            form.save()
            return redirect('admin_event_view')
    else:
        form = Event_Form(instance=events)
    return render(request, 'admin_update_events.html', {'form': form, 'events': events})


@login_required(login_url='login_user')
def admin_delete_events(request, id):
    events = Event_Details_Model.objects.get(id=id)
    events.is_deleted = True
    events.soft_delete()
    return redirect('admin_event_view')

@login_required(login_url='login_user')
def Event_Details(request, event_name):
    events = Event_Details_Model.objects.get(event_name=event_name)
    return render(request, 'event-details.html', {'events': events})

@login_required(login_url='login_user')
def admin_add_ministries(request):
    if request.method == 'POST':
        ministries = MinistriesForm(request.POST, request.FILES)
        if ministries.is_valid():
            ministries.save()
            return HttpResponseRedirect('admin_ministries_view')  # Redirect to a page showing all products
    else:
        ministries = MinistriesForm()

    return render(request, 'admin_add_ministries.html', {'ministries': ministries})

@login_required(login_url='login_user')
def admin_ministries_view(request):
    view = MinistriesModel.objects.all()
    return render(request, 'admin_ministries_view.html', {'view': view})

@login_required(login_url='login_user')
def admin_update_ministries(request, id):
    ministries = get_object_or_404(MinistriesModel, id=id)

    if request.method == 'POST':
        form = MinistriesForm(request.POST, instance=ministries)
        if form.is_valid():
            form.save()
            return redirect('admin_ministries_view')
    else:
        form = MinistriesForm(instance=ministries)

    return render(request, 'admin_update_ministries.html', {'form': form, 'ministries': ministries})

@login_required(login_url='login_user')
def admin_delete_ministries(request, id):
    ministries = MinistriesModel.objects.get(id=id)
    ministries.delete()
    return redirect('admin_ministries_view')

@login_required(login_url='login_user')
def admin_add_mass_times(request):
    if request.method == 'POST':
        mass_days = request.POST['mass_days']
        mass_date = request.POST['mass_date']
        mass_time = request.POST['mass_time']
        end_time = request.POST['end_time']
        mass_description = request.POST['mass_description']
        data = Daily_Mass(mass_days=mass_days, mass_date=mass_date, mass_time=mass_time, end_time=end_time,
                          mass_description=mass_description)
        data.save()
        return HttpResponseRedirect('admin_daily_mass_view')
    return render(request, 'admin_add_mass_times.html')

@login_required(login_url='login_user')
def admin_daily_mass_view(request):
    mass_times = Daily_Mass.non_deleted_objects.all()
    return render(request, 'admin_daily_mass_view.html', {'mass_times': mass_times})

@login_required(login_url='login_user')
def admin_update_mass_times(request, id):
    mass_time = get_object_or_404(Daily_Mass, id=id)
    if request.method == 'POST':
        form = Daily_Mass_Form(request.POST, instance=mass_time)
        if form.is_valid():
            form.save()
            return redirect('admin_daily_mass_view')
    else:
        form = Daily_Mass_Form(instance=mass_time)
    return render(request, 'admin_update_mass_times.html', {'form': form, 'mass_time': mass_time})

@login_required(login_url='login_user')
def admin_delete_mass_times(request, id):
    mass_times = Daily_Mass.objects.get(id=id)
    mass_times.soft_delete()
    return redirect('admin_daily_mass_view')

@login_required(login_url='login_user')
def admin_add_special_masses(request):
    if request.method == 'POST':
        event_name = request.POST['event_name']
        date = request.POST['date']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        description = request.POST['description']
        data = Special_Masses(event_name=event_name, date=date, start_time=start_time, end_time=end_time,
                              description=description)
        data.save()
        return HttpResponseRedirect('admin_special_mass_view')
    return render(request, 'admin_add_special_masses.html')

@login_required(login_url='login_user')
def admin_special_mass_view(request):
    special_mass = Special_Masses.objects.all()
    return render(request, 'admin_special_mass_view.html', {'special_mass': special_mass})

@login_required(login_url='login_user')
def admin_update_special_mass(request, id):
    data = get_object_or_404(Special_Masses, id=id)

    if request.method == 'POST':
        special_mass = Special_Masses_Form(request.POST, request.FILES, instance=data)
        if special_mass.is_valid():
            special_mass.save()
            return redirect('admin_special_mass_view')
    return render(request, 'admin_update_special_mass.html', {'special_mass': special_mass})

@login_required(login_url='login_user')
def admin_update_special_mass(request, id):
    special_mass = get_object_or_404(Special_Masses, id=id)
    if request.method == 'POST':
        form = Special_Masses_Form(request.POST, instance=special_mass)
        if form.is_valid():
            form.save()
            return redirect('admin_special_mass_view')
    else:
        form = Special_Masses_Form(instance=special_mass)
    return render(request, 'admin_update_special_mass.html', {'form': form, 'special_mass': special_mass})

@login_required(login_url='login_user')
def admin_delete_special_mass(request, id):
    special_mass = Special_Masses.objects.get(id=id)
    special_mass.delete()
    return redirect('admin_special_mass_view')


def mass_times(request):
    # daily_mass = timezone.now().date() + timedelta(days=1)
    # Daily_Mass.objects.filter(end_time__date=daily_mass).delete()
    daily_mass = Daily_Mass.objects.all()
    special_mass = Special_Masses.objects.all()
    return render(request, 'masses.html', {'daily_mass': daily_mass, 'special_mass': special_mass})


def obituary(request):
    obituary = Obituary_Model.objects.all()
    return render(request, 'obituary.html', {'obituary': obituary})

@login_required(login_url='login_user')
def admin_add_obituary(request):
    if request.method == 'POST':
        obituary = Obituary_Form(request.POST, request.FILES)
        if obituary.is_valid():
            obituary.save()
            return HttpResponseRedirect('admin_obituary_view')  # Redirect to a page showing all products
    else:
        obituary = Obituary_Form()

    return render(request, 'admin_add_obituary.html', {'obituary': obituary})

@login_required(login_url='login_user')
def admin_obituary_view(request):
    obituary = Obituary_Model.objects.all()
    return render(request, 'admin_obituary_view.html', {'obituary': obituary})

@login_required(login_url='login_user')
def admin_update_obituary(request, id):
    data = Obituary_Model.objects.get(id=id)
    obituary = Obituary_Form(instance=data)
    if request.method == 'POST':
        obituary = Obituary_Form(request.POST, request.FILES, instance=data)
        if obituary.is_valid():
            obituary.save()
            return redirect('admin_obituary_view')
    return render(request, 'admin_update_obituary.html', {'obituary': obituary})

@login_required(login_url='login_user')
def admin_delete_obituary(request, id):
    obituary = Obituary_Model.objects.get(id=id)
    obituary.delete()
    return redirect('admin_obituary_view')

@login_required(login_url='login_user')
def update_upload_image(request,category):
    images = get_object_or_404(UploadedImage, category=category)
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, instance=images)
        if form.is_valid():
            form.save()
            return redirect('upload_image_view')
    else:
        form = ImageUploadForm(instance=images)
    return render(request, 'update_upload_image.html', {'form': form, 'images': images})

@login_required(login_url='login_user')
def admin_add_blog(request):
    if request.method == 'POST':
        blog = Blog_News_Form(request.POST, request.FILES)
        if blog.is_valid():
            blog.save()
            return HttpResponseRedirect('admin_blog_view')  # Redirect to a page showing all products
    else:
        blog = Blog_News_Form()

    return render(request, 'admin_add_blog.html', {'blog': blog})

@login_required(login_url='login_user')
def admin_blog_view(request):
    blog = Blog_News_Model.objects.all()
    return render(request, 'admin_blog_view.html', {'blog': blog})

@login_required(login_url='login_user')
def admin_update_blog(request, id):
    data = Blog_News_Model.objects.get(id=id)
    blog = Blog_News_Form(instance=data)
    if request.method == 'POST':
        blog = Blog_News_Form(request.POST, request.FILES, instance=data)
        if blog.is_valid():
            blog.save()
            return redirect('admin_blog_view')
    return render(request, 'admin_update_blog.html', {'blog': blog})

@login_required(login_url='login_user')
def admin_delete_blog(request, id):
    blog = Blog_News_Model.objects.get(id=id)
    blog.delete()
    return redirect('admin_blog_view')


def blog_single(request):
    return render(request, 'blog-single.html')


def admin_base(request):
    return render(request, 'admin-base.html')


def blog(request):
    blog = Blog_News_Model.objects.all()
    return render(request, 'blog.html', {'blog': blog})


def test(request):
    return render(request, 'admin-dashboard.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        Phone = request.POST['Phone']
        address = request.POST['address']
        pincode = request.POST['pincode']
        message = request.POST['message']
        data = Contact_Model(name=name, email=email, Phone=Phone, address=address, pincode=pincode, message=message)
        data.save()
        return HttpResponseRedirect('contact')
    return render(request, 'contact.html')

@login_required(login_url='login_user')
def admin_contact_view(request):
    contact = Contact_Model.objects.all()
    return render(request, 'admin_contact_view.html', {'contact': contact})

@login_required(login_url='login_user')
def admin_delete_contacts(request, id):
    contact = Contact_Model.objects.get(id=id)
    contact.delete()
    return redirect('admin_contact_view')

def gallery(request):
    gallery = GalleryModel.objects.all()
    return render(request,'gallery.html',{'gallery': gallery})

@login_required(login_url='login_user')
def admin_add_gallery(request):
    if request.method == 'POST':
        gallery = Gallery_Form(request.POST, request.FILES)
        if gallery.is_valid():
            gallery.save()
            return HttpResponseRedirect('admin_gallery_view')  
    else:
        gallery = Gallery_Form()
    return render(request, 'admin_add_gallery.html', {'gallery': gallery})

@login_required(login_url='login_user')
def admin_gallery_view(request):
    images = GalleryModel.objects.all()
    return render(request,'admin_gallery_view.html',{'images':images})

@login_required(login_url='login_user')
def admin_update_gallery(request, gallery_name):
    gallery = get_object_or_404(GalleryModel, gallery_name=gallery_name)
    if request.method == 'POST':
        form = Gallery_Form(request.POST, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('admin_gallery_view')
    else:
        form = Gallery_Form(instance=gallery)
    return render(request, 'admin_update_gallery.html', {'form': form, 'gallery': gallery})

@login_required(login_url='login_user')
def admin_delete_gallery(request, id):
    gallery = GalleryModel.objects.get(id=id)
    gallery.delete()
    return redirect('admin_gallery_view')


def gallery_details(request,name):
    if(Category.objects.filter(name=name, status=0)):
        gallery = Gallery.objects.filter(category__name=name)
        category_name = Category.objects.filter(name=name).first()
        context = {'gallery': gallery,'category_name':category_name}
        return render(request,"gallery_detail.html",context)
    else:
        messages.warning(request,"No such category found")
        return redirect("collections")

    
@login_required(login_url='login_user')
def admin_add_category(request):
    if request.method == 'POST':
        category = CategoryForm(request.POST, request.FILES)
        if category.is_valid():
            category.save()
            return HttpResponseRedirect('admin_add_main_gallery')  
    else:
        category = CategoryForm()
    return render(request, 'admin_add_category.html', {'category': category})

@login_required(login_url='login_user')
def admin_category_view(request):
    category = Category.objects.all()
    return render(request,'admin_category_view.html',{'category':category})

@login_required(login_url='login_user')
def admin_update_category(request, name):
    gallery = get_object_or_404(Category, name=name)
    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('admin_category_view')
    else:
        form = CategoryForm(instance=gallery)
    return render(request, 'admin_update_category.html', {'form': form,'gallery': gallery})

@login_required(login_url='login_user')
def admin_delete_category(request, id):
    gallery = Category.objects.get(id=id)
    gallery.delete()
    return redirect('admin_category_view')

def admin_news_category(request):
    if request.method == 'POST':
        category = News_Ctegory_Form(request.POST, request.FILES)
        if category.is_valid():
            category.save()
            return HttpResponse('admin_add_main_gallery')  
    else:
        category = News_Ctegory_Form()
    return render(request, 'admin_news_category.html', {'category': category})

def admin_news_category_view(request):
    news_category = News_Category.objects.all()
    return render(request,'admin_news_category_view.html',{'news_category':news_category})

@login_required(login_url='login_user')
def admin_add_main_gallery(request):
    if request.method == 'POST':
        gallery = GalleryForm(request.POST, request.FILES)
        if gallery.is_valid():
            gallery.save()
            return HttpResponseRedirect('admin_main_gallery_view')  
    else:
        gallery = GalleryForm()

    categories = Category.objects.all() 
    return render(request, 'add_main_gallery.html', {'gallery': gallery,'categories':categories})

@login_required(login_url='login_user')
def admin_main_gallery_view(request):
    gallery = Gallery.objects.all()
    return render(request,'admin_main_gallery_view.html',{'gallery':gallery})

@login_required(login_url='login_user')
def admin_update_main_gallery(request, id):
    gallery = get_object_or_404(Gallery, id=id)
    if request.method == 'POST':
        form = GalleryForm(request.POST, instance=gallery)
        if form.is_valid():
            form.save()
            return redirect('admin_main_gallery_view')
    else:
        form = GalleryForm(instance=gallery)
    return render(request, 'admin_update_main_gallery.html', {'form': form,'gallery': gallery})

# <----------------- FORANE ---------------->
def parishes(request):
    return render(request,'forane/parishes.html')

def eucharistic(request):
    return render(request,'forane/eucharistic.html')

# <------------------ PARISH ----------------->

def administration(request):
    return render(request,'parish/administrations.html')

def former_vicar(request):
    return render(request,'parish/former_vicar.html')

def former_asst_vicar(request):
    return render(request,'parish/former_asst_vicar.html')

def former_trustees(request):
    return render(request,'parish/former_trustees.html')

def institution(request):
    return render(request,'parish/institution.html')

def wards(request):
    return render(request,'parish/wards.html')

# <---------------ASSOCIATIONS--------------->

def st_vincent_de_paul_society(request):
    return render(request,'associations/st_vincent_de_paul_society.html')

def st_vincent_association(request):
    if request.method == 'POST':
        details = St_Vincent_Association_Form(request.POST, request.FILES)
        if details.is_valid():
            details.save()
            return HttpResponseRedirect('st_vincent_association_view')  
    else:
        details = St_Vincent_Association_Form()
    return render(request, 'St_Vincent_Association/St_vincent_association.html', {'details': details})


def st_vincent_association_view(request):
    data = St_Vincent_Association.objects.all()
    return render(request,'St_Vincent_Association/st_vincent_association_view.html',{'data':data})


def st_vincent_association_updation(request,id):
    details = get_object_or_404(St_Vincent_Association, id=id)
    if request.method == 'POST':
        form = St_Vincent_Association_Form(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('st_vincent_association_view')
    else:
        form = St_Vincent_Association_Form(instance=details)
    return render(request, 'St_Vincent_Association/st_vincent_association_updation.html', {'form': form,'details': details})

def st_vincent_association_delete(request, id):
    details = St_Vincent_Association.objects.get(id=id)
    details.delete()
    return redirect('st_vincent_association_view')


def stars_pithruvedi(request):
    return render(request,'associations/stars_pithruvedi.html')

def stars_pithruvedi_association(request):
    if request.method == 'POST':
        details = Stars_Pithruvedi_Form(request.POST, request.FILES)
        if details.is_valid():
            details.save()
            return HttpResponseRedirect('stars_pithruvedi_view')  
    else:
        details = Stars_Pithruvedi_Form()
    return render(request, 'Stars_Pithruvedi_Association/stars_pithruvedi_association.html', {'details': details})

def stars_pithruvedi_view(request):
    data = Stars_Pithruvedi_Association.objects.all()
    return render(request,'Stars_Pithruvedi_Association/stars_pithruvedi_view.html',{'data':data})

def stars_pithruvedi_updation(request,id):
    details = get_object_or_404(Stars_Pithruvedi_Association, id=id)
    if request.method == 'POST':
        form = Stars_Pithruvedi_Form(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('stars_pithruvedi_view')
    else:
        form = Stars_Pithruvedi_Form(instance=details)
    return render(request, 'Stars_Pithruvedi_Association/stars_pithruvedi_updation.html', {'form': form,'details': details})

def stars_pithruvedi_delete(request, id):
    details = Stars_Pithruvedi_Association.objects.get(id=id)
    details.delete()
    return redirect('stars_pithruvedi_view')


def mathru_jyothi(request):
    return render(request,'associations/mathru_jyothi.html')

def mathru_jyothi_association(request):
    if request.method == 'POST':
        details = Mathrujyothi_Association_Form(request.POST, request.FILES)
        if details.is_valid():
            details.save()
            return HttpResponseRedirect('mathru_jyothi_view')  
    else:
        details = Mathrujyothi_Association_Form()
    return render(request, 'Mathru_Jyothi_Association/mathru_jyothi_association.html', {'details': details})

def mathru_jyothi_view(request):
    data = Mathrujyothi_Association.objects.all()
    return render(request,'Mathru_Jyothi_Association/mathru_jyothi_view.html',{'data':data})

def mathru_jyothi_updation(request,id):
    details = get_object_or_404(Mathrujyothi_Association, id=id)
    if request.method == 'POST':
        form = Mathrujyothi_Association_Form(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('mathru_jyothi_view')
    else:
        form = Mathrujyothi_Association_Form(instance=details)
    return render(request, 'Mathru_Jyothi_Association/mathru_jyothi_updation.html', {'form': form,'details': details})

def mathru_jyothi_delete(request, id):
    details = Mathrujyothi_Association.objects.get(id=id)
    details.delete()
    return redirect('mathru_jyothi_view')

def styf(request):
    return render(request, 'associations/styf.html')


def styf_association(request):
    if request.method == 'POST':
        details = Styf_Association_Form(request.POST, request.FILES)
        if details.is_valid():
            details.save()
            return HttpResponseRedirect('styf_association_view')  
    else:
        details = Styf_Association_Form()
    return render(request, 'Styf_Association/styf_association.html', {'details': details})


def styf_association_view(request):
    data = Styf_Association.non_deleted_objects.all()
    return render(request,'Styf_Association/styf_association_view.html', {'data':data})

def styf_association_updation(request,id):
    details = get_object_or_404(Styf_Association, id=id)
    if request.method == 'POST':
        form = Styf_Association_Form(request.POST, instance=details)
        if form.is_valid():
            form.save()
            return redirect('styf_association_view')
    else:
        form = Styf_Association_Form(instance=details)
    return render(request, 'Styf_Association/styf_association_updation.html', {'form': form,'details': details})

def styf_association_delete(request, id):
    details = Styf_Association.objects.get(id=id)
    details.soft_delete()
    return redirect('styf_association_view')

def user_home(request):
    return render(request,'user/home.html')

def st_vincent_home(request):
    return render(request,'user/st_vincent_home.html')

def stars_pithrivedhi_home(request):
    return render(request,'user/starts_pithrivedhi_home.html')

def mathru_jyothi_home(request):
    return render(request,'user/mathru_jyothi_home.html')

def styf_home(request):
    return render(request,'user/styf_home.html')

def altar_servents_home(request):
    return render(request,'user/altar_servents_home.html')

def bible_readers_home(request):
    return render(request,'userbible_readers_home.html')

def choir_home(request):
    return render(request,'user/choir_home.html')

def CML_home(request):
    return render(request,'user/CML_home.html')

def holy_childhood_home(request):
    return render(request,'user/holy_childhood_home.html')

# --------------------------- #

def catechism(request):
    return render(request,'catechism.html')
# -----------------------------------------------

def error(request):
    return render(request,'error-404.html')


def UserRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        privilege = request.POST['privilege']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            b = UserRegisterModel(username=username, privilege=privilege, firstname=firstname,
                                  lastname=lastname, email=email, phone=phone,password=password, confirmpassword=confirmpassword)
            b.save()
            return redirect('UserLogin')
        else:
            return HttpResponse("Incorrect Password!")
    return render(request, 'User/signup.html')

def admin_registration_view(request):
    register = UserRegisterModel.non_deleted_objects.all()
    return render(request,'admin_registration_view.html',{'register':register})

def admin_registration_delete(request,id):
    register = UserRegisterModel.objects.get(id=id)
    register.soft_delete()
    return redirect('admin_registration_view')


def UserLogin(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form['username'].value()
            password = form['password'].value()
            try:
                request.session['username']=username
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='St.VincentDePaulSociety')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/st_vincent_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='StarsPithruvedi')
                if user is not None:
                    cid=user.id
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/starts_pithrivedhi_home.html', {'username':username, 'cid':cid})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='MathruJyothi')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/mathru_jyothi_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='STYF')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/styf_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='AltarServants')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/altar_servents_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='BibleReadersForum')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/userbible_readers_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='Choir')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/choir_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='CML')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/CML_home.html', {'username':username})
            except:
                pass

            try:
                user = UserRegisterModel.objects.get(username=username, password=password, privilege='HolyChildhood')
                if user is not None:
                    username=request.session['username']
                    messages.info(request, f"You are now logged in as {username}.")
                    return render(request, 'user/holy_childhood_home.html', {'username':username})
            except:
                pass
        else:
            return HttpResponse('Login Failed')
    return render(request, 'User/login.html')

def auditorium_booking(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        booking = Auditorium_Booking(name=name, email=email, phone=phone,start_date=start_date,end_date=end_date)
        booking.save()
        return HttpResponseRedirect('auditorium_booking')
    return render(request, 'auditorium_booking.html')

@login_required(login_url='login_user')
def admin_booking_view(request):
    booking = Auditorium_Booking.non_deleted_objects.all()
    return render(request,'admin_booking_view.html',{'booking':booking})

@login_required(login_url='login_user')
def admin_delete_booking(request,id):
    booking = Auditorium_Booking.objects.get(id=id)
    booking.soft_delete()
    return redirect('admin_booking_view')

def blog_single(request):
    return render(request,'blog-single.html')

# def admin_st_vincent_association_view(request):
#     data = St_Vincent_Association.objects.all()
#     return render(request,'admin_st_vincent_association_view.html',{'data':data})

# def admin_stars_pithruvedi_view(request):
#     data = Stars_Pithruvedi_Association.objects.all()
#     return render(request,'admin_stars_pithruvedi_view.html',{'data':data})

# def admin_mathru_jyothi_view(request):
#     data = Mathrujyothi_Association.objects.all()
#     return render(request,'admin_mathru_jyothi_view.html',{'data':data})

# def admin_styf_association_view(request):
#     data = Styf_Association.non_deleted_objects.all()
#     return render(request,'admin_styf_association_view.html', {'data':data})

