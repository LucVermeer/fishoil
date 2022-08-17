df_comparison = rolling_predictions.to_frame().rename(columns={'peru_price': 'price_prediction'}).merge(df_original[['peru_price', 'date']].set_index('date'), left_index=True, right_index=True)

million = 1000000
yearly_expenses = 60*million

total_volume = (yearly_expenses / 12 * len(df_comparison)) / df_comparison['peru_price'].mean()
monthly_volume = total_volume / len(df_comparison)

print(total_volume)

expenses = 0
volume_to_buy = monthly_volume
volume_bought = 0

for i in range(len(df_comparison) - 1):
    month = df_comparison.index[i]
    next_month = df_comparison.index[i + 1]
    current_month_data = df_comparison.loc[month]
    next_month_data = df_comparison.loc[next_month]
    if next_month_data['price_prediction'] >= 0:
        # buy
        print("month {}: buying {} metric tons for {:,} usd".format(i+1, volume_to_buy, current_month_data['peru_price']))
        expenses += volume_to_buy * current_month_data['peru_price']
        volume_bought += volume_to_buy
        volume_to_buy = monthly_volume
    else:
        # postpone buy
        volume_to_buy += monthly_volume
        # if it is the last month buy anyway
        if i == (len(df_comparison) - 2):
            print("month {}: buying {} metric tons for {:,} usd".format(i+1, volume_to_buy, current_month_data['peru_price']))
            expenses += volume_to_buy * current_month_data['peru_price']
            volume_bought += volume_to_buy



print("Bought a total of {:,} usd".format(expenses))
print(total_volume, volume_bought)
display(df_comparison)