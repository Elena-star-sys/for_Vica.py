import time
from os import replace


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)


class Video:

    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration  # int(time.time(duration)) ?
        self.time_now = 0
        self.adult_mode = False



class UrTube:

    def __init__(self,users, videos, current_user):
        self.users = {}
        self.videos = []
        self.current_user = None


    def log_in(self, nickname, password):
        user =  self.users.get(nickname)
        password = self.users.get(hash(password))
        if user in self.users and password in self.log_in(password):
            self.current_user = user


    def register(self, nickname, password, age):
        if not nickname in self.users:
            nickname.add(self.users)
            if nickname in self.users:
                print(f'Пользователь {nickname} уже существует')

    def toggle_adult_mode(self):
        self.adult_mode = not self.adult_mode


    def log_out(self, nickname):
        if not nickname in self.users:
            current_user = None













ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')


















