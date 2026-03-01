# Slide-by-Slide PPT Script (10-12 Slides)

## 1) Title + Objective
**Title:** Profit-Maximizing Recommendation System for a Zomato-like Platform  
**Narration:** We aim to recommend food items that optimize user relevance *and* business profitability.

## 2) Problem Statement
- Current recommenders focus mostly on CTR/relevance
- Limited consideration of margin, delivery feasibility, and repeat potential

## 3) Why Existing Recommendation Misses Profit Optimization
- High CTR items may have low margin
- Fast-selling items can still hurt SLA if prep is slow
- Discounts can over-subsidize baskets

## 4) Proposed End-to-End Architecture
Use the workflow diagram:
- Data sources
- Feature engineering
- Candidate generation
- Ranking
- Business rules
- Online serving
- Feedback loop
- Monitoring + A/B testing

## 5) Data Pipeline & Feature Categories
- User features: cuisine affinity, price sensitivity, past orders
- Item features: price, margin, category
- Context features: time-of-day, city zone, weather/event peaks
- Ops features: prep time, cancellation rate, SLA risk

## 6) Database Schema (ER Diagram)
Highlight core tables:
- users
- restaurants
- menu_items
- orders
- order_items
- user_events
- restaurant_metrics
- recommendation_logs

## 7) Recommendation Logic
- Candidate generation from user history + geo + trending
- Rule-based ranking score:
  `score = user_preference_match + ctr_signal + margin_weight + delivery_time_penalty`
- Business constraints: SLA threshold, fairness guardrails, promo budget caps

## 8) Dummy Demo Output
Show top 5 recommendations for sample user with score table from `scoring_demo.py`.

## 9) KPI and A/B Testing Framework
Primary metrics:
- Conversion rate
- AOV
- Margin/order
- Repeat purchase rate
Guardrail metrics:
- Cancellation rate
- Delivery SLA breaches
- Restaurant coverage fairness

## 10) Estimated Business Impact
Assumption example:
- +3% conversion
- +5% AOV
- +2% repeat rate
Use simulation output to estimate incremental monthly revenue and profit.

## 11) Risks & Mitigations
- Cold start users/restaurants → trending + geo + quality priors
- Ops volatility → real-time SLA penalties in ranking
- Bias towards large chains → fairness constraints per cohort

## 12) Roadmap
- **Phase 1:** rule-based baseline (this deliverable)
- **Phase 2:** learning-to-rank model with profit-aware objective
- **Phase 3:** contextual bandits + dynamic budget optimization
