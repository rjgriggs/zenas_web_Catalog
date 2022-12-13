import streamlit
import snowflake.connector
import pandas
my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")

streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

