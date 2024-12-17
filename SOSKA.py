import sys, PyQt5, random
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from SOSKA_main_window_ui import Ui_MainWindow

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        # Инициализация окна
        super(MainWindow, self).__init__()
        self.MainWinUi = Ui_MainWindow()
        self.MainWinUi.setupUi(self)
        self.setWindowTitle('СОСКА')
        self.setWindowIcon(QtGui.QIcon("bmstu_logo.png"))
        # Добавления логотипа
        self.pix = QtGui.QPixmap("bmstu_logo.png").scaledToHeight(self.height() // 5)
        self.MainWinUi.BMSTULogoLabel.setPixmap(self.pix)
        # Добавленик сигналов на кнопки
        self.MainWinUi.CreateButton.clicked.connect(self.form_table)
        self.MainWinUi.MinimizeButton.clicked.connect(self.minimize_automate)
        self.MainWinUi.FormEkvivTableButton.clicked.connect(self.form_ekviv_table)
        self.MainWinUi.CheckEkvivButton.clicked.connect(self.check_ekviv)
        # Работа с таблицами
        self.MainWinUi.AutomateTable.setStyleSheet("QHeaderView{border: 1px solid black}")
        self.MainWinUi.MinimizedAutomateTable.setStyleSheet("QHeaderView{border: 1px solid black}")
        # Сокрытие таблиц и лэйблов
        self.MainWinUi.TableGroupBox.hide()
        self.MainWinUi.MinimizedAutomateTable.hide()
        self.MainWinUi.AutomateInfoLable.hide()
        self.MainWinUi.tabWidget.hide()
        self.MainWinUi.label_2.hide()
        self.MainWinUi.EkvivAutoTable.hide()
        self.MainWinUi.CheckEkvivButton.hide()
        self.MainWinUi.EnterAutoLabel.hide()
        # Добавление стиля
        self.MainWinUi.mainGroupBox.setStyleSheet("QGroupBox {background-color: #D7EAF6}")
        self.MainWinUi.HeaderGroupBox.setStyleSheet("QGroupBox {background-color: #BFE6FE}")
        self.MainWinUi.ButtonsGroupBox.setStyleSheet("QGroupBox {background-color: #B8DCFF}")
        self.MainWinUi.TableGroupBox.setStyleSheet("QGroupBox {background-color: #C8D3FB}")
        self.MainWinUi.SystemNameLabel.setStyleSheet("QLabel {font-size: 12pt;}")
        self.MainWinUi.DescriptionLabel.setStyleSheet("QLabel {border: 5px solid #B8DCFF; font-size: 9pt;}")
        self.MainWinUi.EnterXLabel.setStyleSheet("QLabel {border: 5px solid #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.EnterQLabel.setStyleSheet("QLabel {border: 5px solid #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.XSpinBox.setStyleSheet("QSpinBox {background-color: #B8DCFF; font-size: 10pt;}")
        self.MainWinUi.QSpinBox.setStyleSheet("QSpinBox {background-color: #B8DCFF; font-size: 10pt;}")
        self.MainWinUi.CreateButton.setStyleSheet("QPushButton {background-color: #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.tabWidget.setStyleSheet("QTabWidget {background-color: #BADCDF; font-size: 10pt;}")
        self.MainWinUi.tab.setStyleSheet("QWidget {background-color: #E4FEFF; font-size: 10pt;}")
        self.MainWinUi.tab_2.setStyleSheet("QWidget {background-color: #E4FEFF; font-size: 10pt;}")
        self.MainWinUi.ToCheckMinimizationCheckBox.setStyleSheet("QCheckBox {border: 5px solid #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.MinimizeButton.setStyleSheet("QPushButton {background-color: #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.CheckEkvivButton.setStyleSheet("QPushButton {background-color: #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.FormEkvivTableButton.setStyleSheet("QPushButton {background-color: #C8D3FB; font-size: 10pt;}")
        self.MainWinUi.scrollArea_2.setStyleSheet("QWidget {background-color: #E4FEFF; font-size: 10pt;}")
        self.MainWinUi.AutomateInfoLable.setStyleSheet("QLabel {background-color: #C8D3FB; font-size: 12pt;}")
        self.MainWinUi.AutomateInfoLable.setAlignment(PyQt5.QtCore.Qt.AlignCenter)

    def form_table(self):
        # Изменение видимости объектов
        self.MainWinUi.MinimizedAutomateTable.hide()
        self.MainWinUi.AutomateInfoLable.hide()
        self.MainWinUi.tabWidget.hide()
        self.MainWinUi.label_2.hide()
        self.MainWinUi.TableGroupBox.show()
        # Параметры состояний и сигналов
        self.conditions = int(self.MainWinUi.QSpinBox.text())
        self.inputs = int(self.MainWinUi.XSpinBox.text())
        # Заполнение заголовков таблиц
        x_cols = []
        y_cols = []
        # Очистка текущих таблиц
        for row in range(0, self.MainWinUi.AutomateTable.rowCount()):
            self.MainWinUi.AutomateTable.removeRow(0)
        # Новые заголовки
        for x in range(0, self.inputs):
            x_cols.append(f'x{x + 1}')
        for y in range(0, self.inputs):
            y_cols.append(f'y{y + 1}')
        table_header = []
        for x in range(0, self.inputs):
            table_header.append(x_cols[x])
        for y in range(self.inputs, 2 * self.inputs):
            table_header.append(y_cols[y - self.inputs])
        self.MainWinUi.AutomateTable.setColumnCount(2 * self.inputs)
        self.MainWinUi.AutomateTable.setHorizontalHeaderLabels(table_header)
        # Заполнение таблицы генерируемыми значениями
        for q in range(0, self.conditions):
            self.MainWinUi.AutomateTable.insertRow(q)
            for x in range(0, self.inputs):
                self.MainWinUi.AutomateTable.setItem(q, x, QTableWidgetItem(str(random.randint(1,self.conditions))))
                self.MainWinUi.AutomateTable.item(q, x).setTextAlignment(4)
            for y in range(self.inputs, 2 * self.inputs):
                self.MainWinUi.AutomateTable.setItem(q, y, QTableWidgetItem(str(random.randint(0, 1))))
                self.MainWinUi.AutomateTable.item(q, y).setTextAlignment(4)
        # Изменение параметров объектов
        self.MainWinUi.AutomateTable.setFixedHeight(self.conditions * 40 + 20)
        self.MainWinUi.tabWidget.show()

    def form_ekviv_table(self):
        # Изменение видимости объектов
        self.MainWinUi.EkvivAutoTable.show()
        self.MainWinUi.CheckEkvivButton.show()
        # Задание параметров
        self.ekviv_conditions = int(self.MainWinUi.Q2SpinBox.text())
        self.inputs = int(self.MainWinUi.XSpinBox.text())
        # Заполнение заголовков таблиц
        x_cols = []
        y_cols = []
        # Очистка текущих таблиц
        for row in range(0, self.MainWinUi.EkvivAutoTable.rowCount()):
            self.MainWinUi.EkvivAutoTable.removeRow(0)
        # Новые заголовки
        for x in range(0, self.inputs):
            x_cols.append(f'x{x + 1}')
        for y in range(0, self.inputs):
            y_cols.append(f'y{y + 1}')
        table_header = []
        for x in range(0, self.inputs):
            table_header.append(x_cols[x])
        for y in range(self.inputs, 2 * self.inputs):
            table_header.append(y_cols[y - self.inputs])
        self.MainWinUi.EkvivAutoTable.setColumnCount(2 * self.inputs)
        self.MainWinUi.EkvivAutoTable.setHorizontalHeaderLabels(table_header)
        # Заполнение таблицы генерируемыми значениями
        for q in range(0, self.ekviv_conditions):
            self.MainWinUi.EkvivAutoTable.insertRow(q)
            for x in range(0, self.inputs):
                self.MainWinUi.EkvivAutoTable.setItem(q, x, QTableWidgetItem(str(random.randint(1, self.ekviv_conditions))))
                self.MainWinUi.EkvivAutoTable.item(q, x).setTextAlignment(4)
            for y in range(self.inputs, 2 * self.inputs):
                self.MainWinUi.EkvivAutoTable.setItem(q, y, QTableWidgetItem(str(random.randint(0, 1))))
                self.MainWinUi.EkvivAutoTable.item(q, y).setTextAlignment(4)
        # Изменение параметров объектов
        self.MainWinUi.EkvivAutoTable.setFixedHeight(self.ekviv_conditions * 40 + 20)

    def check_ekviv(self):
        # Проверка на одинаковый входной алфавит
        if self.MainWinUi.AutomateTable.columnCount() != self.MainWinUi.EkvivAutoTable.columnCount():
            msg = QMessageBox.critical(self, "Эквивалентность", "Входные алфавиты автоматов различны.\nАвтоматы НЕ эквивалентны")
        else:
            # Проверка на цифры в таблицах
            is_dig1 = self.inspect_matrix(self.MainWinUi.AutomateTable)
            is_dig2 = self.inspect_matrix(self.MainWinUi.EkvivAutoTable)
            if (not is_dig1 or not is_dig2):
                msg = QMessageBox.critical(self, "Ввод данныъ", "Входные данные не являются цифрами.\nИзмените данные таблиц переходов и выходов")
            else:
                # Заполнение таблиц двух автоматов
                automate1_table = [0] * self.conditions
                automate2_table = [0] * self.ekviv_conditions
                for row in range(0, self.MainWinUi.AutomateTable.rowCount()):
                    automate1_table[row] = [0] * (self.inputs * 2)
                    for col in range(0, self.MainWinUi.AutomateTable.columnCount()):
                        automate1_table[row][col] = int(self.MainWinUi.AutomateTable.item(row, col).text())
                for row in range(0, self.MainWinUi.EkvivAutoTable.rowCount()):
                    automate2_table[row] = [0] * (self.inputs * 2)
                    for col in range(0, self.MainWinUi.EkvivAutoTable.columnCount()):
                        automate2_table[row][col] = int(self.MainWinUi.EkvivAutoTable.item(row, col).text())
                # Заполнение таблицы полного произведения
                full_composition_table = [0] * (self.conditions * self.ekviv_conditions)
                condition1 = 1
                condition2 = 1
                for row in range(0, self.conditions * self.ekviv_conditions):
                    full_composition_table[row] = [0] * (self.inputs * 2 + 1)
                    for col in range(0, self.inputs * 2):
                        full_composition_table[row][col + 1] = int(str(automate1_table[condition1 - 1][col]) + str(automate2_table[condition2 - 1][col]))
                    full_composition_table[row][0] = condition1 * 10 + condition2
                    condition2 += 1
                    if condition2 > self.ekviv_conditions:
                        condition1 += 1
                        condition2 = 1
                # Найдем недостижимые состояния и вычеркнем их
                reachable_conditions = []
                for row in range(0, self.conditions * self.ekviv_conditions):
                    for col in range(1, self.inputs + 1):
                        if not (full_composition_table[row][col] in reachable_conditions):
                            reachable_conditions.append(full_composition_table[row][col])
                new_comp_table = []
                for row in range(0, self.conditions * self.ekviv_conditions):
                    if (full_composition_table[row][0] in reachable_conditions):
                        new_comp_table.append(full_composition_table[row])
                # Среди достижимых состояний проверяем равенство выходных сигналов
                is_Ekvivalent = True
                for row in range(0, len(new_comp_table)):
                    for col in range(len(new_comp_table[row]) - self.inputs, len(new_comp_table[row])):
                        if ((new_comp_table[row][col] != 0) and (new_comp_table[row][col] != 11)):
                            is_Ekvivalent = False
                if is_Ekvivalent:
                    msg = QMessageBox.information(self, "Эквивалентность", "Введенные автоматы эквивалентны")
                else:
                    msg = QMessageBox.critical(self, "Эквивалентность", "Введенные автоматы  НЕ эквивалентны")

    def minimize_automate(self):
        # Проверка на цифры в таблицах
        is_dig1 = self.inspect_matrix(self.MainWinUi.AutomateTable)
        if (not is_dig1):
            msg = QMessageBox.critical(self, "Ввод данныъ",
                                       "Входные данные не являются цифрами.\nИзмените данные таблиц переходов и выходов")
        else:
            # Подготовка полей. Очистка места
            self.MainWinUi.AutomateInfoLable.setText("")
            self.minimization_text = "Процесс минимизации:\n"
            self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
            self.MainWinUi.AutomateInfoLable.setText('Минимизирован')
            self.MainWinUi.AutomateInfoLable.show()
            # Создание переменных
            N = self.conditions
            FlagOK = True
            isChecking = self.MainWinUi.ToCheckMinimizationCheckBox.isChecked()
            matrix_transition = [0] * N
            matrix_outputs = [0] * N
            over_all_M = 1 + 2 * self.inputs
            over_all_matrix = [0] * N
            # Заполнение матриц переходов и выходов
            for i in range(0, N):
                matrix_transition[i] = []
                matrix_outputs[i] = []
                matrix_transition[i] = [0] * self.inputs
                matrix_outputs[i] = [0] * self.inputs
                for j in range(0, self.inputs):
                    matrix_transition[i][j] = int(self.MainWinUi.AutomateTable.item(i, j).text())
                    matrix_outputs[i][j] = int(self.MainWinUi.AutomateTable.item(i, j + self.inputs).text())
                    if ((matrix_transition[i][j] > N) or (matrix_transition[i][j] <= 0) or (matrix_outputs[i][j] < 0) or (matrix_outputs[i][j] > 1)):
                        self.MainWinUi.AutomateInfoLable.setText("")
                        FlagOK = False # Флаг правильного ввода матриц
                        break
            # Заполнение итоговой матрицы
            for i in range(0, N):
                over_all_matrix[i] = []
                over_all_matrix[i] = [0] * over_all_M
                over_all_matrix[i][0] = i + 1;
                for j in range(0, self.inputs):
                    over_all_matrix[i][j + 1] = matrix_transition[i][j]
                for j in range(self.inputs, (2 * self.inputs)):
                    over_all_matrix[i][j + 1] = matrix_outputs[i][j - self.inputs]
            # Если неверно выводим оповещение
            if (not FlagOK):
                msg = QMessageBox.critical(self, "Ошибка", "В таблице исходного автомата\nнекорректные данные")
            else:
                # Создание локальных переменных
                flags = [0] * N
                pi0 = [0] * N
                pi1 = [0] * N
                razbienie_s_0 = ""
                razbienie_s_1 = ""
                position = 0
                FlagEnd = True
                razbienie_number = 0
                razbienie_count = 0
                # Разбиение 0
                for i in range(0, N):
                    pi0[i] = i + 1
                self.minimization_text += f'Разбиение 𝝅{razbienie_number}: < '
                razbienie_s_0 += '< '
                # Вывод разбиения 0
                for i in range(0, N):
                    self.minimization_text += f'{pi0[i]} '
                    razbienie_s_0 += f'{pi0[i]} '
                self.minimization_text += '>\n'
                razbienie_s_0 += '>'
                self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
                # Создание матрицы флагов
                for i in range(0, N):
                    flags[i] = [0] * N
                    for j in range(0, N):
                        is_same_output = True
                        for k in range(0, self.inputs):
                            if (matrix_outputs[i][k] != matrix_outputs[j][k]):
                                is_same_output = False
                        if ((i == j) or is_same_output):
                            flags[i][j] = 1
                # Разбиение 1
                for i in range(0, N):
                    for j in range(0, N):
                        if (flags[i][j]):
                            inRazb = False
                            for w in range(0, N):
                                if (pi1[w] == j + 1):
                                    inRazb = True
                            if (inRazb == False):
                                pi1[position] = j + 1
                                position += 1
                                if (position == N):
                                    break
                razbienie_number += 1
                # Вывод разбиения 1
                self.minimization_text += f'Разбиение 𝝅{razbienie_number}: < {pi1[0]} '
                razbienie_s_1 += f'<{pi1[0]}'
                for i in range(1, N):
                    if (flags[pi1[i] - 1][pi1[i - 1] - 1] == 0):
                        self.minimization_text += '> < '
                        razbienie_s_1 += '><'
                        FlagEnd = False
                    self.minimization_text += f'{pi1[i]} '
                    razbienie_s_1 += f'{pi1[i]}'
                self.minimization_text += '>\n'
                razbienie_s_1 += '>'
                self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
                # Проверка совпадения разбиений
                for i in range(0, len(razbienie_s_1)):
                    if (razbienie_s_1[i] == '>'):
                        razbienie_count += 1
                # Проверка завершения алгоритма
                if ((razbienie_s_0 == razbienie_s_1) or (razbienie_count == N) or FlagEnd):
                    self.minimization_text += 'Процесс минимизации завершён.\n'
                    self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
                    self.update_table(over_all_matrix, over_all_M, isChecking)
                else:
                    self.minimization(isChecking, N, flags, pi1, razbienie_number, over_all_M, over_all_matrix, matrix_transition, matrix_outputs, razbienie_s_1)

    def minimization(self, isChecking, N, flags, pi_prev, razbienie_number, over_all_M, over_all_matrix, matrix_transition, matrix_outputs, razbienie_s_0):
        # Создание локальных переменных
        marker = 0
        ekviv_picks = [0] * N
        z = 1
        FlagEnd = True
        pi_new = [0] * N
        new_transitions = [0] * N
        razbienie_s_1 = ""
        razbienie_count = 0
        ekviv_picks[0] = 0
        # Классы эквивалентности
        while (z < N):
            if (flags[pi_prev[z] - 1][pi_prev[z - 1] - 1] == 0):
                marker += 1
            ekviv_picks[pi_prev[z] - 1] += marker
            z += 1
        razbienie_number += 1
        # Вывод классов эквивалентности и новой матрицы переходов
        if (isChecking):
            self.minimization_text += f'Матрица переходов разбиения 𝝅{razbienie_number}:\n'
        for i in range(0, N):
            new_transitions[i] = [0] * self.inputs
            s = []
            for j in range(0, self.inputs):
                new_transitions[i][j] = ekviv_picks[matrix_transition[i][j] - 1]
                s.append(chr(97 + new_transitions[i][j]))
            if (isChecking):
                for k in range(0, len(s)):
                    self.minimization_text += f'{s[k]}{razbienie_number - 1} '
                self.minimization_text += '\n'
        self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
        # Дополнение итоговой матрицы
        new_over_all_M = over_all_M + self.inputs
        new_over_all_matrix = [0] * N
        for i in range(0, N):
            new_over_all_matrix[i] = [0] * new_over_all_M
        for i in range(0, len(over_all_matrix)):
            for j in range(0, len(over_all_matrix[i])):
                new_over_all_matrix[i][j] = over_all_matrix[i][j]
        for i in range(0, N):
            for j  in range(over_all_M, new_over_all_M):
                s = chr(97 + new_transitions[i][j - over_all_M])
                new_over_all_matrix[i][j] = str(s + str(razbienie_number - 1))
        over_all_M = new_over_all_M
        over_all_matrix = new_over_all_matrix
        # Разбиение
        position = 1
        while (position < N):
            for i in range(0, N):
                is_same_razb = True
                for j in range(0, self.inputs):
                    if (new_transitions[i][j] != new_transitions[position - 1][j]):
                        is_same_razb = False
                if ((ekviv_picks[i] == ekviv_picks[position - 1]) and (not is_same_razb)):
                    flags[i][position - 1] = 0
                    flags[position - 1][i] = 0
            position += 1
        position = 0
        for i in range(0, N):
            for j in range(0, N):
                if (flags[i][j]):
                    inRazb = False
                    for w in range(0, N):
                        if (pi_new[w] == j + 1):
                            inRazb = True
                    if (inRazb == False):
                        pi_new[position] = j + 1
                        position += 1
                        if (position == N):
                            break
        # Вывод разбиения
        self.minimization_text += f'Разбиение 𝝅{razbienie_number}: < {pi_new[0]} '
        razbienie_s_1 += f'<{pi_new[0]}'
        for i in range(1, N):
            if (flags[pi_new[i] - 1][pi_new[i - 1] - 1] == 0):
                self.minimization_text += '> < '
                razbienie_s_1 += '><'
                FlagEnd = False
            self.minimization_text += f'{pi_new[i]} '
            razbienie_s_1 += f'{pi_new[i]}'
        self.minimization_text += '>\n'
        razbienie_s_1 += '>'
        self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
        # Проверка совпадения разбиений
        for i in range(0, len(razbienie_s_1)):
            if (razbienie_s_1[i] == '>'):
                razbienie_count += 1
        if ((razbienie_s_0 == razbienie_s_1) or (razbienie_count == N) or FlagEnd):
            self.minimization_text += 'Процесс минимизации завершён.'
            self.MainWinUi.AutomateInfoLable.setText(self.minimization_text)
            self.update_table(over_all_matrix, over_all_M, isChecking)
        else:
            self.minimization(isChecking, N, flags, pi_new, razbienie_number, over_all_M, over_all_matrix, matrix_transition, matrix_outputs, razbienie_s_1)

    def update_table(self, matrix, m, is_checking):
        # Изменение видимости обхектов
        self.MainWinUi.MinimizedAutomateTable.show()
        self.MainWinUi.label_2.show()
        x_cols = []
        y_cols = []
        # Очистка таблицы
        for row in range(0, self.MainWinUi.MinimizedAutomateTable.rowCount()):
            self.MainWinUi.MinimizedAutomateTable.removeRow(0)
        # Заполнение выходов и выходов
        for x in range(0, self.inputs):
            x_cols.append(f'x{x + 1}')
        for y in range(0, self.inputs):
            y_cols.append(f'y{y + 1}')
        # Создание заголовка
        if (is_checking):
            table_header = []
        else:
            table_header = ["Состояния"]
        header_length = 2 * self.inputs + 1
        for x in range(0, self.inputs):
            table_header.append(x_cols[x])
        for y in range(self.inputs, 2 * self.inputs):
            table_header.append(y_cols[y - self.inputs])
        # Проверка расширенного режима
        if (is_checking):
            header_length = m - 1
            razb_numb = 1
            col_counter = 0
            for z in range(2 * self.inputs, m - 1):
                table_header.append(f'δ{razb_numb}')
                col_counter += 1
                if (col_counter == self.inputs):
                    razb_numb += 1
                    col_counter = 0
        # Параметры таблицы
        self.MainWinUi.MinimizedAutomateTable.setColumnCount(header_length)
        self.MainWinUi.MinimizedAutomateTable.setHorizontalHeaderLabels(table_header)
        # Заполнение таблицы
        if (is_checking):
            for i in range(0, self.conditions):
                self.MainWinUi.MinimizedAutomateTable.insertRow(i)
                for j in range(0, header_length):
                    self.MainWinUi.MinimizedAutomateTable.setItem(i, j, QTableWidgetItem(str(matrix[i][j + 1])))
                    self.MainWinUi.MinimizedAutomateTable.item(i, j).setTextAlignment(4)
        else:
            if (m - 1 <= self.inputs * 2):
                for i in range(0, self.conditions):
                    self.MainWinUi.MinimizedAutomateTable.insertRow(i)
                    for j in range(0, header_length):
                        self.MainWinUi.MinimizedAutomateTable.setItem(i, j, QTableWidgetItem(str(matrix[i][j])))
                        self.MainWinUi.MinimizedAutomateTable.item(i, j).setTextAlignment(4)
            else:
                new_trans = []
                new_table = []
                condition_counter = 0
                for i in range(0, self.conditions):
                    if not ([matrix[i][3], matrix[i][4], matrix[i][m-2], matrix[i][m-1]] in new_table):
                        new_trans.append([matrix[i][m - 2], matrix[i][m - 1], matrix[i][3], matrix[i][4]])
                        new_table.append([matrix[i][3], matrix[i][4], matrix[i][m-2], matrix[i][m-1]])
                for i in range(0, len(new_trans)):
                    self.MainWinUi.MinimizedAutomateTable.insertRow(i)
                    self.MainWinUi.MinimizedAutomateTable.setItem(i, 0, QTableWidgetItem(str(chr(97 + condition_counter))))
                    self.MainWinUi.MinimizedAutomateTable.item(i, 0).setTextAlignment(4)
                    condition_counter += 1
                    self.MainWinUi.MinimizedAutomateTable.setItem(i, 1, QTableWidgetItem(str(new_trans[i][0])[:-1]))
                    self.MainWinUi.MinimizedAutomateTable.item(i, 1).setTextAlignment(4)
                    self.MainWinUi.MinimizedAutomateTable.setItem(i, 2, QTableWidgetItem(str(new_trans[i][1])[:-1]))
                    self.MainWinUi.MinimizedAutomateTable.item(i, 2).setTextAlignment(4)
                    self.MainWinUi.MinimizedAutomateTable.setItem(i, 3, QTableWidgetItem(str(new_trans[i][2])))
                    self.MainWinUi.MinimizedAutomateTable.item(i, 3).setTextAlignment(4)
                    self.MainWinUi.MinimizedAutomateTable.setItem(i, 4, QTableWidgetItem(str(new_trans[i][3])))
                    self.MainWinUi.MinimizedAutomateTable.item(i, 4).setTextAlignment(4)
        self.MainWinUi.MinimizedAutomateTable.setFixedHeight(self.conditions * 40 + 20)

    def inspect_matrix(self, tbl):
        is_all_digits = True
        r_count = tbl.rowCount()
        c_count = tbl.columnCount()
        for row in range(0, r_count):
            for col in range(0, c_count):
                item = tbl.item(row, col).text()
                if not (item.isdigit()):
                    is_all_digits = False
        return is_all_digits

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Подтверждение', 'Вы уверены, что хотите завершить работу программы?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())