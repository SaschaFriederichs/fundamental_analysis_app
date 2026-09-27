from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QWidget


# Tab with market value, book value, EPS, EPS diluted        
class SecondCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Second Calculation")        
        
        # Gross profit (Bruttogewinn)
        gross_profit_label = QLabel("<b>Gross profit (Bruttogewinn)</b>")
        self.gross_profit_table_widget = QTableWidget(4, 3)
        self.gross_profit_table_widget.setEnabled(False)
        self.gross_profit_table_widget.setHorizontalHeaderLabels(("Date", "Gross profit [Mio. EUR]", "Percentage of revenue [%]"))
        self.gross_profit_table_widget.setColumnWidth(0, 100)
        self.gross_profit_table_widget.setColumnWidth(1, 300)
        self.gross_profit_table_widget.setColumnWidth(2, 300)
        self.gross_profit_table_widget.verticalHeader().setVisible(False)
        
        # Operating income (Betribsbewinn)
        operating_income_label = QLabel("<b>Operating income (Betriebsgewinn)</b>")
        self.operating_income_table_widget = QTableWidget(4, 3)
        self.operating_income_table_widget.setEnabled(False)
        self.operating_income_table_widget.setHorizontalHeaderLabels(("Date", "Operating income [Mio. EUR]", "Percentage of revenue [%]"))
        self.operating_income_table_widget.setColumnWidth(0, 100)
        self.operating_income_table_widget.setColumnWidth(1, 300)
        self.operating_income_table_widget.setColumnWidth(2, 300)
        self.operating_income_table_widget.verticalHeader().setVisible(False)
        
        # Net income (Nettogewinn)
        net_income_label = QLabel("<b>Net income (Nettogewinn)</b>")
        self.net_income_table_widget = QTableWidget(4, 3)
        self.net_income_table_widget.setEnabled(False)
        self.net_income_table_widget.setHorizontalHeaderLabels(("Date", "Net income [Mio. EUR]", "Percentage of revenue [%]"))
        self.net_income_table_widget.setColumnWidth(0, 100)
        self.net_income_table_widget.setColumnWidth(1, 300)
        self.net_income_table_widget.setColumnWidth(2, 300)
        self.net_income_table_widget.verticalHeader().setVisible(False)
        
        # Earnings per share (EPS)
        earnings_per_share_label = QLabel("<b>Earnings per share (EPS) (Gewinn pro Aktie)</b>")
        self.earnings_per_share_table_widget = QTableWidget(4, 2)
        self.earnings_per_share_table_widget.setEnabled(False)
        self.earnings_per_share_table_widget.setHorizontalHeaderLabels(("Date", "Earnings per share (EPS) [EUR]"))
        self.earnings_per_share_table_widget.setColumnWidth(0, 100)
        self.earnings_per_share_table_widget.setColumnWidth(1, 300)
        self.earnings_per_share_table_widget.verticalHeader().setVisible(False)
        
        # Earnings per share diluted (EPS diluted)
        earnings_per_share_diluted_label = QLabel("<b>Earnings per share diluted (EPS diluted) (Verwässerter Gewinn pro Aktie)</b>")
        self.earnings_per_share_diluted_table_widget = QTableWidget(4, 2)
        self.earnings_per_share_diluted_table_widget.setEnabled(False)
        self.earnings_per_share_diluted_table_widget.setHorizontalHeaderLabels(("Date", "Earnings per share diluted (EPS dil.) [EUR]"))
        self.earnings_per_share_diluted_table_widget.setColumnWidth(0, 100)
        self.earnings_per_share_diluted_table_widget.setColumnWidth(1, 300)
        self.earnings_per_share_diluted_table_widget.verticalHeader().setVisible(False)
        
        # Second calculation widget and layout
        second_calculation_widget = QWidget()
        second_calculation_layout = QGridLayout()
        second_calculation_layout.addWidget(gross_profit_label, 0, 0)
        second_calculation_layout.addWidget(self.gross_profit_table_widget, 1, 0)
        second_calculation_layout.addWidget(operating_income_label, 2, 0)
        second_calculation_layout.addWidget(self.operating_income_table_widget, 3, 0)
        second_calculation_layout.addWidget(net_income_label, 4, 0)
        second_calculation_layout.addWidget(self.net_income_table_widget, 5, 0)
        second_calculation_layout.addWidget(earnings_per_share_label, 7, 0, 1, 2)
        second_calculation_layout.addWidget(self.earnings_per_share_table_widget, 8, 0, 1, 2)
        second_calculation_layout.addWidget(earnings_per_share_diluted_label, 9, 0, 1, 2)
        second_calculation_layout.addWidget(self.earnings_per_share_diluted_table_widget, 10, 0, 1, 2)
        second_calculation_widget.setLayout(second_calculation_layout)
        self.setCentralWidget(second_calculation_widget)  
        
    def set_gross_profit(self, gross_profit, revenue, currency):
        for i in range(4):
            gross_profit_date = gross_profit.index[i].date()
            gross_profit_value = gross_profit.iat[i]
            revenue_value = revenue.iat[i]
            percentage_of_revenue = 100.0*gross_profit_value/revenue_value
            self.gross_profit_table_widget.setItem(i, 0, QTableWidgetItem(str(gross_profit_date)))
            self.gross_profit_table_widget.setItem(i, 1, QTableWidgetItem(str(gross_profit_value/1e6)))
            self.gross_profit_table_widget.setItem(i, 2, QTableWidgetItem(f"{percentage_of_revenue:.2f}"))
        self.gross_profit_table_widget.setHorizontalHeaderLabels(("Date", "Gross profit [Mio. " + currency + "]", "Percentage of revenue [%]"))   
            
    def set_operating_income(self, operating_income, revenue, currency):
        for i in range(4):
            operating_income_date = operating_income.index[i].date()
            operating_income_value = operating_income.iat[i]
            revenue_value = revenue.iat[i]
            percentage_of_revenue = 100.0*operating_income_value/revenue_value
            self.operating_income_table_widget.setItem(i, 0, QTableWidgetItem(str(operating_income_date)))
            self.operating_income_table_widget.setItem(i, 1, QTableWidgetItem(str(operating_income_value/1e6)))
            self.operating_income_table_widget.setItem(i, 2, QTableWidgetItem(f"{percentage_of_revenue:.2f}"))
        self.operating_income_table_widget.setHorizontalHeaderLabels(("Date", "Operating income [Mio. " + currency + "]", "Percentage of revenue [%]"))   
     
    def set_net_income(self, net_income, revenue, currency):
        for i in range(4):
            net_income_date = net_income.index[i].date()
            net_income_value = net_income.iat[i]
            revenue_value = revenue.iat[i]
            percentage_of_revenue = 100.0*net_income_value/revenue_value
            self.net_income_table_widget.setItem(i, 0, QTableWidgetItem(str(net_income_date)))
            self.net_income_table_widget.setItem(i, 1, QTableWidgetItem(str(net_income_value/1e6)))
            self.net_income_table_widget.setItem(i, 2, QTableWidgetItem(f"{percentage_of_revenue:.2f}"))
        self.net_income_table_widget.setHorizontalHeaderLabels(("Date", "Net income [Mio. " + currency + "]", "Percentage of revenue [%]"))   
                    
    def set_earnings_per_share(self, data, currency):
        i = 0
        for date, value in data.items():
            self.earnings_per_share_table_widget.setItem(i, 0, QTableWidgetItem(str(date.date())))
            self.earnings_per_share_table_widget.setItem(i, 1, QTableWidgetItem(str(value)))
            i += 1
        self.earnings_per_share_table_widget.setHorizontalHeaderLabels(("Date", "Earnings per share (EPS) [" + currency + "]"))    
        
    def set_earnings_per_share_diluted(self, data, currency):
        i = 0
        for date, value in data.items():
            self.earnings_per_share_diluted_table_widget.setItem(i, 0, QTableWidgetItem(str(date.date())))
            self.earnings_per_share_diluted_table_widget.setItem(i, 1, QTableWidgetItem(str(value)))
            i += 1
        self.earnings_per_share_diluted_table_widget.setHorizontalHeaderLabels(("Date", "Earnings per share diluted (EPS dil.) [" + currency + "]"))
           
    