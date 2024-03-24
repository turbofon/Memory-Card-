from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (
        QApplication, QWidget, 
        QHBoxLayout, QVBoxLayout, 
        QGroupBox, QButtonGroup, QRadioButton,  
        QPushButton, QLabel)
from random import shuffle
import random


app = QApplication([])

win = QWidget()
win.setGeometry(0, 0, 600 , 400)
win.setStyleSheet("""QTabWidget::tab-bar {alignment: center;}
QTabBar::tab {padding-right: 7px; background: #35363a; color: white; border-radius: 5px; min-width: 100px; padding: 7px; margin: 5px 5px 5px 5px; border: 3px solid rgb(19, 200, 255);}
QTabBar::tab:selected {background: #4b4d53; color: white;}
QWidget{background-color: #262626; color: #F0F0F0;}
QLineEdit {color:white; background: #202124; border: 3px solid rgb(19, 200, 255); border-radius: 15px; padding: 5px;}
QPushButton { 
    border-radius: 10px;
    background-color: rgb(54, 54, 54);
    color: white;
    border: 3px solid rgb(19, 200, 255);
    padding: 4px;
}

QWidget {
    font-family: "Arials", "Arial", bold;
    font-size: 18px;
}

QPushButton:hover:pressed
{
    
    background-color: rgb(125, 125, 125);
}

QGroupBox{
    border: 3px solid white;
    border-radius: 10px;
}
""")

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

questions = [
    Question("Какой язык больше подходит для нейросетей?", "Python", "C#", "C++", "Rust"), 
    Question("Какой язык самый новый (языук должен быть уже использован программистами)?", "Rust", "Java", "Python", "Mojo"), 
    Question("Какой самый новый голосовой помошник?", "Yasha", "Stella", "Алиса", "Маруся"),
    Question("Самая популярная IDK для программирования?", "VS Code", "Visual Studio", "PyCharm", "Subline Text"),
    Question("Какой самый популярный браузер?", "Chrome", "Yandex", "Edge", "FireFox"),
    Question("Самый популярный Windows?", "Windows 10", "Windows 11", "Windows 7", "Windows 8.1"),
    Question("Самый популярный мессенджер?", "Whatsup", "Telegram", "VK", "SnapChat"),
    Question("Что такое API?", "Application Programming Interface", "Application Protocol Interface", "Application Processing Interface", "Application Program Interface"),
    Question("Что такое SQL?", "Structured Query Language", "Synchronized Query Language", "Structured Question Language", "Synchronized Question Language"),
    Question("Что такое URL?", "Uniform Resource Locator", "Universal Resource Locator", "Uniform Reference Locator", "Universal Reference Locator"),
    Question("Что такое рекурсия?", "Способ определения функции или алгоритма, в котором функция вызывает саму себя", "Способ определения класса, в котором класс наследует сам себя", "Способ определения переменной, в которой переменная принимает саму себя", "Способ определения цикла, в котором цикл выполняет сам себя"),
    Question("Что такое алгоритм сортировки?", "Алгоритм, который упорядочивает элементы в определенном порядке", "Алгоритм, который проверяет соблюдение правил форматирования кода", "Алгоритм, который определяет сложность работы программы", "Алгоритм, который определяет сложность алгоритма"),
    Question("Что такое алгоритм?", "Упорядоченная последовательность инструкций для решения определенной задачи", "Упорядоченный список данных", "Случайная последовательность инструкций", "Список инструкций без определенной последовательности"),
    Question("Чем отличается переменная типа int от переменной типа float?", "int представляет целое число, а float представляет число с плавающей запятой", "int представляет число с плавающей запятой, а float представляет целое число", "int и float - это одно и то же", "int и float не имеют отношения друг к другу"),
    Question("В чем разница между классом и объектом?", "Класс - это определение объекта, а объект - экземпляр этого класса", "Класс и объект - это одно и то же", "Объект - это определение класса, а класс - экземпляр этого объекта", "Класс и объект не имеют отношения друг к другу"),
    Question("Какое расширение имеют файлы с исходным кодом на языке C++?", ".cpp", ".java", ".py", ".html"),
    Question("Какая функция используется для вывода текста в языке программирования C++?", "cout", "print", "display", "output"),
    Question("В каком году был создан язык программирования Java?", "1995", "1985", "2005", "2000"),
    Question("Что такое асинхронность?", "Выполнение нескольких задач одновременно", "Выполнение каждой задачи последовательно", "Выполнение сложных математических операций", "Выполнение задачи только после выполнения другой"),
    Question("Что такое рефакторинг?", "Процесс изменения структуры программного кода без изменения его функциональности", "Процесс тестирования программного кода", "Процесс создания новых функций программы", "Процесс удаления ошибок из программного кода"),
    Question("Что такое HTTP?", "Протокол передачи гипертекста", "Способ хранения файлов на сервере", "Язык программирования для веб-разработки", "База данных для хранения информации в интернете")
]

