from PySide6.QtWidgets import QMainWindow, QLabel, QGridLayout, QLineEdit, QWidget, QSizePolicy


class SeventhCalculation(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Fifth Calculation")      
        
        # Evaluation (Bewertung)
        evaluation_label = QLabel("<b>Evaluation (Bewertung)</b>")
        evaluation_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        # Total cash per share (Barmittel pro Aktie)
        self.total_cash_per_share_label = QLabel("Total cash per share (Barmittel pro Aktie) [EUR]")
        self.total_cash_per_share_line_edit = QLineEdit()
        self.total_cash_per_share_line_edit.setEnabled(False)
        
        # Management efficiency (Effektivität des Managements)
        management_efficiency_label = QLabel("<b>Management efficiency (Effektivität des Managements)</b>")
        management_efficiency_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        # Return on assets (Vermögensrendite) 
        self.return_on_assets_label = QLabel("Return on assets (Vermögensrendite) [%]")
        self.return_on_assets_line_edit = QLineEdit()
        self.return_on_assets_line_edit.setEnabled(False)
        
        # Intrinsic value (Innerer Wert)
        intrinsic_value_label = QLabel("<b>Intrinsic value (Innerer Wert)</b>")
        intrinsic_value_label.setSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        
        # Share value according to dividend discount model (Aktienwert nach Dividendendiskontierungsmodell)
        self.share_value_dividend_discount_model_label = QLabel("Share value according to dividend discount model\
        \n(Aktienwert nach Dividendendiskontierungsmodell) [EUR]")
        self.share_value_dividend_discount_model_line_edit = QLineEdit()
        self.share_value_dividend_discount_model_line_edit.setEnabled(False)
        
        # Share value according to discounted cashflow analysis
        self.share_value_discounted_cashflow_analysis_label = QLabel("Share value according to discounted cashflow analysis (DCF)\
        \n(Aktienwert nach Discounted-Cashflow-Verfahren) [EUR]")
        self.share_value_discounted_cashflow_analysis_line_edit = QLineEdit()
        self.share_value_discounted_cashflow_analysis_line_edit.setEnabled(False)
        
        # Sixth calculation widget and layout
        sixth_calculation_widget = QWidget()
        sixth_calculation_layout = QGridLayout()
        sixth_calculation_layout.addWidget(evaluation_label, 0, 0)
        sixth_calculation_layout.addWidget(self.total_cash_per_share_label, 1, 0)
        sixth_calculation_layout.addWidget(self.total_cash_per_share_line_edit, 1, 1)
        sixth_calculation_layout.addWidget(management_efficiency_label, 2, 0)
        sixth_calculation_layout.addWidget(self.return_on_assets_label, 3, 0)
        sixth_calculation_layout.addWidget(self.return_on_assets_line_edit, 3, 1)
        sixth_calculation_layout.addWidget(intrinsic_value_label, 4, 0)
        sixth_calculation_layout.addWidget(self.share_value_dividend_discount_model_label, 5, 0)
        sixth_calculation_layout.addWidget(self.share_value_dividend_discount_model_line_edit, 5, 1)
        sixth_calculation_layout.addWidget(self.share_value_discounted_cashflow_analysis_label, 6, 0)
        sixth_calculation_layout.addWidget(self.share_value_discounted_cashflow_analysis_line_edit, 6, 1)
        sixth_calculation_widget.setLayout(sixth_calculation_layout)
        self.setCentralWidget(sixth_calculation_widget)  
        
    def set_total_cash_per_share(self, number_shares_outstanding, cash_and_cash_equivalent, short_term_investments, currency):
        total_cash_per_share = (cash_and_cash_equivalent.iat[0]+short_term_investments.iat[0])/number_shares_outstanding
        self.total_cash_per_share_line_edit.setText(f"{total_cash_per_share:.2f}")
        self.total_cash_per_share_label.setText("Total cash per share (Barmittel pro Aktie) [" + currency + "]")

    def set_return_on_assets(self, ebit, tax_rate, total_assets):
        tax_adjusted_ebit = ebit.iat[0]*(1.0-tax_rate)
        average_assets = (total_assets.iat[0]+total_assets.iat[1])/2.0
        return_on_assets = 100.0*tax_adjusted_ebit/average_assets
        self.return_on_assets_line_edit.setText(f"{return_on_assets:.2f}")     
   
    def set_share_value_dividend_discount_model(self, annual_dividend, beta, currency):
        risk_free_rate = 0.035
        growth_rate = 0.085
        long_term_growth_rate = 0.03
        
        # Calculate the CAPM discount rate (CAPM Abzinsungssatz)
        capm_discount_rate = risk_free_rate+(growth_rate-risk_free_rate)*beta
        required_profit = capm_discount_rate

        # Calculate the dividend discount model (Dividendendiskontierungsmodell)
        fair_value = annual_dividend.iat[-1]*(1.0+long_term_growth_rate)/(required_profit-long_term_growth_rate)
        self.share_value_dividend_discount_model_line_edit.setText(f"{fair_value:.2f}")  
        self.share_value_dividend_discount_model_label.setText("Share value according to dividend discount model\
        \n(Aktienwert nach Dividendendiskontierungsmodell) [" + currency + "]")
        
        #print("Required profit ", required_profit)
        #print("Annual dividend ", annual_dividend.iat[-1])

        
    def set_share_value_discounted_cashflow_analysis(self, beta, free_cashflow, number_shares_outstanding, currency):
        risk_free_rate = 0.035
        growth_rate = 0.085
        long_term_growth_rate = 0.03
        
        # Calculate the CAPM discount rate (CAPM Abzinsungssatz)
        capm_discount_rate = risk_free_rate+(growth_rate-risk_free_rate)*beta
        
        # Calculate future cash flows 
        future_free_cashflows = []
        for i in range(5):
            if i == 0:
                future_free_cashflows.append(free_cashflow.iat[0]*(1.0+growth_rate))
            else:
                future_free_cashflows.append(future_free_cashflows[i-1]*(1.0+growth_rate)) 
        
        # Calculate the residual value of future cash flows
        future_free_cashflow_residual_value = future_free_cashflows[4]*(1.0+long_term_growth_rate)/(capm_discount_rate-long_term_growth_rate)
        
        # Calculate discounted free cash flows
        discounted_free_cashflows = []
        for i in range(5):
            discounted_free_cashflows.append(future_free_cashflows[i]/(1.0+capm_discount_rate)**(i+1))
        
        # Calculate discounted residual value of free cash flows 
        discounted_free_cashflow_residual_value = future_free_cashflow_residual_value/(1.0+capm_discount_rate)**5
        
        # Calculate the intrinsic company value
        intrinsic_value = 0
        for i in range(5):
            intrinsic_value += discounted_free_cashflows[i]
        intrinsic_value += discounted_free_cashflow_residual_value
        
        # Calculate the intrinsic value per share
        inner_value_per_share = intrinsic_value/number_shares_outstanding
        self.share_value_discounted_cashflow_analysis_line_edit.setText(f"{inner_value_per_share:.2f}")
        self.share_value_discounted_cashflow_analysis_label.setText("Share value according to discounted cashflow analysis (DCF)\
        \n(Aktienwert nach Discounted-Cashflow-Verfahren) [" + currency + "]")  
        
        #print("CAPM ",capm_discount_rate)
        #print("Beta ", beta)
        #print("Free cashflow ", free_cashflow.iat[0])
        #print("Future free cashflows ", future_free_cashflows)
        #print("Residual value future free cashflows ", future_free_cashflow_residual_value)
        #print("Discounted free cashflows ", discounted_free_cashflows)
        #print("Discounted residual value of free cashflows ", discounted_free_cashflow_residual_value)
        #print("inner value ", intrinsic_value)
        #print("Inner value per share ", inner_value_per_share)
        
        
        
        