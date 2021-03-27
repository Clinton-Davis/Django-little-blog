from django import forms
from .models import Blog, BlogComment, Category


choices = Category.objects.all().values_list('name', 'name')
choices_list = []

for item in choices:
    choices_list.append(item)


class BlogForm(forms.ModelForm):
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(), empty_label='Select the category')

    class Meta:
        model = Blog
        fields = ('title', 'category', 'content', 'thumbnail',)

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

        placeholders = {
            'title': 'Your Blogs Title, 50 Characters max',
            'content': 'Write your Blog in here',
            'thumbnail': '830x450px',

        }

        self.fields['title'].widget.attrs['autofocus'] = True
        self.fields['category'].widget.attrs['choices'] = choices_list

        for field in self.fields:
            if field != 'category':
                placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'mont_r'
            self.fields[field].label = False


class BlogCommentForm(forms.ModelForm):
    content = forms.CharField(required=True, widget=forms.Textarea(attrs={
        'rows': 4,
    }), label="")

    class Meta:
        model = BlogComment
        fields = ('content', )