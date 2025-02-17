def calculate_growth(current, previous):
    if previous == 0:
        return None  # Avoid division by zero
    return ((current - previous) / previous) * 100

def calculate_pe(stock_price, eps):
    if eps == 0:
        return None  # Avoid division by zero
    return stock_price / eps

def calculate_peg(pe, eps_growth):
    if eps_growth == 0:
        return None  # Avoid division by zero
    return pe / eps_growth

def calculate_roe(net_income, shareholder_equity):
    if shareholder_equity == 0:
        return None  # Avoid division by zero
    return (net_income / shareholder_equity) * 100

def classify_pe(pe):
    if pe is None:
        return "N/A"
    if pe < 15:
        return "Cheap (Undervalued)"
    elif 15 <= pe <= 25:
        return "Reasonable (Fair Value)"
    else:
        return "Expensive (Overvalued)"

def classify_peg(peg):
    if peg is None:
        return "N/A"
    if peg < 1.0:
        return "Cheap (Undervalued)"
    elif 1.0 <= peg <= 2.0:
        return "Reasonable (Fair Value)"
    else:
        return "Expensive (Overvalued)"

def analyze_stock():
    # User Inputs
    current_revenue = float(input("Enter current year revenue: "))
    previous_revenue = float(input("Enter previous year revenue: "))
    current_eps = float(input("Enter current EPS: "))
    previous_eps = float(input("Enter previous EPS: "))
    stock_price = float(input("Enter stock price: "))
    net_income = float(input("Enter net income: "))
    total_shares = float(input("Enter total shares outstanding: "))
    shareholder_equity = float(input("Enter shareholder equity: "))
    
    # Calculations
    revenue_growth = calculate_growth(current_revenue, previous_revenue)
    eps_growth = calculate_growth(current_eps, previous_eps)
    eps = net_income / total_shares if total_shares != 0 else None
    pe = calculate_pe(stock_price, eps)
    peg = calculate_peg(pe, eps_growth)
    roe = calculate_roe(net_income, shareholder_equity)
    
    # Analysis
    print("\nStock Analysis Report:")
    print(f"Revenue Growth: {revenue_growth:.2f}%")
    print(f"EPS Growth: {eps_growth:.2f}%")
    print(f"P/E Ratio: {pe:.2f} ({classify_pe(pe)})")
    print(f"PEG Ratio: {peg:.2f} ({classify_peg(peg)})")
    print(f"ROE: {roe:.2f}%")
    
    # Final Verdict
    if revenue_growth >= 10 and eps_growth >= 10 and pe < 25 and peg < 1.5 and roe > 15:
        print("✅ This stock meets NAIC criteria for a strong investment.")
    else:
        print("❌ This stock does not fully meet NAIC criteria.")

# Run the stock analysis
analyze_stock()
