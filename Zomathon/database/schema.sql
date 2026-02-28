CREATE TABLE users (
  user_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT,
  preferred_cuisine TEXT,
  veg_preference BOOLEAN,
  signup_date TIMESTAMP
);

CREATE TABLE restaurants (
  restaurant_id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  city TEXT,
  cuisine TEXT,
  avg_rating NUMERIC(3,2),
  is_active BOOLEAN DEFAULT TRUE
);

CREATE TABLE menu_items (
  item_id INTEGER PRIMARY KEY,
  restaurant_id INTEGER NOT NULL REFERENCES restaurants(restaurant_id),
  item_name TEXT NOT NULL,
  category TEXT,
  price NUMERIC(10,2) NOT NULL,
  cost NUMERIC(10,2) NOT NULL,
  is_available BOOLEAN DEFAULT TRUE
);

CREATE TABLE orders (
  order_id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(user_id),
  restaurant_id INTEGER NOT NULL REFERENCES restaurants(restaurant_id),
  order_timestamp TIMESTAMP NOT NULL,
  status TEXT,
  total_amount NUMERIC(10,2),
  discount_amount NUMERIC(10,2) DEFAULT 0,
  delivery_time_min INTEGER
);

CREATE TABLE order_items (
  order_item_id INTEGER PRIMARY KEY,
  order_id INTEGER NOT NULL REFERENCES orders(order_id),
  item_id INTEGER NOT NULL REFERENCES menu_items(item_id),
  quantity INTEGER NOT NULL,
  unit_price NUMERIC(10,2) NOT NULL
);

CREATE TABLE user_events (
  event_id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(user_id),
  item_id INTEGER NOT NULL REFERENCES menu_items(item_id),
  event_type TEXT CHECK (event_type IN ('view', 'click', 'add_to_cart')),
  event_timestamp TIMESTAMP NOT NULL,
  session_id TEXT
);

CREATE TABLE restaurant_metrics (
  metric_id INTEGER PRIMARY KEY,
  restaurant_id INTEGER NOT NULL REFERENCES restaurants(restaurant_id),
  metric_date DATE NOT NULL,
  prep_time_avg_min NUMERIC(5,2),
  cancellation_rate NUMERIC(5,4),
  acceptance_rate NUMERIC(5,4),
  delivery_sla_breach_rate NUMERIC(5,4)
);

CREATE TABLE recommendation_logs (
  rec_log_id INTEGER PRIMARY KEY,
  user_id INTEGER NOT NULL REFERENCES users(user_id),
  item_id INTEGER NOT NULL REFERENCES menu_items(item_id),
  score NUMERIC(8,4),
  rank_position INTEGER,
  model_version TEXT,
  shown_timestamp TIMESTAMP,
  clicked BOOLEAN,
  ordered BOOLEAN
);
