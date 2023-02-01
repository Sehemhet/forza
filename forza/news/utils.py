# menu = [
#     {'name':'Добавить статью', 'url_name':'add_post'}
# ]
#
# class DataMixin:
#     def get_context_data(self, *, object_list=None, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['menu'] = menu
#         new_menu = menu.copy()
#         if not self.request.user.is_authenticated:
#             new_menu.pop(0)
#         context['menu'] = new_menu
#         return context