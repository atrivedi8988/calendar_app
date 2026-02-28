"""Business impact back-of-the-envelope simulation."""


def simulate_impact(
    monthly_orders: int = 1_000_000,
    baseline_conversion: float = 0.20,
    baseline_aov: float = 320.0,
    baseline_margin_pct: float = 0.22,
    conversion_lift: float = 0.03,
    aov_lift: float = 0.05,
    repeat_rate_lift: float = 0.02,
) -> dict[str, float]:
    baseline_revenue = monthly_orders * baseline_conversion * baseline_aov
    baseline_profit = baseline_revenue * baseline_margin_pct

    improved_conversion = baseline_conversion * (1 + conversion_lift)
    improved_aov = baseline_aov * (1 + aov_lift)
    effective_orders = monthly_orders * improved_conversion * (1 + repeat_rate_lift)

    improved_revenue = effective_orders * improved_aov
    improved_profit = improved_revenue * baseline_margin_pct

    return {
        "baseline_revenue": baseline_revenue,
        "improved_revenue": improved_revenue,
        "incremental_revenue": improved_revenue - baseline_revenue,
        "baseline_profit": baseline_profit,
        "improved_profit": improved_profit,
        "incremental_profit": improved_profit - baseline_profit,
    }


def main() -> None:
    result = simulate_impact()
    print("Monthly Business Impact Simulation")
    print("-" * 40)
    for key, value in result.items():
        print(f"{key:>20}: INR {value:,.2f}")


if __name__ == "__main__":
    main()
