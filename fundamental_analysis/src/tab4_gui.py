from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QLineEdit, QWidget


class ForthCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Forth Calculation")      
        
        # Market value
        self.market_value_label = QLabel("Market value (Marktkapitalisierung) [Mio. EUR]")
        self.market_value_line_edit = QLineEdit()
        self.market_value_line_edit.setEnabled(False)
        
        # Book value
        self.book_value_label = QLabel("Book value (Buchwert) [Mio. EUR]")
        self.book_value_line_edit = QLineEdit()
        self.book_value_line_edit.setEnabled(False)
        
        # Earnings quality
        self.earnings_quality_label = QLabel("Earnings quality (Ertragsqualität) [Ratio]")
        self.earnings_quality_line_edit = QLineEdit()
        self.earnings_quality_line_edit.setEnabled(False)
        
        # Free cashflow
        self.free_cashflow_label = QLabel("Free cashflow [Mio. EUR]")
        self.free_cashflow_line_edit = QLineEdit()
        self.free_cashflow_line_edit.setEnabled(False)
        
        # Cash burn rate
        self.cash_burn_rate_label = QLabel("Cash burn rate [year]")
        self.cash_burn_rate_line_edit = QLineEdit()
        self.cash_burn_rate_line_edit.setEnabled(False)
        
        # Forth calculation widget and layout
        forth_calculation_widget = QWidget()
        forth_calculation_layout = QGridLayout()
        forth_calculation_layout.addWidget(self.market_value_label, 0, 0)
        forth_calculation_layout.addWidget(self.market_value_line_edit, 0, 1)
        forth_calculation_layout.addWidget(self.book_value_label, 1, 0)
        forth_calculation_layout.addWidget(self.book_value_line_edit, 1, 1)
        forth_calculation_layout.addWidget(self.earnings_quality_label, 2, 0)
        forth_calculation_layout.addWidget(self.earnings_quality_line_edit, 2, 1)
        forth_calculation_layout.addWidget(self.free_cashflow_label, 3, 0)
        forth_calculation_layout.addWidget(self.free_cashflow_line_edit, 3, 1)
        forth_calculation_layout.addWidget(self.cash_burn_rate_label, 4, 0)
        forth_calculation_layout.addWidget(self.cash_burn_rate_line_edit, 4, 1)
        forth_calculation_widget.setLayout(forth_calculation_layout)
        self.setCentralWidget(forth_calculation_widget)  
        
    def set_market_value(self, market_value, currency):
        market_value /= 1e6
        self.market_value_line_edit.setText(f"{market_value:.3f}")
        self.market_value_label.setText("Market value (Marktkapitalisierung) [Mio. " + currency + "]")
              
    def set_book_value(self, total_equity, currency):
        book_value = total_equity.iat[0]/1e6
        self.book_value_line_edit.setText(f"{book_value:.3f}")
        self.book_value_label.setText("Book value (Buchwert) [Mio. " + currency + "]")  
    
    def set_earnings_quality(self, operating_cash_flow, annual_net_income):
        earnings_quality = operating_cash_flow.iat[0]/annual_net_income.iat[0]
        self.earnings_quality_line_edit.setText(f"{earnings_quality:.3f}")
        
    def set_free_cashflow(self, free_cashflow, currency):
        free_cashflow_value = free_cashflow.iat[0]/1e6
        self.free_cashflow_line_edit.setText(f"{free_cashflow_value:.3f}")
        self.free_cashflow_label.setText("Free cashflow [Mio. " + currency + "]")      
        
    def set_cash_burn_rate(self, cash_burn_rate):
        self.cash_burn_rate_line_edit.setText(f"{cash_burn_rate:.3f}")    
        