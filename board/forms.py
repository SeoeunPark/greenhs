from django import forms

from board.models import Introduction


class IntroductionForm(forms.ModelForm):
    class Meta:
        model = Introduction
        fields = ['repository', 'version', 'contents', 'access']  # '__all__'
        labels = {
            'repository' : '주제',
            'version' : '글 번호',
            'contents': '글내용',
            'access': '작성자',
        }
