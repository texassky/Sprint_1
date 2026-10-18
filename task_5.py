class TestCase:

    # В конструкторе инициализируем поля steps и result
    def __init__(self, steps = {}, result = None):
        self.steps = steps
        self.result = result

    # метод для добавления в словарь steps шагов тест-кейса
    def set_step(self, step_number, step_text):
        self.steps[step_number] = step_text

    # метод для удаления шагов из словаря steps по переданному ключу
    def delete_step(self, step_number):
        del self.steps[step_number]

    # метод для добавления ожидаемого результата
    def set_result(self, result):
        self.result = result

    # метод для вывода информации о составе тест-кейса в заданном формате
    def get_test_case(self): 
        case_to_view = {} 
        case_to_view['Шаги'] = self.steps
        case_to_view['Ожидаемый результат'] = self.result
        print(case_to_view)
        
test_case_1 = TestCase()
test_case_1.set_step(1, 'Перейти на сайт')
test_case_1.set_step(3, 'Перейти в раздел Товары')
test_case_1.delete_step(3)
test_case_1.set_step(2, 'Перейти в раздел Товары')
test_case_1.set_step(3, 'Нажать кнопку «В корзину» у первого товара')
test_case_1.set_result('Товар окажется в корзине')
test_case_1.get_test_case()

test_case_2 = TestCase()
test_case_2.set_step(1, 'Перейти на сайт')
test_case_2.set_step(2, 'Перейти в раздел Корзина')
test_case_2.set_step(3, 'Нажать кнопку "Удалить"')
test_case_2.set_result('Товар удален из корзины')
test_case_2.get_test_case()