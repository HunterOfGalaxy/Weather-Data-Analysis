

# Weather vs Temperature
fig_temp = px.box(df, x='Summary', y='Temperature (C)', title='Weather vs Temperature')
fig_temp.update_layout(xaxis_title='Weather Type', yaxis_title='Temperature (C)', xaxis={'categoryorder':'total descending'})
fig_temp.show()

# Weather vs Humidity
fig_humidity = px.box(df, x='Summary', y='Humidity', title='Weather vs Humidity')
fig_humidity.update_layout(xaxis_title='Weather Type', yaxis_title='Humidity', xaxis={'categoryorder':'total descending'})
fig_humidity.show()

# Weather vs Pressure
fig_pressure = px.box(df, x='Summary', y='Pressure (millibars)', title='Weather vs Pressure')
fig_pressure.update_layout(xaxis_title='Weather Type', yaxis_title='Pressure (millibars)', xaxis={'categoryorder':'total descending'})
fig_pressure.show()
