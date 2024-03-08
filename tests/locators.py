class MainLocators:
    input_name_field = "//label[contains(text(),'Имя')]"  # локатор для имени
    input_email_field = "//label[contains(text(),'Email')]/../input"  # локатор для email
    input_password_field = "//label[contains(text(),'Пароль')]"  # локатор для пароля
    button_register = "//button[contains(text(),'Зарегистрироваться')]"  # локатор для кнопки "зарегистрироваться"
    wrong_pass_alert = "//p[contains(text(),'Некорректный пароль')]"  # локатор для алерта "некорректный пароль"
    button_login_mainpage = "//button[contains(text(),'Войти в аккаунт')]"  # локатор для кнопки "войти в аккаунт" на главной стр
    button_log_loginpage = "//button[contains(text(),'Войти')]"  # локатор для кнопки "войти" на стр /login
    button_blue_login = "//a[contains(text(),'Войти')]"  # Синяя кнопка войти
    button_pers_acc = "//p[contains(text(),'Личный Кабинет')]"  # кнопка "личный кабинет"
    button_constr = "//p[contains(text(),'Конструктор')]"  # кнопка конструктор
    button_exit = "//button[contains(text(),'Выход')]"  # кнопка выхода
    sauces_tab = "//span[contains(text(),'Соусы')]/parent::*"  # таб соусы
    bread_tab = "//span[contains(text(),'Булки')]/parent::*" # булки
    fillings_tab = "//span[contains(text(),'Начинки')]/parent::*" #начинки
