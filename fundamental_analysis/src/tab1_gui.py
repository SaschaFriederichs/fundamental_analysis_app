from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QWidget


# Tab with revenue and net income                  
class FirstCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Main Calculation")
        
        # Table widgets for revenue and net income
        annual_revenue_label = QLabel("<b>Annual revenue (Jahresumsätze)</b>")
        self.annual_revenue_table_widget = QTableWidget(4, 3)
        self.annual_revenue_table_widget.setEnabled(False)
        self.annual_revenue_table_widget.setHorizontalHeaderLabels(("Date", "Annual revenue [Mio. EUR]", "Change [%]"))
        self.annual_revenue_table_widget.setColumnWidth(0, 100)
        self.annual_revenue_table_widget.setColumnWidth(1, 300)
        self.annual_revenue_table_widget.setColumnWidth(2, 300)
        self.annual_revenue_table_widget.verticalHeader().setVisible(False)
        annual_net_income_label = QLabel("<b>Annual net income (Jahresgewinne)</b>")
        self.annual_net_income_table_widget = QTableWidget(4, 3)
        self.annual_net_income_table_widget.setEnabled(False)
        self.annual_net_income_table_widget.setHorizontalHeaderLabels(("Date", "Annual net income [Mio. EUR]", "Change [%]"))
        self.annual_net_income_table_widget.setColumnWidth(0, 100)
        self.annual_net_income_table_widget.setColumnWidth(1, 300)
        self.annual_net_income_table_widget.setColumnWidth(2, 300)
        self.annual_net_income_table_widget.verticalHeader().setVisible(False)
        quarterly_revenue_label = QLabel("<b>Quarterly revenue (Quartalsumsätze)</b>")
        self.quarterly_revenue_table_widget = QTableWidget(4, 3)
        self.quarterly_revenue_table_widget.setEnabled(False)
        self.quarterly_revenue_table_widget.setHorizontalHeaderLabels(("Date", "Quarterly revenue [Mio. EUR]", "Change [%]"))
        self.quarterly_revenue_table_widget.setColumnWidth(0, 100)
        self.quarterly_revenue_table_widget.setColumnWidth(1, 300)
        self.quarterly_revenue_table_widget.setColumnWidth(2, 300)
        self.quarterly_revenue_table_widget.verticalHeader().setVisible(False)
        quarterly_net_income_label = QLabel("<b>Quarterly net income (Quartalsgewinne)</b>")
        self.quarterly_net_income_table_widget = QTableWidget(4, 3)
        self.quarterly_net_income_table_widget.setEnabled(False)
        self.quarterly_net_income_table_widget.setHorizontalHeaderLabels(("Date", "Quarterly net income [Mio. EUR]", "Change [%]"))
        self.quarterly_net_income_table_widget.setColumnWidth(0, 100)
        self.quarterly_net_income_table_widget.setColumnWidth(1, 300)
        self.quarterly_net_income_table_widget.setColumnWidth(2, 300)
        self.quarterly_net_income_table_widget.verticalHeader().setVisible(False)
        
        # Main calculation widget and layout
        main_calculation_widget = QWidget()
        main_calculation_layout = QGridLayout()
        main_calculation_layout.addWidget(annual_revenue_label, 0, 0)
        main_calculation_layout.addWidget(self.annual_revenue_table_widget, 1, 0)
        main_calculation_layout.addWidget(annual_net_income_label, 2, 0)
        main_calculation_layout.addWidget(self.annual_net_income_table_widget, 3, 0)
        main_calculation_layout.addWidget(quarterly_revenue_label, 4, 0)
        main_calculation_layout.addWidget(self.quarterly_revenue_table_widget, 5, 0)
        main_calculation_layout.addWidget(quarterly_net_income_label, 6, 0)
        main_calculation_layout.addWidget(self.quarterly_net_income_table_widget, 7, 0)
        main_calculation_widget.setLayout(main_calculation_layout)
        self.setCentralWidget(main_calculation_widget)
        
    def set_annual_revenue(self, annual_revenue, currency):
        for i in range(4):
            annual_revenue_date = annual_revenue.index[i].date()
            annual_revenue_value = annual_revenue.iat[i]
            self.annual_revenue_table_widget.setItem(i, 0, QTableWidgetItem(str(annual_revenue_date)))
            self.annual_revenue_table_widget.setItem(i, 1, QTableWidgetItem(str(annual_revenue_value/1e6)))
            if i > 0:
                self.annual_revenue_table_widget.setItem(i-1, 2, QTableWidgetItem(self.percentage_change_string(annual_revenue.iat[i-1], annual_revenue_value)))
        self.annual_revenue_table_widget.setHorizontalHeaderLabels(("Date", "Annual revenue [Mio. " + currency + "]", "Change [%]"))
           
    def set_annual_net_income(self, annual_net_income, currency):
        for i in range(4):
            annual_net_income_date = annual_net_income.index[i].date()
            annual_net_income_value = annual_net_income.iat[i]
            self.annual_net_income_table_widget.setItem(i, 0, QTableWidgetItem(str(annual_net_income_date)))
            self.annual_net_income_table_widget.setItem(i, 1, QTableWidgetItem(str(annual_net_income_value/1e6)))
            if i > 0:
                self.annual_net_income_table_widget.setItem(i-1, 2, QTableWidgetItem(self.percentage_change_string(annual_net_income.iat[i-1], annual_net_income_value)))
        self.annual_net_income_table_widget.setHorizontalHeaderLabels(("Date", "Annual net income [Mio. " + currency + "]", "Change [%]"))
        
    def set_quarterly_revenue(self, quarterly_revenue, currency):
        for i in range(4):
            quarterly_revenue_date = quarterly_revenue.index[i].date()
            quarterly_revenue_value = quarterly_revenue.iat[i]
            self.quarterly_revenue_table_widget.setItem(i, 0, QTableWidgetItem(str(quarterly_revenue_date)))
            self.quarterly_revenue_table_widget.setItem(i, 1, QTableWidgetItem(str(quarterly_revenue_value/1e6)))
            if i > 0:
                self.quarterly_revenue_table_widget.setItem(i-1, 2, QTableWidgetItem(self.percentage_change_string(quarterly_revenue.iat[i-1], quarterly_revenue_value)))
        self.quarterly_revenue_table_widget.setHorizontalHeaderLabels(("Date", "Quarterly revenue [Mio. " + currency + "]", "Change [%]"))
        
    def set_quarterly_net_income(self, quarterly_net_income, currency):
        for i in range(4):
            quarterly_net_income_date = quarterly_net_income.index[i].date()
            quarterly_net_income_value = quarterly_net_income.iat[i]
            self.quarterly_net_income_table_widget.setItem(i, 0, QTableWidgetItem(str(quarterly_net_income_date)))
            self.quarterly_net_income_table_widget.setItem(i, 1, QTableWidgetItem(str(quarterly_net_income_value/1e6)))
            if i > 0:
                self.quarterly_net_income_table_widget.setItem(i-1, 2, QTableWidgetItem(self.percentage_change_string(quarterly_net_income.iat[i-1], quarterly_net_income_value)))
        self.quarterly_net_income_table_widget.setHorizontalHeaderLabels(("Date", "Quarterly net income [Mio. " + currency + "]", "Change [%]"))
        
    def percentage_change_string(self, new_value, old_value):
        percentage_change = 100.0*(new_value-old_value)/old_value
        return f"{percentage_change:+.2f}"
    