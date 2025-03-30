menu2=[
    {'title':'о сайте', 'url_name':'women:about'},
    {'title':'Добавить статью', 'url_name':'women:addpage'},
    {'title':'Обратная связь', 'url_name':'women:contact'},
    {'title':'Войти', 'url_name':'women:login'},
    
]

class DataMixin:
    title_page=None
    cat_selected=None
    extra_context={}

    def __init__(self):
        if self.title_page:
            self.extra_context['title']=self.title_page

        if self.cat_selected is not None:
            self.extra_context['cat_selected']=self.cat_selected

        if 'menu2' not in self.extra_context:
            self.extra_context['menu2']=menu2

    def get_mixin_context(self, context, **kwargs):
        context['menu2']=menu2
        context['cat_selected']=None
        context.update(kwargs)
        return context