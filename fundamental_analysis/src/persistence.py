import shelve


class Persistence:
    def __init__(self):
        self.analysis_data = None
    
    def open_analysis(self, file_name):
        self.analysis_data = shelve.open(file_name)
    
    def close_analysis(self):
        self.analysis_data.close()
    
    def set_long_name(self, long_name):
        self.analysis_data['long_name'] = long_name
    
    def get_long_name(self):
        return self.analysis_data['long_name']
    
    def set_currency(self, currency):
        self.analysis_data['currency'] = currency
        
    def get_currency(self):
        return self.analysis_data['currency']
    
    def set_annual_revenue(self, annual_revenue):
        self.analysis_data['annual revenue'] = annual_revenue
        
    def get_annual_revenue(self):
        return self.analysis_data['annual revenue']
    
    def set_annual_net_income(self, annual_net_income):
        self.analysis_data['annual net income'] = annual_net_income
        
    def get_annual_net_income(self):
        return self.analysis_data['annual net income']
    
    def set_quarterly_revenue(self, quarterly_revenue):
        self.analysis_data['quarterly revenue'] = quarterly_revenue
        
    def get_quarterly_revenue(self):
        return self.analysis_data['quarterly revenue']
    
    def set_quarterly_net_income(self, quarterly_net_income):
        self.analysis_data['quarterly net income'] = quarterly_net_income
        
    def get_quarterly_net_income(self):
        return self.analysis_data['quarterly net income']
    
    def set_gross_profit(self, gross_profit): # Bruttogewinn
        self.analysis_data['gross profit'] = gross_profit
        
    def get_gross_profit(self): # Bruttogewinn
        return self.analysis_data['gross profit']
    
    def set_operating_income(self, operating_income): # Betriebsgewinn
        self.analysis_data['operating income'] = operating_income
        
    def get_operating_income(self): # Betriebsgewinn
        return self.analysis_data['operating income']
    
    def set_earnings_per_share(self, earnings_per_share):
        self.analysis_data['earnings per share'] = earnings_per_share 
        
    def get_earnings_per_share(self):
        return self.analysis_data['earnings per share']
    
    def set_earnings_per_share_diluted(self, earnings_per_share_diluted):
        self.analysis_data['earnings per share diluted'] = earnings_per_share_diluted 
        
    def get_earnings_per_share_diluted(self):
        return self.analysis_data['earnings per share diluted']
    
    def set_total_equity(self, total_equity):
        self.analysis_data['total equity'] = total_equity 
        
    def get_total_equity(self):
        return self.analysis_data['total equity']
    
    def set_current_liabilities(self, current_liabilities):
        self.analysis_data['current liabilities'] = current_liabilities 
        
    def get_current_liabilities(self):
        return self.analysis_data['current liabilities']
    
    def set_total_non_current_liabilities(self, total_non_current_liabilities):
        self.analysis_data['total non current liabilities'] = total_non_current_liabilities 
        
    def get_total_non_current_liabilities(self):
        return self.analysis_data['total non current liabilities']
        
    def set_total_assets(self, total_assets):
        self.analysis_data['total assets'] = total_assets
        
    def get_total_assets(self):
        return self.analysis_data['total assets']
    
    def set_cash_and_cash_eqivalents(self, cash_and_cash_equivalents):
        self.analysis_data['cash and cash equivalents'] = cash_and_cash_equivalents
        
    def get_cash_and_cash_equivalents(self):
        return self.analysis_data['cash and cash equivalents']
    
    def set_accounts_receivable(self, accounts_receivable): # Forderungen aus Lieferungen und Leistungen
        self.analysis_data['accounts receivable'] = accounts_receivable
        
    def get_accounts_receivable(self): # Forderungen aus Lieferungen und Leistungen 
        return self.analysis_data['accounts receivable']
    
    def set_other_current_assets(self, other_current_assets): # Andere kurzfristige Vermögenswerte
        self.analysis_data['other current assets'] = other_current_assets
        
    def get_other_current_assets(self): # Andere kurzfristige Vermögenswerte
        return self.analysis_data['other current assets']
    
    def set_inventory(self, inventory): # Vorräte
        self.analysis_data['inventory'] = inventory
        
    def get_inventory(self): # Vorräte
        return self.analysis_data['inventory']
    
    def set_common_stock(self, common_stock): # Stammaktien
        self.analysis_data['common stock'] = common_stock
        
    def get_common_stock(self): # Stammaktien
        return self.analysis_data['common stock']
    
    def set_treasury_stock(self, treasury_stock): # eigene Aktien des Unternehmens
        self.analysis_data['treasury stock'] = treasury_stock
        
    def get_treasury_stock(self): # eigene Aktien des Unternehmens
        return self.analysis_data['treasury stock']
    
    def set_additional_paid_in_capital(self, additional_paid_in_capital): # Kapitalrücklage
        self.analysis_data['additional paid in capital'] = additional_paid_in_capital
        
    def get_additional_paid_in_capital(self): # Kapitalrücklage
        return self.analysis_data['additional paid in capital']
    
    def set_retained_earnings(self, retained_earnings): # Gewinnrücklagen
        self.analysis_data['retained earnings'] = retained_earnings
        
    def get_retained_earnings(self): # Gewinnrücklagen
        return self.analysis_data['retained earnings']

    def set_stockholders_equity(self, stockholders_equity):
        self.analysis_data['stockholders equity'] = stockholders_equity
        
    def get_stockholders_equity(self):
        return self.analysis_data['stockholders equity']
    
    def set_minority_interest(self, minority_interest): # Minderheitenanteil
        self.analysis_data['minority interest'] = minority_interest
        
    def get_minority_interest(self): # Minderheitenanteil
        return self.analysis_data['minority interest']
  
    def set_market_value(self, market_value):
        self.analysis_data['market value'] = market_value
                
    def get_market_value(self):
        return self.analysis_data['market value']   
    
    def set_current_assets(self, current_assets): # Umlaufvermögen
        self.analysis_data['current assets'] = current_assets
        
    def get_current_assets(self): # Umlaufvermögen
        return self.analysis_data['current assets']
    
    def set_operating_cash_flow(self, operating_cash_flow): # Cashflow aus Betriebstätigkeit
        self.analysis_data['operating cash flow'] = operating_cash_flow
        
    def get_operating_cash_flow(self): # Cashflow aus Betriebstätigkeit
        return self.analysis_data['operating cash flow']
            
    def set_free_cash_flow(self, free_cash_flow): 
        self.analysis_data['free cash flow'] = free_cash_flow
        
    def get_free_cash_flow(self): 
        return self.analysis_data['free cash flow']
    
    def set_cash_burn_rate(self, cash_burn_rate): 
        self.analysis_data['cash burn rate'] = cash_burn_rate
        
    def get_cash_burn_rate(self): 
        return self.analysis_data['cash burn rate']
    
    def set_ebit(self, ebit):
        self.analysis_data['EBIT'] = ebit
        
    def get_ebit(self):
        return self.analysis_data['EBIT']
    
    def set_tax_rate(self, tax_rate):
        self.analysis_data['tax rate'] = tax_rate
        
    def get_tax_rate(self):
        return self.analysis_data['tax rate']
               
    def set_interest_expense(self, interest_expense): # Zinsaufwand
        self.analysis_data['interest expense'] = interest_expense
        
    def get_interest_expense(self): # Zinsaufwand
        return self.analysis_data['interest expense']
    
    def set_number_of_employees(self, number_of_employees):
        self.analysis_data['number of employees'] = number_of_employees
        
    def get_number_of_employees(self):
        return self.analysis_data['number of employees']
    
    def set_cost_of_revenue(self, cost_of_revenue): # Kosten der verkauften Waren
        self.analysis_data['cost of revenue'] = cost_of_revenue
        
    def get_cost_of_revenue(self): # Kosten der verkauften Waren
        return self.analysis_data['cost of revenue']
    
    def set_accounts_payable(self, accounts_payable): # Verbindlichkeiten aus Lieferungen und Leistungen
        self.analysis_data['accounts payable'] = accounts_payable
        
    def get_accounts_payable(self): # Verbindlichkeiten aus Lieferungen und Leistungen
        return self.analysis_data['accounts payable']
    
    def set_current_share_price(self, current_share_price):
        self.analysis_data['current share price'] = current_share_price
        
    def get_current_share_price(self):
        return self.analysis_data['current share price']
    
    def set_number_shares_outstanding(self, number_shares_outstanding):
        self.analysis_data['number shares outstanding'] = number_shares_outstanding
        
    def get_number_shares_outstanding(self):
        return self.analysis_data['number shares outstanding']
    
    def set_dividend_yield(self, dividend_yield): # Dividendenrendite
        self.analysis_data['dividend yield'] = dividend_yield
        
    def get_dividend_yield(self): # Dividendenrendite
        return self.analysis_data['dividend yield']
    
    def set_annual_dividend(self, annual_dividend):
        self.analysis_data['annual dividend'] = annual_dividend
        
    def get_annual_dividend(self):
        return self.analysis_data['annual dividend']
    
    def set_forward_earnings_per_share(self, forward_earnings_per_share):
        self.analysis_data['forward earnings per share'] = forward_earnings_per_share
 
    def get_forward_earnings_per_share(self):
        return self.analysis_data['forward earnings per share'] 
       
    def set_peg_ratio(self, peg_ratio): # Kurs-Gewinn-Wachstums-Verhältnis KGWV
        self.analysis_data['peg ratio'] = peg_ratio
        
    def get_peg_ratio(self): # Kurs-Gewinn-Wachstums-Verhältnis KGWV
        return self.analysis_data['peg ratio']
    
    def set_other_short_term_investments(self, other_short_term_investments): # sonstige kurzfristige Finanzanlagen
        self.analysis_data['other short term investments'] = other_short_term_investments
        
    def get_other_short_term_investments(self): # sonstige kurzfristige Finanzanlagen
        return self.analysis_data['other short term investments']
    
    def set_beta(self, beta):
        self.analysis_data['beta'] = beta
        
    def get_beta(self):
        return self.analysis_data['beta']
    
        
        
        
            
        
    