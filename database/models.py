from sqlalchemy import Column, Integer, Text, Date, DateTime, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base


class Company(Base):
    __tablename__ = "company"

    id = Column(Integer, primary_key=True)
    company_name = Column(Text, nullable=False)
    cik = Column(Text, nullable=False)
    sic = Column(Text, nullable=False)

    # one-to-many → Security
    securities = relationship("Security", back_populates="company")


class Security(Base):
    __tablename__ = "security"

    id = Column(Integer, ForeignKey("company.id"), primary_key=True)
    company_id = Column(Integer, ForeignKey("company.id"), nullable=False)
    ticker_root = Column(Text)
    ticker_suffix = Column(Text)
    ticker = Column(Text, unique=True)
    is_active = Column(Boolean, default=True)
    list_date = Column(Date)
    delisted_utc = Column(Date)
    locale = Column(Text)

    # backrefs
    company = relationship("Company", back_populates="securities")
    prices = relationship(
        "Price", back_populates="security", cascade="all, delete-orphan"
    )
    fundamentals = relationship(
        "FundamentalSnapshot", back_populates="security", cascade="all, delete-orphan"
    )


class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    security_id = Column(Integer, ForeignKey("security.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    open = Column(Float)
    high = Column(Float)
    low = Column(Float)
    close = Column(Float)
    volume = Column(Float)

    security = relationship("Security", back_populates="prices")


class FundamentalSnapshot(Base):
    __tablename__ = "fundamental_snapshot"

    id = Column(Integer, primary_key=True)
    security_id = Column(Integer, ForeignKey("security.id"), nullable=False)
    report_date = Column(Date, nullable=False)
    fiscal_period = Column(Integer, nullable=False)

    security = relationship("Security", back_populates="fundamentals")
    income_statement = relationship(
        "IncomeStatement",
        uselist=False,
        back_populates="snapshot",
        cascade="all, delete-orphan",
    )
    balance_sheet = relationship(
        "BalanceSheet",
        uselist=False,
        back_populates="snapshot",
        cascade="all, delete-orphan",
    )
    cash_flow = relationship(
        "CashFlowStatement",
        uselist=False,
        back_populates="snapshot",
        cascade="all, delete-orphan",
    )


class IncomeStatement(Base):
    __tablename__ = "income_statement"

    id = Column(Integer, primary_key=True)
    snapshot_id = Column(
        Integer, ForeignKey("fundamental_snapshot.id"), nullable=False, unique=True
    )
    revenue = Column(Float, default=0.0)
    cost_of_revenue = Column(Float, default=0.0)
    gross_profit = Column(Float, default=0.0)
    operating_expense = Column(Float, default=0.0)
    selling_general_and_admin = Column(Float, default=0.0)
    depreciation_and_amortization = Column(Float, default=0.0)
    research_and_development = Column(Float, default=0.0)
    other_operating_expenses = Column(Float, default=0.0)
    operating_income_loss = Column(Float, default=0.0)
    interest_and_debt_expense = Column(Float, default=0.0)
    income_tax_expense_benefit = Column(Float, default=0.0)
    net_income_loss = Column(Float, default=0.0)
    basic_average_shares = Column(Float, default=0.0)
    diluted_average_shares = Column(Float, default=0.0)
    common_stock_dividends = Column(Float, default=0.0)

    snapshot = relationship("FundamentalSnapshot", back_populates="income_statement")


class BalanceSheet(Base):
    __tablename__ = "balance_sheet"

    id = Column(Integer, primary_key=True)
    snapshot_id = Column(
        Integer, ForeignKey("fundamental_snapshot.id"), nullable=False, unique=True
    )
    assets = Column(Float, default=0.0)
    current_assets = Column(Float, default=0.0)
    cash = Column(Float, default=0.0)
    accounts_receivable = Column(Float, default=0.0)
    inventory = Column(Float, default=0.0)
    prepaid_expenses = Column(Float, default=0.0)
    other_current_assets = Column(Float, default=0.0)
    noncurrent_assets = Column(Float, default=0.0)
    long_term_investments = Column(Float, default=0.0)
    fixed_assets = Column(Float, default=0.0)
    intangible_assets = Column(Float, default=0.0)
    non_current_prepaid_expense = Column(Float, default=0.0)
    other_noncurrent_assets = Column(Float, default=0.0)
    liabilities = Column(Float, default=0.0)
    current_liabilities = Column(Float, default=0.0)
    accounts_payable = Column(Float, default=0.0)
    interest_payable = Column(Float, default=0.0)
    wages = Column(Float, default=0.0)
    other_current_liabilities = Column(Float, default=0.0)
    noncurrent_liabilities = Column(Float, default=0.0)
    long_term_debt = Column(Float, default=0.0)
    other_noncurrent_liabilities = Column(Float, default=0.0)
    commitments_and_contingencies = Column(Float, default=0.0)
    equity = Column(Float, default=0.0)
    equity_attributable_to_noncontrolling = Column(Float, default=0.0)
    equity_attributable_to_parent = Column(Float, default=0.0)
    liabilities_and_equity = Column(Float, default=0.0)

    snapshot = relationship("FundamentalSnapshot", back_populates="balance_sheet")


class CashFlowStatement(Base):
    __tablename__ = "cash_flow_statement"

    id = Column(Integer, primary_key=True)
    snapshot_id = Column(
        Integer, ForeignKey("fundamental_snapshot.id"), nullable=False, unique=True
    )
    net_cash_flow_from_operating = Column(Float, default=0.0)
    net_cash_flow_from_investing = Column(Float, default=0.0)
    net_cash_flow_from_financing = Column(Float, default=0.0)
    net_cash_flow = Column(Float, default=0.0)

    snapshot = relationship("FundamentalSnapshot", back_populates="cash_flow")
