from django import forms

from board.models import Introduction, Comment


class IntroductionForm(forms.ModelForm):
    class Meta:
        model = Introduction
        fields = ['title','repository', 'version', 'contents', 'access']  # '__all__'
        widgets = {
            'title':forms.Textarea(attrs={'class': 'form-control', 'rows': 1}),
            'contents': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }

        labels = {
            'title': '  글 제목',
            'repository': '  주제   ',
            'version': '  글 번호',
            'contents': '  글 내용',
            'access': '  작성자',
        }

        class CommentForm(forms.ModelForm):
            class Meta:
                model = Comment
                fields = ['introduction', 'comment']  # '__all__'
                labels = {
                    'introduction': '  글 제목',
                    'comment': '  댓글   ',
                }