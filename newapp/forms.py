from django import forms
from .models import MinistriesModel,Daily_Mass,Special_Masses,Obituary_Model,Blog_News_Model,Contact_Model,Event_Details_Model,GalleryModel,Category,Gallery,UserRegisterModel,UserLoginModel,St_Vincent_Association,Stars_Pithruvedi_Association,Mathrujyothi_Association,Styf_Association,Auditorium_Booking,News_Category,News_Updates


# class Event_Form(forms.ModelForm):
#     cost = forms.CharField(max_length=10, required=False)
#     email = forms.EmailField(required=False)
#     phone = forms.IntegerField(required=False)
    
#     class Meta:
#         model = Event_Details
#         fields =  '__all__'

class Event_Form(forms.ModelForm):
    class Meta:
        model = Event_Details_Model
        fields =  '__all__'

class MinistriesForm(forms.ModelForm):
    class Meta:
        model = MinistriesModel
        fields = '__all__'


class Daily_Mass_Form(forms.ModelForm):
    class Meta:
        model = Daily_Mass
        fields = '__all__'

class Special_Masses_Form(forms.ModelForm):
    class Meta:
        model = Special_Masses
        fields = '__all__'

class Obituary_Form(forms.ModelForm):
    class Meta:
        model = Obituary_Model
        fields = '__all__'




class Blog_News_Form(forms.ModelForm):
    class Meta:
        model = Blog_News_Model
        fields = '__all__'



class Contact_Form(forms.ModelForm):
    class Meta:
        model = Contact_Model
        fields = '__all__'



class Gallery_Form(forms.ModelForm):
    class Meta:
        model = GalleryModel
        fields = ['gallery_name', 'image']


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name','image','status']



class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['category','name','gallery_image','status']

class News_Ctegory_Form(forms.ModelForm):
    class Meta:
        model = News_Category
        fields = ['image','news_heading','date','status']

class News_Updates_Form(forms.ModelForm):
    class Meta:
        model = News_Updates
        fields = ['news_category','main_image','image','description','status']


class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = UserRegisterModel
        fields = '__all__'

class UserLoginForm(forms.ModelForm):
    class Meta:
        model = UserLoginModel
        fields = '__all__'
        

class St_Vincent_Association_Form(forms.ModelForm):
    class Meta:
        model = St_Vincent_Association
        fields = '__all__'

class Stars_Pithruvedi_Form(forms.ModelForm):
    class Meta:
        model = Stars_Pithruvedi_Association
        fields = '__all__'

class Mathrujyothi_Association_Form(forms.ModelForm):
    class Meta:
        model = Mathrujyothi_Association
        fields = '__all__'

class Styf_Association_Form(forms.ModelForm):
    class Meta:
        model = Styf_Association
        fields = '__all__'

class Auditorium_Booking_Form(forms.ModelForm):
    class Meta:
        model = Auditorium_Booking
        fields = '__all__'