from django import forms
from .models import Orders, ContactMessage, Comment, Post

# class OrdersForm(forms.ModelForm):
#     class Meta:
#         model = Orders
#         fields = [
#             'pick_up_location', 'delivery_location', 'open_enclosed',
#             'make', 'model', 'year', 'name', 'email', 'phone_number', 'date','condition', 'operable'
#         ]
#
#         widgets = {
#             'pick_up_location': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Pick up ZIP or CITY',
#             }),
#             'delivery_location': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Delivery ZIP or CITY',
#             }),
#             'open_enclosed': forms.RadioSelect(),
#             'make': forms.TextInput(attrs={
#                     'class': 'form-control autocomplete-input',
#                     'placeholder': 'Choose make',
#                     'required': 'required'
#                 }),
#             'model': forms.TextInput(attrs={
#                 'class': 'form-control autocomplete-input',
#                 'placeholder': 'Choose model',
#                 'required': 'required'
#             }),
#             'year': forms.TextInput(attrs={
#                 'class': 'form-control autocomplete-input',
#                 'placeholder': 'Choose year',
#                 'required': 'required'
#             }),
#             'operable': forms.RadioSelect(),
#             'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full name'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
#             'phone_number': forms.TextInput(
#                 attrs={'class': 'form-control', 'placeholder': 'Phone number', 'id': 'phone_number'}),
#             'date': forms.DateInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter date',
#                 'type': 'date'
#             }),
#             'condition': forms.CheckboxInput(attrs={'class': 'form-form-check-input', 'id': 'condition'}),
#         }

from django import forms
from .models import Orders, Make, Model, Year


class OrdersForm(forms.Form):
    pick_up_location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Pick up ZIP or CITY'
        })
    )
    delivery_location = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Delivery ZIP or CITY'
        })
    )
    open_enclosed = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=Orders.TRANSPORT_TYPE_CHOICES
    )
    make = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control autocomplete-input',
            'placeholder': 'Choose make',
            'required': 'required'
        })
    )
    model = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control autocomplete-input',
            'placeholder': 'Choose model',
            'required': 'required'
        })
    )
    year = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control autocomplete-input',
            'placeholder': 'Choose year',
            'required': 'required'
        })
    )
    operable = forms.ChoiceField(
        widget=forms.RadioSelect(),
        choices=Orders.OPERABLE
    )
    name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Full name'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email'
        })
    )
    phone_number = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Phone number',
            'id': 'phone_number'
        })
    )
    date = forms.DateField(
        widget=forms.DateInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter date',
            'type': 'date'
        })
    )
    condition = forms.BooleanField(
        widget=forms.CheckboxInput(attrs={
            'class': 'form-check-input',
            'id': 'condition'
        }),
        required=False
    )

    def save(self, commit=True):
        # Get the cleaned data
        data = self.cleaned_data

        # Look up the related objects
        make = Make.objects.get(name=data['make'])
        model = Model.objects.get(name=data['model'], make=make)
        year = Year.objects.get(year=int(data['year']))

        # Create the Orders instance
        order = Orders(
            pick_up_location=data['pick_up_location'],
            delivery_location=data['delivery_location'],
            open_enclosed=data['open_enclosed'],
            operable=data['operable'],
            make=make,
            model=model,
            year=year,
            name=data['name'],
            email=data['email'],
            phone_number=data['phone_number'],
            date=data['date'],
            condition=data['condition']
        )

        if commit:
            order.save()

        return order


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone', 'message']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Email',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone',
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Leave us a message...',
                'rows': 4,
            }),
        }


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'publish', 'image', 'status']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the title here',
            }),
            'slug': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the slug here',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Enter the post content here',
            }),
            'publish': forms.DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'image': forms.FileInput(attrs={
                'class': 'form-control-file',
            }),
            'status': forms.Select(attrs={
                'class': 'form-control',
            }),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your email',
            }),
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your comment',
            }),
        }
