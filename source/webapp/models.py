from django.db import models


class Poll(models.Model):
    question = models.TextField(max_length=300, null=True, blank=True, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return self.question

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Choice(models.Model):
    choice_text = models.TextField(max_length=300, null=True, blank=True, verbose_name='Вариант ответа')
    poll = models.ForeignKey('webapp.Poll', related_name='choices', on_delete=models.CASCADE,
                             verbose_name='Вопрос')

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант ответа'
        verbose_name_plural = 'Варианты ответа'
