import streamlit
import pandas
import snowflake.connector



streamlit.title('Zena\'s Amazing Atheleisure Catalog')
streamlit.text("Hello from Snowflake:")

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(),CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)
