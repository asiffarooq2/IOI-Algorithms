# Python linear-time solution for the Stock Span Problem


def calculate_stock_span(prices, spans):
    number_of_days = len(prices)

    # Stack stores the indices of useful previous days
    index_stack = []
    index_stack.append(0)

    # Span of the first day is always 1
    spans[0] = 1

    for current_day in range(1, number_of_days):

        # Remove days whose prices are less than or equal
        # to the current day's price
        while (
            len(index_stack) > 0
            and prices[index_stack[-1]] <= prices[current_day]
        ):
            index_stack.pop()

        # Calculate the span
        if len(index_stack) == 0:
            spans[current_day] = current_day + 1
        else:
            spans[current_day] = current_day - index_stack[-1]

        # Add the current day to the stack
        index_stack.append(current_day)


def print_array(values, number_of_elements):
    for index in range(number_of_elements):
        print(values[index], end=" ")


# Stock prices for each day
stock_prices = [10, 4, 5, 90, 120, 80]

# Array to store the stock spans
stock_spans = [0 for _ in range(len(stock_prices) + 1)]

# Calculate the stock span
calculate_stock_span(stock_prices, stock_spans)

# Display the result
print_array(stock_spans, len(stock_prices))
