from allClasses import Search
import MyToken
#  Данные аутентификации
login = 'SeVDy'
token = MyToken.get_token()

# Параметры запроса
url_srch = 'https://api.github.com/search/'
type_srch = ('code', 'repositories', 'users')
q = ('eval', 'sql', 'pickle')
user = ('DanteOnline', '')
language = ('python', 'django')

# Создаем объект класса Search
new_srch = Search()

# Задаем параметры аутентификации
new_srch.auth_param(login, token)

# Создаем запрос на сайт
for i in range(3):
    new_srch.get_data(url_srch, type_srch[0], q[i], language[0])
    # Фильтр
    new_srch.data_filter()

# Печатаем результат после фильтра в консоль
new_srch.print_data_with_filter()

# Сохраняем в файл json отфильтрованные данные
new_srch.save_at_file('file_warn.json')
