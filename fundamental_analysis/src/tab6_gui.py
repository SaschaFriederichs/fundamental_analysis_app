from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QLineEdit, QWidget, QSizePolicy


class SixthCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fifth Calculation")      
        
        # Evaluation (Bewertung)
        evaluation_label = QLabel("<b>Evaluation (Bewertung)</b>")
        evaluation_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        # Price to book ratio PB (Kurs-Buchwert-Verhätnis KBV)
        self.price_to_book_ratio_label = QLabel("Price to book ratio PB (Kurs-Buchwert-Verhältnis KBV) [Ratio]")
        self.price_to_book_ratio_line_edit = QLineEdit()
        self.price_to_book_ratio_line_edit.setEnabled(False)
        
        # Dividend yield (Dividendenrendite)
        self.dividend_yield_label = QLabel("Dividend yield (Dividendenrendite) [%]")
        self.dividend_yield_line_edit = QLineEdit()
        self.dividend_yield_line_edit.setEnabled(False)
        
        # Dividend payout ratio (Dividendenausschüttungsquote)
        self.dividend_payout_ratio_label = QLabel("Dividend payout ratio (Dividendenausschüttungsquote) [%]")
        self.dividend_payout_ratio_line_edit = QLineEdit()
        self.dividend_payout_ratio_line_edit.setEnabled(False)
        
        # Earnings yield (Gewinnrendite) 
        self.earnings_yield_label = QLabel("Earnings yield (Gewinnrendite) [%]")
        self.earnings_yield_line_edit = QLineEdit()
        self.earnings_yield_line_edit.setEnabled(False)
        
        # Trailing price to earnings (PE) ratio (Nachlaufendes Kurs-Gewinn-Verhälfnis KGV)
        self.trailing_pe_ratio_label = QLabel("Trailing price to earnings (PE) ratio (Nachlaufendes KGV) [Ratio]")
        self.trailing_pe_ratio_line_edit = QLineEdit()
        self.trailing_pe_ratio_line_edit.setEnabled(False)
        
        # Current price to earnings (PE) ratio (Aktuelles Kurs-Gewinn-Verhältnis KGV)
        self.current_pe_ratio_label = QLabel("Current price to earnings (PE) ratio (Aktuelles KGV) [Ratio]")
        self.current_pe_ratio_line_edit = QLineEdit()
        self.current_pe_ratio_line_edit.setEnabled(False)
        
        # Forward price to earnings (PE) ratio (Zukünftiges Kurs-Gewinn-Verhältnis)
        self.forward_pe_ratio_label = QLabel("Forward price to earnings (PE) ratio (Zukünftiges KGV) [Ratio]")
        self.forward_pe_ratio_line_edit = QLineEdit()
        self.forward_pe_ratio_line_edit.setEnabled(False)
        
        # Operational price to earnings (PE) ratio (Operatives Kurs-Gewinn-Verhältnis KGV)
        self.operational_pe_ratio_label = QLabel("Operational price to earnings (PE) ratio (Operatives KGV) [Ratio]")
        self.operational_pe_ratio_line_edit = QLineEdit()
        self.operational_pe_ratio_line_edit.setEnabled(False)
        
        # As-reported price to earnings (PE) ratio (Ausgewiesenes Kurs-Gewinn-Verhältnis KGV)
        self.as_reported_pe_ratio_label = QLabel("As-reported price to earnings (PE) ratio (Ausgewiesenes KGV) [Ratio]")
        self.as_reported_pe_ratio_line_edit = QLineEdit()
        self.as_reported_pe_ratio_line_edit.setEnabled(False)
        
        # Price to earnings growth (PEG) ratio (Kurs-Gewinn-Wachstums-Verhältnis KGWV)
        self.peg_ratio_label = QLabel("Price to earnings growth (PEG) ratio (KGWV) [Ratio]")
        self.peg_ratio_line_edit = QLineEdit()
        self.peg_ratio_line_edit.setEnabled(False)
        
        # Sixth calculation widget and layout
        sixth_calculation_widget = QWidget()
        sixth_calculation_layout = QGridLayout()
        sixth_calculation_layout.addWidget(evaluation_label, 0, 0)
        sixth_calculation_layout.addWidget(self.price_to_book_ratio_label, 1, 0)
        sixth_calculation_layout.addWidget(self.price_to_book_ratio_line_edit, 1, 1)
        sixth_calculation_layout.addWidget(self.dividend_yield_label, 2, 0)
        sixth_calculation_layout.addWidget(self.dividend_yield_line_edit, 2, 1)
        sixth_calculation_layout.addWidget(self.dividend_payout_ratio_label, 3, 0)
        sixth_calculation_layout.addWidget(self.dividend_payout_ratio_line_edit, 3, 1)
        sixth_calculation_layout.addWidget(self.earnings_yield_label, 4, 0)
        sixth_calculation_layout.addWidget(self.earnings_yield_line_edit, 4, 1)
        sixth_calculation_layout.addWidget(self.trailing_pe_ratio_label, 5, 0)
        sixth_calculation_layout.addWidget(self.trailing_pe_ratio_line_edit, 5, 1)
        sixth_calculation_layout.addWidget(self.current_pe_ratio_label, 6, 0)
        sixth_calculation_layout.addWidget(self.current_pe_ratio_line_edit, 6, 1)
        sixth_calculation_layout.addWidget(self.forward_pe_ratio_label, 7, 0)
        sixth_calculation_layout.addWidget(self.forward_pe_ratio_line_edit, 7, 1)
        sixth_calculation_layout.addWidget(self.operational_pe_ratio_label, 8, 0)
        sixth_calculation_layout.addWidget(self.operational_pe_ratio_line_edit, 8, 1)
        sixth_calculation_layout.addWidget(self.as_reported_pe_ratio_label, 9, 0)
        sixth_calculation_layout.addWidget(self.as_reported_pe_ratio_line_edit, 9, 1)
        sixth_calculation_layout.addWidget(self.peg_ratio_label, 10, 0)
        sixth_calculation_layout.addWidget(self.peg_ratio_line_edit, 10, 1)
        sixth_calculation_widget.setLayout(sixth_calculation_layout)
        self.setCentralWidget(sixth_calculation_widget)  
    
    def set_price_to_book_ratio(self, current_share_price, number_shares_outstanding, total_equity):        
        price_to_book_ratio = (current_share_price*number_shares_outstanding)/total_equity.iat[0]
        self.price_to_book_ratio_line_edit.setText(f"{price_to_book_ratio:.2f}")
            
    def set_dividend_yield(self, dividend_yield):
        self.dividend_yield_line_edit.setText(f"{dividend_yield:.2f}")
    
    def set_dividend_payout_ratio(self, annual_dividend, earnings_per_share):
        dividend_payout_ratio = 100.0*annual_dividend.iat[-1]/earnings_per_share.iat[0]
        self.dividend_payout_ratio_line_edit.setText(f"{dividend_payout_ratio:.2f}")

    def set_earnings_yield(self, earnings_per_share, current_share_price):
        earnings_yield = 100.0*earnings_per_share.iat[0]/current_share_price
        self.earnings_yield_line_edit.setText(f"{earnings_yield:.2f}")
        
    def set_trailing_pe_ratio(self, earnings_per_share, current_share_price):
        trailing_pe_ratio = current_share_price/earnings_per_share.iat[0]
        self.trailing_pe_ratio_line_edit.setText(f"{trailing_pe_ratio:.2f}")
        
    def set_current_pe_ratio(self, earnings_per_share, forward_earnings_per_share, current_share_price):
        average_earnings_per_share = (forward_earnings_per_share+earnings_per_share.iat[0]+earnings_per_share.iat[1])/3.0
        current_pe_ratio = current_share_price/average_earnings_per_share
        self.current_pe_ratio_line_edit.setText(f"{current_pe_ratio:.2f}")
    
    def set_forward_pe_ratio(self, earnings_per_share, forward_earnings_per_share, current_share_price):
        average_earnings_per_share = (forward_earnings_per_share+earnings_per_share.iat[0])/2.0
        forward_pe_ratio = current_share_price/average_earnings_per_share
        self.forward_pe_ratio_line_edit.setText(f"{forward_pe_ratio:.2f}")    
          
    def set_operational_pe_ratio(self, ebit, number_of_shares_outstanding, current_share_price):
        operational_pe_ratio = number_of_shares_outstanding*current_share_price/ebit.iat[0]
        self.operational_pe_ratio_line_edit.setText(f"{operational_pe_ratio:.2f}")
        
    def set_as_reported_pe_ratio(self, number_of_shares_outstanding, current_share_price, annual_net_income):
        as_reported_pe_ratio = number_of_shares_outstanding*current_share_price/annual_net_income.iat[0]
        self.as_reported_pe_ratio_line_edit.setText(f"{as_reported_pe_ratio:.2f}")
        
    def set_peg_ratio(self, peg_ratio):
        self.peg_ratio_line_edit.setText(f"{peg_ratio:.2f}")
         
        