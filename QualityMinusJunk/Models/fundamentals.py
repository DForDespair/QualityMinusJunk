from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional
from enum import Enum

class FiscalPeriod(Enum):
    Q1: 1
    Q2: 2
    Q3: 3
    Q4: 4


@dataclass
class IncomeStatement:
    revenue: float = 0.0
    cost_of_revenue: float = 0.0
    gross_profit: float = 0.0
    operating_expense: float = 0.0
    selling_general_and_administrative_expenses: float = 0.0
    depreciation_and_amortization: float = 0.0
    research_and_development: float = 0.0
    other_operating_expenses: float = 0.0
    operating_income_loss: float = 0.0
    interest_and_debt_expense: float = 0.0
    income_tax_expense_benefit: float = 0.0
    net_income_loss: float = 0.0
    basic_average_shares: float = 0.0
    diluted_average_shares: float = 0.0
    common_stock_dividends: float = 0.0


@dataclass
class BalanceSheet:
    assets: float = 0.0
    current_assets: float = 0.0
    cash: float = 0.0
    accounts_receivable: float = 0.0
    inventory: float = 0.0
    prepaid_expenses: float = 0.0
    other_current_assets: float = 0.0
    noncurrent_assets: float = 0.0
    long_term_investments: float = 0.0
    fixed_assets: float = 0.0
    intangible_assets: float = 0.0
    non_current_prepaid_expense: float = 0.0
    other_noncurrent_assets: float = 0.0
    liabilities: float = 0.0
    current_liabilities: float = 0.0
    accounts_payable: float = 0.0
    interest_payable: float = 0.0
    wages: float = 0.0
    other_current_liabilities: float = 0.0
    noncurrent_liabilities: float = 0.0
    long_term_debt: float = 0.0
    other_noncurrent_liabilities: float = 0.0
    commitments_and_contingencies: float = 0.0
    equity: float = 0.0
    equity_attributable_to_noncontrolling_interest: float = 0.0
    equity_attributable_to_parent: float = 0.0
    liabilities_and_equity: float = 0.0


@dataclass
class CashFlowStatement:
    net_cash_flow_from_operating_activities: float = 0.0
    net_cash_flow_from_investing_activities: float = 0.0
    net_cash_flow_from_financing_activities: float = 0.0
    net_cash_flow: float = 0.0
    
@dataclass
class FundamentalSnapshot:
    report_date: datetime
    fiscal_period: FiscalPeriod
    income_statement: IncomeStatement
    balance_sheet: BalanceSheet
    cash_flow_statement: CashFlowStatement    
