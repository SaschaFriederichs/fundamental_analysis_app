from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QTableWidget, QTableWidgetItem, QWidget


class ThirdCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Third Calculation")      
    
        # Assets (Aktiva)
        assets_label = QLabel("<b>Assets (Aktiva)</b>")
        self.assets_table_widget = QTableWidget(7, 3)
        self.assets_table_widget.setEnabled(False)
        self.assets_table_widget.setHorizontalHeaderLabels(("Asset", "Value [Mio. EUR]", "Percentage of\ntotal assets [%]"))
        self.assets_table_widget.setColumnWidth(0, 370)
        self.assets_table_widget.setColumnWidth(1, 165)
        self.assets_table_widget.setColumnWidth(2, 165)
        self.assets_table_widget.verticalHeader().setVisible(False)
        
        # Liabilities (Passiva)
        liabilities_label = QLabel("<b>Equity and liabilities (Passiva)</b>")
        self.liabilities_table_widget = QTableWidget(7, 3)
        self.liabilities_table_widget.setEnabled(False)
        self.liabilities_table_widget.setHorizontalHeaderLabels(("Equity and liabilities", "Value [Mio. EUR]", 
                                                                 "Percentage of\ntotal assets [%]"))
        self.liabilities_table_widget.setColumnWidth(0, 370)
        self.liabilities_table_widget.setColumnWidth(1, 165)
        self.liabilities_table_widget.setColumnWidth(2, 165)
        self.liabilities_table_widget.verticalHeader().setVisible(False)
        
        # Equity (Eigenkapital)
        equity_label = QLabel("<b>Equity (Eigenkapital)</b>")
        self.equity_table_widget = QTableWidget(7, 3)
        self.equity_table_widget.setEnabled(False)
        self.equity_table_widget.setHorizontalHeaderLabels(("Equity", "Value [Mio. EUR]", 
                                                            "Percentage of\ntotal assets [%]"))
        self.equity_table_widget.setColumnWidth(0, 370)
        self.equity_table_widget.setColumnWidth(1, 165)
        self.equity_table_widget.setColumnWidth(2, 165)
        self.equity_table_widget.verticalHeader().setVisible(False)
        
        # Third calculation widget and layout
        third_calculation_widget = QWidget()
        third_calculation_layout = QGridLayout()
        third_calculation_layout.addWidget(assets_label, 0, 0)
        third_calculation_layout.addWidget(self.assets_table_widget, 1, 0)
        third_calculation_layout.addWidget(liabilities_label, 2, 0)
        third_calculation_layout.addWidget(self.liabilities_table_widget, 3, 0)
        third_calculation_layout.addWidget(equity_label, 4, 0)
        third_calculation_layout.addWidget(self.equity_table_widget, 5, 0)
        third_calculation_widget.setLayout(third_calculation_layout)
        self.setCentralWidget(third_calculation_widget)  
        
    def set_assets(self, cash_and_cash_equivalents, accounts_receivable, other_current_assets, inventory, total_assets, currency):
        titel = ("Cash and equivalents (Zahlungsmittel und Zahlungsmittelequivalente",
                 "Accounts receivable (Forerungen aus Lieferungen und Leistungen", 
                 "Other current assets (Übrige Vermögenswerte)",
                 "Inventory (Vorräte)",
                 "Total assets (Aktiva)")
        total_assets_value = total_assets.iat[0]
        self.assets_table_widget.setItem(0, 0, QTableWidgetItem(titel[0]))
        self.assets_table_widget.setItem(0, 1, QTableWidgetItem(str(cash_and_cash_equivalents.iat[0]/1e6)))
        cash_and_cash_equivalents_percentage = 100.0*cash_and_cash_equivalents.iat[0]/total_assets_value
        self.assets_table_widget.setItem(0, 2, QTableWidgetItem(f"{cash_and_cash_equivalents_percentage:.2f}"))
        self.assets_table_widget.setItem(1, 0, QTableWidgetItem(titel[1]))
        self.assets_table_widget.setItem(1, 1, QTableWidgetItem(str(accounts_receivable.iat[0]/1e6)))
        accounts_receivable_percentage = 100.0*accounts_receivable.iat[0]/total_assets_value
        self.assets_table_widget.setItem(1, 2, QTableWidgetItem(f"{accounts_receivable_percentage:.2f}"))
        self.assets_table_widget.setItem(2, 0, QTableWidgetItem(titel[2]))
        self.assets_table_widget.setItem(2, 1, QTableWidgetItem(str(other_current_assets.iat[0]/1e6)))
        other_current_assets_percentage = 100.0*other_current_assets.iat[0]/total_assets_value
        self.assets_table_widget.setItem(2, 2, QTableWidgetItem(f"{other_current_assets_percentage:.2f}"))
        self.assets_table_widget.setItem(3, 0, QTableWidgetItem(titel[3]))
        self.assets_table_widget.setItem(3, 1, QTableWidgetItem(str(inventory.iat[0]/1e6)))
        inventory_percentage = 100.0*inventory.iat[0]/total_assets_value
        self.assets_table_widget.setItem(3, 2, QTableWidgetItem(f"{inventory_percentage:.2f}"))
        self.assets_table_widget.setItem(4, 0, QTableWidgetItem(titel[4]))
        self.assets_table_widget.setItem(4, 1, QTableWidgetItem(str(total_assets.iat[0]/1e6)))
        #total_assets_percentage = cash_and_cash_equivalents_percentage+accounts_receivable_percentage+other_current_assets_percentage
        self.assets_table_widget.setItem(4, 2, QTableWidgetItem(f"{100.0:.2f}"))
        self.assets_table_widget.setHorizontalHeaderLabels(("Assets", "Value [Mio. " + currency + "]", 
                                                            "Percentage of\ntotal assets [%]"))   
    
    def set_liabilities(self, total_equity, current_liabilities, non_current_liabilities,  total_assets, currency):
        titel = ("Total equity (Eigenkapital)", "Current liabilities (Kurzfristige Verbindlichkeiten)",
                 "Non current liabilites (Langfristige Verbindlichkeiten)", "Total equity & liabilities (Passiva)")
        total_equity_and_liabilities = total_assets.iat[0]
        self.liabilities_table_widget.setItem(0, 0, QTableWidgetItem(titel[0]))
        self.liabilities_table_widget.setItem(0, 1, QTableWidgetItem(str(total_equity.iat[0]/1e6)))
        total_equity_percentage = 100.0*total_equity.iat[0]/total_equity_and_liabilities
        self.liabilities_table_widget.setItem(0, 2, QTableWidgetItem(f"{total_equity_percentage:.2f}"))
        self.liabilities_table_widget.setItem(1, 0, QTableWidgetItem(titel[1]))
        self.liabilities_table_widget.setItem(1, 1, QTableWidgetItem(str(current_liabilities.iat[0]/1e6)))
        current_liabilities_percentage = 100.0*current_liabilities.iat[0]/total_equity_and_liabilities
        self.liabilities_table_widget.setItem(1, 2, QTableWidgetItem(f"{current_liabilities_percentage:.2f}"))
        self.liabilities_table_widget.setItem(2, 0, QTableWidgetItem(titel[2]))
        self.liabilities_table_widget.setItem(2, 1, QTableWidgetItem(str(non_current_liabilities.iat[0]/1e6)))
        non_current_liabilities_percentage = 100.0*non_current_liabilities.iat[0]/total_equity_and_liabilities
        self.liabilities_table_widget.setItem(2, 2, QTableWidgetItem(f"{non_current_liabilities_percentage:.2f}"))
        self.liabilities_table_widget.setItem(3, 0, QTableWidgetItem(titel[3]))
        self.liabilities_table_widget.setItem(3, 1, QTableWidgetItem(str(total_assets.iat[0]/1e6)))
        sum_percentage = total_equity_percentage+current_liabilities_percentage+non_current_liabilities_percentage
        self.liabilities_table_widget.setItem(3, 2, QTableWidgetItem(f"{sum_percentage:.2f}"))
        self.liabilities_table_widget.setHorizontalHeaderLabels(("Equity and liabilities", "Value [Mio. " + currency + "]", 
                                                                 "Percentage of\ntotal assets [%]"))   
            
    def set_equity(self, common_stock, treasury_stock, additional_paid_in_capital, retained_earnings, stockholder_equity,
                   minority_interest, total_equity, total_assets, currency):
        titel = ("Common stocks (Gezeichnetes Kapital)",
                 "Treasury stocks (Eigene Anteile)",
                  "Additional paid in capital (Kapitalrücklage)",
                  "Retained earnings (Gewinnrücklage)",
                  "Stockholder equity (Anteile der Eigentümer)",
                  "Minority interest (Anteile anderer Gesellschafter)", 
                  "Total equity (Eigenkapital)")
        total_assets_value = total_assets.iat[0]
        self.equity_table_widget.setItem(0, 0, QTableWidgetItem(titel[0]))
        self.equity_table_widget.setItem(0, 1, QTableWidgetItem(str(common_stock.iat[0]/1e6)))
        common_stock_percentage = 100.0*common_stock.iat[0]/total_assets_value
        self.equity_table_widget.setItem(0, 2, QTableWidgetItem(f"{common_stock_percentage:.2f}"))     
        self.equity_table_widget.setItem(1, 0, QTableWidgetItem(titel[1]))
        self.equity_table_widget.setItem(1, 1, QTableWidgetItem(str(-treasury_stock.iat[0]/1e6)))
        treasury_stock_percentage = 100.0*-treasury_stock.iat[0]/total_assets_value
        self.equity_table_widget.setItem(1, 2, QTableWidgetItem(f"{treasury_stock_percentage:.2f}"))     
        self.equity_table_widget.setItem(2, 0, QTableWidgetItem(titel[2]))
        self.equity_table_widget.setItem(2, 1, QTableWidgetItem(str(additional_paid_in_capital.iat[0]/1e6)))
        additional_paid_in_capital_percentage = 100.0*additional_paid_in_capital.iat[0]/total_assets_value
        self.equity_table_widget.setItem(2, 2, QTableWidgetItem(f"{additional_paid_in_capital_percentage:.2f}"))    
        self.equity_table_widget.setItem(3, 0, QTableWidgetItem(titel[3]))
        self.equity_table_widget.setItem(3, 1, QTableWidgetItem(str(retained_earnings.iat[0]/1e6)))
        retained_earnings_percentage = 100.0*retained_earnings.iat[0]/total_assets_value
        self.equity_table_widget.setItem(3, 2, QTableWidgetItem(f"{retained_earnings_percentage:.2f}"))       
        self.equity_table_widget.setItem(4, 0, QTableWidgetItem(titel[4]))
        self.equity_table_widget.setItem(4, 1, QTableWidgetItem(str(stockholder_equity.iat[0]/1e6)))
        stockholder_equity_percentage = 100.0*stockholder_equity.iat[0]/total_assets_value
        self.equity_table_widget.setItem(4, 2, QTableWidgetItem(f"{stockholder_equity_percentage:.2f}")) 
        self.equity_table_widget.setItem(5, 0, QTableWidgetItem(titel[5]))
        self.equity_table_widget.setItem(5, 1, QTableWidgetItem(str(minority_interest.iat[0]/1e6)))
        minority_interest_percentage = 100.0*minority_interest.iat[0]/total_assets_value
        self.equity_table_widget.setItem(5, 2, QTableWidgetItem(f"{minority_interest_percentage:.2f}")) 
        self.equity_table_widget.setItem(6, 0, QTableWidgetItem(titel[6]))
        self.equity_table_widget.setItem(6, 1, QTableWidgetItem(str(total_equity.iat[0]/1e6)))
        total_equity_percentage = 100.0*total_equity.iat[0]/total_assets_value
        self.equity_table_widget.setItem(6, 2, QTableWidgetItem(f"{total_equity_percentage:.2f}")) 
        self.equity_table_widget.setHorizontalHeaderLabels(("Equity", "Value [Mio. " + currency + "]", 
                                                            "Percentage of\ntotal assets [%]"))   
            