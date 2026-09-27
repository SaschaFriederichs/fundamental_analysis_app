from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QLineEdit, QWidget, QSizePolicy


class FifthCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fifth Calculation")      
        
        # Profitability (Rentabilität)
        profitability_label = QLabel("<b>Profitability (Rentabilität)</b>")
        profitability_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
                            
        # Return on equity (Eigenkapitalrendite)
        self.return_on_equity_label = QLabel("Return on equity (Eigenkapitalrendite) [%]")
        self.return_on_equity_line_edit = QLineEdit()
        self.return_on_equity_line_edit.setEnabled(False)
        
        # Return on total capital (Gesamtkapitalrendite)
        self.return_on_total_capital_label = QLabel("Return on total capital (Gesamtkapitalrendite) [%]")
        self.return_on_total_capital_line_edit = QLineEdit()
        self.return_on_total_capital_line_edit.setEnabled(False)
        
        # Efficiency (Effizienz)
        efficiency_label = QLabel("<b>Efficiency (Effizienz)</b>")
        efficiency_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        # Employee productivity (Mitarbeiterproduktivität)
        self.employee_productivity_label = QLabel("Employee productivity (Mitarbeiterproduktivität) [Mio. EUR]")
        self.employee_productivity_line_edit = QLineEdit()
        self.employee_productivity_line_edit.setEnabled(False)
        
        # Accounts receivable turnover (Debitorenumschlag)
        self.days_sales_outstanding_label = QLabel("Days sales outstanding (Debitorenlaufzeit) [days]")
        self.days_sales_outstanding_line_edit = QLineEdit()
        self.days_sales_outstanding_line_edit.setEnabled(False)
        
        # Inventory turnover rate (Lagerumschlagshäufigkeit)
        self.inventory_turnover_period_label = QLabel("Inventory turnover period (Lagerumschlagsdauer) [days]")
        self.inventory_turnover_period_line_edit = QLineEdit()
        self.inventory_turnover_period_line_edit.setEnabled(False)
        
        # Accounts payable turnover rate (Kreditorenumsatz)
        self.accounts_payable_turnover_rate_label = QLabel("Accounts payable turnover rate (Kreditorenumsatz) [days]")
        self.accounts_payable_turnover_rate_line_edit = QLineEdit()
        self.accounts_payable_turnover_rate_line_edit.setEnabled(False)
        
        # Financial status (Finanzielle Lage)
        financial_situation_label = QLabel("<b>Financial situation (Finanzielle Lage)</b>")
        financial_situation_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        # Debt to equity ratio (Verschuldungsgrad)
        self.debt_to_equity_ratio_label = QLabel("Debt to equity ratio (Verschuldungsgrad) [%]")
        self.debt_to_equity_ratio_line_edit = QLineEdit()
        self.debt_to_equity_ratio_line_edit.setEnabled(False)
        
        # Current ratio (Liquidität 3. Grades)
        self.current_ratio_label = QLabel("Current ratio (Liquidität 3. Grades) [Ratio]")
        self.current_ratio_line_edit = QLineEdit()
        self.current_ratio_line_edit.setEnabled(False)
        
        # Quick ratio (Liquidität 2. Grades)
        self.quick_ratio_label = QLabel("Quick ratio (Liquidität 2. Grades) [Ratio]")
        self.quick_ratio_line_edit = QLineEdit()
        self.quick_ratio_line_edit.setEnabled(False)
        
        # Interest coverage ratio (Zinsdeckungsgrad)
        self.interest_coverage_ratio_label = QLabel("Interest coverage ratio (Zinsdeckungsgrad) [Ratio]")
        self.interest_coverage_ratio_line_edit = QLineEdit()
        self.interest_coverage_ratio_line_edit.setEnabled(False)
        
        # Fifth calculation widget and layout
        fifth_calculation_widget = QWidget()
        fifth_calculation_layout = QGridLayout()
        fifth_calculation_layout.addWidget(profitability_label, 0, 0)
        fifth_calculation_layout.addWidget(self.return_on_equity_label, 1, 0)
        fifth_calculation_layout.addWidget(self.return_on_equity_line_edit, 1, 1)
        fifth_calculation_layout.addWidget(self.return_on_total_capital_label, 2, 0)
        fifth_calculation_layout.addWidget(self.return_on_total_capital_line_edit, 2, 1)
        fifth_calculation_layout.addWidget(efficiency_label, 3, 0)
        fifth_calculation_layout.addWidget(self.employee_productivity_label, 4, 0)
        fifth_calculation_layout.addWidget(self.employee_productivity_line_edit, 4, 1)
        fifth_calculation_layout.addWidget(self.days_sales_outstanding_label, 5, 0)
        fifth_calculation_layout.addWidget(self.days_sales_outstanding_line_edit, 5, 1)
        fifth_calculation_layout.addWidget(self.inventory_turnover_period_label, 6, 0)
        fifth_calculation_layout.addWidget(self.inventory_turnover_period_line_edit, 6, 1)
        fifth_calculation_layout.addWidget(self.accounts_payable_turnover_rate_label, 7, 0)
        fifth_calculation_layout.addWidget(self.accounts_payable_turnover_rate_line_edit, 7, 1)
        fifth_calculation_layout.addWidget(financial_situation_label, 8, 0)
        fifth_calculation_layout.addWidget(self.debt_to_equity_ratio_label, 9, 0)
        fifth_calculation_layout.addWidget(self.debt_to_equity_ratio_line_edit, 9, 1)
        fifth_calculation_layout.addWidget(self.current_ratio_label, 10, 0)
        fifth_calculation_layout.addWidget(self.current_ratio_line_edit, 10, 1)
        fifth_calculation_layout.addWidget(self.quick_ratio_label, 11, 0)
        fifth_calculation_layout.addWidget(self.quick_ratio_line_edit, 11, 1)
        fifth_calculation_layout.addWidget(self.interest_coverage_ratio_label, 12, 0)
        fifth_calculation_layout.addWidget(self.interest_coverage_ratio_line_edit, 12, 1)
        fifth_calculation_widget.setLayout(fifth_calculation_layout)
        self.setCentralWidget(fifth_calculation_widget)  
        
    def set_return_on_equity(self, annual_net_income, total_equity):
        average_total_equity = (total_equity.iat[0] + total_equity.iat[1])/2.0
        return_on_equity_percentage = 100.0*annual_net_income.iat[0]/average_total_equity
        self.return_on_equity_line_edit.setText(f"{return_on_equity_percentage:.2f}")
        
    def set_return_on_total_capital(self, ebit, tax_rate, interest_expense, total_assets):    
        tax_adjusted_ebit = ebit.iat[0]*(1.0-tax_rate)
        average_total_capital = (total_assets.iat[0]+total_assets.iat[1])/2.0
        return_on_total_capital_percentage = 100.0*(tax_adjusted_ebit+interest_expense.iat[0])/average_total_capital
        self.return_on_total_capital_line_edit.setText(f"{return_on_total_capital_percentage:.2f}")
        
    def set_employee_productivity(self, annual_revenue, employees, currency):
        employee_productivity = annual_revenue.iat[0]/employees/1e6
        self.employee_productivity_line_edit.setText(f"{employee_productivity:.3f}")
        self.employee_productivity_label.setText("Employee productivity (Mitarbeiterproduktivität) [Mio. " + currency + "]")
            
    def set_days_sales_outstanding(self, accounts_receivable, annual_revenue):
        average_accounts_receivable = (accounts_receivable.iat[0]+accounts_receivable.iat[1])/2.0
        days_sales_outstanding = 365*average_accounts_receivable/annual_revenue.iat[0]
        self.days_sales_outstanding_line_edit.setText(f"{days_sales_outstanding:.2f}")

    def set_inventory_turnover_period(self, inventory, cost_of_revenue):    
        average_inventory = (inventory.iat[0]+inventory.iat[1])/2.0
        inventory_turnover_period = 365*average_inventory/cost_of_revenue.iat[0]
        self.inventory_turnover_period_line_edit.setText(f"{inventory_turnover_period:.2f}")
    
    def set_accounts_payable_turnover_rate(self, accounts_payable, inventory, cost_of_revenue):
        average_accounts_payable = (accounts_payable.iat[0]+accounts_payable.iat[1])/2.0
        difference_inventory = inventory.iat[0]-inventory.iat[1]
        cost_of_goods_sold = cost_of_revenue.iat[0]
        accounts_payable_turnover_rate = 365*average_accounts_payable/(difference_inventory+cost_of_goods_sold)
        self.accounts_payable_turnover_rate_line_edit.setText(f"{accounts_payable_turnover_rate:.2f}")
      
    def set_debt_to_equity_ratio(self, total_current_liabilities, total_non_current_liabilities, total_equity): 
        debt_to_equity_ratio = 100.0*(total_current_liabilities.iat[0]+total_non_current_liabilities.iat[0])/total_equity.iat[0]
        self.debt_to_equity_ratio_line_edit.setText(f"{debt_to_equity_ratio:.2f}")
        
    def set_current_ratio(self, current_assets, current_liabilities):
        current_ratio = current_assets.iat[0]/current_liabilities.iat[0]
        self.current_ratio_line_edit.setText(f"{current_ratio:.2f}")    
        
    def set_quick_ratio(self, current_assets, inventory, current_liabilities):
        quick_ratio = (current_assets.iat[0]-inventory.iat[0])/current_liabilities.iat[0]
        self.quick_ratio_line_edit.setText(f"{quick_ratio:.2f}")
    
    def set_interest_coverage_ratio(self, ebit, interest_expense):
        interest_coverage_ratio = ebit.iat[0]/interest_expense.iat[0]
        self.interest_coverage_ratio_line_edit.setText(f"{interest_coverage_ratio:.2f}")
            
    
                