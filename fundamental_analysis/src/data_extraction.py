import datetime
import pandas as pd
from persistence import Persistence
import yfinance as yf


class FundamentalAnalysis:
    def __init__(self):
        super().__init__()
        self.persistence = Persistence()
        
    def get_financial_data(self, ticker_symbol):    
        # Get financial data from Yahoo finance
        try:
            ticker = yf.Ticker(ticker_symbol)
            
            # Company name
            self.long_name = ticker.info['longName']
        
            # The currency may vary with the ticker symbol
            self.currency = ticker.info.get('currency')
        
            # Annual revenue & net income (Jahresumsätze & Jahresgewinne)
            annual_financials = ticker.financials
            self.annual_revenue = annual_financials.loc['Total Revenue']
            self.annual_net_income = annual_financials.loc['Net Income']
            
            # Quarterly revenue & net income (Quartalsumsätze & Quartalsgewinne)
            quarterly_financials = ticker.quarterly_financials
            self.quarterly_revenue = quarterly_financials.loc['Total Revenue']
            self.quarterly_net_income = quarterly_financials.loc['Net Income']
            
            # Gross profit (Bruttogewinn)
            self.gross_profit = annual_financials.loc['Gross Profit']
            
            # Operating income (Betriebsgewinn)
            self.operating_income = annual_financials.loc['Operating Income']
            
            # Earnings per share (EPS) (Gewinn pro Aktie)
            self.earnings_per_share = annual_financials.loc['Basic EPS']
            
            # Earnings per share diluted (EPS dil.) (Verwässerter Gewinn pro Aktie)
            self.earnings_per_share_diluted = annual_financials.loc['Diluted EPS']
            
            # Balance sheet analysis
            balance_sheet = ticker.balance_sheet
            
            # Aktiva
            # Dummy date for no existing balance sheet entries
            dummy_series = pd.Series([0.0, 0.0, 0.0, 0.0],['None', 'None', 'None', 'None'])
            
            # Cash and cash equivalents (Zahlungsmittel und Zahlungsmittelequivalent)
            self.cash_and_cash_equivalents = balance_sheet.loc['Cash And Cash Equivalents']
            
            # Accounts receivable (Forderungen aus Lieferungen und Leistungen)
            self.accounts_receivable  = balance_sheet.loc['Accounts Receivable']
            
            # Other current assets (Sonstige finanzielle Vermögenswerte)
            if 'Other Current Assets' in balance_sheet.index:
                self.other_current_assets = balance_sheet.loc['Other Current Assets']
            else:
                self.other_current_assets = dummy_series  
                print('no other current assets')   
            
            # Other short term investments (Kurzfristige Finanzanlagen)
            if 'Other Short Term Investments' in balance_sheet.index:
                self.other_short_term_investments = balance_sheet.loc['Other Short Term Investments']
            else:
                self.other_short_term_investments = dummy_series
                print('no other short term investments')
            
            # Current assets (Kurzfristige Vermögenswerte)
            if 'Current Assets' in balance_sheet.index:
                self.current_assets = balance_sheet.loc['Current Assets']
            else:
                self.current_assets = dummy_series  
                print("no current assets")   
                       
            # Inventory (Vorräte)
            if 'Inventory' in balance_sheet.index:
                self.inventory = balance_sheet.loc['Inventory']  # Inventory gibt es nicht immer
            else:
                self.inventory = dummy_series
                print("no inventory")
                
            # Total assets (Bilanzsumme)
            self.total_assets = balance_sheet.loc['Total Assets'] # Gesamtkapital oder Bilanzsumme richtig
            
            # Passiva
            # Total Equity Gross Minority Interest (Gesamtes Eigenkapital)
            self.total_equity = balance_sheet.loc['Total Equity Gross Minority Interest']
            
            # Current liabilities (Kurzfristige Verbindlichkeiten)
            self.current_liabilities = balance_sheet.loc['Current Liabilities']
            
            # Accounts payable (Verbindlichkeiten aus Lieferungen und Leistungen)
            self.accounts_payable = balance_sheet.loc['Accounts Payable']
            
            # Total non current liabilities net minority interest (Langfristige Verbindlichkeiten)
            self.total_non_current_liabilities = balance_sheet.loc['Total Non Current Liabilities Net Minority Interest']          
                       
            # Equity
            # Common stock (Gezeichnetes Kapital)
            self.common_stock = balance_sheet.loc['Common Stock']
            
            # Treasury stock
            if 'Treasury Stock' in balance_sheet.index:
                self.treasury_stock = balance_sheet.loc['Treasury Stock']
            else:
                self.treasury_stock = dummy_series
                print("no treasury stock")
                
            # Additional paid in capital (Kapitalrücklage)
            if 'Additional Paid In Capital' in balance_sheet.index:
                self.additional_paid_in_capital = balance_sheet.loc['Additional Paid In Capital']
            else:
                self.additional_paid_in_capital = dummy_series
                print("no additional paid in capital")
            
            # Retained earnings (Gewinnrücklage)
            if 'Retained Earnings' in balance_sheet.index:
                self.retained_earnings = balance_sheet.loc['Retained Earnings']
            else:
                self.retained_earnings = dummy_series
                print("no retained earnings")
                
            # Miority interest (Anteil anderer Gesellschafter)
            if 'Minority Interest' in balance_sheet.index:
                self.minority_interest = balance_sheet.loc['Minority Interest']
            else:
                self.minority_interest = dummy_series
                print("no minority interest")     
                      
            # Stockholders Equity (Eigenkapital der Aktionäre)
            self.stockholders_equity = balance_sheet.loc['Stockholders Equity']
            
            # Earnings quality
            # Market value
            self.market_value = ticker.info['marketCap']

            # Operating cash flow
            self.operating_cash_flow = ticker.cashflow.loc['Operating Cash Flow']
            
            # Free cashflow
            self.free_cash_flow = ticker.cashflow.loc['Free Cash Flow']
            
            # Cash burn rate
            self.cash_burn_rate = self.cash_and_cash_equivalents.iat[0]/self.free_cash_flow.iat[0]
            
            # Cost of revenue
            self.cost_of_revenue = annual_financials.loc['Cost Of Revenue'] # Materialaufwand oder Equivalent für z.B. Service 
                   
            # Evaluation
            # Number of employees (Mitarbeiterzahl)
            self.number_of_employees = ticker.info['fullTimeEmployees']
            
            self.ebit = annual_financials.loc['EBIT']
            
            self.tax_rate = annual_financials.loc['Tax Provision'].iat[0]/annual_financials.loc['Pretax Income'].iat[0]

            # Interest expense (Zinsaufwand)
            self.interest_expense = annual_financials.loc['Interest Expense']
            
            self.number_shares_outstanding = ticker.info['sharesOutstanding']
            
            self.current_share_price = ticker.info['currentPrice']

            self.dividend_yield = ticker.info['dividendYield']

            self.annual_dividend = ticker.dividends.resample('YE').sum()

            # Convert the index into full years (e.g. 2024 instead of 2024-12-31)
            self.annual_dividend.index = self.annual_dividend.index.year

            # Exclude the actual incomplete year
            self.annual_dividend = self.annual_dividend[self.annual_dividend.index < datetime.datetime.now().year]
            
            self.forward_earnings_per_share = ticker.info['forwardEps']     
           
            self.peg_ratio = ticker.info['pegRatio']
            
            self.beta = ticker.info['beta']

            #for key, value in ticker.info.items():
            #    print("Key: ", key, "  Value: ", value)
            
            #for key, value in annual_financials.iterrows():
            #    print("key: ", key, " value: ", value)
                
            #for key, value in balance_sheet.iterrows():    
            #    print("key: ", key, " value: ", value)
            
            #for key, value in ticker.incomestmt.iterrows():
            #    print("key: ", key, " value: ", value)
            
            #for key, value in ticker.cashflow.iterrows():
            #    print("key: ", key, " value: ", value)
            
            #for key, value in ticker.dividends.iterrows():
            #  print("key: ", key, " value: ", value)
            
            #print(balance_sheet)
        except:
            return False
        return True
    
    def save_financial_data(self, file_name):
        self.persistence.open_analysis(file_name)
    
        self.persistence.set_long_name(self.long_name)
        self.persistence.set_currency(self.currency)
        self.persistence.set_annual_revenue(self.annual_revenue)
        self.persistence.set_annual_net_income(self.annual_net_income)
        self.persistence.set_quarterly_revenue(self.quarterly_revenue)
        self.persistence.set_quarterly_net_income(self.quarterly_net_income)
        self.persistence.set_gross_profit(self.gross_profit)
        self.persistence.set_operating_income(self.operating_income)
        self.persistence.set_earnings_per_share(self.earnings_per_share)
        self.persistence.set_earnings_per_share_diluted(self.earnings_per_share_diluted)
        self.persistence.set_total_equity(self.total_equity)
        self.persistence.set_current_liabilities(self.current_liabilities)
        self.persistence.set_total_non_current_liabilities(self.total_non_current_liabilities)
        self.persistence.set_total_assets(self.total_assets)
        self.persistence.set_cash_and_cash_eqivalents(self.cash_and_cash_equivalents)
        self.persistence.set_accounts_receivable(self.accounts_receivable)
        self.persistence.set_other_current_assets(self.other_current_assets)
        self.persistence.set_inventory(self.inventory)
        self.persistence.set_common_stock(self.common_stock)
        self.persistence.set_treasury_stock(self.treasury_stock)
        self.persistence.set_additional_paid_in_capital(self.additional_paid_in_capital)
        self.persistence.set_retained_earnings(self.retained_earnings)
        self.persistence.set_stockholders_equity(self.stockholders_equity)
        self.persistence.set_minority_interest(self.minority_interest)
        self.persistence.set_market_value(self.market_value)
        self.persistence.set_current_assets(self.current_assets)
        self.persistence.set_operating_cash_flow(self.operating_cash_flow)
        self.persistence.set_free_cash_flow(self.free_cash_flow)
        self.persistence.set_cash_burn_rate(self.cash_burn_rate) 
        self.persistence.set_ebit(self.ebit)
        self.persistence.set_tax_rate(self.tax_rate)
        self.persistence.set_interest_expense(self.interest_expense)
        self.persistence.set_number_of_employees(self.number_of_employees)
        self.persistence.set_cost_of_revenue(self.cost_of_revenue)
        self.persistence.set_accounts_payable(self.accounts_payable)
        self.persistence.set_current_share_price(self.current_share_price)
        self.persistence.set_number_shares_outstanding(self.number_shares_outstanding)
        self.persistence.set_dividend_yield(self.dividend_yield)
        self.persistence.set_annual_dividend(self.annual_dividend)
        self.persistence.set_forward_earnings_per_share(self.forward_earnings_per_share)
        self.persistence.set_peg_ratio(self.peg_ratio)
        self.persistence.set_other_short_term_investments(self.other_short_term_investments)
        self.persistence.set_beta(self.beta)
        
        self.persistence.close_analysis()
           
    def load_financial_data(self, file_name):       
        self.persistence.open_analysis(file_name)
            
        self.long_name = self.persistence.get_long_name()
        self.currency = self.persistence.get_currency()
        self.annual_revenue = self.persistence.get_annual_revenue()
        self.annual_net_income = self.persistence.get_annual_net_income()
        self.quarterly_revenue = self.persistence.get_quarterly_revenue()
        self.quarterly_net_income = self.persistence.get_quarterly_net_income()
        self.gross_profit = self.persistence.get_gross_profit()
        self.operating_income = self.persistence.get_operating_income()
        self.earnings_per_share = self.persistence.get_earnings_per_share()
        self.earnings_per_share_diluted = self.persistence.get_earnings_per_share_diluted()
        self.total_equity = self.persistence.get_total_equity()
        self.current_liabilities = self.persistence.get_current_liabilities()
        self.total_non_current_liabilities = self.persistence.get_total_non_current_liabilities()
        self.total_assets = self.persistence.get_total_assets()
        self.cash_and_cash_equivalents = self.persistence.get_cash_and_cash_equivalents()
        self.accounts_receivable = self.persistence.get_accounts_receivable() 
        self.other_current_assets = self.persistence.get_other_current_assets()
        self.inventory = self.persistence.get_inventory()
        self.common_stock = self.persistence.get_common_stock()
        self.treasury_stock = self.persistence.get_treasury_stock()
        self.additional_paid_in_capital = self.persistence.get_additional_paid_in_capital()
        self.retained_earnings = self.persistence.get_retained_earnings()
        self.stockholders_equity = self.persistence.get_stockholders_equity()
        self.minority_interest = self.persistence.get_minority_interest()
        self.market_value = self.persistence.get_market_value()
        self.current_assets = self.persistence.get_current_assets()
        self.operating_cash_flow = self.persistence.get_operating_cash_flow()
        self.free_cash_flow = self.persistence.get_free_cash_flow() 
        self.cash_burn_rate = self.persistence.get_cash_burn_rate() 
        self.ebit = self.persistence.get_ebit()
        self.tax_rate = self.persistence.get_tax_rate()
        self.interest_expense = self.persistence.get_interest_expense()
        self.number_of_employees = self.persistence.get_number_of_employees()
        self.cost_of_revenue = self.persistence.get_cost_of_revenue()
        self.accounts_payable = self.persistence.get_accounts_payable()
        self.current_share_price = self.persistence.get_current_share_price()
        self.number_shares_outstanding = self.persistence.get_number_shares_outstanding()
        self.dividend_yield = self.persistence.get_dividend_yield()
        self.annual_dividend = self.persistence.get_annual_dividend()
        self.forward_earnings_per_share = self.persistence.get_forward_earnings_per_share()
        self.peg_ratio = self.persistence.get_peg_ratio()
        self.other_short_term_investments = self.persistence.get_other_short_term_investments()
        self.beta = self.persistence.get_beta()
        
        self.persistence.close_analysis()    
                       
    def get_long_name(self):
        return self.long_name  
       
    def get_currency(self):
        return self.currency   
    
    # Income statement   
    def get_annual_revenue(self):
        return self.annual_revenue
    
    def get_annual_net_income(self):
        return self.annual_net_income
    
    def get_quarterly_revenue(self):
        return self.quarterly_revenue
        
    def get_quarterly_net_income(self):
        return self.quarterly_net_income
          
    def get_gross_profit(self):
        return self.gross_profit
    
    def get_operating_income(self):
        return self.operating_income
    
    def get_earnings_per_share(self):
        return self.earnings_per_share
    
    def get_earnings_per_share_diluted(self):
        return self.earnings_per_share_diluted
    
    # Balance sheet
    # Aktiva
    def get_cash_and_cash_equivalents(self):
        return self.cash_and_cash_equivalents
    
    def get_accounts_receivable(self):
        return self.accounts_receivable
    
    def get_other_current_assets(self):
        return self.other_current_assets
    
    def get_other_short_term_investments(self):
        return self.other_short_term_investments
    
    def get_current_assets(self):
        return self.current_assets
        
    def get_inventory(self):
        return self.inventory
    
    def get_total_assets(self):
        return self.total_assets
    
    # Passiva
    def get_total_equity(self):
        return self.total_equity
    
    def get_current_liabilities(self):
        return self.current_liabilities
    
    def get_accounts_payable(self):
        return self.accounts_payable
    
    def get_total_non_current_liabilities(self):
        return self.total_non_current_liabilities
    
    # Eigenkapital
    def get_common_stock(self):
        return self.common_stock
        
    def get_treasury_stock(self):
        return self.treasury_stock
    
    def get_additional_paid_in_capital(self):
        return self.additional_paid_in_capital
    
    def get_retained_earnings(self):
        return self.retained_earnings
    
    def get_stockholders_equity(self):
        return self.stockholders_equity
    
    def get_minority_interest(self):
        return self.minority_interest
    
    # Earnings quality
    def get_market_value(self):
        return self.market_value
        # shares outstanding: sind alle Aktien im Umlauf, jedoch nicht die vom Unternehmen zurückgekauften
        
    def get_operating_cash_flow(self):
        return self.operating_cash_flow    
        
    def get_free_cash_flow(self):
        return self.free_cash_flow    
        
    def get_cash_burn_rate(self):
        return self.cash_burn_rate    
        
    # Evaluation
    def get_number_of_employees(self):
        return self.number_of_employees
    
    def get_ebit(self):
        return self.ebit

    def get_tax_rate(self):
        return self.tax_rate
        
    def get_interest_expense(self):
        return self.interest_expense
        
    def get_number_shares_outstanding(self):
        return self.number_shares_outstanding
    
    def get_current_share_price(self):
        return self.current_share_price
        
    def get_dividend_yield(self):
        return self.dividend_yield
        
    def get_annual_dividend(self):
        return self.annual_dividend    
        
    def get_forward_earnings_per_share(self):
        return self.forward_earnings_per_share
              
    def get_peg_ratio(self):
        return self.peg_ratio          
               
    def get_beta(self):
        return self.beta
               
    def get_cost_of_revenue(self):
        return self.cost_of_revenue
    
   
        