old_question = None

def next_question():
    win.total += 1
    
    while True:
        rnd = random.randint(0, len(questions)-1)
        if questions[rnd].question != old_question:
            break
    ask(questions[rnd])

def click_ok():
    if btn_OK.text() == "Ответить":
        check_answer()
    else:
        next_question()

def show_result():
    group_box.hide()
    AnsGroupBox.show()
    btn_OK.setText("Следующий вопрос")
    
def show_question():
    group_box.show()
    AnsGroupBox.hide()
    btn_OK.setText("Ответить")
    
def start_test():
    txt = btn_OK.text()
    if txt == "Ответить":
        show_result()
    else:
        show_question()
        
def ask(q: Question):
    old_question = q.question
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    question.setText(q.question)
    lb_Correct.setText(q.right_answer) 
    show_question() 

    
def check_answer():
    if answers[0].isChecked():
        win.score += 1
        show_correct('Правильно!')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def show_correct(res):
    lb_Result.setText(res)
    lb_score.setText(f"Ваш рейтинг: {int(win.score / win.total * 100)}")
    show_result()


win.setWindowTitle("Memory Card")

question = QLabel("Есть вопросы пишите по адресу...")

btn_OK = QPushButton("Ответить")
btn_OK.clicked.connect(click_ok)

group_box = QGroupBox("Варианты ответов")

rb_1 = QRadioButton("Первый 1 ответа")
rb_2 = QRadioButton("Первый 2 ответа")
rb_3 = QRadioButton("Первый 3 ответа")
rb_4 = QRadioButton("Первый 4 ответа")

win.counter = -1
win.total = 0
win.score = 0

RadioGroup = QButtonGroup()

RadioGroup.addButton(rb_1)
RadioGroup.addButton(rb_2)
RadioGroup.addButton(rb_3)
RadioGroup.addButton(rb_4)

answers = [rb_1, rb_2, rb_3, rb_4]

# создаем лейауты
layout_ans1 = QHBoxLayout()  

layout_ans2 = QVBoxLayout() # вертикальные будут внутри горизонтального
layout_ans3 = QVBoxLayout()

# размещаем на вертикальных лэйаутах четыре кнопки с ответами
layout_ans2.addWidget(rb_1) # два ответа в первый столбец
layout_ans2.addWidget(rb_2)

layout_ans3.addWidget(rb_3) # два ответа во второй столбец
layout_ans3.addWidget(rb_4)

# размещаем на горизонтальном лэйауте два вертикальных
layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) # разместили столбцы в одной строке

# размещаем в группбокс горизонтальный лэйаут с вариантами ответов
group_box.setLayout(layout_ans1) # готова "панель" с вариантами ответов

AnsGroupBox = QGroupBox("Результат")
lb_Result = QLabel('прав ты или нет?') # здесь размещается надпись "правильно" или "неправильно"
lb_Correct = QLabel('ответ будет тут!') # здесь будет написан текст правильного ответа
lb_score = QLabel('Ваш рейтинг: ')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter, stretch=2)
layout_res.addWidget(lb_score, alignment=Qt.AlignHCenter, stretch=2)
AnsGroupBox.setLayout(layout_res)

# создаем основные лэйауты
layout_line1 = QHBoxLayout() # лэйаут для вопроса
layout_line2 = QHBoxLayout() # лэйаут для вариантов ответов или результат теста
layout_line3 = QHBoxLayout() # лэйаут для кнопки "Ответить"

# размещаем  на лэйаутах вопрос и группбокс с ответами
layout_line1.addWidget(question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(group_box)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()
# размещаем на лэйауте кнопку и ее форматируем
layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) # кнопка должна быть большой
layout_line3.addStretch(1)



# Теперь созданные строки разместим друг под другой:
# создаем основной вертикальный лэйаут
layout_card = QVBoxLayout()

# размещаем горизонтальные лэйауты с виджетами на основной и форматируем
layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) # пробелы между содержимым

# размещаем основной лэйаут в окне
win.setLayout(layout_card)
next_question()
# запускаем приложение
win.show()
app.exec_()