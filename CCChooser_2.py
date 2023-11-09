### This was Chatgpt's rendition of my code. I don't know what I'm going to do with it but want
### to have it when I need it

#Realizing this doesn't work with yearly numbers. I wonder why? Will figure out later.

# Credit card comparison tool

# Function to gather spending data
def get_spending_data(period):
    print(f"Hello! Let's gather your spending data for {period}.\n"
          "Please enter your monthly spending in the following categories:")

    spending_data = {}
    categories = [
        "Travel", "Dining", "Gas", "Bills and Utilities", "Education",
        "Entertainment", "Personal", "Home", "Groceries", "Shopping"
    ]

    for category in categories:
        spending_data[category] = float(input(f"Monthly {category} Spend = $"))

    return spending_data

# Function to calculate monthly rewards
def calculate_rewards(spending_data, card_name, annual_fee, rewards_multiplier):
    total_spending = sum(spending_data.values())
    monthly_rewards = rewards_multiplier * total_spending - (annual_fee / 12)
    annual_rewards = monthly_rewards * 12
    print(f"\nWith the {card_name}, your monthly rewards will be ${monthly_rewards:.2f}.")
    print(f"Your annual rewards will be ${annual_rewards:.2f}.")

# Compare credit cards
def compare_credit_cards():
    card_info = [
        {"name": "Chase Sapphire Preferred", "annual_fee": 95, "rewards_multiplier": 1.25},
        {"name": "Chase Sapphire Reserve", "annual_fee": 550, "rewards_multiplier": 1.5}
    ]

    period = input("Would you like to input monthly (M) or yearly (Y) numbers? ")
    spending_data = get_spending_data("months" if period == "M" else "years")

    for card in card_info:
        print(f"\n--- {card['name']} ---")
        calculate_rewards(spending_data, card['name'], card['annual_fee'], card['rewards_multiplier'])

# Main program
compare_credit_cards()