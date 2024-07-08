class User:
    count = 0
    def __init__(self, n, l, p):
        self.__name = n
        self.__login = l
        self.__password = p
        User.count += 1

    def get_name(self):
        return self.__name
    def set_name(self,v):
        self.__name = v

    name = property(get_name, set_name)

    def get_login(self):
        return self.__login

    def set_login(self, value):
        raise AttributeError('Нельзя менять значение')

    login = property(get_login, set_login)

    def get_password(self):
        return '******'

    def set_password(self, value):
        self.__password = value

    password = property(get_password, set_password)

    def show_info(self):
        print(f'Name: {self.__name}')
        print(f'Login: {self.__login}')
        print(f'User count: {self.count}')

class SuperUser(User):
    count = 0
    def __init__(self, n, l, p, r):
        super().__init__(n,l,p)
        self.__role = r
        SuperUser.count += 1
        User.count -= 1

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):
        super().show_info()
        print(f'Role: {self.__role}')


user1 = User('Paul McCar', 'paul', '1234')
user2 = User('George Harrison', 'george', '5678')
user3 = User('Richard Starkey', 'ringo', '0000')
admin = SuperUser('Johon Hjkls', 'john', '9999', 'admin')

print(f'Всего обычных юзеров {User.count}')
print(f'Всего супер юзеров {SuperUser.count}')
