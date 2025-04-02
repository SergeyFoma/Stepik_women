from women.utils import menu2
#для общих данных. Для частных нельзя
def get_women_context(request):
    return {'mainmenu':menu2}